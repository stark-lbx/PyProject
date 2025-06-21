import web

# login_urls =(
#     '/login','Login',
# )
# class Login:
#     def GET(self):
#         return "hello"
# login_app = web.application(login_urls,globals())


# 正则表达式.*
urls = (
    '/(.*)', 'Hello',
)
# 创建一个application
app = web.application(urls, globals())


class Hello:
    def GET(self, name):
        if not name:
            name = "World"
        return "Hello " + name + "!"


application = app.wsgifunc()  # 返回了一个simple_app


# if __name__ == "__main__":
#     app.run()
