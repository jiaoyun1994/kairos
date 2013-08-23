'''
Functional tests for mongo timeseries
'''
import time
import datetime

from pymongo import *
from chai import Chai

from . import helpers
from .helpers import unittest, os

@unittest.skipUnless( os.environ.get('TEST_MONGO','true').lower()=='true', 'skipping mongo' )
class MongoSeriesTest(helpers.SeriesHelper):

  def setUp(self):
    self.client = MongoClient('localhost')
    super(MongoSeriesTest,self).setUp()

@unittest.skipUnless( os.environ.get('TEST_MONGO','true').lower()=='true', 'skipping mongo' )
class MongoHistogramTest(helpers.HistogramHelper):

  def setUp(self):
    self.client = MongoClient('localhost')
    super(MongoHistogramTest,self).setUp()

@unittest.skipUnless( os.environ.get('TEST_MONGO','true').lower()=='true', 'skipping mongo' )
class MongoCountTest(helpers.CountHelper):

  def setUp(self):
    self.client = MongoClient('localhost')
    super(MongoCountTest,self).setUp()

@unittest.skipUnless( os.environ.get('TEST_MONGO','true').lower()=='true', 'skipping mongo' )
class MongoGaugeTest(helpers.GaugeHelper):

  def setUp(self):
    self.client = MongoClient('localhost')
    super(MongoGaugeTest,self).setUp()

@unittest.skipUnless( os.environ.get('TEST_MONGO','true').lower()=='true', 'skipping mongo' )
class MongoGregorianTest(helpers.GregorianHelper):

  def setUp(self):
    self.client = MongoClient('localhost')
    super(MongoGregorianTest,self).setUp()
