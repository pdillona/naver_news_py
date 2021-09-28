import requests

def getNewsApi():

    url = "http://localhost:8080/news"

    response = requests.get(url)

    newsDto = response.json();



    if newsDto["code"] == 1:
        #print(type(newsDto["data"]))
        return newsDto["data"]  #이거는 전체
        #print(newsDto["data"][0]) [0]을 통해 첫번째 기사를 가져올수 있음
    else:
        print(newsDto["msg"])

