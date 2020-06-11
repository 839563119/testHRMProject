#登录参数话
# 导包
import unittest
import logging
import app

# 创建测试类
from api.employee import EmployeeApi
from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLoginParams(unittest.TestCase):
    # 初始化unnitte的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 实现登录接口
    def test01_login_success(self):
        # 发送登录接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)