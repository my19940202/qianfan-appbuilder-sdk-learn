FROM python:alpine3.19 AS app

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

CMD ["sh","run.sh"]