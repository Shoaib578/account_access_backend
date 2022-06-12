from application import db,app
from flask import Blueprint,render_template,redirect,flash,url_for
from application.models import Users
from application.Main.form import LoginForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main',__name__,static_folder="../static")

@main.route('/login',methods=['GET','POST'])
def Login():
    form=LoginForm()
    hash_pw = generate_password_hash('admin26')

    if Users.query.filter_by(is_admin=1).count()==1:

        pass
    else:
        
        admin = Users(email='theadmin21@gmail.com',password=hash_pw,is_admin=1)
        db.session.add(admin)
        db.session.commit()
        
  
   
        

    form = LoginForm()
    
    user = Users.query.filter_by(name=form.name.data).first()

    if form.validate_on_submit():
    
        if user and check_password_hash(user.password,form.password.data):
            

            login_user(user, False)
            return redirect(url_for('main.Index'))
        

        else:
            flash('Login Unsuccessful. Please check email and password')
    return render_template('login.html', form=form)



@main.route('/')
@login_required
def Index():
    if current_user.is_authenticated:
        if current_user.is_admin == 1:

            return redirect(url_for('admin.Index'))
      


    return render_template('main/index.html')



@main.route('/logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('main.Index'))