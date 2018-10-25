from flask import Blueprint,request,jsonify,session
from utility.pymongo_crud import register_new_users,user_login
from flask_jwt_extended import ( jwt_required, create_access_token,
    get_jwt_claims
)

authentication_blueprint = Blueprint('authentication',__name__,template_folder='templates')


@authentication_blueprint.route('/',methods=['GET'],endpoint='read_all_user_names')
def read_all_user_names():
    return "Umm digital"


@authentication_blueprint.route('/signin',methods=['POST'],endpoint='registration')
def registration():
    content = request.get_json()
    username = content['username']
    password = content['password']
    message,status_code = register_new_users(username,password)
    print("Status code:",status_code)
    return jsonify(message)


@authentication_blueprint.route('/login',methods=['POST'],endpoint='login')
def login():
    content = request.get_json()
    username = content['username']
    password = content['password']
    message, status_code = user_login(username, password)
    #print("Access token: ",create_access_token(username))
    print("Status code:", status_code)
    if status_code == 200: # success
        session['username'] = username
    return jsonify(message)

@authentication_blueprint.route('/dashboard',methods=['GET'],endpoint='dashboard')
def dashboard():
    return jsonify({'username':session['username']})

@authentication_blueprint.route('/logout',methods=['GET'],endpoint='logout')
def logout():
    session['username'] = None
    return jsonify({'message':'Logged out successfully'})

