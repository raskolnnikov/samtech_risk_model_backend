import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            password=data['password'],
            org=data['org'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Email in use. Please login.',
        }
        return response_object, 409

def update_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        user.email = data['email']
        user.org = data['org']
        save_changes(user)
        response_object = {
            'status': 'Success',
            'message': 'User updated successfully.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User doesnt exist.',
        }
        return response_object, 409


def toggle_user_admin(user_public_id):
    user = User.query.filter_by(public_id=user_public_id).first()
    if user:
        user.admin = not user.admin
        save_changes(user)
        response_object = {
            'status': 'Success',
            'message': 'User updated successfully.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User doesn''t exist.',
        }
        return response_object, 409


def toggle_user_active(user_public_id):
    user = User.query.filter_by(public_id=user_public_id).first()
    if user:
        user.active = not user.active
        save_changes(user)
        response_object = {
            'status': 'Success',
            'message': 'User updated successfully.',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User doesn''t exist.',
        }
        return response_object, 409

def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def get_all_clients(public_id):
    return User.query.filter_by(public_id=public_id).first().clients


def get_all_analysis(public_id):
    return User.query.filter_by(public_id=public_id).first().analysis


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'user': {
                'id': user.public_id,
                'email': user.email,
                'admin_flag': user.admin
            },
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()
