# flask服务器测试
from flask import Flask, request, render_template, jsonify
import appbuilder
from appbuilder.core.console.agent_builder import data_class
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
        # 每次迭代返回AgentBuilderAnswer结构，内可能包括多个事件内容
        # 采集detail数据，用于升入了解message类型的数据
        detailList = []
        for key, value in qianfan_res.content:
            if key == "events":
                for event in value:
                    content_type = event.content_type
                    detail = event.detail
                    # 根据content类型对事件详情进行解析
                    if content_type == "code":
                        code_detail = data_class.CodeDetail(**detail)
                        print(code_detail.code)
                    elif content_type == "text":
                        text_detail = data_class.TextDetail(**detail)
                        print(text_detail.text)
                    elif content_type == "image":
                        image_detail = data_class.ImageDetail(**detail)
                        print(image_detail.url)
                    elif content_type == "rag":
                        rag_detail = data_class.RAGDetail(**detail)
                        print(rag_detail)
                    elif content_type == "function_call":
                        function_call_detail = data_class.FunctionCallDetail(**detail)
                        print(function_call_detail)
                    elif content_type == "audio":
                        audio_detail = data_class.AudioDetail(**detail)
                        print(audio_detail)
                    elif content_type == "video":
                        video_detail = data_class.VideoDetail(**detail)
                        print(video_detail)
                    elif content_type == "status":
                        status_detail = data_class.StatusDetail(**detail)
                        print(status_detail)
                    else:
                        default_detail = data_class.DefaultDetail(**detail)
                        print(default_detail)
        ret = {
            "err_no": 0,
            "data": qianfan_res.content.answer
            # ,"events": jsonify(detailList)
        }
    except Exception as e:
        print(e)
        ret = {
            "err_no": 1,
            "data": "机器人繁忙"
        }

    return ret
