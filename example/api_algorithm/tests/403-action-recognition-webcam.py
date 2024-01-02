import collections
import os
import time
from typing import Tuple, List

import cv2
import numpy as np
import openvino as ov
from openvino.runtime.ie_api import CompiledModel

# Fetch `notebook_utils` module
# import urllib.request
# urllib.request.urlretrieve(
#     url='https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/main/notebooks/utils/notebook_utils.py',
#     filename='notebook_utils.py'
# )

##########################
# A directory where the model will be downloaded.
base_model_dir = "model"
# The name of the model from Open Model Zoo.
model_name = "action-recognition-0001"
# Selected precision (FP32, FP16, FP16-INT8).
precision = "FP16"
model_path_decoder = (
    f"403/model/intel/{model_name}/{model_name}-decoder/{precision}/{model_name}-decoder.xml"
)
model_path_encoder = (
    f"403/model/intel/{model_name}/{model_name}-encoder/{precision}/{model_name}-encoder.xml"
)


with open("403/data/kinetics.txt") as f:
    labels = [line.strip() for line in f]

print(labels[0:9], np.shape(labels))

##########################
device = "GPU"
# Initialize OpenVINO Runtime.
core = ov.Core()


def model_init(model_path: str, device: str) -> Tuple:
    """
    Read the network and weights from a file, load the
    model on CPU and get input and output names of nodes

    :param:
            model: model architecture path *.xml
            device: inference device
    :retuns:
            compiled_model: Compiled model
            input_key: Input node for model
            output_key: Output node for model
    """

    # Read the network and corresponding weights from a file.
    model = core.read_model(model=model_path)
    # Compile the model for specified device.
    compiled_model = core.compile_model(model=model, device_name=device)
    # Get input and output names of nodes.
    input_keys = compiled_model.input(0)
    output_keys = compiled_model.output(0)
    return input_keys, output_keys, compiled_model


# Encoder initialization
input_key_en, output_keys_en, compiled_model_en = model_init(model_path_encoder, device)
# Decoder initialization
input_key_de, output_keys_de, compiled_model_de = model_init(model_path_decoder, device)

# Get input size - Encoder.
height_en, width_en = list(input_key_en.shape)[2:]
# Get input size - Decoder.
frames2decode = list(input_key_de.shape)[0:][1]


def center_crop(frame: np.ndarray) -> np.ndarray:
    """
    Center crop squared the original frame to standardize the input image to the encoder model

    :param frame: input frame
    :returns: center-crop-squared frame
    """
    img_h, img_w, _ = frame.shape
    min_dim = min(img_h, img_w)
    start_x = int((img_w - min_dim) / 2.0)
    start_y = int((img_h - min_dim) / 2.0)
    roi = [start_y, (start_y + min_dim), start_x, (start_x + min_dim)]
    return frame[start_y : (start_y + min_dim), start_x : (start_x + min_dim), ...], roi


def adaptive_resize(frame: np.ndarray, size: int) -> np.ndarray:
    """
     The frame going to be resized to have a height of size or a width of size

    :param frame: input frame
    :param size: input size to encoder model
    :returns: resized frame, np.array type
    """
    h, w, _ = frame.shape
    scale = size / min(h, w)
    w_scaled, h_scaled = int(w * scale), int(h * scale)
    if w_scaled == w and h_scaled == h:
        return frame
    return cv2.resize(frame, (w_scaled, h_scaled))


def rec_frame_display(frame: np.ndarray, roi) -> np.ndarray:
    """
    Draw a rec frame over actual frame

    :param frame: input frame
    :param roi: Region of interest, image section processed by the Encoder
    :returns: frame with drawed shape

    """

    cv2.line(frame, (roi[2] + 3, roi[0] + 3), (roi[2] + 3, roi[0] + 100), (0, 200, 0), 2)
    cv2.line(frame, (roi[2] + 3, roi[0] + 3), (roi[2] + 100, roi[0] + 3), (0, 200, 0), 2)
    cv2.line(frame, (roi[3] - 3, roi[1] - 3), (roi[3] - 3, roi[1] - 100), (0, 200, 0), 2)
    cv2.line(frame, (roi[3] - 3, roi[1] - 3), (roi[3] - 100, roi[1] - 3), (0, 200, 0), 2)
    cv2.line(frame, (roi[3] - 3, roi[0] + 3), (roi[3] - 3, roi[0] + 100), (0, 200, 0), 2)
    cv2.line(frame, (roi[3] - 3, roi[0] + 3), (roi[3] - 100, roi[0] + 3), (0, 200, 0), 2)
    cv2.line(frame, (roi[2] + 3, roi[1] - 3), (roi[2] + 3, roi[1] - 100), (0, 200, 0), 2)
    cv2.line(frame, (roi[2] + 3, roi[1] - 3), (roi[2] + 100, roi[1] - 3), (0, 200, 0), 2)
    # Write ROI over actual frame
    FONT_STYLE = cv2.FONT_HERSHEY_SIMPLEX
    org = (roi[2] + 3, roi[1] - 3)
    org2 = (roi[2] + 2, roi[1] - 2)
    FONT_SIZE = 0.5
    FONT_COLOR = (0, 200, 0)
    FONT_COLOR2 = (0, 0, 0)
    cv2.putText(frame, "ROI", org2, FONT_STYLE, FONT_SIZE, FONT_COLOR2)
    cv2.putText(frame, "ROI", org, FONT_STYLE, FONT_SIZE, FONT_COLOR)
    return frame


