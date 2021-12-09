import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def converter(tags, items):
    l = []
    for item in items:
        ob = {}
        for tag in tags:
            i = item.find(tag)
            if i is None:
                continue
            ob[tag] = i.text
        l.append(ob)
    return json.dumps(l, indent=1, ensure_ascii=False)


def writer(fileName, jsonData):
    f = open(fileName, "w", encoding='utf8')
    f.write(jsonData)
    f.close()


def run():
    tree = ET.parse(urlopen('https://lenta.ru/rss'))
    root = tree.getroot()
    items = root.find('channel').findall('item')
    writer("news.json", converter(["pubDate", "title"], items))
    writer("fullNews.json", converter(sorted(map(lambda x: x.tag, items[0].iter())), items))


run()
