#!/usr/bin/python3

import cgi
import pickle

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
yearexp = mydata.getvalue('yearexp')

my_ln_model = pickle.load(open('salarydata.pk1', 'rb'))

result = my_ln_model.predict([[yearexp]])

print("Salary for {} experience is Rs.{:.2f}".format(yearexp,result[0]))
