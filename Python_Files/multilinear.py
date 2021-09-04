#!/usr/bin/python3

import cgi
import pickle

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
rd_spend = mydata.getvalue('rd_spend')
administration = mydata.getvalue('admin')
marketing_spend = mydata.getvalue('marketing')
state = mydata.getvalue('state')

my_mln_model = pickle.load(open('50_startups.pk1', 'rb'))

if state == "California":
    result = my_mln_model.predict([[rd_spend,administration,marketing_spend,1,0]])
elif state == "Florida":
    result = my_mln_model.predict([[rd_spend,administration,marketing_spend,0,1]])
elif state == "New York":
    result = my_mln_model.predict([[rd_spend,administration,marketing_spend,0,0]])

print("Profit for StartUps is Rs.{:.2f}".format(result[0]))
