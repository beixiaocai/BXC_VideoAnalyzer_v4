from controllers.BaseHandler import BaseHandler
import json


class IndexHandler(BaseHandler):
    async def get(self, *args, **kwargs):
        data = await self.do()
        self.response_json(data)

    async def do(self):
        request_params = self.request_get_params()
        version = float(request_params.get("version", "0"))
        print(version)

        res = {
            "code": 1000,
            "msg": "success"
        }
        return res
