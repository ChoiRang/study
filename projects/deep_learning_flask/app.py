from flask import Flask, render_template
from service import Service

service = Service()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
	label = service.extract_label()
	return render_template('index.html', label=label)


@app.post('/used_car_info')
def my_car():
	return render_template('user_car_price.html')


if __name__ == '__main__':
	app.run()
