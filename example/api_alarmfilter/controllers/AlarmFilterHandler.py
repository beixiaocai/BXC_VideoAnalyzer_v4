from controllers.BaseHandler import BaseHandler
import json
from datetime import datetime


class AlarmFilterHandler(BaseHandler):
    async def post(self, *args, **kwargs):
        data = await self.do()
        self.response_json(data)

    async def do(self):
        ret = False
        msg = "未知错误"

        request_params = self.request_post_params()

        print("request_params=", datetime.now(), request_params)
        # 注意: ret=True表示，过滤器检测通过，ret=False表示，过滤器检测失败
        ret = True
        msg = "success"

        res = {
            "code": 1000 if ret else 0,
            "msg": msg
        }
        return res
