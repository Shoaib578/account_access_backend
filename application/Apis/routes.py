from application import db,app
from flask import Blueprint,render_template,redirect,flash,url_for,request,jsonify
from application.models import Users,UsersSchema
from werkzeug.security import generate_password_hash,check_password_hash
apis = Blueprint('apis',__name__,static_folder="../static")


@apis.route('/login',methods=['POST'])
def Login():
    name= request.form.get('name')
    password = request.form.get('password')
    
    user = Users.query.filter_by(name=name).first()

    
    
    if user and check_password_hash(user.password,password):
            
        users_schema = UsersSchema()
        user_data = users_schema.dump(user)
        return jsonify({
                "msg":"success",
                "user":user_data
                })
        

    else:
        return jsonify({
                "msg":"failed",
                })
    

@apis.route('/get_user',methods=['GET'])
def get_user():
    id = request.args.get('id')
    print(id)
    user= Users.query.get(id)
    user_schema= UsersSchema()
    user_data = user_schema.dump(user)
    return jsonify({'user': user_data})