# -*- coding: utf-8 -*
import time

print('new person tag param bulid-begin')
baseDemo = '{"data":[{"key":"feepay","value":0}],"dataId":"86_572950","modelCode":"vender","time":1660896307228}'
base1 = '{"data":[{"key":"o2o_global_sell_new_user_pay","value":0}],"dataId":"'
base2 = '","modelCode":"user","time":'
base3 = '}'
timeStr = str(int(time.time()) * 1000)
dataId = raw_input('plz input dataId:')
print(base1 + str(dataId) + base2 + timeStr + base3)
print('new person tag param bulid-end. click anywhere to exit~~')
dataId = raw_input()
# 1660902351605
# 1660902389000
# 1660902335
