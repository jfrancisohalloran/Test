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

    def testColnames(self):
      truth = pd.read_csv("tests/files/answer.csv")

      self.assertTrue(all(truth.columns[i] == lego2019.columns[i] for i in range(len(truth.columns))), "Your dataset does not contain all of the required columns.")
