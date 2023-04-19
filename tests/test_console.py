#!/usr/bin/python3
''' Test suite for the console'''


import sys
import models
import unittest
from unittest.mock import create_autospec
from os import getenv
from console import HBNBCommand
from io import StringIO

db = getenv("HBNB_TYPE_STORAGE", "fs")

class test_console(unittest.TestCase):
    ''' Test cases for the console module '''

    def setUp(self):
        ''' setup before execution '''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        ''' tear down after execution '''
        sys.stdout = self.backup
