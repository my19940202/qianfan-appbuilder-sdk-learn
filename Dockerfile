FROM python:alpine3.19 AS app

WORKDIR /app

RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY . ./

CMD ["sh","run.sh"]