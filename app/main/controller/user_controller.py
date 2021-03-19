from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from app.main.service.auth_helper import Auth

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, update_user, toggle_user_active, toggle_user_admin

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully updated.')
    @api.doc('updates a new user')
    def put(self):
        """Updates a new User """
        data = request.json
        return update_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user, envelope='data')
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/<public_id>/toggle_admin')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @admin_token_required
    @api.doc('Toggle the user''s admin status')
    def put(self, public_id):
        """Toggle the user''s admin status"""
        response = toggle_user_admin(public_id)
        if not response:
            api.abort(404)
        else:
            return response

@api.route('/<public_id>/toggle_active')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @admin_token_required
    @api.doc('Toggle the user''s active status')
    def put(self, public_id):
        """Toggle the user''s active status"""
        response = toggle_user_active(public_id)
        if not response:
            api.abort(404)
        else:
            return response
