from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()
    admin_user = User.query.filter_by(username='su_379f_nsl4').first()
    if not admin_user:
        admin_user = User(username='su_379f_nsl4', password='dAvku3aMvo_sak', is_admin=True)
        db.session.add(admin_user)
        db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       user = User.query.filter_by(username=username).first()
       if user and user.password == password:
           login_user(user)
           return render_template('start_page.html')
       else:
           return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    if current_user.is_admin:
        if request.method == 'POST':
            new_username = request.form['username']
            new_password = request.form['password']
            user = User(username=new_username, password=new_password)
            db.session.add(user)
            db.session.commit()
            return "User registered successfully"
        return render_template('admin_register.html')
    else:
        return "You do not have permission to access this page"


@app.route('/survey1')
def survey1():
    return render_template('index.html')

@app.route('/survey2')
def survey2():
    return render_template('survey2.html')

@app.route('/survey3')
def survey3():
    return render_template('survey3.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    answers = {
        'question1': request.form['question1'],
        'question2': request.form['question2'],
        'question3': request.form['question3']
    }
    return render_template('result.html', answers=answers)

@app.route('/submit_survey2', methods=['POST'])
def submit_survey2():
    answers = {
        'color': request.form['color'],
        'animal': request.form['animal'],
        'food': request.form['food']
    }
    return render_template('survey2_results.html', answers=answers)

@app.route('/submit_survey3', methods=['POST'])
def submit_survey3():
    a = request.form['season']
    b = request.form['hobby']
    c = request.form['transportation']
    answers = {
        'season': a,
        'hobby': b,
        'transportation': c,
        'summ': int(a) + int(b) + int(c)
    }
    return render_template('survey3_results.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
