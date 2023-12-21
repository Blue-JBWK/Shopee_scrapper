import requests
import csv
import json
from tqdm import tqdm
# URL for the GET request
url = 'https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11035567&limit=60&offset=0'

# Headers based on your curl command
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
    # 'Accept-Encoding': 'gzip, deflate, br',
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
    'Connection': 'keep-alive',
    # 'Cookie': '_gcl_au=1.1.484966276.1703145432; _med=affiliates; csrftoken=BOoeaEOuPTTu3CqcHb5bZRTlYyJei7fl; _sapid=2049be44f8a63d21050ef4ae47d0148ff5fdf7a2af5a3f3a9e5ac55d; SPC_SI=s2+BZQAAAABsSHlVUDB5WPKVIQAAAAAAYzc2STdGdWY=; SPC_SEC_SI=v1-MFFjU3ZMempUeVBHOU02bY++geQjQa4gwsRvL2atTnhmDd7HBk+pFeC8tFDuNvvE7VSsG1v7ZfhavC5XnJAEK80l7SK7TGtgzXu6lERLLu8=; _QPWSDCXHZQA=b44f1e7f-7f3b-4c34-b5b4-24ecf5c68177; REC7iLP4Q=98af4814-7c84-4e7b-8b71-30bb29207457; _ga_4GPP1ZXG63=GS1.1.1703162070.5.1.1703164833.0.0.0; _ga=GA1.2.267206771.1703145434; _fbp=fb.1.1703145433506.2027171804; SPC_T_ID=tQ2X4CnjcPeTZs27vdoike3OHy/USbkbmfLVzdKz/bbWinZZ94ur5sygTC29hZy+h9mFnFw4HV3TcCitzyyIAVi6YlSUJLkxAv9ep0GY8E1Zwmb6UFihcQ4BRpZSFloojd+E9UAh+6lz8dNObk6bdEgPSeJcxXVD996AuJhuIAw=; SPC_T_IV=djBjaWhSVnFram9rM000NA==; SPC_F=JP1HBbYqT0kA60x8Ck1J3GfjCyfL10vl; REC_T_ID=8d24c7a2-9fd6-11ee-b637-92d0ee91ef2f; SPC_R_T_ID=tQ2X4CnjcPeTZs27vdoike3OHy/USbkbmfLVzdKz/bbWinZZ94ur5sygTC29hZy+h9mFnFw4HV3TcCitzyyIAVi6YlSUJLkxAv9ep0GY8E1Zwmb6UFihcQ4BRpZSFloojd+E9UAh+6lz8dNObk6bdEgPSeJcxXVD996AuJhuIAw=; SPC_R_T_IV=djBjaWhSVnFram9rM000NA==; _gid=GA1.2.408444429.1703145435; shopee_webUnique_ccd=YF4IZnXUjqraQ%2B1XLUwlxg%3D%3D%7CvHuFfC2z2%2FpMGOIbZCCHpjNbsveXpjZ0dqHZ8%2FBogYEUQgbR84os7q6gMXEA6X1RAwxQ0lSxsYE%2Fa8E%3D%7C5t7xuSv3cwvdfFaL%7C08%7C3; ds=ad9eabc005d88616ae5c9fb2346faabc; _hjSessionUser_868286=eyJpZCI6IjllYTZkMWFkLTUwOWQtNTM2Yi1hZWEyLWIxYWI3MzRmY2IzMCIsImNyZWF0ZWQiOjE3MDMxNDU0MzUxODUsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_868286=0; SPC_CLIENTID=SlAxSEJiWXFUMGtBcahihdachfobvrmc; SPC_U=291346699; _ga_3XVGTY3603=GS1.1.1703162009.2.1.1703162224.60.0.0; SPC_SC_SA_TK=; SPC_SC_SA_UD=; AMP_TOKEN=%24NOT_FOUND; _hjSession_868286=eyJpZCI6ImQ0NTkxMjQyLTRmMjMtNGY1NS1iNWNmLTk5N2U1YWI3MjVmYiIsImMiOjE3MDMxNjIwNzAyODEsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; _ga_FV78QC1144=GS1.1.1703162197.1.0.1703162198.59.0.0; SPC_EC=.SmpRRGI3cUVhbnh2Nk9XTzjtTGmXQfzFq3Mqd+YEI4tH5buJPQ59dRqNeRtDaBM3VYUNkvKTgGrpCd4UXbqTUScO2fTasb1OseKQjSZspNVOLtrgqdoZbeynA2knp22wDHi0R4VXY47zO2XSGO5dpt7ceIHyMVUBJeoHdMpZYb8ltyyJKxsFa+GuUduUecX1hSmUcvuMJKMxElPSG3bCL2pDWT2FCAKa9tL2/Wk5/K8=; SPC_ST=.SmpRRGI3cUVhbnh2Nk9XTzjtTGmXQfzFq3Mqd+YEI4tH5buJPQ59dRqNeRtDaBM3VYUNkvKTgGrpCd4UXbqTUScO2fTasb1OseKQjSZspNVOLtrgqdoZbeynA2knp22wDHi0R4VXY47zO2XSGO5dpt7ceIHyMVUBJeoHdMpZYb8ltyyJKxsFa+GuUduUecX1hSmUcvuMJKMxElPSG3bCL2pDWT2FCAKa9tL2/Wk5/K8=',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'bundle': 'category_landing_page',
    'cat_level': '2',
    'catid': '11035567',
    'limit': '500',
    'offset': '0',
}

categories = requests.get('https://shopee.vn/api/v4/pages/get_category_tree',cookies=cookies,headers=headers)
categories_json = categories.json()
#print(categories.json())
parent_id = []
child_id = []

for category in categories_json["data"]["category_list"]:
    parent_id.append(category["catid"])
    if category["children"]:
        for child in category["children"]:
            child_id.append(child["catid"])

print(parent_id)
print(child_id)

for cat_id in tqdm(child_id, desc="Processing Categories"):
    # Update the offset in the parameters
    params['catid'] = str(cat_id)

    # Send the request

    response = requests.get('https://shopee.vn/api/v4/recommend/recommend', params=params, cookies=cookies,headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        #print(f"Response received successfully.")
        data = response.json()
        extracted_data = []
        for section in data['data']['sections']:
            for item in section.get('data', {}).get('item', []):
                product_id = item.get('itemid')
                product_name = item.get('name')
                product_rating = item.get('item_rating', {}).get('rating_star')
                product_price = item.get('price')
                historical_sold = item.get('historical_sold')
                product_revenue = product_price * historical_sold

                # Construct product URL
                product_url = f"https://shopee.vn/product/{item['shopid']}/{product_id}"

                # Append the extracted data
                extracted_data.append({
                    'product_id': product_id,
                    'product_name': product_name,
                    'product_url': product_url,
                    'product_rating': product_rating,
                    'product_price': product_price,
                    'historical_sold': historical_sold,
                    'product_revenue': product_revenue
                })
        csv_file = "products.csv"
        csv_columns = ['product_id', 'product_name', 'product_url', 'product_rating', 'product_price',
                       'historical_sold',
                       'product_revenue']

        with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)

            # Write only the header if the file is new/empty
            if csvfile.tell() == 0:
                writer.writeheader()

            for data in extracted_data:
                writer.writerow(data)

        #print(f"Data written to {csv_file}")

    else:
        print( "is empty")