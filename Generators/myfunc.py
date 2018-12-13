import requests
def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def multiply (a, b):
    return a*b

# response = requests.get("http://sm.qa.cww.comodo.od.ua/domains")
#
# print(response.status_code)
# print(response.headers["content-type"])
# print(response.json())