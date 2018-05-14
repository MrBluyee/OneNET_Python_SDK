# Python based SDK of OneNET HTTP protocol device
## 环境：Python 3.6
## 库依赖：urllib3 、 urllib 、os 、json
## 说明：onenet_http_api模块使用非常简单，使用该模块，用户不需要将精力放在网络通信接口上，而可以更多的去关注数据内容。

### 开始使用：
import 模块：
```Python
>>> import onenet_http_api
```
然后创建一个OneNetHTTPHandle实例。该实例处理与OneNet以HTTP协议通信的所有内容。
```Python
>>> h = onenet_http_api.OneNetHTTPHandle()
```
## API介绍：
### 设备：
#### 1.注册设备：
```Python
register_device(master_key,register_code,new_device_authinfo,new_device_name)
```
参数：
master_key: 为产品的APIKEY<br>
register_code: 正式环境注册码<br>
new_device_authinfo: 新建HTTP设备的设备唯一编号<br>
new_device_name: 新建HTTP设备的设备名<br>
返回：<br>
若成功，则返回一个包含device_id和key的dict<br>
若失败，则返回错误信息<br>


例：<br>
```Python
>>> master_key = '6K9Nxxxxxxxxxxxxxxxxxx'
>>> register_code = '1Wxxxxxxxxxxxx3'
>>> new_device_authinfo = '201805141201'
>>> new_device_name = 'device1'
>>> h.register_device(master_key,register_code,new_device_authinfo,new_device_name)
{'device_id': '31036923', 'key': 'VfmTxxxxxxxxxxxxxxx'}
```
