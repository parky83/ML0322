import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
# utf-16 �씤肄붾뵫�쑝濡� �뙆�씪�쓣 �뿴怨� 湲��옄瑜� 異쒕젰�븯湲� --- (���1)
fp = codecs.open("./src/ch6/2BEXXX06.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
# body = soup.select_one("body > text")
body = soup.select_one("body")
# print(body)
text = body.getText()
# �뀓�뒪�듃瑜� �븳 以꾩뵫 泥섎━�븯湲� --- (���2)
twitter = Twitter()
word_dic = {}
lines = text.split("\n")
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == "Noun": #  紐낆궗 �솗�씤�븯湲� --- (���3)
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 移댁슫�듃�븯湲�
# 留롮씠 �궗�슜�맂 紐낆궗 異쒕젰�븯湲� --- (���4)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()