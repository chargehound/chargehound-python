from collections import namedtuple
from bunch import Bunch


class ChargehoundObject(Bunch):
    pass


class List(ChargehoundObject):
    pass


class Dispute(ChargehoundObject):
    pass


class Product(ChargehoundObject):
    pass


Response = namedtuple('Response', 'status')
