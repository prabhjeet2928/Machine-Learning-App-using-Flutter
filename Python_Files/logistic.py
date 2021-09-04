#!/usr/bin/python3

import cgi
import pickle

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
age = mydata.getvalue('age')
pclass = mydata.getvalue('pclass')
sex = mydata.getvalue('sex')
sibsp = mydata.getvalue('sibsp')
embarked = mydata.getvalue('embarked')
parch = mydata.getvalue('parch')

my_lr_model = pickle.load(open('titanic.pk1','rb'))

if pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]])


elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0]])


elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])

elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0]])

elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]])

elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]])

elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]])

elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "3"and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]])
elif pclass == "1" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]])










elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]])


elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0]])

elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0]])

elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]])

elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]])

elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]])

elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "3"and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]])
elif pclass == "2" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]])








elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "0":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0]])


elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "1":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0]])

elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "2":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0]])

elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "3":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0]])

elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "4":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]])

elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "5":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]])

elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "S" and parch == "6":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0]])

elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "C" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "3"and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "8" and embarked == "Q" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "0" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "0" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "1" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "1" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "2" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "2" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "3" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "3" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "4" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "4" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "5" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "female" and sibsp == "5" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1]])
elif pclass == "3" and sex == "male" and sibsp == "8" and embarked == "S" and parch == "9":
    result = my_lr_model.predict([[age,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]])
else:
    result = my_lr_model.predict([[age,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]])

if result[0] == 0:
    print("This is Not Survived")
else:
    print("This is Survived")
