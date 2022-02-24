from flask import Flask, render_template
from static.python_files.keys import keys

app = Flask(__name__)
app.secret_key = keys.APP_SECRET_KEY


@app.route('/')
def root():
	return render_template('welcome.html')


if __name__ == '__main__':
	app.run(debug=True)
