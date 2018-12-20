# Flask
work hard and study Flask
## 1.@before request
Making user login authentication base on before request<br>
--berofe_request.py--<br>
--detail.html--<br>
--index.html--<br>
--login.html--<br>
## 2.@after request
Focus on the execution sequence
## 3.Customization error
@app.errorhandler(404)<br>
def error_404(*args):<br>
&nbsp; &nbsp;&nbsp; &nbsp;return "404!!!"<br>
## 4.Customization func
@@app.add_template_global<br>
def add(a,b):<br>
&nbsp; &nbsp;&nbsp; &nbsp;return a+b<br><br><br>
{{add(1,2}}
## 5.Customization filter
@app.add_template_filter<br>
def db(a,b,c):<br>
&nbsp; &nbsp;&nbsp; &nbsp;return a+b+c<br><br><br>
{{1|(2,3)}}
