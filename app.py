from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from model.db import db
from model.message import Message
from forms.add_message import AddMessageForm

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = b'x\xfa\xd4\x04x]g,(t\xb5\xf7j\xb9\x8c\x13'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:mysql@mysql:3306/db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:mysql@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.app = app
db.init_app(app)

db.create_all()
db.session.commit()

# Flask-Bootstrap requires this line
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
	form = AddMessageForm()
	if form.validate_on_submit():
		db.session.add(Message(form.content.data))
		db.session.commit()

	return render_template('message_list.html', form=form, messages=Message.query.all())


if __name__ == '__main__':
	app.run(debug=False, port=5000, host='0.0.0.0')
