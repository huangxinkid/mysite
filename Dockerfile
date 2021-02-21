# 建立 python3.7 环境
FROM python:3.7

COPY pip.conf /root/.pip/pip.conf

RUN mkdir -p /root/mysite

WORKDIR /root/mysite

ADD . /root/mysite

# 更新pip版本
RUN /usr/local/bin/python -m pip install --upgrade pip

# 利用 pip 安装依赖
RUN pip install -r requirements.txt

# 给start.sh可执行权限
RUN chmod +x ./start.sh
