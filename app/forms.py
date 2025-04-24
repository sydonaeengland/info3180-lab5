from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    # String field for the movie title that cannot be left empty
    title = StringField('Title', validators=[DataRequired()])

     # Text area for the movie description that cannot be empty 
    description = TextAreaField('Description', validators=[DataRequired()])

    # File upload field for the movie posters. This onyl accepts files with certain extensions.
    poster = FileField('Poster', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])