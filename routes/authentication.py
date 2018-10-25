from flask import Blueprint,request,jsonify
from utility.pymongo_crud import register_new_users,user_login

authentication_blueprint = Blueprint('authentication',__name__,template_folder='templates')


@authentication_blueprint.route('/',methods=['GET'],endpoint='read_all_user_names')
def read_all_user_names():
    return "Umm digital"


@authentication_blueprint.route('/signin',methods=['POST'],endpoint='registration')
def registration():
    content = request.get_json()
    username = content['username']
    password = content['password']
    return jsonify(register_new_users(username,password))


@authentication_blueprint.route('/login',methods=['POST'],endpoint='login')
def login():
    content = request.get_json()
    username = content['username']
    password = content['password']
    return jsonify(user_login(username, password))
