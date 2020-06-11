#实现员工管理模块
#导包
import requests
#获取登录接口
respose = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                        json={"mobile":"13800000002","password":"123456"},
                        headers={"Content-Type":"application/json"})
#查看登录结果
print("登录结果为：",respose.json())