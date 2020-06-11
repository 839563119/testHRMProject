# 导入requests
import requests

# 发送登录接口请求
response = requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 打印登录的结果
print("登录结果为：", response.json())
# 提取登录返回的令牌
token = 'Bearer ' + response.json().get('data')
print("提取的令牌为：", token)
# 发送添加员工的接口
headers = {"Content-Type": "application/json", "Authorization": token}
response = requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/user",
                         json={"username": "夏目友人帐5", "mobile": "15127209873", "timeOfEntry": "2012-05-05",
                               "formOfEmployment": 1,
                               "departmentName": "测试部",
                               "departmentId": "1063678149528784896",
                               "correctionTime": "2020-05-30T16:00:00.000Z"
                               },
                         headers=headers)
# 打印添加员工的接口
print("添加员工的接口返回数据为：", response.json())
# 提取添加员工返回的id
emp_id = response.json().get("data").get("id")
print("提取的员工id:", emp_id)

# 拼接查询员工接口的url
query_url = "http://ihrm-test.itheima.net" + "/api/sys/user" + "/" + emp_id
# 发送查询员工的接口请求
response = requests.get(url=query_url, headers=headers)
print("拼接查询员工接口的请求", response.json())

#拼接修改员工的接口请求
modify_url="http://ihrm-test.itheima.net" + "/api/sys/user" + "/" + emp_id
response =requests.put(url=modify_url,json={"username":"夏目的烦恼"},headers=headers)
print("拼接修改员工接口请求",response.json())

#拼接删除员工的接口请求
delecte_url="http://ihrm-test.itheima.net" + "/api/sys/user" + "/" + emp_id
response=requests.delete(url=delecte_url,headers=headers)
print("拼接删除员工接口请求",response.json())