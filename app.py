from flask import Flask
from flask_restplus import Api
from pushapp_firebase import pushapp_firebase

app = Flask(__name__)
api = Api(app)

api.add_resource(pushapp_firebase.PushAppFireBase, '/update', endpoint='datareciver')

if __name__ == '__main__':
    app.run(debug=True)