import requests
import sys

acces_key = input("Give the right acces key in the fixer.io")
url = "http://data.fixer.io/api/latest?access_key="+acces_key
firstCurrency=input("Which currency do you transform? ")
howMuch=input("How much money do you have: ")
response=requests.get(url)
json_data=response.json()
try:
    print(float(json_data["rates"][firstCurrency])*float(howMuch),firstCurrency)
except KeyError:
    sys.stderr.write("Please Enter the correct CURRENCY")
    sys.stderr.flush()



