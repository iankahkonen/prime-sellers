#! python3 
import requests, bs4, pyperclip, openpyxl, mechanize

from selectorlib import Extractor

clipboard = str(pyperclip.paste())
clipboard_list = clipboard.splitlines()


# initialize simulated chrome browser	
chrome = mechanize.Browser()
chrome.set_handle_robots(False)
chrome.addheaders = [('User-agent', 
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('Amazon_Sellers.yml')


for i in range(len(clipboard_list)):
	asin = clipboard_list[i]
	asin_url = 'https://www.amazon.com/gp/offer-listing/' + asin + '/'
	# Yurl = 'http://api.scraperapi.com/?api_key=f0759471ae73755feab08ef9ac6e299d&url=' + asin_url

	res = chrome.open(asin_url)

#asin_html = bs4.BeautifulSoup(res.text, 'html.parser')
	print(e.extract(res.text))
