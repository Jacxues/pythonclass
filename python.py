#! python3

from flask import (
  Flask,
  render_template
)
app = Flask(_name_, template_folder="templates")

@app.route('/')
def home:
return_template('home.html')