from tools.api import request_tool

# 增加产品
def test_hwx_addProd(pub_data):
    pub_data["productCode"] =  "自动生成 字符串 5 数字 hwx"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token":pub_data["token"],'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "阿迪达斯",
  "colors": [
    "黑色","白色"
  ],
  "price": 10000,
  "productCode":"${productCode}",
  "productName": "boost",
  "sizes": [
    "40","41"
  ],
  "type": "shoes"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

# 查询商品
def test_hwx_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token":pub_data["token"],'Host': 'qa.yansl.com:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://qa.yansl.com:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}
    json_path=[{"skuCode":'$.data[0].skuCode'}]


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    headers = {"token":pub_data["token"],'Host': 'qa.yansl.com:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://qa.yansl.com:8084', 'Referer': 'http://qa.yansl.com:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '213', 'skuCode': '${skuCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

