import requests

url = "https://entp.yjj.gxzf.gov.cn/appnet/appEntpDetail.action?entpId=1649309&entpType=007"

# payload = {
#     "xkzbh":"sc",
#     "zszl":"00102",
#     "fzjg":"",
#     "rows":20,
#     "page":1
# }
headers = {
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Cookie': 'C9nvPf17Htt4O=5S_E0U4BHfkEa6sZy5jhCv2ft0OADKV9SGEuq5Xee9P1mKcJNHLZa32i3ufcGy2rFC2hyT4RbX0El4PP1ANEY2A; 849899999d514676a3=2849534d163fd9d6a7384fb2986215a1; JSESSIONID=0DEFAF7DE7AC515A25B5D4DBDE49107E; C9nvPf17Htt4P=b7B2QcNNmU7k5fYbYFr_5EqFSgQd3GeJEAIBnZzloHE_UhKMKUdMP7JsBkFr8PdqgTjnaP25mSKRpfKdYTQh2vVJp7Uc8ju7.dKJ437mafxsjW5uGtnF3ddGdU9FY9F3m0jfd8Kqn0gNc.N0yHuYCmT.N5PLDfikiJuQMq6ByQxaDQc_t3SxG57LEySpnazFNbSNrzng2XqsHSfDqgJTPoIEkxcj7cfMAr7v1RXkoaGuZVggteAfzkwwoH1a_Ppk5dnfg.O0MKtcE5AMWqgnCAF9ZjDhjohKeMevL_B2Ev050jXKQ9iKAejrWlxc1.65Y8qMrXAOHhlNYVOwyjKPfVl_lpH8FVoiN2EdfoMaaJU2XUCPT8cfOda8nvBdX_ehfpcnue1BsDIy4h23mw_JyaoNtBsEnCpPvqs6PHA9DEVWkF5FGGa6qIJqp2vFV2sS'
}

# response = requests.request("GET", url, headers=headers, data=payload)
response = requests.request("GET", url)

print(response.text)