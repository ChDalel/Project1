def currencyconversion():


print('Please enter the code of the currency to convert from:')
f=input()
print('Please enter the code of the currency to convert to:')
t=input()
print('Please enter a date with this format => YYYY-MM-DD:')
d=input()
api='4976d29d2ffb43259ac94f12ff54646d'
url = 'http://api.coinlayer.com/convert? access_key = 4976d29d2ffb43259ac94f12ff54646d & from = f& to = t& amount = 10 &date = d'
params = {'access_key': api, 'from': f,'to':t, 'amount': 10,'date':d}
r = requests.get('http://api.coinlayer.com/convert', params = params)
convcoin = r.json()
print (convcoin)    
