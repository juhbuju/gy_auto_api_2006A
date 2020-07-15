import random

import allure
import requests
from config.conf import API_URL

@allure.feature("用户管理")# 一级分类
@allure.story("充值提现模块")#  二级分类
@allure.title("扣款接口-账户余额不足")# 修改用例标题
def test_recharge_1(db):
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
    account_name = random.choice(res)[0]
    data = {
        "accountName": account_name,
        "changeMoney": 2020
    }
    r = requests.post(API_URL+"/acc/charge",json=data)
    print(r.text)

@allure.feature("用户管理")# 一级分类
@allure.story("扣款记录")#  二级分类
@allure.title("扣款接口-账户余额不足")# 修改用例标题
def test_recharge_2(db):
    with allure.step("第1步、执行sql语句"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
    with allure.step("第2步、从查询结果中随机获取一条，取第一个数据"):
        account_name = random.choice(res)[0]
    with allure.step("第3步、准备请求数据"):
        data = {
        "accountName": account_name,
        "changeMoney": 2020
    }
    with allure.step("第4步、发送请求"):
        r = requests.post(API_URL+"/acc/charge",json=data)
    with allure.step("第5步、获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求方法",allure.attachment_type.TEXT)
    with allure.step("第6步、获取响应内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响应正文",allure.attachment_type.TEXT)
    with allure.step("第7步、断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("账户余额不足","预期结果",allure.attachment_type.TEXT)
        assert "账户余额不足" in r.text