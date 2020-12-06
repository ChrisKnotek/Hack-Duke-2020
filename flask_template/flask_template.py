from flask import Flask, request, redirect, url_for
from flask import render_template
from database import db_session
from models import Company
import pdb


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


#worth noting when we're embedding python in flask we're using something called a
#jinja template https://jinja.palletsprojects.com/en/2.10.x/templates/
@app.route('/python')
def show_python():
  return render_template(
    'python.html',
    revs = Company.query.all()
  )


@app.route('/database')
def database():
  return render_template(
    'database.html',
    revs= Company.query.all()
  )


@app.route('/add_rev')
def add_rev():
  
  standard = request.args.get("standard")
  points = request.args.get("points")
  additional_info = request.args.get("additional_info")

  rev = Company(standard, points, additional_info)
  db_session.add(rev)
  db_session.commit()

  return redirect(url_for('database'))


@app.route('/style')
def style():
    return render_template('index_with_style.html')

@app.route('/companyName')
def companyName():
  return render_template(
    'companyName.html', 
    revs = Company.query.all()
    )

@app.route('/companyName2')
def companyName2():
  return render_template(
    'companyName2.html', 
    revs = Company.query.all()
    )

@app.route('/companyName3')
def companyName3():
  return render_template(
    'companyName3.html', 
    revs = Company.query.all()
    )

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()