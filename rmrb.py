import requests
from bs4 import BeautifulSoup

def gethtml(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def maketxt(txt):
    soup = BeautifulSoup(txt, "html.parser")

    str = ''
    p = soup.find_all("p")
    for k,i in enumerate(p):
        try:
            if(i["class"] == ["p1",]):#通过debug，发现在存储的时候是以列表形式存储的，所以如果判断其是否为字符串p1会出现错误
                continue
        except:
            pass
        str += i.get_text()
    return str

def savetxt(str, i):
    with open(r"E:\python\scrapy\rmrb\rmrb{}.txt".format(i), "w", encoding = "utf-8") as f:
        f.write(str)


if __name__ == '__main__':
    url = "http://paper.people.com.cn/rmrb/html/{0:4}-{1:02}/{2:02}/nw.D110000renmrb_{0:4}{1:02}{2:02}_{3}-{4:02}.htm"#(2018)(12)(01-31)(2018)(12)(05) (1,2,3) (01-24)
    "http://paper.people.com.cn/rmrb/html/2017-01/01/nw.D110000renmrb_20170101_1-01.htm"
    strs = ''
    count = 1
    for year in (2017, 2018):
        for month in range(1, 13):
            for day in range (1,32):
                i = 0
                j = 0
                while(True):
                    try:
                        j += 1
                        while(True):
                            i += 1
                            try:
                                txt = gethtml(url.format(year, month, day, i, j))
                                str = maketxt(txt)
                                savetxt(str, count)
                                count += 1
                                strs += str
                                print(count) #测试
                            except:
                                raise Exception
                                break
                    except:
                        break

    savetxt(strs, 0)