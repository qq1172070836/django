from wsgiref.simple_server import make_server

def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>电脑前的你真好看！</h1>',encoding='utf-8'), ]

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8001, run_server)
    httpd.serve_forever()
