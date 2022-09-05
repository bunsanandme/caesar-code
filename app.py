from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from crypto_utils import caesar

app = Flask(__name__)
app.config['SECRET_KEY']='LongAndRandomSecretKey'

class CryptForm(FlaskForm):
    input_string = StringField(validators=[DataRequired()])
    key_string = StringField(validators=[DataRequired()])
    code_option = RadioField('', choices=[('encode','Зашифровать'),('decode','Расшифровать')])
    submit = SubmitField('Рассчитать')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CryptForm()
    if form.validate_on_submit():
        if form.code_option.data == "encode":
            result = caesar(form.input_string.data, int(form.key_string.data))
        else:
             result = caesar(form.input_string.data, int(form.key_string.data), decode=True)
        return render_template("index.html", form=form, result=result)
    return render_template("index.html", form=form, result="")