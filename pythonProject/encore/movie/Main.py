import encore.movie.service as service

if __name__ == '__main__':
    serv = service.BoxOffService()
    # res = serv.getBoxOfficeDaily()
    # serv.printBoxOfficeDaily(res)
    serv.get_movie_detail('20124079')
