import re
import requests
from bs4 import BeautifulSoup


MAIN_URL = "https://sfile.mobi/"


class Search(requests.Session):
	
	def __init__(self) -> None:
		super().__init__()
		self.__data = []
		
	def response(self, keyword: str = None) -> BeautifulSoup:
		response = self.get(MAIN_URL + "search.php?q=" + keyword)
		return BeautifulSoup(response.text, "html.parser")
		
	def getData(self, soup: BeautifulSoup) -> dict:
		main = soup.find("div", attrs={"class": "w3-container"})
		file_found = soup.find("h3")
		for _, data in enumerate(main.findAll("div", attrs={"class": "list"})[:-1]):
			icon = data.find("img")
			id, title = re.findall('\<a\shref=\"https:\/\/sfile\.mobi\/(.*?)\">(.*?)<\/a\>', str(data))[0]
			size = re.findall('\((.*?)\)', str(data))[0]
			self._Search__data.append(
				{
					"icon": icon['src'],
					"size": size,
					"title": title,
					"id": id,
				}
			)
		return {"data": self._Search__data, "file_found": re.search(r'<\/i>.*?(\d+).*?<\/h3\>', str(file_found)).group(1), "next": True if len(self._Search__data) >= 20 else None}
		
	def search(self, keyword, page = "") -> list:
		soup = self.response(keyword + page)
		return self.getData(soup)
		
class Download(requests.Session):
	
	def __init__(self) -> None:super().__init__()
		
	def response(self, data: str = None) -> BeautifulSoup:
		response = self.get(MAIN_URL + data)
		return BeautifulSoup(response.text, "html.parser")
		
	def getData(self, id: str) -> dict:
		soup = self.response(id)
		download_href = soup.find("a", id="download")['href']
		upload_date = re.search('Uploaded\:\s(.*?)<\/', str(soup)).group(1)
		download_count = re.search('Downloads\:\s(.*?)<\/', str(soup)).group(1)
		return {"url": download_href, "date": upload_date, "downloaded": download_count}
		
