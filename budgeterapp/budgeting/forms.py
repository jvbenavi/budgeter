from datetime import datetime as dt

from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Site


class SiteForm(FlaskForm):
    base_url = fields.StringField(validators=[Required()])


class VisitForm(FlaskForm):
    browser = fields.StringField()
    date = fields.DateField(default=dt.now)
    event = fields.StringField()
    url = fields.StringField(validators=[Required()])
    ip_address = fields.StringField()
    location = fields.StringField()
    latitude = fields.StringField()
    longitude = fields.StringField()
    site = QuerySelectField(validators=[Required()], query_factory=lambda: Site.query.all())
