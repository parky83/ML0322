# 이미지 데이터 추출하기
import requests
# r = requests.get("http://wikibook.co.kr/wikibook.png")
r = requests.get("http://www.foodnmed.com/news/photo/201903/18296_3834_4319.jpg")
# 바이너리 형식으로 데이터 저장하기
with open("test.jpg", "wb") as f:
    f.write(r.content)
print("saved")
