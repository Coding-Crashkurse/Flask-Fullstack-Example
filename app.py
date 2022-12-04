from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = "secret"
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()



@app.route('/', methods=["POST", "GET"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Form validated!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=3000)