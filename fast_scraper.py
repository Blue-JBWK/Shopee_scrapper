import asyncio
import aiohttp
import csv
import requests
from tqdm import tqdm
import random
import time
from urllib.parse import urljoin, urlencode



url = 'https://shopee.vn/api/v4/recommend/recommend'

cookies = {
    '_gcl_au': '1.1.484966276.1703145432',
    '_med': 'affiliates',
    'csrftoken': 'BOoeaEOuPTTu3CqcHb5bZRTlYyJei7fl',
    '_sapid': '2049be44f8a63d21050ef4ae47d0148ff5fdf7a2af5a3f3a9e5ac55d',
    'SPC_SI': 's2+BZQAAAABsSHlVUDB5WPKVIQAAAAAAYzc2STdGdWY=',
    'SPC_SEC_SI': 'v1-MFFjU3ZMempUeVBHOU02bY++geQjQa4gwsRvL2atTnhmDd7HBk+pFeC8tFDuNvvE7VSsG1v7ZfhavC5XnJAEK80l7SK7TGtgzXu6lERLLu8=',
    '_QPWSDCXHZQA': 'b44f1e7f-7f3b-4c34-b5b4-24ecf5c68177',
    'REC7iLP4Q': '98af4814-7c84-4e7b-8b71-30bb29207457',
    '_ga_4GPP1ZXG63': 'GS1.1.1703162070.5.1.1703164833.0.0.0',
    '_ga': 'GA1.2.267206771.1703145434',
    '_fbp': 'fb.1.1703145433506.2027171804',
    'SPC_T_ID': 'tQ2X4CnjcPeTZs27vdoike3OHy/USbkbmfLVzdKz/bbWinZZ94ur5sygTC29hZy+h9mFnFw4HV3TcCitzyyIAVi6YlSUJLkxAv9ep0GY8E1Zwmb6UFihcQ4BRpZSFloojd+E9UAh+6lz8dNObk6bdEgPSeJcxXVD996AuJhuIAw=',
    'SPC_T_IV': 'djBjaWhSVnFram9rM000NA==',
    'SPC_F': 'JP1HBbYqT0kA60x8Ck1J3GfjCyfL10vl',
    'REC_T_ID': '8d24c7a2-9fd6-11ee-b637-92d0ee91ef2f',
    'SPC_R_T_ID': 'tQ2X4CnjcPeTZs27vdoike3OHy/USbkbmfLVzdKz/bbWinZZ94ur5sygTC29hZy+h9mFnFw4HV3TcCitzyyIAVi6YlSUJLkxAv9ep0GY8E1Zwmb6UFihcQ4BRpZSFloojd+E9UAh+6lz8dNObk6bdEgPSeJcxXVD996AuJhuIAw=',
    'SPC_R_T_IV': 'djBjaWhSVnFram9rM000NA==',
    '_gid': 'GA1.2.408444429.1703145435',
    'shopee_webUnique_ccd': 'YF4IZnXUjqraQ%2B1XLUwlxg%3D%3D%7CvHuFfC2z2%2FpMGOIbZCCHpjNbsveXpjZ0dqHZ8%2FBogYEUQgbR84os7q6gMXEA6X1RAwxQ0lSxsYE%2Fa8E%3D%7C5t7xuSv3cwvdfFaL%7C08%7C3',
    'ds': 'ad9eabc005d88616ae5c9fb2346faabc',
    '_hjSessionUser_868286': 'eyJpZCI6IjllYTZkMWFkLTUwOWQtNTM2Yi1hZWEyLWIxYWI3MzRmY2IzMCIsImNyZWF0ZWQiOjE3MDMxNDU0MzUxODUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjIncludedInSessionSample_868286': '0',
    'SPC_CLIENTID': 'SlAxSEJiWXFUMGtBcahihdachfobvrmc',
    'SPC_U': '291346699',
    '_ga_3XVGTY3603': 'GS1.1.1703162009.2.1.1703162224.60.0.0',
    'SPC_SC_SA_TK': '',
    'SPC_SC_SA_UD': '',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_hjSession_868286': 'eyJpZCI6ImQ0NTkxMjQyLTRmMjMtNGY1NS1iNWNmLTk5N2U1YWI3MjVmYiIsImMiOjE3MDMxNjIwNzAyODEsInMiOjAsInIiOjAsInNiIjoxfQ==',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga_FV78QC1144': 'GS1.1.1703162197.1.0.1703162198.59.0.0',
    'SPC_EC': '.SmpRRGI3cUVhbnh2Nk9XTzjtTGmXQfzFq3Mqd+YEI4tH5buJPQ59dRqNeRtDaBM3VYUNkvKTgGrpCd4UXbqTUScO2fTasb1OseKQjSZspNVOLtrgqdoZbeynA2knp22wDHi0R4VXY47zO2XSGO5dpt7ceIHyMVUBJeoHdMpZYb8ltyyJKxsFa+GuUduUecX1hSmUcvuMJKMxElPSG3bCL2pDWT2FCAKa9tL2/Wk5/K8=',
    'SPC_ST': '.SmpRRGI3cUVhbnh2Nk9XTzjtTGmXQfzFq3Mqd+YEI4tH5buJPQ59dRqNeRtDaBM3VYUNkvKTgGrpCd4UXbqTUScO2fTasb1OseKQjSZspNVOLtrgqdoZbeynA2knp22wDHi0R4VXY47zO2XSGO5dpt7ceIHyMVUBJeoHdMpZYb8ltyyJKxsFa+GuUduUecX1hSmUcvuMJKMxElPSG3bCL2pDWT2FCAKa9tL2/Wk5/K8=',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567',
    'X-Shopee-Language': 'vi',
    'X-Requested-With': 'XMLHttpRequest',
    'X-API-SOURCE': 'pc',
    'If-None-Match-': '55b03-151f9dce207e84fbb38dfa7bfdaee1a2',
    'x-sap-ri': 'a23b8465ff73d9e026c3ea360301f489c4682e401914f5e53a1d',
    'x-sap-sec': '03mpuuRmlzzzzzzzyRzbzzAzyRzzzzAzzzzlzzzzRzbzzjzmzzzjzzzz+COss5RzzzzRzRzzgzbzziOKdaXTmlRFf56HjcpFBEdF5MqxZiMFnCjP5UeaMfdhFLmGNW5NwMoz31WmNX5HtWXr9W4LRJdkruolNh6PseKb8P5w9KrXtYI1Pr3bEec+f31bI8tRtBlMZcCrre3sox7Ts3AXgUBaszP9odVti5JxvQXZe5WMW9VA2NKImm2ulInwgupQp2og3Su/y4diBIAAPKYoo5NjC8IKEfNStTLN2rLf04+36nk6JetT8H/QTn5OwsSZvl+JIYsv61AetaZDZK2+QhspsZrkxtu+dZaf53eF+XShb47kKb0WMUTEyMnzUn1thBViK2CZTcQ/n76PgRAStbwwysAMAMZ5EHWX+pnpVYmG+az6mLbUn2mtaa8aLJZXkxlmVvlCK1pzKQFaaC3bA1gV/YUI9KbeBy5SBxM04nv6O6+ZvrEihhUPV3DCD6D10Sq5CezPqzBS8AWyk9VmYECxcFPdvflLzat0gz5oN9VkvcjIidfYjqqyFXz+qMT0yL8JZ6Xcj1vAgd50QDxeDC4y1eYeyPUI3RV9YlJsLca6AK0i3z6wGnpPlcgWfRTF6mCEtW9rnorLUNaMc2Nwk2K+ch0MTCUVhSFxZVaOtzzMP6DesayHYJSKueANznQ5giOR6qa19sPNdpAO4vCS9pA+ZEMvP5RrKCiWrLSS8xgIxTM1um0gbJfv3weVJk7Wk0i5E7F8MPr6WRhrkn63ZMLFmzzzzlN5YPb4YIzkzzzzzwIssspbzzzzfzzzzyAzzzmx8QPg3tYwF27SmhgsfDjZKldOjRRzzzyQwlT+1lwk1Azzzzzbzz5zmzzjzzRzzzzbzzzzfzzzzyAzzzz+m7x8we0IyYCZzB6PXPIZROlxvzuzzzzSV89dwMwIzC==',
    'af-ac-enc-sz-token': 'YF4IZnXUjqraQ+1XLUwlxg==|vHuFfC2z2/pMGOIbZCCHpjNbsveXpjZ0dqHZ8/BogYEUQgbR84os7q6gMXEA6X1RAwxQ0lSxsYE/a8E=|5t7xuSv3cwvdfFaL|08|3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive'
}

