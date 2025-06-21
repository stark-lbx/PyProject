import time
from wsgiref.simple_server import make_server


# 一次请求耗时记录的中间件
class ResponseTimingMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, env, start_response):
        start_time = time.time()
        response = self.app(env, start_response)
        end_time = time.time()
        res_time = (end_time - start_time) + 1000
        timing_text = "记录请求耗时中间件输出\n\n本次请求耗时:{:.10f}ms\n".format(res_time)
        response.append(timing_text.encode())
        return response


def simple_app(env, start_response):
    status_code = '200 OK'
    response_header = [('Content-type', 'text/plain; charset=utf-8')]

    return_body =[]
    for k,v in env.items():
        return_body.append(f"{k}: {v}")

    start_response(status_code, response_header)
    return ["\n\n".join(return_body).encode()]


response_timing__middleware = ResponseTimingMiddleware(app=simple_app)
server = make_server('127.0.0.1', 8888, app=response_timing__middleware)
server.serve_forever()

# client 通过 middleware 间接调用 app
# 在client中:
#           #deal something
#           middleware = middleware_type(app=simple_app)    #通过simpleapp初始化middleware类型变量
#           rev_list = middleware(env, start_response)  #通过middleware调用应用获得返回的列表
#           #deal rev_list

# 在middleware中:
#           __call__(self,env,start_response)
#               #deal something
#               response = self.app(env, start_response)
#               #deal something
#               return response

# 在server中:
#           server = make_server(ipv4, port, app = middleware()) #make server-设置服务器
#           server.server_forever() #run server-运行服务器
