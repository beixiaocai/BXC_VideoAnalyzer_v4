import json
import tornado.web
import time
from datetime import date,datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        # 初始化函数，一般用于初始化环境变量（连接数据库）
        pass


    def get_request_ip(self):
        request_ip = self.request.headers.get("X-Real-IP") or self.request.headers.get("X-Forwarded-For") or \
                    self.request.remote_ip
        return request_ip
    def get_request_port(self):
        # address = self.request.connection.context.address
        request_port = 20000
        return request_port

    def request_get_params(self):
        params = {}

        for key in self.request.arguments:
            params[key] = self.get_argument(key)

        return params

    def request_post_params(self):
        post_params = self.request.arguments
        post_params = {x: post_params.get(x)[0].decode("utf-8") for x in post_params.keys()}

        # print("获取POST 表单请求参数：",type(post_params),post_params)

        # tornado 接收json方式上传的参数
        if not post_params:
            post_params = self.request.body.decode('utf-8')
            post_params = json.loads(post_params)
            # print("获取POST json请求参数：", type(post_params), post_params)

        return post_params


    def response_json(self, data):

        # self.write(json.dumps(data, cls=ComplexEncoder))
        self.write(json.dumps(data))
