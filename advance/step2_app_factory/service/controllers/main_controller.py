'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''
from flask import render_template, request
from  service.controllers   import bp_main as main
from service.forms import FormQuestion

# 플라스크 객체뿐 아니라 등록한 blueprint 객체도 라우팅 가능
# ~/main/
@main.route('/')
def home():
    return render_template('index.html')

# ~/main/question
@main.route('/question')
def question():
    form = FormQuestion()
    return render_template('question.html', wtf=form)