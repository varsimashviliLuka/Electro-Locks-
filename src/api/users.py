from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.api.nsmodels import users_ns, users_model
from src.models import User, Role

@users_ns.route('/users')
@users_ns.doc(responses={200: 'OK', 400: 'Invalid Argument', 401: 'JWT Token Expires', 403: 'Unauthorized', 404: 'Not Found'})
class UsersListAPI(Resource):
    
    @users_ns.marshal_with(users_model)
    @jwt_required()
    @users_ns.doc(security="JsonWebToken")
    def get(self):
        '''წამოვიღოთ ყველა სადგურების ინფორმაცია'''
        
        stations = User.query.all()
        if not stations:
            return {"error": "სადგურები არ მოიძებნა."}, 404
        
        return stations, 200
    