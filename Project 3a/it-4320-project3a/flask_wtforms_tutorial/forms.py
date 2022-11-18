"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
#from wtforms.fields import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length
import json
import urllib.request
import requests



class StockForm(FlaskForm):
    """Generate Your Graph."""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    url = 'https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_json/data/e8ad01974d4110e790b227dc1541b193/nyse-listed_json.json'
    response = requests.request("GET", url)
    data = response.json()
    emptyDict = {}
    counter = 0
    for i in data:
        if i["ACT Symbol"]:
            emptyDict[i["ACT Symbol"]] = str(counter)
            counter+=1

    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
            choices = emptyDict,
            #("IBM", "IBM"),
            #("GOOGL", "GOOGL"),
        
        #],
    )

    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "3. Weekly"),
            ("4", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")



