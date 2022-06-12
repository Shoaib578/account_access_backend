from application import db,login_manager,ma


from flask_login import UserMixin
import datetime 


@login_manager.user_loader
def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
    return Users.query.get(int(id))





class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100),nullable=False) 
    password = db.Column(db.String(200),nullable=False)
    phone_no = db.Column(db.String(100))
    account = db.Column(db.String(500))
    address = db.Column(db.String(500))
    name = db.Column(db.String(500))
    code = db.Column(db.String(500))
    routing = db.Column(db.String(200))
    product_name = db.Column(db.String(200))
    is_admin = db.Column(db.Integer)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password','is_admin','product_name','address','phone_no','code','routing','account','')

