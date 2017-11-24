from arrested import ArrestedAPI

from .characters import characters_resource
from .middleware import basic_auth
from .users import users_resource


api_v1 = ArrestedAPI(url_prefix='/v1', before_all_hooks=[basic_auth])
api_v1.register_resource(users_resource, defer=True)
api_v1.register_resource(characters_resource, defer=True)
