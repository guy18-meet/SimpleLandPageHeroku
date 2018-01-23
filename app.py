from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
heroku = Heroku(app)
db = SQLAlchemy(app)

# Create our database model
class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    bname = db.Column(db.String(120))
    title = db.Column(db.String(120))
    desc = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    loc = db.Column(db.String(20))

    def __init__(self, bname, title, desc, age, loc):
        self.bname = bname

    def __repr__(self):
        return '<E-mail %r>' % self.bname


# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/businesses')
def businesses():
    return render_template('businesses.html')


# Save e-mail to database and send to success page
@app.route('/jobpost', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        bname = request.form['bname']
        title = request.form['title']
        desc = request.form['desc']
        age = request.form['age']
        loc = request.form['loc']
        job = Job(bname=bname,title=title,desc=desc,age=age,loc=loc,)
        db.session.add(job)
        db.session.commit()
        return render_template('businesses.html')
    

if __name__ == '__main__':
    #app.debug = True
    app.run()