import unittest
import json
import pandas as pd

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            compile("".join(i['source']), '<string>', 'exec')

lego2019 = pd.read_csv("lego2019.csv")

class testCases(unittest.TestCase):

    def testPrice(self):
      truth = pd.read_csv("tests/files/answer.csv")

      self.assertTrue(float(lego2019.loc[lego2019['Set']=='Frozen Ice Castle', 'Price_Euro'])==49.99, "The prices you scraped do not match the prices on the results page.")