def display_text_fnc(frame: np.ndarray, display_text: str, index: int):
    """
    Include a text on the analyzed frame

    :param frame: input frame
    :param display_text: text to add on the frame
    :param index: index line dor adding text

    """
    # Configuration for displaying images with text.
    FONT_COLOR = (0, 0, 255)
    FONT_COLOR2 = (255, 0, 0)
    FONT_STYLE = cv2.FONT_HERSHEY_DUPLEX
    FONT_SIZE = 0.7
    TEXT_VERTICAL_INTERVAL = 25
    TEXT_LEFT_MARGIN = 15
    # ROI over actual frame
    (processed, roi) = center_crop(frame)
    # Draw a ROI over actual frame.
    frame = rec_frame_display(frame, roi)
    # Put a text over actual frame.
    text_loc = (TEXT_LEFT_MARGIN, TEXT_VERTICAL_INTERVAL * (index + 1))
    text_loc2 = (TEXT_LEFT_MARGIN + 1, TEXT_VERTICAL_INTERVAL * (index + 1) + 1)
    cv2.putText(frame, display_text, text_loc2, FONT_STYLE, FONT_SIZE, FONT_COLOR2)
    cv2.putText(frame, display_text, text_loc, FONT_STYLE, FONT_SIZE, FONT_COLOR)


def preprocessing(frame: np.ndarray, size: int) -> np.ndarray:
    """
    Preparing frame before Encoder.
    The image should be scaled to its shortest dimension at "size"
    and cropped, centered, and squared so that both width and
    height have lengths "size". The frame must be transposed from
    Height-Width-Channels (HWC) to Channels-Height-Width (CHW).

    :param frame: input frame
    :param size: input size to encoder model
    :returns: resized and cropped frame
    """
    # Adaptative resize
    preprocessed = adaptive_resize(frame, size)
    # Center_crop
    (preprocessed, roi) = center_crop(preprocessed)
    # Transpose frame HWC -> CHW
    preprocessed = preprocessed.transpose((2, 0, 1))[None,]  # HWC -> CHW
    return preprocessed, roi

def softmax(x: np.ndarray) -> np.ndarray:
    """
    Normalizes logits to get confidence values along specified axis
    x: np.array, axis=None
    """
    exp = np.exp(x)
    return exp / np.sum(exp, axis=None)

if __name__ == '__main__':


    sample_duration = frames2decode  # Decoder input size - From Cell 5_7

    encoder_output = []
    decoded_labels = []
    decoded_top_probs = []
    top_k = 5


    # Create a text template to show inference results over video.
    text_inference_template = "Infer Time:{Time:.1f}ms,{fps:.1f}FPS"
    text_template = "{label},{conf:.2f}%"
    #url = "test.mp4"
    url = 0
    
    cap = cv2.VideoCapture(url)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))


    while True:
        r, frame = cap.read()
        if r:
            # frame = cv2.imread("test_images/image2117.jpg")

            scale = 1280 / max(frame.shape)

            # Adaptative resize for visualization.
            if scale < 1:
                frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            else:
                frame = cv2.resize(frame,(1280,720))

            # Preprocess frame before Encoder.
            (preprocessed, _) = preprocessing(frame, height_en)

            # Measure processing time.
            start_time = time.time()

            # Encoder Inference per frame
            output_key_en = compiled_model_en.output(0)
            infer_result_encoder = compiled_model_en([preprocessed])[output_key_en]
            encoder_output.append(infer_result_encoder)

            if len(encoder_output) == sample_duration:
                print("encode success")
                # Concatenate sample_duration frames in just one array
                decoder_input = np.concatenate(encoder_output, axis=0)
                # Organize input shape vector to the Decoder (shape: [1x16x512]]
                decoder_input = decoder_input.transpose((2, 0, 1, 3))
                decoder_input = np.squeeze(decoder_input, axis=3)
                output_key_de = compiled_model_de.output(0)
                # Get results on action-recognition-0001-decoder model
                result_de = compiled_model_de([decoder_input])[output_key_de]

                # 规范化logits以获得沿指定轴的置信值
                probs = softmax(result_de - np.max(result_de))

                # 将最高概率解码为相应的标签名称 start
                top_ind = np.argsort(-1 * probs)[:top_k]
                out_label = np.array(labels)[top_ind.astype(int)]

                # decoded_labels = [out_label[0][0], out_label[0][1], out_label[0][2]]
                decoded_labels = []
                for i in range(top_k):
                    decoded_labels.append(out_label[0][i])

                top_probs = np.array(probs)[0][top_ind.astype(int)]

                # decoded_top_probs = [top_probs[0][0], top_probs[0][1], top_probs[0][2]]
                decoded_top_probs = []
                for i in range(top_k):
                    decoded_top_probs.append(top_probs[0][i])

                # 将最高概率解码为相应的标签名称 end

                encoder_output = []

            print("显示检测结果")
            print(decoded_labels)
            print(decoded_top_probs)

            for i in range(len(decoded_labels)):
                display_text = text_template.format(
                    label=decoded_labels[i],
                    conf=decoded_top_probs[i] * 100,
                )
                display_text_fnc(frame, display_text, i)

            display_text = text_inference_template.format(Time=0, fps=fps)
            display_text_fnc(frame, display_text, top_k)

            cv2.imshow("frame", frame)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

            # title = "403"
            # cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_AUTOSIZE)
            # cv2.imshow(title, frame)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        else:
            break

