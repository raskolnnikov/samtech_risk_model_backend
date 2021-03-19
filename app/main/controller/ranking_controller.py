from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from app.main.service.auth_helper import Auth

from ..util.dto import RankingEntryDto
from ..service.ranking_service import get_latest_ranking_list

api = RankingEntryDto.api
_ranking_entry = RankingEntryDto.ranking_entry

@api.route('/')
class Ranking(Resource):
    @api.doc('Operations related to the risk index ranking.')
    #@token_required
    @api.marshal_list_with(_ranking_entry, envelope='data')
    def get(self):
        """List all registered users"""
        response = get_latest_ranking_list()
        if not response:
            api.abort(404)
        else:
            return response
