from wsgiref.simple_server import make_server


def home(request):
    return request


def register(request):
    return request


def login(request):
    return request


def index(request):
    return request


pattern_url = {
    "/": home,
    "/login": login,
    "/register": register,
    "/index": index
}  # 预访问的(url: method)字典


def simple_app(env, start_response):
    url = env.get('PATH_INFO')  # 从环境变量env中提取get出地址信息PATH_INFO，也就是所谓的路由url
    params = env.get('QUERY_STRING')  # 从环境变量env中提取get出请求信息QUERY_STRING，也就是所谓的参数params
    if url is None or url not in pattern_url.keys():
        start_response('404 not found', [('Content_type', 'text/plain')])
        return [b'404 page not found']

    res = pattern_url.get(url)  # 从字典中找到键为url的函数传给res，res将作为响应路由地址的函数
    if res is None:
        start_response('404 not found', [('Content_type', 'text/plain')])
        return [b'404 page not found']

    start_response('200 OK', [('Content-type', 'text/plain')])
    return [res(params).encode()]


server = make_server('127.0.0.1', 8888, app=simple_app)  # "192.168.30.1"
server.serve_forever()

# encode(encoding,errors)
# encoding:指定编码格式,默认utf-8
# errors:指定编码错误的处理方式,默认strict
# decode()
