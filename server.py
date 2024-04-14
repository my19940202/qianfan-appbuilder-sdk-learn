# flask服务器测试
from flask import Flask, request, render_template, jsonify
import appbuilder
import os

app = Flask(__name__)

# get请求测试
# http://127.0.0.1:8800/send?num=134132
@app.route('/chat', methods=['GET'])
def get_api():
    ret = {}
    # 获取查询参数
    querys = request.args

    # 获取请求中的msg
    msg = querys.get('msg')
    appid = querys.get('appid') or os.environ.get('APPID')

    # 执行对话
    try:
        # 每次会话使用最新的appid
        agent_builder = appbuilder.AgentBuilder(appid)
        conversation_id = agent_builder.create_conversation()

        # 执行对话
        qianfan_res = agent_builder.run(conversation_id, msg)
        ret = {
            "err_no": 0,
            "data": qianfan_res.content.answer
        }
    except Exception as e:
        print(e)
        ret = {
            "err_no": 1,
            "data": "机器人繁忙"
        }

    return ret
