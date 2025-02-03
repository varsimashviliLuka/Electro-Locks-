from flask_restx import reqparse, inputs
from src.extensions import api


auth_ns = api.namespace('Authentification', description='API მომხმარებლის აუტენტიფიკაციის შესახებ', path='/api')

registration_parser = reqparse.RequestParser()

registration_parser.add_argument('name', type=str, required=True, help="გთხოვთ შეიყვანეთ სახელი")
registration_parser.add_argument('last_name', type=str, required=True, help="გთხოვთ შეიყვანეთ გვარი")
registration_parser.add_argument('username', type=str, required=True, help="გთხოვთ შეიყვანეთ მომხმარებელი")

registration_parser.add_argument('phone_number', type=str, required=True, help="გთხოვთ შეიყვანეთ ტელეფონის ნომერი")
registration_parser.add_argument('email', type=inputs.email(check=True), help="გთხოვთ შეიყვანეთ მეილი (luka.varsimashvili@iliauni.edu.ge)")

registration_parser.add_argument('role_name', type=str, required=False, default='user', help="შეიყვანეთ როლი (user/admin)")

registration_parser.add_argument('password', type=str, required=True, help="გთხოვთ შეიყვანეთ პაროლი")
registration_parser.add_argument('passwordRepeat', type=str, required=True, help='გთხოვთ გაიმეორეთ პაროლი')



# Auth parser
auth_parser = reqparse.RequestParser()
auth_parser.add_argument("username", required=True, type=str, help="გთხოვთ შეიყვანეთ მეილი (luka.varsimashvili@iliauni.edu.ge)")
auth_parser.add_argument("password", required=True, type=str, help="გთხოვთ შეიყვანეთ პაროლი")