# -*- coding: utf-8 *-*
import unittest
import module_name

from pymongo import MongoClient


class TestPyMongoOps(unittest.TestCase):

    def setUp(self):
        foo = module_name.MyClassFromModule()
        foo.run()

        self.db_name = 'dbname'
        self.collection_name = 'col'

        self.conn = MongoClient()
        self.db = self.conn[self.db_name]
        self.collection = self.db[self.collection_name]

        self.conn.drop_database(self.db_name)

    def tearDown(self):
        self.conn.drop_database(self.db_name)

    def test_insertion(self):
        self.collection.insert({'name': 'Jorge', 'last': u'Puente Sarrín'})
        doc = self.collection.find_one({'name': 'Jorge'})
        self.assertEquals(doc['last'], u'Puente Sarrín')
