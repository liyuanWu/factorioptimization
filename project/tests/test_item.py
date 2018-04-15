import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from main.item import ItemFactory,TechFactory
from main.itemMetaConfig import *

class itemTest(unittest.TestCase):
    def test_load_item(self):
        itemFactory = ItemFactory()
        self.assertNotEqual(len(itemFactory),0)

        accumulator_name = 'Accumulator'
        accumulator = itemFactory.getItem(accumulator_name)
        self.assertEqual(accumulator.name, accumulator_name)
        self.assertEqual(accumulator.getFieldWithKeys((ITEM_NAME,)), accumulator_name)
    
    def test_load_tech(self):
        techFactory = TechFactory()
        self.assertNotEqual(len(techFactory),0)

if __name__ == '__main__':
    unittest.main()