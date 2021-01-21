# import requests
# URL = 'http://13.124.188.64:3000/dbinsert'
# data = {'minor_1' : '10', 'rssi_1' : '10', 'tx_1' : '10',
#         'minor_2' : '10', 'rssi_2' : '10', 'tx_2' : '10',
#         'minor_3' : '10', 'rssi_3' : '10', 'tx_3' : '10',}
# res = requests.post(URL, data=data)
# print(res.status_code)
# print(res.raise_for_status())
# print(res.json())


data = {'1': [1,2,3], '2': [2,3,4], '3': [3,4,5], '4': [4,5,6], '5': [5,6,7]}

a = sorted(data.items(), key=lambda item: item[1][2], reverse=True)

print(a)
