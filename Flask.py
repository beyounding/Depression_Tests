from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

db.drop_all()
db.create_all()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

class Participant2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    comments = db.Column(db.Text)
    result1 = db.Column(db.Integer, nullable=True)
    result2 = db.Column(db.Integer, nullable=True)
    result3 = db.Column(db.Integer, nullable=True)
    result4 = db.Column(db.Integer, nullable=True)


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
           return render_template('participant_info.html')
       else:
           return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')


@app.route('/main_menu', methods=['GET', 'POST'])
def main_menu():
    return render_template('participant_info.html')

@app.route('/add_participant', methods=['POST'])
def add_participant():
    name = request.form['name']
    dob = request.form['dob']
    sex = request.form['sex']
    comments = request.form['comments']

    new_participant = Participant2(name=name, dob=dob, sex=sex, comments=comments, result1=0, result2=0, result3=0, result4=0)
    db.session.add(new_participant)
    db.session.commit()

    return render_template('start_page.html')

    
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

@app.route('/survey4')
def survey4():
    return render_template('survey4.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    answers = {
        'question1': request.form['question1'],
        'question2': request.form['question2'],
        'question3': request.form['question3'],
        'question4': request.form['question4'],
        'question5': request.form['question5'],
        'question6': request.form['question6'],
        'question7': request.form['question7'],
        'question8': request.form['question8'],
        'question9': request.form['question9'],
        'question10': request.form['question10']
    }
    return render_template('result.html', answers=answers)

@app.route('/submit_survey2', methods=['POST'])
def submit_survey2():
    answers = {
        'questionn1': request.form['questionn1'],
        'questionn2': request.form['questionn2'],
        'questionn3': request.form['questionn3'],
        'questionn4': request.form['questionn4'],
        'questionn5': request.form['questionn5'],
        'questionn6': request.form['questionn6'],
        'questionn7': request.form['questionn7'],
        'questionn8': request.form['questionn8'],
        'questionn9': request.form['questionn9'],
        'questionn10': request.form['questionn10']
    }
    return render_template('survey2_results.html', answers=answers)

@app.route('/submit_survey3', methods=['POST'])
def submit_survey3():
    answers = {
        'questionnn1': request.form['questionnn1'],
        'questionnn2': request.form['questionnn2'],
        'questionnn3': request.form['questionnn3'],
        'questionnn4': request.form['questionnn4'],
        'questionnn5': request.form['questionnn5'],
        'questionnn6': request.form['questionnn6'],
        'questionnn7': request.form['questionnn7'],
        'questionnn8': request.form['questionnn8'],
        'questionnn9': request.form['questionnn9'],
        'questionnn10': request.form['questionnn10'],
        'questionnn11': request.form['questionnn11'],
        'questionnn12': request.form['questionnn12'],
        'questionnn13': request.form['questionnn13'],
        'questionnn14': request.form['questionnn14'],
        'questionnn15': request.form['questionnn15'],
        'questionnn16': request.form['questionnn16'],
        'questionnn17': request.form['questionnn17'],
        'questionnn18': request.form['questionnn18'],
        'questionnn19': request.form['questionnn19'],
        'questionnn12': request.form['questionnn20'],
        'questionnn21': request.form['questionnn21'],
        'questionnn22': request.form['questionnn22'],
        'questionnn23': request.form['questionnn23'],
        'questionnn24': request.form['questionnn24'],
        'questionnn25': request.form['questionnn25'],
        'questionnn26': request.form['questionnn26'],
        'questionnn27': request.form['questionnn27'],
        'questionnn28': request.form['questionnn28'],
        'questionnn29': request.form['questionnn29'],
        'questionnn30': request.form['questionnn30'],
        'questionnn31': request.form['questionnn31'],
        'questionnn32': request.form['questionnn32'],
        'questionnn33': request.form['questionnn33'],
        'questionnn34': request.form['questionnn34'],
        'questionnn35': request.form['questionnn35'],
        'questionnn36': request.form['questionnn36'],
        'questionnn37': request.form['questionnn37'],
        'questionnn38': request.form['questionnn38'],
        'questionnn39': request.form['questionnn39'],
        'questionnn40': request.form['questionnn40'],
        'questionnn41': request.form['questionnn41'],
        'questionnn42': request.form['questionnn42'],
        'questionnn43': request.form['questionnn43'],
        'questionnn44': request.form['questionnn44'],
        'questionnn45': request.form['questionnn45'],
        'questionnn46': request.form['questionnn46'],
        'questionnn47': request.form['questionnn47'],
        'questionnn48': request.form['questionnn48'],
        'questionnn49': request.form['questionnn49'],
        'questionnn50': request.form['questionnn50'],
        'questionnn51': request.form['questionnn51'],
        'questionnn52': request.form['questionnn52']
    }
    return render_template('survey3_results.html', answers=answers)


@app.route('/submit_survey4', methods=['POST'])
def submit_survey4():

    depression_sum = 0
    alarm_sum = 0
    stress_sum = 0
    

    depression_sum += int(request.form['q3']) + int(request.form['q5']) + int(request.form['q10']) + int(request.form['q13']) + int(request.form['q16']) + int(request.form['q17']) + int(request.form['q21']) + int(request.form['q24']) + int(request.form['q26']) + int(request.form['q31']) + int(request.form['q34']) + int(request.form['q37']) + int(request.form['q38']) + int(request.form['q42'])
    alarm_sum += int(request.form['q2']) + int(request.form['q4']) + int(request.form['q7']) + int(request.form['q9']) + int(request.form['q15']) + int(request.form['q19']) + int(request.form['q20']) + int(request.form['q23']) + int(request.form['q25']) + int(request.form['q28']) + int(request.form['q30']) + int(request.form['q36']) + int(request.form['q40']) + int(request.form['q41']) 
    stress_sum += int(request.form['q1']) + int(request.form['q6']) + int(request.form['q8']) + int(request.form['q11']) + int(request.form['q12']) + int(request.form['q14']) + int(request.form['q18']) + int(request.form['q22']) + int(request.form['q27']) + int(request.form['q29']) + int(request.form['q32']) + int(request.form['q33']) + int(request.form['q35']) + int(request.form['q39']) 

    return render_template('survey4_results.html', depression_sum=depression_sum, alarm_sum=alarm_sum, stress_sum=stress_sum)

@app.route('/participant_list')
def participant_list():
    participants = Participant2.query.all()
    return render_template('participant_list.html', participants=participants)



if __name__ == '__main__':
    app.run(debug=True)
