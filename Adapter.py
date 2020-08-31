import json
import requests
from collections import OrderedDict
response=requests.get("http://220.227.12.140:8081/Violation/GetViolationByTimePeriodDetails?FromDate=2019-11-0800:00:00&ToDate=2019-11-08%2020:15:00&StartPage=1&EndPage=1")
new_data=response.json()
result=new_data['timePeriodViolation']
print(result)
l=len(result)
list_of_data=[]
for i in range(l):
    rs_data = {}
    try:
        rs_data["id"] = "resource-server-name/resource-group-name/resource-item-name"
        rs_data["resourceGroup"] = "varanasi property echallan tax by ward wise"
        rs_data["ViolationId"] = result[i]['ViolationId']
        rs_data["ViolationName"] = result[i]['ViolationName']
        rs_data["EqpId2"] = result[i]['EqpId2']
        rs_data["JunctionName"] = result[i]['JunctionName']
        rs_data["OwnerName"] = result[i]['OwnerName']
        rs_data["OwnerAddress"] = result[i]['OwnerAddress']
        rs_data["Mobile"] = result[i]['Mobile']
        rs_data["ViolationType"] = result[i]['ViolationType']
        rs_data["EqpId"] = result[i]['EqpId']
        rs_data["VehicleColor"] = result[i]['VehicleColor']
        rs_data["MakeModel"] = result[i]['MakeModel']
        rs_data["ChallanAmount"] = result[i]['ChallanAmount']
        rs_data["PaymentStatus"] = result[i]['PaymentStatus']
        rs_data["ImageFileName"] = result[i]['ImageFileName']
        rs_data["ChallanType"] = result[i]['ChallanType']
        list_of_data.append(rs_data)
    except Exception as e:
        print("error in process_response")
        print(e)
print(json.dumps(list_of_data, indent=4))
with open("modified_Adapter.json", "w+") as outs:
    json.dump(list_of_data, outs, indent=4)

