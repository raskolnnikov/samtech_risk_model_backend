from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from app.main.service.auth_helper import Auth

from ..util.dto import DetallePatenteDiaDto
from ..service.detalle_patente_dia_service import get_patente_history, get_patente_ranking_change, get_component_series, get_decision_plot, get_geofences

api = DetallePatenteDiaDto.api
_detail = DetallePatenteDiaDto.detail

@api.route('/<patente>')
class PatentDayDetail(Resource):
    @api.doc('Operations related to the detailed recent activity of a patent.')
    #@token_required
    @api.marshal_list_with(_detail, envelope='data')
    def get(self, patente):
        """List all registered users"""
        response = get_patente_history(patente, 10)
        if not response:
            api.abort(404)
        else:
            return response

@api.route('/<patente>/series/')
class PatentDaySeries(Resource):
    @api.doc('Operations related to the time series of a patent''s activity.')
    #@token_required
    #@api.marshal_list_with(_detail, envelope='data')
    def get(self, patente):
        """List all registered users"""
        response = get_component_series(patente)
        if not response:
            api.abort(404)
        else:
            return response

@api.route('/<patente>/decision_plot/<step_id_week>')
class PatentDecisionPlot(Resource):
    @api.doc('Operations related to the visualization of the model''s decision.')
    #@token_required
    #@api.marshal_list_with(_detail, envelope='data')
    def get(self, patente, step_id_week):
        """List all registered users"""
        print(patente)
        print(step_id_week)
        response = get_decision_plot(patente, step_id_week)
        if not response:
            api.abort(404)
        else:
            return response

@api.route('/<patente>/geofences/<step_id_week>')
class PatentGeofences(Resource):
    @api.doc('Operations related to the visualization of the model''s geofences.')
    #@token_required
    #@api.marshal_list_with(_detail, envelope='data')
    def get(self, patente, step_id_week):
        """List all registered users"""
        print(patente)
        print(step_id_week)
        response = get_geofences(patente, step_id_week)
        if not response:
            api.abort(404)
        else:
            return response
