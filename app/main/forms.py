from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, IntegerField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourslef.", validators=[Required()])  
    submit = SubmitField('Submit')

class Subscribe(FlaskForm):
    email = StringField("Enter your email address", valodators=[Required()])
    phone_number= IntegerField("Enter Your Phone Number", validators=[Required()])
    country = StringField("Enter your country or region", validators=[Required()])
    submit = SubmitField('Subscribe')

class ReviewForm(FlaskForm):
    title= StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review')
    submit=SubmitField('Submit')