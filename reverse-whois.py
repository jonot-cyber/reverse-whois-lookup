import requests
from lxml import html
var = requests.get("https://viewdns.info/reversewhois/?q={}".format(input('What would you like to search for? ')), headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"})
tree = html.fromstring(var.content)
print("Found websites are:\n")
print("\n".join([x.text for x in tree.xpath('.//td')[8::3]]))