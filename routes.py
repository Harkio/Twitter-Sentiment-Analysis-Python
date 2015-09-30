from flask import *
from functools import wraps
import MySQLdb
from GChartWrapper import *


app = Flask(__name__)
# app.config.from_object(__name__)



app.secret_key = '05834503'


def connect_db():
    db = MySQLdb.connect(host="localhost",
                         user="graham",
                         passwd="A05bf311",
                         db="twitter",
                         port=3306)
    return db


# Render Homepage
@app.route('/')
def home():
    return render_template('home.html')


# Accept Login
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You Need To Log In First.')
            return redirect(url_for('log'))

    return wrap


# Render Welcome Page
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# Render cities Page
@app.route('/cities')
@login_required
def cities():
    return render_template('cities.html')


# Render document page Page
@app.route('/documentation')
@login_required
def documentation():
    return render_template('documentation.html')


# Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You Were Logged Out')
    return redirect(url_for('log'))


###############################################################################################################################

						   ###########################################################################################
@login_required
# HTML Results of What is In Database
@app.route('/galway')
def galway():
    db = MySQLdb.connect(host="localhost", user="graham", passwd="A05bf311", db="twitter", port=3306)

    cur = db.cursor()
    cur.execute(
        "SELECT user, score FROM `galway` WHERE location LIKE '%Galway%' OR location LIKE '%Ireland%' ORDER BY `score` ASC LIMIT 10")
    tweet = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute(
        "SELECT user, score FROM `galway` WHERE location LIKE '%Galway%' OR location LIKE '%Ireland%' ORDER BY `score` DESC LIMIT 10")
    tweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, score FROM `galway`WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    atweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, tweet FROM `galway` WHERE time LIKE '%Aug%' ORDER BY `score` ASC LIMIT 10")
    btweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]


    cur.execute("SELECT user, tweet FROM `galway` WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    ctweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `galway` WHERE time LIKE '%Aug%' GROUP BY `sentiment`")
    dtweets = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `galway` WHERE time LIKE '%Aug%' GROUP BY `sentiment` DESC")
    low = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    low = row[1] /100

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `galway` WHERE time LIKE '%Aug%' GROUP BY `sentiment` ASC")
    high = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    high = row[1] /100

    g= VerticalBarStack([high,low]).title('How Many Tweets').color('orange','blue').label('positive', 'negative').bar(50,50).size(160,200)

    cur.execute("SELECT `sentiment`,CAST(AVG(`score`) AS DECIMAL(10,2)) FROM `galway` WHERE time LIKE '%Aug%'")
    average = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]
    average = row[1]

    if average:
       emotion = 'mosthappy'
    elif average:
       emotion = 'superhappy'
    elif average:
       emotion = 'mehhappy'
    elif average:
       emotion = 'mostsad'
    else:
       emotion = 'mostsad'



    cur.execute("SELECT `user`,COUNT(`user`)FROM `galway` WHERE time LIKE '%Aug%' GROUP BY `user` ORDER BY COUNT(`user`) DESC LIMIT 1")
    ftweets = [dict(user=row[0], count=row[1]) for row in cur.fetchall()]

    return render_template('galway.html', tweet=tweet, tweets=tweets, atweets=atweets,btweets=btweets
                           ,ctweets=ctweets, dtweets=dtweets, ftweets=ftweets,g=g, low=low, high=high,emotion=emotion)

						###############################################################################################################################

						   ###########################################################################################
