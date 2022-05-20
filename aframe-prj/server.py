from flask import Flask
from flask import request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    html_txt='Hell0'
    #with open("index_shadow3.html","r") as  txt:
    with open("indexVR-try.html","r") as  txt:
        html_txt = ""
        html = list(txt.readlines())
        html_txt = "".join(html )
    
    return html_txt





@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''





@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='1' and request.form['password']=='1':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'



if __name__ == '__main__':
    app.run(debug=False,host='192.168.31.239',port=8000,ssl_context="adhoc")
#debug=False,host='192.168.1.111',port=5000 192.168.9.106
    #ipconfig 192.168.1.111 127.0.9.1
