## Check that the duration column (between checkout and return) is an integer 
## Check that the same column is above zero
## Do any other function you've created (or mine)

import unittest
import pandas as pd
from nirosh_code import fileLoader, duplicateCleaner, naCleaner, dateCleaner, enrich_dateDuration

data = fileLoader('./data/03_Library Systembook.csv')
data = duplicateCleaner(data)
data = naCleaner(data)
for col in ['Book checkout', 'Book Returned']:
        data = dateCleaner(col, data)
data = enrich_dateDuration(df=data, colA='Book Returned', colB='Book checkout')

class TestOperations(unittest.TestCase):

    #test duration column is an integer
    def test_duration_is_int(self):
         for d in data['date_delta']:
            self.assertTrue(d is int, "value is not int")
    
    #test duration column is above zero
    def test_duration_is_above_0(self):
         for d in data['date_delta']:
            self.assertGreater(d, 0, "value not greater than 0")

if __name__ == '__main__':
    unittest.main()