from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://deciamtbizqvbs:0d4fe8dbd3e5b155871508f77ab6eac59514ac117e6c3bdb916f8e303dea106f@ec2-54-243-193-227.compute-1.amazonaws.com:5432/dfpm0hd1lbhejh'
#heroku = Heroku(app)
db = SQLAlchemy(app)


# Create our database model
class Job(db.Model):
    __tablename__ = "Job"
    id = db.Column(db.Integer, primary_key=True)
    bname = db.Column(db.String(120))
    title = db.Column(db.String(120))
    desc = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    loc = db.Column(db.String(20))
    num = db.Column(db.String(25))
    #pic = db.Column(db.LargeBinary)
'''
    def __init__(self, bname, title, desc, age, loc):
        self.bname = bname
        self.title

    def __repr__(self):
        return '<E-mail %r>' % self.bname
'''
#db.create_all()
# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs',methods=['GET','POST'])
def jobs():
    if request.method == 'POST':
        age = request.form['age']
        loc = request.form['location']
        jobs=Job.query.filter(Job.loc==loc,Job.age<=age)
        return render_template('jobs.html',jobs=jobs)
    else:
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
        num = request.form['num']
        #pic = request.form['pic']
        job = Job(bname=bname,title=title,desc=desc,age=age,loc=loc,num=num)
        db.session.add(job)
        db.session.commit()
        return render_template('businesses.html')
    

if __name__ == '__main__':
    app.debug = True
    app.run()