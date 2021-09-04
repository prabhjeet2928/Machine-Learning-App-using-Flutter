#!/usr/bin/python3

import cgi
import pickle

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
satisfaction = mydata.getvalue('satisfaction')
loyalty = mydata.getvalue('loyalty')

my_kmeans_model = pickle.load(open('kmeans.pk1', 'rb'))

result = my_kmeans_model.predict([[satisfaction,loyalty]])

if result[0] == 0:
   print("This category comes in First Cluster Group")
elif result[0] == 1:
   print("This category comes in Second Cluster Group")
else:
   print("This category comes in Third Cluster Group")
