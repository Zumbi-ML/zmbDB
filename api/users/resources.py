# encoding: utf-8
from flask import request
from flask_restx import Resource, Namespace, fields

user = Namespace('User', description='User resources')
user_mdl = user.model('UserModel', {
    'hash': fields.Integer,
    'name': fields.String
})

@user.route('/')
class UserResource(Resource):
    @user.response(200, "Success")
    def get(self):
        return {"data": [400, 500, 600], "message": "Success"}, 200

    @user.expect(user_mdl)
    def post(self):
        return True, 200

@user.route('/<id>')
class UserIdResource(Resource):
    @user.response(200, "Success")
    def get(self, id:int):
        return {f"{str(id)}": {"name": f"name {str(id)}"}, "message": "Success"}, 200
