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
            source = "".join(i['source'])
            compile(source, '<string>', 'exec')

lego2019 = pd.read_csv("lego2019.csv")

class testCases(unittest.TestCase):

    def testFunction(self):

      self.assertTrue("def collectLegoSets(" in source, "The `collectLegoSets` function is not defined in your code.")