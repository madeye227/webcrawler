import requests
from bs4 import BeautifulSoup
import validators

class Crawler:
    # name = 'Crawler'
    #
    # def __init__(self):
    #     self.url = url
    #     self.depth = depth

    def getData(self, url, depth):
        data = {}
        data['url'] = url
        data['depth'] = depth
        data["pageImages"] = []
        data["pageLinks"] = []
        data['nesting'] = {}
        urlTemp = url
        if not urlTemp.startswith(("http://", "https://")):
            urlTemp = "http://"+urlTemp

        print("-------------------------------------request.text----------------------------")
        request = requests.get(urlTemp)

        try:
            if request.status_code == 200:
                html_doc = request.text
                soup = BeautifulSoup(html_doc, "html.parser")
                images = soup.findAll('img')
                # srcs = [img['src'] for img in soup.find_all('img')]
                for image in images:
                    try:
                        if image.has_attr('src'):
                            if image["src"].startswith("http"):
                                data["pageImages"].append(image["src"])
                            else:
                                data["pageImages"].append(urlTemp+image["src"])
                    except KeyError:
                        pass
                for links in soup.findAll("a"):
                    try:
                        if links.has_attr('href'):
                            if validators.url(links["href"])  or validators.url(urlTemp+links["href"]):
                                if links["href"].startswith("http"):
                                    data["pageLinks"].append(links["href"])
                                else:
                                    data["pageLinks"].append(urlTemp+links["href"])
                    except KeyError:
                        pass

                if depth >= 1:
                    depthTemp = depth - 1
                    for link in data["pageLinks"]:
                        try:
                            data['nesting'] = self.getData(link, depthTemp)
                        except:
                            pass
            else:
                data["urlError"] = 'invalid url'
                print(request.status_code)
        except:
            print("except ")

        return data

# if __name__ == '__main__':
#     print("python main function")
#     crawler = Crawler()
#     data = crawler.getData('https://www.pexels.com/search/nature/', 1)
#     print(data)
