#import modules
import json
import requests
import sys

#define r as response from api.coindesk.com
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#define rate and convert it into float
rate = float(json.dumps(r.json()["bpi"]["USD"]["rate"], indent=2).replace("\"", "").replace(",",""))

#try to convent quantity into float. if it's not possible exit via error message
try:
    quantity = float(sys.argv[1])
except:
    sys.exit("Error")

#define amount as multiplication of quantity and rate
amount = quantity * rate

print(f"${amount:,.4f}")
