#! /usr/bin/python
# -*- coding: utf-8 -*-
# put script in path
# to use from command line
# eg python addDKPartToBom-ex.py ATMEGA644A-AU-ND
import sys
from bs4 import BeautifulSoup
import urllib2
import re
import Tkinter
import tkMessageBox

# import os
# # pip install psutil
# import psutil

# do stuff here

# if psutil.Process(os.getpid()).parent.name == 'terminal':
#     raw_input("Press enter to close...")

#import urllib
# import ctypes  # An included library with Python install.


# This is our path to the BOM-EX database file
# $HOME/external_lbrs/
PARTSDB = "/Users/silvermac/external_lbrs/partsdb/partsdb.txt"

verno = "1.1"
mfgPartNo = None
desc = None
mfg = None
package = "None"

DIGIKEY_URL = 'http://www.digikey.com/product-detail/en/0/'
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19"

# import ctypes  # An included library with Python install.
# def Mbox(title, text, style):
#     return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# Mbox('Your title', 'Your text', 1)

# An information box
# tkMessageBox.showinfo("Information","Created in Python.")

with open(PARTSDB, 'a') as file:
	
	# Assume the digikey part number is the first argument
	if len(sys.argv)<2:
		print "\n"
   		print"You need to specify a Digikey partNo!\n"
   		print"Version: "+ verno +"\nUsage: python addDKPartToBom-ex.py DigikeyPartNo\n"
   	else:
		partNo = sys.argv[1]

		# There's a more robust way to do this
		url = DIGIKEY_URL + partNo.replace("/", "%2F").replace("#", "%23")

		# Grab the data!
		 # BeautifulSoup(YOUR_MARKUP, "html.parser")
		# req = urllib2.Request(url)
		request = urllib2.Request(url)

		try:
			urllib2.urlopen(request)
		# except urllib2.HTTPError as e:
		# 	print(e.code)
			# print(e.read())
		except urllib2.HTTPError as e:
		    print("The server couldn\'t fulfill the request."+"\nDigikey Part Number "+partNo+" is not available on website")
		    tkMessageBox.showerror("Error","The server couldn\'t fulfill the request"+"\nDigikey Part Number "+partNo+" is not available on website")
 
 #https://www.digikey.com/products/en?keywords=ATMEGA644A-AUR

		     # , "Error code: " , e.code)
		    # print("Error code: ", e.code)
		    # print(partNo, " not available on website")
		except urllib2.URLError as e:
		    print('We failed to reach a server.')
		    print('Reason: ', e.reason) 
		    # print('Part Number', partNo, 'not on website')

			# if e.code is 404:
			#     print ('Not Found', 'Nothing matches the given URI')
			#     sys.exit(1)
		else:
			print ('We\'re good to go')
			# request = urllib2.Request(url)
			request.add_header('User-Agent', USER_AGENT)
			opener = urllib2.build_opener()
			data = opener.open(request).read()
			soup = BeautifulSoup(data,"html.parser")
			

			# try: urllib.request.urlopen(request)
			# except urllib.error.URLError as e:
			# 	print(e.reason)
			# 	(4, 'getaddrinfo failed')     

	# 		>>> req = urllib.request.Request('http://www.pretend_server.org')
	# >>> try: urllib.request.urlopen(req)
	# ... except urllib.error.URLError as e:
	# ...     print(e.reason)      
	# ...
	# (4, 'getaddrinfo failed')


				# Parse out the Manufacturer Part Number
			for elem in soup(text=re.compile(r'Manufacturer Part Number')):
				try:
					parent = elem.parent.parent.td.meta.attrs
					mfgPartNo = parent['content']
				except:
					pass

			# Parse out the Description
			for elem in soup(text=re.compile(r'Description')):
				try:
					parent = elem.parent.parent.td
					desc = parent.contents[0]
				except:
					pass

			# Parse out the Manufacturer
			for elem in soup(text=re.compile(r'Manufacturer')):
				try:
					parent = elem.parent.parent
					mfg = parent.span.span.contents[0]
				except:
					pass

			# Parse out the Package
			for elem in soup(text=re.compile(r'Package / Case')):
				try:
					parent = elem.parent.parent.td
					package = parent.contents[0]
					if u"®" in package:
						package = package.replace(u"®" "")
				except:
					pass

			# We got everything we needed! Add the part to the database.
			if mfgPartNo is not None and mfg is not None and desc is not None and package is not None:

				entry = "%s\t%s\tDK\t%s\t%s\t%s\n" % (mfgPartNo, mfg, partNo, desc, package)
				entry = entry.replace('\n', '')
		  		entry = entry.replace('\r', '')
		  		entry = entry + '\n'


				entry = entry.encode('utf-8')
				print entry

				file.write(entry)
				# tkMessageBox.showinfo("Information","Digikey Part Number: "+partNo+" has been added to parts db")


			# Something went wrong, the part was not found, DigiKey changed their site layout, etc.
			else:
				print mfgPartNo, mfg, partNo, desc, package
				print "Error adding entry"
				sys.exit(1)
