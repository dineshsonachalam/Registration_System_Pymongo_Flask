from flask import Flask
from routes.authentication import authentication_blueprint
app = Flask(__name__)
app.register_blueprint(authentication_blueprint)

# Register the blueprint

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)