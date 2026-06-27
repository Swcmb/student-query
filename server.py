#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os
import webbrowser
import logging
from threading import Timer
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('server.log')
    ]
)
logger = logging.getLogger(__name__)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头部以支持本地文件访问
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        # 健康检查端点
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'service': 'student-query'
            }
            self.wfile.write(str(response).encode())
            return

        # 记录请求日志
        logger.info(f"GET {self.path} from {self.client_address[0]}")
        super().do_GET()

def open_browser():
    webbrowser.open('http://localhost:8000')

def start_server():
    PORT = int(os.environ.get('PORT', 8000))

    # 切换到脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # 检查端口是否被占用
    try:
        with socketserver.TCPServer(("", PORT), None) as test_server:
            pass
    except OSError:
        logger.error(f"端口 {PORT} 已被占用，请检查是否有其他服务在运行")
        return

    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        logger.info(f"🚀 服务器启动成功！")
        logger.info(f"📱 访问地址: http://localhost:{PORT}")
        logger.info(f"📁 服务目录: {os.getcwd()}")
        logger.info(f"⏹️  按 Ctrl+C 停止服务器")

        # 2秒后自动打开浏览器（仅在非 Docker 环境下）
        if not os.environ.get('DOCKER_CONTAINER'):
            Timer(2.0, open_browser).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("🛑 服务器已停止")

if __name__ == "__main__":
    start_server()