params = {
    'bundle': 'category_landing_page',
    'cat_level': '2',
    'limit': '500',
    'offset': '0'
}

def login(email, password):
    login_url = 'https://shopee.vn/api/v4/account/login_by_password'
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
    data = {
        'email': email,
        'password': password,
        'support_ivs': True,
        'client_identifier': {
            'security_device_fingerprint': '46EVGtx+Xx3N74btQMYjpA==|uHuFfC2z2/pMGOIbZCCHpjNbsveXpjZ0dqHZ877GdoEUQgbR84os7q6gMXEA6X1RAwxQ0lSxsYE/a8E=|5t7xuSv3cwvdfFaL|08|3'
        }
    }
    session = requests.Session()
    response = session.post(login_url, headers=headers, json=data)
    if response.status_code == 200:
        print("Login successful.")
        return session
    else:
        print(f"Login failed: {response.status_code} - {response.text}")
        return None

def convert_cookies(requests_cookies):
    return {c.name: c.value for c in requests_cookies}
async def fetch(session, url, params, proxies):
    proxy = random.choice(proxies)
    try:
        async with session.get(url, params=params, proxy=proxy) as response:
            if response.status == 200:
                print("Working proxies:" + proxy)
                return await response.json()
            else:
                print("error" + proxy)
                proxies.remove(proxy)
                return {'error': True, 'status': response.status}
    except Exception as e:
        return {'error': True, 'message': f'Error in fetch with proxy {proxy}: {str(e)}'}

