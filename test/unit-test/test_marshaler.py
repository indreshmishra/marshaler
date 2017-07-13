import unittest2
from rwork.marshaler import CommonObject

class Address(CommonObject):

    def __init__(self):
        self.address =None
        self.state = None
        self.city = None
        self.country = None

class User(CommonObject):

    def __init__(self, address:Address=None):
        self.name=None
        self.contact_number=None
        self.address = address

class TestMarshaler(unittest2.TestCase):

    def test_deserialization(self):
        st = '{"name":"User1","address":{"address":"test address","state":"NY","country":"US"}}'
        u = User()
        u.load_deep_json(st)
        self.assertTrue(u.name=='User1')
        self.assertTrue(u.address.country=='US')
        print(u.name)
        print(u.address.country)
