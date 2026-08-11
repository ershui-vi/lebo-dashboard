"""
乐博经营数据看板 - 本地HTTP服务器
启动后在浏览器访问 http://localhost:8686 查看看板

用法:
    python serve_dashboard.py
"""
import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8686
DASHBOARD_DIR = Path(__file__).parent

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DASHBOARD_DIR), **kwargs)
    
    def end_headers(self):
        # 禁止缓存，确保每次刷新看到最新数据
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

def main():
    os.chdir(str(DASHBOARD_DIR))
    
    with socketserver.TCPServer(("0.0.0.0", PORT), DashboardHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"{'='*50}")
        print(f"  乐博经营数据看板已启动")
        print(f"  访问地址: {url}")
        print(f"  按 Ctrl+C 停止服务器")
        print(f"{'='*50}")
        
        # 自动打开浏览器
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")

if __name__ == "__main__":
    main()
