#!/usr/bin/python3

import cgi
import pickle

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
age = mydata.getvalue('age')
estimated_salary = mydata.getvalue('salary')

my_random_model = pickle.load(open('random_forest.pk1', 'rb'))
sc = pickle.load(open('scaler.pkl', 'rb'))

result = my_random_model.predict(sc.transform([[age,estimated_salary]]))

if result[0] == 0:
   print("It is not Purchased")
else:
   print("It is Purchased")
