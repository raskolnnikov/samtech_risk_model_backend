from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.detalle_patente_dia_controller import api as detail_ns
from .main.controller.ranking_controller import api as ranking_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Samtech Weekly Risk Model API',
          version='1.0',
          description='API for accessing the risk scores and related information from truck telematics.'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(detail_ns, path='/detail')
api.add_namespace(ranking_ns, path='/ranking')
api.add_namespace(auth_ns)
