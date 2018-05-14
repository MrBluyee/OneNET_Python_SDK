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
参数：<br>
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
#### 2.获取指定设备的信息
```Python
get_device_info(key,device_id)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
返回：<br>
若成功，则返回一个包含设备信息的dict<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.get_device_info(key,device_id)
{'private': True, 'protocol': 'HTTP', 'create_time': '2018-05-14 12:02:40', 
'keys': [{'title': 'auto generated device key', 'key': 'VfmTxxxxxxxxxxxxxxxx='}],
 'online': False, 'id': '31xxxx', 'auth_info': '201805141201', 'title': 'device1'}
```
#### 3.获取所有设备的信息：
```Python
get_all_devices_info(master_key)
```
参数：<br>
master_key：masterkey<br>
返回：<br>
若成功，则返回一个包含所有设备信息的dict<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.get_all_devices_info(master_key)
```
#### 4.修改设备信息：
```Python
modify_device_profile(key,device_id,**profile)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
可选参数：<br>
"title": "mydevice", //设备名（可选，最长16个字符）<br>
"desc": "some description", //设备描述（可选，最长16个字符）<br>
"tags": ["china","mobile"] , //设备标签（可选）<br>
"protocol":"HTTP ", //选择一种接入协议（可选）<br>
"location": {"lon":106, "lat": 29, "ele": 370},//设备位置{"经度", "纬度", "高度"}（可选）<br>
"private": true| false, //设备私密性（可选）<br>
"auth_info":"201503041a5829151", //HTTP设备："设备唯一编号"（可选）<br>
"other": {"version": "1.0.0", "manufacturer": "china mobile"} //其他信息（可选）<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> profile = {
... 'title': 'mydevice',
... 'desc': 'some description',
... 'tags': ['china','mobile'],
... 'auth_info': '201805141226'}
>>> h.modify_device_profile(key,device_id,**profile)
'succ'
```
或：
```Python
>>> h.modify_device_profile(key,device_id,title = 'device1')
'succ'
```
#### 5.删除设备：
```Python
delete_device(key,device_id)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>

说明：删除设备会删除该设备下所有数据流和数据点。<br>
删除设备动作是异步的，系统会在后续逐步删除该设备下的数据流和数据点。<br>
例：<br>
```Python
>>> h.delete_device(key,device_id)
'succ'
```
### 数据流：
#### 1.创建数据流：
（建议在网页上通过设置数据流模板代替）
```Python
create_device_datastream(key,device_id,stream_id,**profile)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
stream_id：数据流名称<br>
可选参数：<br>
"tags":["Tag1","Tag2"], //数据流标签（可选，可以为一个或多个）<br>
"unit":"celsius", //单位（可选）<br>
"unit_symbol":"C" //单位符号（可选）<br>
返回：<br>
若成功，则返回包含ds_uuid的dict<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> stream_id = 'datastream'
>>> h.create_device_datastream(key,device_id,stream_id)
{'ds_uuid': '8a9497b0-8863-58a6-8277-xxxxxxxxxxxxxxxxxx'}
```
#### 2.修改数据流参数：
```Python
modify_device_datastream_profile(key,device_id,stream_id,**profile)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
stream_id：数据流名称<br>
可选参数：<br>
"tags":["Tag1","Tag2"], //数据流标签（可选，可以为一个或多个）<br>
"unit":"celsius", //单位（可选）<br>
"unit_symbol":"C" //单位符号（可选）<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> modify_profile = {
... 'tags': ['Tag1','Tag2'],
... 'unit': 'celsius',
... 'unit_symbol': 'C'}
>>> h.modify_device_datastream_profile(key,device_id,stream_id,**modify_profile)
'succ'
```
#### 3.获取数据流：
```Python
get_device_datastream(key,device_id,stream_id)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
stream_id：数据流名称<br>
返回：<br>
若成功，则返回包含数据流信息的dict<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.get_device_datastream(key,device_id,stream_id)
[{'unit': 'celsius', 'create_time': '2018-05-14 12:35:12', 'unit_symbol': 'C', 'id': 'datastream', 'uuid': '8a9497b0-8863-58a6-8277-xxxxxxx', 'tags': ['Tag1', 'Tag2']}]

```
#### 4.删除数据流：
```Python
delete_device_datastream(key,device_id,stream_id)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
stream_id：数据流名称<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.delete_device_datastream(key,device_id,stream_id)
'succ'
```
### 数据点：
#### 1.新增数据点：
```Python
post_datapoints(key,device_id,datapoints)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
datapoints：数据点<br>
datapoints格式为：<br>
datapoints = {stream_id:data}<br>
可选参数：<br>
local_timestamp：本地时间戳<br>
格式必须为"YYYY-MM-DDThh:mm:ss"的形式<br>
(例如：2018-05-14T13:21:12）<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> datapoints = {
... stream_id:10}
>>> h.post_datapoints(key,device_id,datapoints)
'succ'

>>> datapoints = {
... stream_id:'hello'}
>>> h.post_datapoints(key,device_id,datapoints)
'succ'

>>> datapoints = {
... stream_id:20}
>>> h.post_datapoints(key,device_id,datapoints,local_timestamp = '2018-05-14T13:21:12')
'succ'
```
#### 2.获取数据点：
```Python
get_datapoints(key,device_id,**args)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
可选参数：<br>
datastream_id=a,b,c //查询的数据流，多个数据流之间用逗号分隔（可选）<br>
start=2015-01-10T08:00:35 //提取数据点的开始时间（可选）<br>
end=2015-01-10T08:00:35 //提取数据点的结束时间（可选）<br>
duration=3600 //查询时间区间（可选，单位为秒）<br>
（start+duration：按时间顺序返回从start开始一段时间内的数据点）<br>
（end+duration：按时间倒序返回从end回溯一段时间内的数据点）<br>
limit=100 //限定本次请求最多返回的数据点数，0<n<=6000（可选，默认1440）<br>
cursor= //指定本次请求继续从cursor位置开始提取数据（可选）<br>
sort=DESC | ASC //值为DESC|ASC时间排序方式，DESC:倒序，ASC升序，<br>
（带任何参数或仅携带limit参数-默认降序，其他情况-默认升序）<br>
返回：<br>
若成功，则返回选择获取的数据点<br>
若失败，则返回错误信息<br>
说明：<br>
1.若不携带任何可选参数，返回本设备所存在的所有数据流中的最新数据。<br>
2.若不携带数据流id参数，携带limit参数时，会返回该设备每个数据流最多limit条数据。<br>
其他情况limit参数用于限制返回数据点总数。<br>
3.若要查看某一条数据流数据，需在可选参数中携带参数datastream_id。<br>
4.要查看某一条数据流在某个时间范围内的数据，可以在增加start和end参数。<br>
例：<br>
```Python
>>> h.get_datapoints(key,device_id)
{'count': 1, 'datastreams': [{'datapoints': [{'at': '2018-05-14 13:21:12.000', 'value': 20}], 'id': 'datastream'}]}

