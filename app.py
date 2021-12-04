from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from model.db import db
from model.message import Message

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:mysql@mysql:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.app = app
db.init_app(app)

db.create_all()
db.session.add(Message("docker c'est de la merde"))
db.session.commit()

# Flask-Bootstrap requires this line
Bootstrap(app)


@app.route("/")
def hello_world():
	return render_template('message_list.html', messages=Message.query.all())


if __name__ == '__main__':
	app.run(debug=False, port=5000, host='0.0.0.0')
