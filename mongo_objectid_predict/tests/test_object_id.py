import unittest

from mongo_objectid_predict.object_id import ObjectId


class TestObjectId(unittest.TestCase):

    SAMPLE = '61246a8c642e3500218b264b'

    def test_parse_str(self):
        o = ObjectId(self.SAMPLE)
        self.assertEqual(str(o), self.SAMPLE)

    def test_looks_like(self):
        self.assertTrue(ObjectId.looks_like(self.SAMPLE))
