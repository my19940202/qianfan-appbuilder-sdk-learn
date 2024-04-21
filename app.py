# flask服务器测试
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# post请求测试
@app.route('/chat', methods=['POST'])
def post_api():
    # 获取查询参数
    query_params = request.args

    # 获取并处理 POST 数据
    if request.form:
        post_data = request.form
    elif request.json:
        post_data = request.json
    else:
        post_data = None
    
    # 将查询参数和 POST 数据组合成一个字典
    response_data = {
        'query': dict(query_params),
        'body': post_data
    }

    # 返回 JSON 响应
    return jsonify(response_data)

# get请求测试
# http://127.0.0.1:8800/send?num=134132
@app.route('/send', methods=['GET'])
def get_api():
    # 获取查询参数
    query_params = request.args
    
    # 你可以直接访问某个特定的查询参数，比如 'param1'
    num = query_params.get('num')
    return {
        "method": "GET",
        "num": num
    }
