import requests
import json

# Create a session
session = requests.Session()

url = 'https://shopee.vn/api/v4/account/login_by_password'

# Headers as per your curl command
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Referer': 'https://shopee.vn/buyer/login?from=https%3A%2F%2Fshopee.vn%2Fuser%2Fpurchase%2F&next=https%3A%2F%2Fshopee.vn%2Fuser%2Fpurchase%2F',
    'X-Shopee-Language': 'vi',
    'X-Requested-With': 'XMLHttpRequest',
    'X-API-SOURCE': 'pc',
    'Origin': 'https://shopee.vn',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'TE': 'trailers'
}

# Data payload as per your curl command
# Replace 'your_email' and 'your_password' with the actual values
data = {
    'email': 'bluec2311@gmail.com',
    'password': '974d40ced6bc6d28c6debc9a6454964a864a905107140634d126f87e58f364aa',
    'support_ivs': True,
    'client_identifier': {
        'security_device_fingerprint': '46EVGtx+Xx3N74btQMYjpA==|uHuFfC2z2/pMGOIbZCCHpjNbsveXpjZ0dqHZ877GdoEUQgbR84os7q6gMXEA6X1RAwxQ0lSxsYE/a8E=|5t7xuSv3cwvdfFaL|08|3'
    }
}

# Sending the POST request using the session
response = session.post(url, headers=headers, json=data)

# Handling the response
if response.status_code == 200:
    print("Request successful.")
    # Process the response
    print(response.json())
else:
    print(f"Request failed: {response.status_code} - {response.text}")