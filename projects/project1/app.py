from flask import Flask, render_template
from pythonfiles.keys import keys

app = Flask(__name__)
a = keys.APP_SECRET_KEY


@app.route('/')
def hello_world():  # put application's code here
	return render_template('welcome.html')


if __name__ == '__main__':
	app.run(debug=True)
