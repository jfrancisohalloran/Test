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

    def testSetnames(self):
      truth = pd.read_csv("tests/files/answer.csv")

      self.assertTrue(all(list(truth['Set'])[i] == list(lego2019['Set'])[i] for i in range(20)), "The sets you scraped do not match the sets on the results page.")
