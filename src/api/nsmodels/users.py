from flask_restx import reqparse, fields, inputs
from src.extensions import api


users_ns = api.namespace('Users', description='API რეგისტრირებული მომხმარებლების შესახებ', path='/api')


users_model = users_ns.model('Users', {
    'id': fields.Integer(required=True, description='მომხმარებლის ID', example=1),
    'name': fields.String(required=True, description='სახელი', example='ლუკა'),
    'last_name': fields.String(required=False, description='გვარი', example='ვარსიმაშვილი'),
    'username': fields.String(required=False, description='მომხმარებელი', example='01124096118'),
    'email': fields.String(required=True, description='ელ-ფოსტა', example='luka.varsimashvili@iliauni.edu.ge'),
    'phone_number': fields.String(required=True, description='ტელეფონის ნომერი', example='592159199'),
    'balance': fields.Float(required=True, description='ბალანსი', example=63.52),
    'role_id': fields.Integer(required=True, description='როლის ID', example=2),
})


# users_parser = reqparse.RequestParser()

# users_parser.add_argument("station_name", required=True, type=str, help="შეიყვანეთ სადგურის სახელი")
# users_parser.add_argument("url", required=True, type=str, help="შეიყვანეთ სადგურის wunderground-ის ლინკი")
# users_parser.add_argument("api", required=True, type=str, help="შეიყვანეთ სადგურის wunderground-ის API-ის ლინკი")
# users_parser.add_argument("latitude", required=True, type=float, help="შეიყვანეთ განედი")
# users_parser.add_argument("longitude", required=True, type=float, help="შეიყვანეთ გრძედი")
# users_parser.add_argument("status", required=True, type=inputs.boolean, help="შეიყვანეთ სტატუსი")