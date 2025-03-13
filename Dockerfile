# 使用 Python 3.12.7 作为基础镜像
FROM python:3.12.7-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 复制依赖文件
COPY flask_version/requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# 复制项目文件
COPY flask_version/ .

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 