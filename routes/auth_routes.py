from flask import Blueprint, render_template, request
from controllers.auth_controller import handle_register, handle_login, handle_logout

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
	return render_template('index.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
	return handle_register(request)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
	return handle_login()

@auth_bp.route('/logout')
def logout():
	return handle_logout()
