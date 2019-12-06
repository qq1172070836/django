from wsgiref.simple_server import make_server

def book(environ, start_response):
    print('book page')
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>book page</h1>', encoding='utf-8'), ]

def cloth(environ, start_response):
    print('cloth page')
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>cloth page</h1>', encoding='utf-8'), ]

def url_dispacher():
    urls = {
        '/book': book,
        '/cloth': cloth,
    }
    return urls

def run_server(environ, start_response):

    urls_list = url_dispacher() # 拿到所有url
    request_url = environ.get('PATH_INFO')
    print('request_url', request_url)

    if request_url in urls_list:
        func_data = urls_list[request_url](environ, start_response)
        return func_data
    else:
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<h1>page not found</h1>',encoding='utf-8'), ]

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8001, run_server)
    httpd.serve_forever()
