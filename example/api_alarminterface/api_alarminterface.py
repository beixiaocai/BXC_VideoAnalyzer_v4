from flask import Flask, request,jsonify
import os
import time
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "index"

@app.route('/interface', methods=['POST', 'GET'])
def interface():
    request_params = request.get_json()
    print("request_params=", datetime.now(), request_params)
    ret = False
    msg = "未知错误"

    ret = True
    msg = "success"

    response_data = {
        "code": 1000 if ret else 0,
        "msg": msg
    }
    return jsonify(response_data)

if __name__ == '__main__':
    # app.debug = True

    # 接口列表
    # http://127.0.0.1:8072
    # http://127.0.0.1:8072/interface

    app.run(host='0.0.0.0', port=8072, debug=False)