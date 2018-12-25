# Flask
work hard and study Flask
## 1.base threading
An user-defined threading to realize the basic functions of threading
## 2.coroutine
A little change to make the base support coroutine
## 3.flask standard
The way to build thread supporting coroutine through object-oriented
## 4.get request
source code analysis<br><br>
example:<br>
<pre>@app.route('/')
def hello_world():
    print(request.method)
    return 'Hello World!'


if __name__ == '__main__':
    app.request_class
    app.run()

Flask->实例化RequestContext->实例化Request

Request对象返还给RequestContext->RequestContext对象返还给Flask->Push 到Local

试图函数中有print(request.method)，调用

从LocalProxy调用->调用函数_lookup_req_object->从Local中取出RequestContext对象->拿出Request对象->还给print函数</pre>

<img src="/detail.png" />