@login_required
@app.route('/belfast')
def belfast():
    db = MySQLdb.connect(host="localhost", user="graham", passwd="A05bf311", db="twitter", port=3306)

    cur = db.cursor()
    cur.execute(
        "SELECT user, score FROM `belfast` WHERE location LIKE '%Galway%' OR location LIKE '%Ireland%' ORDER BY `score` ASC LIMIT 10")
    tweet = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute(
        "SELECT user, score FROM `belfast` WHERE location LIKE '%Galway%' OR location LIKE '%Ireland%' ORDER BY `score` DESC LIMIT 10")
    tweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, score FROM `belfast`WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    atweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, tweet FROM `belfast` WHERE time LIKE '%Aug%' ORDER BY `score` ASC LIMIT 10")
    btweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]


    cur.execute("SELECT user, tweet FROM `belfast` WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    ctweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `belfast` WHERE time LIKE '%Aug%' GROUP BY `sentiment`")
    dtweets = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `belfast` WHERE time LIKE '%Aug%' GROUP BY `sentiment` DESC")
    low = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    low = row[1] /100

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `belfast` WHERE time LIKE '%Aug%' GROUP BY `sentiment` ASC")
    high = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    high = row[1] /100

    g= VerticalBarStack([high,low]).title('How Many Tweets').color('orange','blue').label('positive', 'negative').bar(50,50).size(160,200)

    cur.execute("SELECT `sentiment`,CAST(AVG(`score`) AS DECIMAL(10,2)) FROM `belfast` WHERE time LIKE '%Aug%'")
    average = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]
    average = row[1]

    if average:
       emotion = 'mosthappy'
    elif average:
       emotion = 'superhappy'
    elif average:
       emotion = 'mehhappy'
    elif average:
       emotion = 'mostsad'
    else:
       emotion = 'mostsad'





    cur.execute("SELECT `user`,COUNT(`user`)FROM `belfast` WHERE time LIKE '%Aug%' GROUP BY `user` ORDER BY COUNT(`user`) DESC LIMIT 1")
    ftweets = [dict(user=row[0], count=row[1]) for row in cur.fetchall()]

    return render_template('belfast.html', tweet=tweet, tweets=tweets, atweets=atweets,btweets=btweets
                           ,ctweets=ctweets, dtweets=dtweets, ftweets=ftweets,g=g, low=low, high=high,emotion=emotion)

###############################################################################################################################

						   ###########################################################################################
@login_required
@app.route('/cork')
def cork():
    db = MySQLdb.connect(host="localhost", user="graham", passwd="A05bf311", db="twitter", port=3306)

    cur = db.cursor()
    cur.execute(
        "SELECT user, score FROM `cork` WHERE location LIKE '%Cork%' OR location LIKE '%Ireland%' ORDER BY `score` ASC LIMIT 10")
    tweet = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute(
        "SELECT user, score FROM `cork` WHERE location LIKE '%Cork%' OR location LIKE '%Ireland%' ORDER BY `score` DESC LIMIT 10")
    tweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, score FROM `cork`WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    atweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, tweet FROM `cork` WHERE time LIKE '%Aug%' ORDER BY `score` ASC LIMIT 10")
    btweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]


    cur.execute("SELECT user, tweet FROM `cork` WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    ctweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `cork` WHERE time LIKE '%Aug%' GROUP BY `sentiment`")
    dtweets = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `cork` WHERE time LIKE '%Aug%' GROUP BY `sentiment` DESC")
    low = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    low = row[1] /100

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `cork` WHERE time LIKE '%Aug%' GROUP BY `sentiment` ASC")
    high = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    high = row[1] /100

    g= VerticalBarStack([high,low]).title('How Many Tweets').color('orange','blue').label('positive', 'negative').bar(50,50).size(160,200)

    cur.execute("SELECT `sentiment`,CAST(AVG(`score`) AS DECIMAL(10,2)) FROM `cork` WHERE time LIKE '%Aug%'")
    average = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]
    average = row[1]

    if average:
       emotion = 'mosthappy'
    elif average:
       emotion = 'superhappy'
    elif average:
       emotion = 'mehhappy'
    elif average:
       emotion = 'mostsad'
    else:
       emotion = 'mostsad'





    cur.execute("SELECT `user`,COUNT(`user`)FROM `cork` WHERE time LIKE '%Aug%' GROUP BY `user` ORDER BY COUNT(`user`) DESC LIMIT 1")
    ftweets = [dict(user=row[0], count=row[1]) for row in cur.fetchall()]

    return render_template('cork.html', tweet=tweet, tweets=tweets, atweets=atweets,btweets=btweets
                           ,ctweets=ctweets, dtweets=dtweets, ftweets=ftweets,g=g, low=low, high=high,emotion=emotion)

