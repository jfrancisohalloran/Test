import unittest
import json
import pandas as pd
import re

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

class testCases(unittest.TestCase):

    def testWriteFile(self):

      self.assertTrue(bool(re.search(r".to_csv[(]['\"]lego2019.csv['\"]",source)), "Your code does not create a file named `lego2019.csv`.")
