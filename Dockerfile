# 学号查询系统 Dockerfile
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量，标识为 Docker 容器
ENV DOCKER_CONTAINER=true

# 复制项目文件
COPY index.html .
COPY style.css .
COPY script.js .
COPY students.csv .
COPY server.py .

# 暴露端口
EXPOSE 8000

# 启动服务器
CMD ["python", "server.py"]