>>> h.get_datapoints(key,device_id,datastream_id = stream_id)
{'count': 1, 'datastreams': [{'datapoints': [{'at': '2018-05-14 13:26:12.878', 'value': 'hello'}], 'id': 'datastream'}]}
```
### 二进制数据流：
#### 1.新增二进制数据流：
```Python
post_bindata(key,device_id,stream_id,bindata)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
stream_id：数据流名称<br>
bindata: 要上传的普通二进制数据<br>
返回：<br>
若成功，则返回二进制数据索引号<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> bindata = 'hello world!'
>>> h.post_bindata(key,device_id,stream_id,bindata)
{'index': '31037105_xxxxxxxxxxx0_datastream'}
```
#### 2.获取二进制数据流：
```Python
get_bindata(key,data_index)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
data_index：二进制数据索引号<br>
返回：<br>
若成功，则返回二进制数据<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.get_bindata(key,data_index)
b'hello world!'
```
#### 3.新增文件：
```Python
post_file(key,device_id,stream_id,file_path)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
device_id： device_id<br>
stream_id：数据流名称<br>
file_path: 要上传的文件路径（包含文件名）<br>
文件、图像等（最大限制为800k）<br>
返回：<br>
若成功，则返回文件索引号<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> file_path = '1.jpeg'
>>> h.post_file(key,device_id,stream_id,file_path)
{'index': '31037105_1xxxxxxxxxx_datastream'}
```
#### 4.获取文件：
```Python
get_file(key,file_index)
```
参数：<br>
key：为masterkey 或者 设备apikey<br>
file_index：文件索引号<br>
可选参数：<br>
file_path： 保存的文件路径（不含文件名）<br>
否则保存在当前程序运行目录<br>
例：<br>
```Python
>>> h.get_file(key,file_index)
>>>
```
（文件已保存在当前程序运行目录）<br>
### 触发器：
触发器的含义是：当指定范围内的数据点满足触发条件的要求时，会向url参数指定的地址发送post请求。
#### 1.创建触发器：
```Python
create_trigger(master_key,url,trigger_type,trigger_threshold,**args)
```
参数：<br>
master_key：masterkey<br>
url:例："http://xx.bb.com"<br>
trigger_type：> | >= | < | <= | == | inout | in | out | change | frozen | live<br>
trigger_threshold：阙值。<br>
说明：<br>
1) type为>|>=|<|<=|==时，threshold必须为数值。<br>
2) type为inout时，threshold设置为{"lolmt":40, "uplmt":52}， 表示数据流的值首次进入或离开闭区间[40,52]时触发；<br>
3) type为change时，threshold 参数不用传递；当上传的值有改变时触发告警。<br>
4) type为frozen时，threshold 为数值，指定多少秒内未上报数据触发告警，同时被监控对象进入frozen状态。<br>
5) type为live时，threshold为数值（必选大于0），指定当前上报数据点时间距离上次上报数据点时间间隔超过多少秒触发告警，一般与frozen配合使用。<br>
可选参数：<br>
"title":"wen du jian kong", //设备名（可选）<br>
"ds_id":"gps", //数据流名称（id）（可选）<br>
"dev_id":"1027", //设备ID（可选）<br>
"ds_uuids"://数据流uuid（可选）<br>
说明：<br>
触发器有三种工作触发模式<br>
1)在请求参数中单独指定了ds_id，不包括其他参数，那么当前项目下所有设备的数据流中数据流名称符合ds_id的数据都会进入触发判断逻辑；<br>
2)在请求参数中单独指定了ds_uuids数组，那么只有这些指定的数据流会进入触发判断逻辑；<br>
3)在请求参数中指定了ds_id和dev_ids，那么只有这些指定的设备的数据流会进入触发判断逻辑。<br>
返回：<br>
若成功，则返回触发器ID<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.create_trigger(master_key,url,'>',10,ds_id = stream_id)
{'trigger_id': 112410}

>>> h.create_trigger(master_key,url,'>',10,ds_id = stream_id,dev_id = device_id)
{'trigger_id': 112411}
```
#### 2.修改触发器参数：
```Python
modify_trigger(master_key,trigger_id,**args)
```
参数：<br>
master_key：masterkey<br>
trigger_id：触发器ID<br>
可选参数：<br>
"title":"wen du jian kong", //设备名（可选）<br>
"ds_id":"gps", //数据流名称（id）（可选）<br>
"dev_id":"1027", //设备ID（可选）<br>
"ds_uuids": //数据流uuid（可选）<br>
"url":"//xx.bb.com",<br>
"type":"> | >= | < | <= | == | inout | in | out | change | frozen | live",<br>
"threshold":100 <br>
说明：<br>
1.可选参数ds_id、dev_id、ds_uuids至少要传入一个。<br>
2.要修改type或者threshold时，必须同时传入这两个参数才能够生效。<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.modify_trigger(master_key,trigger_id,ds_id = stream_id,type = '>=',threshold = 100)
'succ'
```
#### 3.获取指定触发器信息：
```Python
get_trigger_info(master_key,trigger_id)
```
参数：<br>
master_key：masterkey<br>
trigger_id：触发器ID<br>
返回：<br>
若成功，则返回触发器信息<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.get_trigger_info(master_key,trigger_id)
{'create_time': '2018-05-14 14:07:26', 'target_type': 0, 'threshold': 100, 'id': 112411, 'type': '>=', 'ds_id': 'datastream', 'url': 'http://www.mrbluyee.com'}
```
#### 4.获取所有触发器信息：
```Python
get_all_triggers_info(master_key)
```
参数：<br>
master_key：masterkey<br>
返回：<br>
若成功，则返回所有触发器信息<br>
若失败，则返回错误信息<br>
例：<br>
```Python
>>> h.get_all_triggers_info(master_key)
```
#### 5.删除触发器：
```Python
delete_trigger(master_key,trigger_id)
```
参数：<br>
master_key：masterkey<br>
trigger_id：触发器ID<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
```Python
>>> h.delete_trigger(master_key,trigger_id)
'succ'
```
### APIKEY:
#### 1.创建APIKey：
```Python
create_apikey(master_key,key_title,resources,access_methods)
```
参数：<br>
master_key：masterkey<br>
key_title： key的名称<br>
resources：被授权的资源<br>
参数格式：<br>
resources = ({"dev_id": device_id1},{"dev_id": device_id2})<br>
access_methods：被授权的命令<br>
参数格式：<br>
access_methods =（'get','put')<br>
说明：授权命令是可选的，另外被授权的命令也可以是get、put、post的一个或几个，如只授权get和put命令："access_methods": \["get","put"]<br>
返回：<br>
若成功，则返回key_string<br>
若失败，则返回错误信息<br>
#### 2.修改APIKey：
```Python
modify_apikey(master_key,key_string,**args)
```
参数：<br>
master_key：masterkey<br>
key_string： key_string<br>
可选参数：<br>
title： key的名称<br>
resources：被授权的资源<br>
access_methods：被授权的命令<br>
说明：<br>
1.对于master key不允许更新操作，masterkey默认具有最大权限，可以访问该用户名下所有设备、所有数据，可以进行POST、GET、PUT、DELETE操作。<br>
如果更新master key系统会返回失败。<br>
2..API key更新是覆盖操作，会将原来存在的授权资源和授权命令覆盖，不会保留原来的授权资源和授权命令。<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
#### 3.获取APIKey信息：
```Python
get_apikey_info(master_key,**args)
```
参数：<br>
master_key：masterkey<br>
可选参数：<br>
key = key_string//可选，只查看该key相关信息<br>
page = 1 //指定页码, 可选<br>
per_page = 10 //指定每页输出个数,可选,默认10，最多100<br>
device_id = xxbbcc//可选,只查看与该设备相关的非master-key<br>
返回：<br>
若成功，则返回APIKey信息<br>
若失败，则返回错误信息<br>
#### 4.删除APIKey：
```Python
delete_apikey(master_key,key_string)
```
参数：<br>
master_key：masterkey<br>
key_string： key_string<br>
返回：<br>
若成功，则返回'succ'<br>
若失败，则返回错误信息<br>
