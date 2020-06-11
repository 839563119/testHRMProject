#导包os模块
import os
#定义全局变量base_dir,通过base_dir定位到项目的根目录
BASE_DIR =os.path.dirname(os.path.abspath(__file__))
#请求头
HEADERS= None
#定义员工ID
EMP_ID=None