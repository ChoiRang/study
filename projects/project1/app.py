from flask import Flask, render_template
from python_files.keys import keys
from python_files.routes.user_route import bp as user_bp
from python_files.routes.apt_route import bp as apt_pb
import json

app = Flask(__name__)
app.secret_key = keys.APP_SECRET_KEY
app.register_blueprint(user_bp)
app.register_blueprint(apt_pb)


@app.get('/')
def root():
	return render_template('welcome.html')


@app.post('/<string:local>')
def root_post(local):
	local = json.loads(local)
	print('post welcome', local['si'])
	return render_template('welcome.html')


if __name__ == '__main__':
	app.run(debug=True)
