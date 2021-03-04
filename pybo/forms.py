from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('필수 입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('필수 입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    username = StringField("사용자 이름", validators=[
        DataRequired('필수 입력 항목입니다.'), Length(min=3, max=25, message='글자 수를 3글자 이상, 25글자 이하로 설정해주세요.')])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired('필수 입력 항목입니다.'), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired('필수 입력 항목입니다.')])
    email = EmailField('이메일', validators=[DataRequired('필수 입력 항목입니다.'), Email('이메일 주소가 적절하지 않습니다.')])


class UserLoginForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])