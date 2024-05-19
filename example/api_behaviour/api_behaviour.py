import json

from flask import Flask, request,jsonify
import os
import time
from datetime import datetime
import numpy as np
import base64
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "index"

@app.route('/modex', methods=['POST', 'GET'])
def modex():
    print("modex")

    ret = False
    msg = "未知错误"

    happen = False
    happenScore = 0.0
    indices = []
    try:
        request_params = request.get_json()
        print("request_params=", datetime.now(), request_params)

        detects = request_params.get("detects")
        if detects:
            indices = list(range(min(len(detects), 3)))  # 模拟只取前三个目标的序号
        else:
            indices = []

    except Exception as e:
        msg = str(e)

    response_data = {
        "code": 1000 if ret else 0,
        "msg": msg,
        "result": {
            "happen": happen,
            "happenScore": happenScore,
            "indices": indices
        }
    }
    return jsonify(response_data)

@app.route('/mode5', methods=['POST', 'GET'])
def mode5():
    print("mode5")

    ret = False
    msg = "未知错误"

    happen = False
    happenScore = 0.0
    detects = []

    try:
        request_params = request.get_json()
        # print("request_params=", datetime.now(), request_params)

        image_base64 = request_params.get("image_base64", None)  # 接收base64编码的图片并转换成cv2的图片格式
        if image_base64:
            encoded_image_byte = base64.b64decode(image_base64)
            image_array = np.frombuffer(encoded_image_byte, np.uint8)
            # image = turboJpeg.decode(image_array)  # turbojpeg 解码
            image = cv2.imdecode(image_array, cv2.COLOR_RGB2BGR)  # opencv 解码

            # video_height,video_width,video_channels = image.shape # 输入图像的的高，宽，channel
            print(image.shape)

            detects.append({
                "x1": 100,
                "y1": 100,
                "x2": 500,
                "y2": 500,
                "class_score": 0.93456,
                "class_id": 0,
                "class_name": "test"
            })

            ret = True
            msg = "success"

            happen = True
            happenScore = 0.97

    except Exception as e:
        msg = str(e)

    response_data = {
        "code": 1000 if ret else 0,
        "msg": msg,
        "result": {
            "happen": happen,
            "happenScore": happenScore,
            "detects": detects
        }
    }
    # return json.dumps(response_data)
    return jsonify(response_data)


if __name__ == '__main__':
    # app.debug = True

    # 接口列表
    # http://127.0.0.1:8070
    # http://127.0.0.1:8070/modex
    # http://127.0.0.1:8070/mode5

    app.run(host='0.0.0.0', port=8070, debug=True)