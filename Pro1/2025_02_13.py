# Application 是一个可以重复调用的可调用对象

from wsgiref.simple_server import make_server


def simple_app(env, start_response):
    # 设置状态码
    status = '200 OK'
    # 消息内容的类型
    response_header = [('Content-type', 'text/plain')]

    if env.get('PATH_INFO') == '/login':
        start_response(status, response_header)
        return [b'this is a login view\n']
    elif env.get('PATH_INFO') == '/register':
        start_response(status, response_header)
        return [b'this is a register view\n']
    else:
        #修改状态码
        status = '404 not found'
        # 可调用接口
        start_response(status, response_header)
        return [b'404 page not found']


server = make_server("192.168.30.1", 8888, app=simple_app)
server.serve_forever()
