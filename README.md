# 测试AppBuildder的能力


## 启动方法
```
docker run  -p 8800:8800 -it -v /Users/xishengbo/Desktop/dev.tmp/git_repo/qianfan-appbuilder-sdk-learn:/app python:alpine3.19 sh
```
## 学习内容
了解了一下message这个Class的层级
``` 
events=[Event(code=0, message='', status='done',
 event_type='function_call', content_type='function_call', detail={'text': {'arguments': {}, 'component_code': 'RAGAgent', 'component_name': '知识问答'}}), Event(code=0, message='', status='preparing',
 event_type='RAGAgent', content_type='status', detail={}), Event(code=0, message='', status='done',
 event_type='RAGAgent', content_type='rag', detail={'references': [{'id': '1', 'content': '我们会觉得这个东西很很没有意义，我们觉得这个东西很不好。就像最开始一些写汇编的人去看我们写高级语言这样的感觉。他会觉得你写出来的东西效率不好，你们写出来东西怎么着？所以我是真的去用过stream late的，是因为我我们因为工作原因，我当时用过一段时间stream late。因为我是前端，我去玩stream late的时候觉得很难受。给大家一点背景，stream的，就是你写一个python的代码，完全不要写一行前端，你就可以跑出一个有前端的一个项目来。它有很多内置的组件，整个过程中你只需要写python，不需要想任何语言。但是我对一个前端，我会对我的项目的UI和它的交互有要求。比如最简单的，我当时想做一个输入框，是一个AI的这种对话的机器人输入框。我就希望它一直处于整个页面的底部，一就固定在那里，但streams stream lit 没有提供给我这个选项，那我就做不了。发言人238:46 我用hack的方式会有很多问题，这是为什么低代码在程序员圈的会有一些反感的原因。所以这个问题就比所以下面的问题就比较尖锐的就是你如何看待低代码的价值。他曾经火爆一时，现在好像我不知道现在是一个什么状态，感觉很久没听过消息了，你们怎么去看？它的真正的价值以及它的一些商业价值。发言人139:10 我觉得跟低代码有一个我个人觉得有一些相关性的对比。但是我估计可能的挺多同学可能不觉得他们具有相关性。就是tell win的CSS在til v的刚刚出现的时候，我个人是觉得这是是垃圾，这东西有什么用呢？', 'type': 'engine', 'from': 'search_db', 'title': 'No.47 和 rrweb 作者 aryu 聊从开源到技术商业化、低代码和 AI、职场软技能_原文.docx', 'segment_id': 'a1732b70-cba1-4b84-8346-d15d3f66c0f5', 'document_id': 'a8e9f40a-a177-46b7-85e0-a958c4074cd8', 'document_name': 'No.47 和 rrweb 作者 aryu 聊从开源到技术商业化、低代码和 AI、职场软技能_原文.docx', 'dataset_id': '2a6bb820-0e55-497a-bb04-2c8d7a447246'}, {'id': '2', 'content': '觉得wait 更好，或者是no bundle方案更好。但是我们不得不说，在过去的相当长那段时间里面，ipad在不断的每一天的解决大家的问题，就像更早的jury rege一样了。所以我觉得首先一项技术它不能长期也不是太大的问题，它如果能解决大家一两年的特定场景的需求，就已经很了不起。发言人143:58 那回到刚刚提到的，为什么我个人觉得低代码跟AI还是有的？集合和这个玩儿一下的原因，首先我觉得现在如果你让我用AI去写一个完整的项目，那他如果是个已有的项目，可能这件事情会更更痛苦。因为我找不到一种很通用很好的方法让AI去理解这个代码库。因为这个代码库只要有很多个人一起协同过，它本身的结构就会越来越的越复杂，然后它的这个抽象也会越来越不统一。发言人144:28 而低代码的特点，其实之所以程序员不喜欢低代码，我觉得其中的一个原因，除了现在很多低代码工具确实做的错误之外。其中另外一个我觉得比较根本的原因是在于低代码限制了大家的发挥的空间。它是把很多的抽象模式已经给你做好了之后，你只在里面填空，你只能做有限的事情。发言人144:48 但是它的好处，其实对AI来说，就是它会看到一个它特别容易理解的一个代码库。因为它的抽象方式是统一的，它能够自由发挥的空间是有限的。然后同时它甚至于在代码和代码之间，你在低代码工具里面，你都写不出一个import 的逻辑，吧？很少能做到这样的事情。很多时候里面的model怎么划分，都是这个工具给你划定好的。所以它的每一块代码不会特别的多，同时它的抽象的模式非常的统一。然后再最后就是它的代码量也相对来讲少，要不然也就称不上低的低贷款了。所以这几件事情我觉得对AI来说是一件好的事情。', 'type': 'engine', 'from': 'search_db', 'title': 'No.47 和 rrweb 作者 aryu 聊从开源到技术商业化、低代码和 AI、职场软技能_原文.docx', 'segment_id': '59d92197-11f2-485e-83a5-75b787286bbc', 'document_id': 'a8e9f40a-a177-46b7-85e0-a958c4074cd8', 'document_name': 'No.47 和 rrweb 作者 aryu 聊从开源到技术商业化、低代码和 AI、职场软技能_原文.docx', 'dataset_id': '2a6bb820-0e55-497a-bb04-2c8d7a447246'}], 'text': ''}), Event(code=0, message='', status='done',
 event_type='RAGAgent', content_type='rag', detail={'text': '对低代码的看法如下：\n\n低代码是指一种快速应用开发的方式，它能够让开发者通过图形化界面和预构建的模块来创建应用程序，而无需编写大量的代码。低代码平台能够提供一些通用的功能和组件，使得开发者可以通过拖拽和配置的方式来快速构建应用程序，从而提高了开发效率和降低了开发难度^[1]^。\n\n然而，低代码平台也存在一些限制，例如可能无法满足特定业务需求、自定义程度有限等。此外，一些开发者认为低代码平台会限制他们的发挥空间，因为很多抽象模式已经被做好了，只能在里面填空，做有限的事情^[2]^。\n\n因此，在选择是否使用低代码平台时，需要根据具体业务需求和团队实际情况进行权衡和选择。', 'references': []}), Event(code=0, message='', status='success',
 event_type='RAGAgent', content_type='status', detail={})]
```

# 参考资料
- https://www.51cto.com/article/712585.html
- flask简单webserver https://dormousehole.readthedocs.io/en/latest/quickstart.html
- github reeadme https://github.com/baidubce/app-builder?tab=readme-ov-file
- 官方文档 https://cloud.baidu.com/doc/AppBuilder/s/Glqb6dfiz
- appbuilder详细一些api https://github.com/baidubce/app-builder/tree/b4f843f969b051bdebab25ebdb7e26e2012afc86/appbuilder/core/console/agent_builder