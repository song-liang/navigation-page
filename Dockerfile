FROM python:3.12-alpine

ENV TZ Asia/Shanghai
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk --no-cache add linux-headers build-base libc-dev tzdata mariadb-connector-c-dev dumb-init pcre-dev && \
    cp /usr/share/zoneinfo/${TZ} /etc/localtime && \
    echo ${TZ} > /etc/timezone

RUN mkdir -p /app && chown -R nobody:nogroup /app
WORKDIR /app

COPY requirements.txt  /app/
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ && \
    pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["uwsgi","--ini","navigation_page/uwsgi.ini"]