###############################################################################################################################

						   ###########################################################################################

						   ###########################################################################################
@login_required
@app.route('/dublin')
def dublin():
    db = MySQLdb.connect(host="localhost", user="graham", passwd="A05bf311", db="twitter", port=3306)

    cur = db.cursor()
    cur.execute(
        "SELECT user, score FROM `dublin` WHERE location LIKE '%Dublin%' OR location LIKE '%Ireland%' ORDER BY `score` ASC LIMIT 10")
    tweet = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute(
        "SELECT user, score FROM `dublin` WHERE location LIKE '%Dublin%' OR location LIKE '%Ireland%' ORDER BY `score` DESC LIMIT 10")
    tweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, score FROM `dublin`WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    atweets = [dict(user=row[0], score=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT user, tweet FROM `dublin` WHERE time LIKE '%Aug%' ORDER BY `score` ASC LIMIT 10")
    btweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]


    cur.execute("SELECT user, tweet FROM `dublin` WHERE time LIKE '%Aug%' ORDER BY `score` DESC LIMIT 10")
    ctweets = [dict(user=row[0], tweet=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `dublin` WHERE time LIKE '%Aug%' GROUP BY `sentiment`")
    dtweets = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `dublin` WHERE time LIKE '%Aug%' GROUP BY `sentiment` DESC")
    low = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    low = row[1] /100

    cur.execute("SELECT `sentiment`,COUNT(`sentiment`)FROM `dublin` WHERE time LIKE '%Aug%' GROUP BY `sentiment` ASC")
    high = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]

    high = row[1] /100

    g= VerticalBarStack([high,low]).title('How Many Tweets').color('orange','blue').label('positive', 'negative').bar(50,50).size(160,200)

    cur.execute("SELECT `sentiment`,CAST(AVG(`score`) AS DECIMAL(10,2)) FROM `dublin` WHERE time LIKE '%Aug%'")
    average = [dict(sentiment=row[0], count=row[1]) for row in cur.fetchall()]
    average = row[1]

    if average > 0.30 and average < 0.50:
       emotion = 'mosthappy'
    elif average > 0.21 and average < 0.29:
       emotion = 'superhappy'
    elif average > 0.10 and average < 0.20:
       emotion = 'mehhappy'
    elif average > 0.0 and average < 0.9:
       emotion = 'mostsad'
    else:
       emotion = 'angry'





    cur.execute("SELECT `user`,COUNT(`user`)FROM `dublin` WHERE time LIKE '%Aug%' GROUP BY `user` ORDER BY COUNT(`user`) DESC LIMIT 1")
    ftweets = [dict(user=row[0], count=row[1]) for row in cur.fetchall()]

    return render_template('dublin.html', tweet=tweet, tweets=tweets, atweets=atweets,btweets=btweets
                           ,ctweets=ctweets, dtweets=dtweets, ftweets=ftweets,g=g, low=low, high=high,emotion=emotion,average=average)


###############################################################################################################################

						   ###########################################################################################




@app.route('/log', methods=['GET', 'POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Please Try Again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('cities'))
    return render_template('log.html', error=error)


# Render Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')


#Accept Login and Insert
@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    error = None
    return render_template('hello.html', error=error)


#Process The Tweets
@app.route('/process', methods=['GET', 'POST'])
@login_required
def process():
    #    tweetGetter = Getter(query, maxTweet)
    return render_template('process.html')


if __name__ == '__main__':
    app.run(debug=True)
__author__ = 'graha_000'
