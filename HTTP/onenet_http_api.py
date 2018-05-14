# -*- coding: UTF-8 -*-

__author__ = 'Mr.Bluyee'

import urllib3
from urllib.parse import urlencode
import json
import os

class OneNetHTTPHandle(object):
	def __init__(self):
		self.http = urllib3.PoolManager()
	
	def register_device(self,master_key,register_code,new_device_authinfo,new_device_name):
		header = {'api-key': master_key}
		encoded_args = urlencode({'register_code':register_code})
		data = {'sn': new_device_authinfo, 'title': new_device_name}
		encoded_data = json.dumps(data).encode('utf-8')
		url = 'http://api.heclouds.com/register_de?' + encoded_args
		r = self.http.request('POST', url, body=encoded_data, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
	
	def delete_device(self,key,device_id):
		header = {'api-key': key}
		url = 'http://api.heclouds.com/devices/' + device_id
		r = self.http.request('DELETE', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		return result['error']
	
	def get_all_devices_info(self,master_key):
		header = {'api-key': master_key}
		url = 'http://api.heclouds.com/devices'
		r = self.http.request('GET', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']		
		
	def get_device_info(self,key,device_id):
		header = {'api-key': key}
		url = 'http://api.heclouds.com/devices/' + device_id
		r = self.http.request('GET', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
	
	def modify_device_profile(self,key,device_id,**profile):
		"""
		"title": "mydevice", //设备名（可选，最长16个字符）
		"desc": "some description", //设备描述（可选，最长16个字符）
		"tags": ["china","mobile"] , //设备标签（可选）
		"protocol":"HTTP ", //选择一种接入协议（可选）
		"location": {"lon":106, "lat": 29, "ele": 370},//设备位置{"经度", "纬度", "高度"}（可选）
		"private": true| false, //设备私密性（可选）
		"auth_info":"201503041a5829151", //HTTP设备："设备唯一编号"（可选）
		"other": {"version": "1.0.0", "manufacturer": "china mobile"} //其他信息（可选）
		"""
		header = {'api-key': key}
		data = {}
		if 'title' in profile:
			data['title'] = profile['title']
		if 'desc' in profile:
			data['desc'] = profile['desc']
		if 'tags' in profile:
			data['tags'] = profile['tags']
		if 'protocol' in profile:
			data['protocol'] = profile['protocol']
		if 'location' in profile:
			data['location'] = profile['location']
		if 'private' in profile:
			data['private'] = profile['private']
		if 'auth_info' in profile:
			data['auth_info'] = profile['auth_info']
		if 'other' in profile:
			data['other'] = profile['other']
		if len(data) > 0:
			encoded_data = json.dumps(data).encode('utf-8')
			url = 'http://api.heclouds.com/devices/' + device_id
			r = self.http.request('PUT', url, body=encoded_data, headers = header)
			result = json.loads(r.data.decode('utf-8'))
			return result['error']
	
	def create_device_datastream(self,key,device_id,stream_id,**profile):
		"""
		"id":"temperature" //数据流名称 示例：温度
		"tags":["Tag1","Tag2"], //数据流标签（可选，可以为一个或多个）
		"unit":"celsius", //单位（可选）
		"unit_symbol":"C" //单位符号（可选）
		"""
		header = {'api-key': key}
		data = {'id': stream_id}
		if 'tags' in profile:
			data['tags'] = profile['tags']
		if 'unit' in profile:
			data['unit'] = profile['unit']
		if 'unit_symbol' in profile:
			data['unit_symbol'] = profile['unit_symbol']
		encoded_data = json.dumps(data).encode('utf-8')
		url = 'http://api.heclouds.com/devices/' + device_id +'/datastreams'
		r = self.http.request('POST', url, body=encoded_data, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
	
	def modify_device_datastream_profile(self,key,device_id,stream_id,**profile):
		"""
		"tags":["Tag1","Tag2"], //数据流标签（可选，可以为一个或多个）
		"unit":"celsius", //单位（可选）
		"unit_symbol":"C" //单位符号（可选）
		"""
		header = {'api-key': key}
		data = {}
		if 'tags' in profile:
			data['tags'] = profile['tags']
		if 'unit' in profile:
			data['unit'] = profile['unit']
		if 'unit_symbol' in profile:
			data['unit_symbol'] = profile['unit_symbol']
		if len(data) > 0:
			encoded_data = json.dumps(data).encode('utf-8')
			url = 'http://api.heclouds.com/devices/' + device_id +'/datastreams/' + stream_id
			r = self.http.request('PUT', url, body=encoded_data, headers = header)
			result = json.loads(r.data.decode('utf-8'))
			return result['error']
			
	def get_device_datastream(self,key,device_id,stream_id):
		header = {'api-key': key}
		url = 'http://api.heclouds.com/devices/' + device_id + '/datastreams'
		r = self.http.request('GET', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
	
	def delete_device_datastream(self,key,device_id,stream_id):
		header = {'api-key': key}
		url = 'http://api.heclouds.com/devices/' + device_id + '/datastreams/' + stream_id
		r = self.http.request('DELETE', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		return result['error']
		
	def post_datapoints(self,key,device_id,datapoints,local_timestamp = 'not use'):
		header = {'api-key': key}
		data = {}
		if local_timestamp != 'not use':
			"""如果local_timestamp存在,其格式必须为"YYYY-MM-DDThh:mm:ss"的形式
			（例如：2015-03-22T22:31:12）
			"""
			encoded_args = urlencode({'type':4})
			for stream_id in datapoints:
				datapoint = {local_timestamp: datapoints[stream_id]}
				data[stream_id] = datapoint
		else:
			encoded_args = urlencode({'type':3})
			for stream_id in datapoints:
				data[stream_id] = datapoints[stream_id]
		encoded_data = json.dumps(data).encode('utf-8')
		url = 'http://api.heclouds.com/devices/' + device_id +'/datapoints?' + encoded_args
		r = self.http.request('POST', url, body=encoded_data, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		return result['error']
			
	def get_datapoints(self,key,device_id,**args):
		"""
		datastream_id=a,b,c //查询的数据流，多个数据流之间用逗号分隔（可选）
		start=2015-01-10T08:00:35 //提取数据点的开始时间（可选）
		end=2015-01-10T08:00:35 //提取数据点的结束时间（可选）
		duration=3600 //查询时间区间（可选，单位为秒）
		start+duration：按时间顺序返回从start开始一段时间内的数据点
		end+duration：按时间倒序返回从end回溯一段时间内的数据点
		limit=100 //限定本次请求最多返回的数据点数，0<n<=6000（可选，默认1440）
		cursor= //指定本次请求继续从cursor位置开始提取数据（可选）
		sort=DESC | ASC //值为DESC|ASC时间排序方式，DESC:倒序，ASC升序，
		（带任何参数或仅携带limit参数-默认降序，其他情况-默认升序）
		</n<=6000（可选，默认1440）
		"""
		header = {'api-key': key}
		field = {}
		if 'datastream_id' in args:
			field['datastream_id'] = args['datastream_id']
		if 'start' in args:
			field['start'] = args['start']
		if 'end' in args:
			field['end'] = args['end']
		if 'duration' in args:
			field['duration'] = args['duration']
		if 'limit' in args:
			field['limit'] = args['limit']
		if 'cursor' in args:
			field['cursor'] = args['cursor']
		if 'sort' in args:
			field['sort'] = args['sort']
		if len(field) == 0:
			field['newadd'] = True
		url = 'http://api.heclouds.com/devices/' + device_id +'/datapoints'
		r = self.http.request('GET', url,fields = field, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
		
	def post_bindata(self,key,device_id,stream_id,bindata):
		"""
		HTTP内容: 普通二进制数据（最大限制为800k）
		"""
		header = {'api-key': key}
		encoded_args = urlencode({'device_id':device_id,'datastream_id':stream_id})
		url = 'http://api.heclouds.com/bindata?' + encoded_args
		r = self.http.request('POST', url, body = bindata, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
			
	def post_file(self,key,device_id,stream_id,file_path):
		"""
		HTTP内容: 文件、图像等（最大限制为800k）
		"""
		if os.path.exists(file_path) == False:
			raise FileExistsError('No exist file!')
		file_name = os.path.split(file_path)[1]
		with open(file_path,'rb') as fp:
			file_data = fp.read()
		header = {'api-key': key}
		file_tup = (file_name,file_data)
		field = {'filefield':file_tup}
		encoded_args = urlencode({'device_id':device_id,'datastream_id':stream_id})
		url = 'http://api.heclouds.com/bindata?' + encoded_args
		r = self.http.request('POST', url, fields = field, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
		
	def get_bindata(self,key,data_index):
		header = {'api-key': key}
		url = 'http://api.heclouds.com/bindata/' + data_index
		r = self.http.request('GET', url, headers = header)
		return r.data
	
	def bytes_find(self,bytes_data,find_byte,beg = 0 ,end = 0):
		if end == 0:
			end = len(bytes_data)
		elif end < 0:
			end += len(bytes_data)
		index = beg
		findbyte = ord(find_byte)
		while index < end:
			if bytes_data[index] == findbyte:
				break
			index += 1
		if index < end:
			return index
		else:
			return -1
		
	def bytes_rfind(self,bytes_data,find_byte,beg = 0 ,end = 0):
		if end == 0:
			end = len(bytes_data)
		elif end < 0:
			end += len(bytes_data)
		index = end - 1
		findbyte = ord(find_byte)
		while index >= beg:
			if bytes_data[index] == findbyte:
				break
			index -= 1
		if index >= beg:
			return index
		else:
			return -1
			
	def get_file(self,key,file_index,file_path = ''):
		header = {'api-key': key}
		url = 'http://api.heclouds.com/bindata/' + file_index
		r = self.http.request('GET', url, headers = header)
		index1 = self.bytes_find(r.data,'\n')
		index2 = self.bytes_find(r.data,'\n',beg = index1 + 1)
		head = r.data[index1+1:index2]
		head_index1 = self.bytes_rfind(head,'\"')
		head_index2 = self.bytes_find(head,';')
		head_index3 = self.bytes_find(head,';',beg = head_index2 + 1)
		filename = head[head_index3 + 12:head_index1].decode('utf-8')
		index3 = self.bytes_find(r.data,'\n',beg = index2 + 1)
		index4 = self.bytes_rfind(r.data,'\n',end = -1)
		filedata = r.data[index3+3:index4 - 1]
		filepath = ''
		if file_path != '':
			filepath = file_path + filename
		else:
			filepath = filename
		with open(filepath,'wb') as file:
			file.write(filedata)
		
	def create_trigger(self,master_key,url,trigger_type,trigger_threshold,**args):
		"""
		"title":"wen du jian kong", //设备名（可选）
		"ds_id":"gps", //数据流名称（id）（可选）
		"dev_id":"1027", //设备ID（可选）
		"ds_uuids":[ //数据流uuid（可选）
		"9ad09uac-7446-512f-b07c-90jdnzj8120ad",
		"4599436e-7146-5349-b07c-79fa0919cs62",],
		"url":"//xx.bb.com",
		"type":"> | >= | < | <= | == | inout | in | out | change | frozen | live",
		"threshold":100 //阙值，根据type不同，见说明
		"""
		header = {'api-key': master_key}
		data = {}
		if 'title' in args:
			data['title'] = args['title']
		if 'ds_id' in args:
			data['ds_id'] = args['ds_id']
		if 'dev_id' in args:
			data['dev_id'] = args['dev_id']
		if 'ds_uuids' in args:
			data['ds_uuids'] = args['ds_uuids']
		data['url'] = url
		data['type'] = trigger_type
		data['threshold'] = trigger_threshold
		encoded_data = json.dumps(data).encode('utf-8')
		url = 'http://api.heclouds.com/triggers'
		r = self.http.request('POST', url, body=encoded_data, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
		
	def modify_trigger(self,master_key,trigger_id,**args):
		header = {'api-key': master_key}
		data = {}
		if 'title' in args:
			data['title'] = args['title']
		if 'ds_id' in args:
			data['ds_id'] = args['ds_id']
		if 'dev_ids' in args:
			data['dev_id'] = args['dev_id']
		if 'ds_uuids' in args:
			data['ds_uuids'] = args['ds_uuids']
		if 'url' in args:
			data['url'] = args['url']
		if 'type' in args:
			data['type'] = args['type']
		if 'threshold' in args:
			data['threshold'] = args['threshold']			
		if len(data) > 0:
			encoded_data = json.dumps(data).encode('utf-8')
			url = 'http://api.heclouds.com/triggers/' + trigger_id
			r = self.http.request('PUT', url, body=encoded_data, headers = header)
			result = json.loads(r.data.decode('utf-8'))
			return result['error']
		
	def get_trigger_info(self,master_key,trigger_id):
		header = {'api-key': master_key}
		url = 'http://api.heclouds.com/triggers/' + trigger_id
		r = self.http.request('GET', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
			
	def get_all_triggers_info(self,master_key,**args):
		"""
		title=name //指定触发器名称
		page=1 //指定页码,可选
		per_page=10 //指定每页输出个数,可选,默认10，最多100
		"""
		header = {'api-key': master_key}
		field = {}
		if 'title' in args:
			field['title'] = args['title']
		if 'page' in args:
			field['page'] = args['page']
		if 'per_page' in args:
			field['per_page'] = args['per_page']
		url = 'http://api.heclouds.com/triggers'
		r = self.http.request('GET', url,fields = field, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
			
	def delete_trigger(self,master_key,trigger_id):
		header = {'api-key': master_key}
		url = 'http://api.heclouds.com/triggers/' + trigger_id
		r = self.http.request('DELETE', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		return result['error']
		
	def create_apikey(self,master_key,key_title,resources,access_methods):
		header = {'api-key': master_key}
		data = {}
		rcs = {}
		acs = {}
		data['title'] = key_title
		rcs['resources'] = resources
		acs['access_methods'] = access_methods
		permissions = (rcs,acs)
		data['permissions'] = permissions
		encoded_data = json.dumps(data).encode('utf-8')
		print(encoded_data)
		url = 'http://api.heclouds.com/keys'
		r = self.http.request('POST', url, body=encoded_data, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
		
	def modify_apikey(self,master_key,key_string,**args):
		header = {'api-key': master_key}
		data = {}
		rcs = {}
		acs = {}
		if 'title' in args:
			data['title'] = args['title']
		if 'resources' in args:
			rcs['resources'] = args['resources']
		if 'access_methods' in args:
			acs['access_methods'] = args['access_methods']
		permissions = (rcs,acs)
		data['permissions'] = permissions
		encoded_data = json.dumps(data).encode('utf-8')
		print(encoded_data)
		url = 'http://api.heclouds.com/keys/' + key_string
		r = self.http.request('PUT', url, body=encoded_data, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		return result['error']
		
	def get_apikey_info(self,master_key,**args):
		header = {'api-key': master_key}
		field = {}
		if 'key' in args:
			field['key'] = args['key']
		if 'page' in args:
			field['page'] = args['page']
		if 'per_page' in args:
			field['per_page'] = args['per_page']
		if 'device_id' in args:
			field['device_id'] = args['device_id']
		url = 'http://api.heclouds.com/keys'
		r = self.http.request('GET', url,fields = field, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		if result['errno'] == 0:
			return result['data']
		else:
			return result['error']
		
	def delete_apikey(self,master_key,key_string):
		header = {'api-key': master_key}
		url = 'http://api.heclouds.com/keys/' + key_string
		r = self.http.request('DELETE', url, headers = header)
		result = json.loads(r.data.decode('utf-8'))
		return result['error']
		
def test():
	pass
	
if __name__ == '__main__':
	test()