from flask import Flask, render_template, session
from routes.bus_route import bp as bus_bp
from routes.member_route import bp as mem_bp

app = Flask(__name__)		# 웹 어플리케이션
app.secret_key = 'asfaf'		# 키 값, 세션 사용시의 시크릿 키
app.register_blueprint(bus_bp)
app.register_blueprint(mem_bp)


@app.route('/')			# 요청 url 등록
def root():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
	