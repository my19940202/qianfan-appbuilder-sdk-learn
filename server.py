# flask服务器测试
from flask import Flask, request, render_template, jsonify
import appbuilder
import os
import re
import time

app = Flask(__name__)

# post请求测试
@app.route('/chat', methods=['POST'])
def post_api():
    ret = {}
    start_time = time.time()
    # 获取并处理 POST 数据
    if request.form:
        post_data = request.form
    elif request.json:
        post_data = request.json
    else:
        post_data = None

    # 获取请求中的msg
    msg = post_data['msg']
    appid = post_data['appid'] or os.environ.get('APPID')

    # 执行对话
    try:
        # 每次会话使用最新的appid
        agent_builder = appbuilder.AgentBuilder(appid)
        conversation_id = agent_builder.create_conversation()
        end_time = time.time()

        # 执行对话
        qianfan_res = agent_builder.run(conversation_id, msg)
        result = qianfan_res.content.answer
        if "^[" in qianfan_res.content.answer:
            result = re.sub(r"\^\[\d+\]\^", "", result)
            result = result.replace("**", "")
        print(appid, msg, result, end_time - start_time)
        ret = {
            "err_no": 0,
            "data": result
        }
    except Exception as e:
        print(e)
        ret = {
            "err_no": 1,
            "data": "小助手繁忙,稍后再试"
        }

    return ret
