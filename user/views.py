from flask import Blueprint
from user.models import User

user_page = Blueprint('user_page', __name__)

@user_page.route('/login')
def login():
    user = User(name='Raymond', password='123', email='email@gmail.com')
    user.save()
    return 'Hello, {}! Your email address is {}'.format(user.name, user.email)