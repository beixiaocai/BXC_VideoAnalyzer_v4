from controllers.BaseHandler import BaseHandler
import json
import numpy as np
import base64
import cv2

class AlgorithmHandler(BaseHandler):
    async def post(self, *args, **kwargs):
        data = await self.do()
        self.response_json(data)

    async def do(self):
        request_params = self.request_post_params()

        # print(request_params)
        happen = False
        happenScore = 0.0
        detects = []

        image_base64 = request_params.get("image_base64", None)  # 接收base64编码的图片并转换成cv2的图片格式
        if image_base64:
            encoded_image_byte = base64.b64decode(image_base64)
            image_array = np.frombuffer(encoded_image_byte, np.uint8)
            # image = turboJpeg.decode(image_array)  # turbojpeg 解码
            image = cv2.imdecode(image_array, cv2.COLOR_RGB2BGR)  # opencv 解码

            # video_height,video_width,video_channels = image.shape # 输入图像的的高，宽，channel
            # print(image.shape)

            detects.append({
                "x1": 100,
                "y1": 100,
                "x2": 500,
                "y2": 500,
                "class_score": 0.93456,
                "class_id": 0,
                "class_name": "test"
            })

            happen = True
            happenScore = 0.97


        result = {
            "happen": happen,
            "happenScore": happenScore,
            "detects": detects
        }

        print(result)
        res = {
            "code": 1000,
            "msg": "success",
            "result": result
        }
        return res
