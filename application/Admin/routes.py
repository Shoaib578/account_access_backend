from application import db,app
from flask import Blueprint,render_template,redirect,flash,url_for
from application.models import Users
from application.Admin.form import LoginForm,AddUserForm,EditUserForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

admin = Blueprint('admin',__name__,static_folder="../static")


@admin.route('/login',methods=['POST','GET'])
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
    
    user = Users.query.filter_by(email=form.email.data).first()

    
    if user and check_password_hash(user.password,form.password.data):
        

        login_user(user, False)
        return redirect(url_for('admin.Index'))
       

    else:
        flash('Login Unsuccessful. Please check email and password')
    return render_template('admin/login.html', form=form)


@admin.route('/')
@login_required
def Index():
    if current_user.is_authenticated:
        if  current_user.is_admin == 0:
            return redirect(url_for('main.Index'))
    users = Users.query.filter_by(is_admin=0).all()
    return render_template('admin/index.html',users=users)
    
@admin.route('/add',methods=['POST','GET'])
@login_required
def Add():
    form = AddUserForm()
    if form.validate_on_submit():
        hash_pw = generate_password_hash(form.password.data)

        user = Users(email=form.email.data,name=form.name.data,account=form.account.data,code=form.code.data,password=hash_pw,phone_no=form.phone_no.data,address=form.address.data,routing=form.routing.data,product_name=form.product_name.data,is_admin=0)
        db.session.add(user)
        db.session.commit()
        flash("User Added")
        return redirect(url_for('admin.Add'))
    return render_template('admin/add.html',form=form)


@admin.route('/edit/<int:id>',methods=['POST','GET'])
@login_required
def EditUser(id):
    form = EditUserForm()
    user = Users.query.get_or_404(id)

    if form.validate_on_submit():
        

        user.email = form.email.data
        user.name= form.name.data
        user.account = form.account.data
        user.routing = form.routing.data
        user.code = form.code.data
        user.product_name = form.product_name.data
        user.address = form.address.data
        user.phone_no = form.phone_no.data
        user.password = generate_password_hash(form.password.data)

        db.session.commit()
        flash("User Updated")
        return redirect(url_for('admin.Index'))
    else:
        form.email.data= user.email
        form.name.data= user.name
        form.account.data= user.account
        form.routing.data= user.routing
        form.product_name.data= user.product_name
        form.code.data= user.code
        form.address.data= user.address
        form.phone_no.data= user.phone_no
        

    return render_template('admin/edit_user.html',form=form,user=user)



@admin.route('/logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('admin.Login'))