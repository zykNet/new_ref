# -*- coding:utf-8 -*-
import time,os
import socket



def HttpResponse(header,whtml):
	os.chdir(r'C:\Users\Administrator\Downloads\KCon-master')
	f = open(whtml,'r')
	contxtlist = f.readlines()
	context = ''.join(contxtlist)
	response = "%s %d\n\n%s\n\n" % (header,len(context),context)
	print response
	return response
httpheader = '''\
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''
if __name__=='__main__':
	socket_srve = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket_srve.bind(('127.0.0.1',80))
	socket_srve.listen(5)
	socket_srve.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )# 重用socket地址
	while True:
		print 'i am ok'
		connection,adderess = socket_srve.accept()
		print (adderess[0],adderess[1])#'Connecttion is from %s:%s'
		buf = connection.recv(1024)
		if buf == '1':
			connection.send('You are python!')
		elif buf == '2':
			connection.send('You are dirty boy *_^')
		else:
			connection.send(HttpResponse(httpheader,"index.html"))
		connection.close()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
