from flask_restful import Resource, reqparse
from models import Trainer, db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name is required')
parser.add_argument('specialization', type=str, required=True,
                    help='Specialization is required')


class TrainerResource(Resource):

    def get(self, trainer_id=None):
        if trainer_id:
            trainer = Trainer.query.get(trainer_id)
            if trainer:
                return {'id': trainer.id, 'name': trainer.name, 'specialization': trainer.specialization}
            else:
                return {'error': 'Trainer not found'}, 404
        else:
            trainers = Trainer.query.all()
            return [{'id': trainer.id, 'name': trainer.name, 'specialization': trainer.specialization} for trainer in trainers]

    def post(self):
        args = parser.parse_args()
        new_trainer = Trainer(
            name=args['name'],
            specialization=args['specialization'],
        )
        db.session.add(new_trainer)
        db.session.commit()
        return {'id': new_trainer.id, 'name': new_trainer.name, 'specialization': new_trainer.specialization}, 201

    def put(self, trainer_id):
        args = parser.parse_args()
        trainer = Trainer.query.get(trainer_id)
        if trainer:
            trainer.name = args['name']
            trainer.specialization = args['specialization']
            db.session.commit()
            return {'id': trainer.id, 'name': trainer.name, 'specialization': trainer.specialization}
        else:
            return {'error': 'Trainer not found'}, 404

    def delete(self, trainer_id):
        trainer = Trainer.query.get(trainer_id)
        if trainer:
            db.session.delete(trainer)
            db.session.commit
