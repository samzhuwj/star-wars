from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin

from .mappers import CharacterMapper
from star_wars.models import Character, db

characters_resource = Resource('characters', __name__, url_prefix='/characters')


class CharactersIndexEndpoint(KimEndpoint, DBListMixin):
    name = 'list'
    many = True
    mapper_class = CharacterMapper
    model = Character

    def get_query(self):

        stmt = db.session.query(Character)
        return stmt


characters_resource.add_endpoint(CharactersIndexEndpoint)
