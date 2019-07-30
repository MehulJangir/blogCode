#! python3
# methadology - open all links in a webpage in new tabs
import webbrowser, bs4, requests

url = input('enter url| ')
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml') # feature format: lxml
print(len(res.text))
newTabs = soup.select('a')
# print(newTabs)
for tab in newTabs:
	if len(tab.attrs) == 1: # not necessary, avoids opening links in navbar etc.
		webbrowser.open(tab.attrs.get('href'))