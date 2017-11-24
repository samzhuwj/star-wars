from kim import field

from .base import BaseMapper
from star_wars.models import Character


class CharacterMapper(BaseMapper):
    __type__ = Character

    name = field.String()
