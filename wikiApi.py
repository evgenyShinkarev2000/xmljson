from json import loads
from urllib.request import urlopen
import itertools
import datetime
import urllib.parse


def deadDate(url):
    data = loads(urlopen(url).read().decode('utf8'))['query']
    title = data["normalized"][0]["to"]
    corrections = data['pages'].popitem()[1]["revisions"]
    corrections = itertools.groupby(corrections, lambda x: datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date())
    corrections = map(lambda x: (x[0], len(list(x[1]))), corrections)
    corrections = sorted(filter(lambda x: x[1] >= 2, corrections), key=lambda x: x[1])
    # for i in corrections:
    #     print(i[0], i[1])
    print(f"{title} предполагаемая дата смерти {corrections[-1][0]}\n")


sample = "https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles="
gradskiy = f'{sample}%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
zanPol = f"{sample}%D0%96%D0%B0%D0%BD_%D0%9F%D0%BE%D0%BB%D1%8C"
gagarin = f"{sample}{urllib.parse.quote('Гагарин,_Юрий_Алексеевич')}"
sid = f"{sample}{urllib.parse.quote('Сид_Вишес')}"
yan = f"{sample}{urllib.parse.quote('Кёртис,_Иэн')}"
jim = f"{sample}{urllib.parse.quote('Моррисон,_Джим')}"

deadDate(gradskiy)
deadDate(zanPol)
deadDate(gagarin)
deadDate(sid)
deadDate(yan)
deadDate(jim)


