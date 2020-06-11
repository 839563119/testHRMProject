# 导包
import requests


# 创建封装接口类
class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    def login(self, jsonData, headers):
        """

        :param jsonData:
        :param headers:
        :return:
        """
        # 发送登录请求
        return requests.post(url=self.login_url, json=jsonData, headers=headers)
