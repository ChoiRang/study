import encore.movie.vo as vo
import requests
import json


class BoxOffService:
    def __init__(self):
        self.url='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
        self.url1 = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
        self.key = 'c374ea9aa157f41f1386151fe2415b61'

    def mkUrl(self, param, date): # param:[0, 2]
        self.url += 'key='+self.key
        self.url += '&targetDt='+date
        val = [('Y', 'N'), ('K', 'F')]
        params = ['&multiMovieYn=', '&repNationCd=']
        for idx, v in enumerate(param):# param:[0, 2]
            if v < 2:
                self.url += params[idx]+val[idx][v]
                print(self.url)

    def getBoxOfficeDaily(self):
        date = input('박스 오피스 기준일(yyyymmdd):')
        p1 = int(input('0.다양성영화 1.상업영화 2.전체(기본)'))
        if p1 < 0 or p1 > 2:
            p1 = 2

        p2 = int(input('0.한국영화 1.외국영화 2.전체(기본)'))
        if p2 < 0 or p2 > 2:
            p2 = 2

        self.mkUrl([p1, p2], date)

        html = requests.get(self.url).text
        res = json.loads(html)
        data = res['boxOfficeResult']
        type = data['boxofficeType']
        date = data['showRange']
        list = data['dailyBoxOfficeList']
        res = []

        for m in list:
            res.append(vo.BoxOff(type, date, m['rank'], m['rankInten'], m['movieNm'], m['openDt'], m['movieCd'], m['salesAmt'], m['audiCnt'], m['audiAcc'], m['scrnCnt']))

        return res

    def printBoxOfficeDaily(self, res):
        for m in res:
            print(m)

    def get_movie_detail(self, movie_code):
        url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
        url += 'key=' + self.key
        url += '&movieCd=' + movie_code

        html = requests.get(url).text
        res = json.loads(html)          # 파싱 명령어
        obj = res['movieInfoResult']
        movie_obj = obj['movieInfo']
        movie_code = movie_obj['movieCd']
        ktitle = movie_obj['movieNm']
        etitle = movie_obj['movieNmEn']
        opendt = movie_obj['openDt']
        director = movie_obj['directors']
        d_names = []
        for d in director:
            d_names.append(d['peopleNm'])

        actors = movie_obj['actors']
        a_names = []
        for i in range(0, 3):
            a_obj = actors[i]
            name = a_obj['peopleNm']
            cast = a_obj['cast']
            a_names.append('배우:' + name + '/ 배역:' + cast)

        print('영화코드:', movie_code)
        print('영화명:', ktitle)
        print('영화명:', etitle)
        print('개봉일:', opendt)
        for n in d_names:
            print('감독:', n)
        print('출연 배우')
        for n in a_names:
            print(n)

