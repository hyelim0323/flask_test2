'''
    - GET 방식으로 데이터 전송하기
        - 클라이언트 (키=값&키=값...)
            - 링크
                <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
            - form 전송, 화면 껌뻑 => 화면 전환
                <form action="" method="get">
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송"/>
                </form>
            - ajax 가능 (jQuery로 표현)
                $.get({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:(res)=>{},
                    error:(err)=>{}
                })
        - 서버
            - get 방식 데이터 추출
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "helloworld"

if __name__ == "__main__":
    app.run(debug=True)