async def fetch_all(session, url_params_pairs, proxies):
    results = await asyncio.gather(
        *[fetch(session, url, params, proxies) for url, params in url_params_pairs],
        return_exceptions=True
    )
    return results


def process_response(data):
    extracted_data = []
    for section in data['data']['sections']:
        for item in section.get('data', {}).get('item', []):
            product_id = item.get('itemid')
            product_name = item.get('name')
            product_rating = item.get('item_rating', {}).get('rating_star')
            product_price = item.get('price')
            historical_sold = item.get('historical_sold')
            product_revenue = product_price * historical_sold
            product_url = f"https://shopee.vn/product/{item['shopid']}/{product_id}"

            extracted_data.append({
                'product_id': product_id,
                'product_name': product_name,
                'product_url': product_url,
                'product_rating': product_rating,
                'product_price': product_price,
                'historical_sold': historical_sold,
                'product_revenue': product_revenue
            })
    return extracted_data


def write_to_csv(extracted_data, csv_file, csv_columns):
    with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        if csvfile.tell() == 0:
            writer.writeheader()
        for data in extracted_data:
            writer.writerow(data)

def format_proxy(file_path):
    with open(file_path, 'r') as file:
        proxies = file.read().splitlines()
    formatted_proxies = []
    for proxy in proxies:
        formatted_proxies.append("http://" +proxy)
    return formatted_proxies

async def main():
    tic = time.perf_counter()
    email = 'bluec2311@gmail.com'
    password = '974d40ced6bc6d28c6debc9a6454964a864a905107140634d126f87e58f364aa'

    # Perform login to set the cookies if needed
    # session_requests = login(email, password)
    # if session_requests:
    #     # Convert cookies for aiohttp
    #     cookies = convert_cookies(session_requests.cookies)
    file_path = 'proxies.txt'  # Replace with your actual file path
    formatted_proxies = format_proxy(file_path)
    print(formatted_proxies)
    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        categories = await session.get('https://shopee.vn/api/v4/pages/get_category_tree')
        categories_json = await categories.json()

    child_id = [child["catid"] for category in categories_json["data"]["category_list"] for child in
                category["children"] if category["children"]]

    url_params_pairs = [(url, {**params, 'catid': str(cat_id)}) for cat_id in child_id]

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        responses = await fetch_all(session, url_params_pairs, formatted_proxies)

    csv_file = "products.csv"
    csv_columns = ['product_id', 'product_name', 'product_url', 'product_rating', 'product_price', 'historical_sold',
                   'product_revenue']
    #print(responses)
    for response in responses:
        if response and not response.get('error'):
            extracted_data = process_response(response)
            write_to_csv(extracted_data, csv_file, csv_columns)
        else:
            print(f"Error in response: {response}")
    toc = time.perf_counter()
    print(f"Done in {toc - tic:0.4f} seconds")


# Run the main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
row_count = sum(1 for line in open('products.csv'))
print("Total line got is " + str(row_count))