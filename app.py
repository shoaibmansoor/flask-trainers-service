from flask import Flask
from flask_restful import Api
from os import environ
from models import db
from trainer_resource import TrainerResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trainers.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    return 'The app is running!'


api.add_resource(TrainerResource, '/trainers', '/trainers/<int:trainer_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=environ.get('PORT', 5000))
