
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired


class ValidationVersionForm(FlaskForm):
    validation_version = IntegerField("validation_version",
        validators=[
            InputRequired("Enter a number"),
        ]
    )
