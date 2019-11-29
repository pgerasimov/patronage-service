from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from webapp import Worker, Properties


def search_worker(options, priceto, pricefrom, agefrom, ageto, gender, shedule):
    Session = sessionmaker()
    engine = create_engine('sqlite:///webapp.db')
    Session.configure(bind=engine)
    sess = Session()

    workers = []
    options_map = {'medical': 0, 'recomendations': 0, 'diabet': 0, 'insult': 0, 'alzheimer': 0, 'dcp': 0, 'bed': 0,
                   'oncology': 0}

    for option in options:
        if option in options_map.keys():
            options_map[option] = 1

    priceto = priceto if priceto != [''] else '10000'
    pricefrom = pricefrom if pricefrom != [''] else '1'
    agefrom = agefrom if agefrom != [''] else '1'
    ageto = ageto if ageto != [''] else '999'


    # if gender != [] and shedule != []:
    #     worker = Worker.query.filter(Worker.gender == gender[0], Worker.age >= agefrom, Worker.age <= ageto,
    #                                  Worker.pricefrom >= pricefrom, Worker.pricefrom <= priceto,
    #                                  Worker.shedule == shedule[0]).all()
    # if gender == [] and shedule != []:
    #     worker = Worker.query.filter(Worker.age >= agefrom, Worker.age <= ageto,
    #                                  Worker.pricefrom >= pricefrom, Worker.pricefrom <= priceto,
    #                                  Worker.shedule == shedule[0]).all()
    #
    # if gender != [] and shedule == []:
    #     worker = Worker.query.filter(Worker.gender == gender[0], Worker.age >= agefrom, Worker.age <= ageto,
    #                                  Worker.pricefrom >= pricefrom, Worker.pricefrom <= priceto).all()
    #
    # if gender == [] and shedule == []:
    #     worker = Worker.query.filter(Worker.age >= agefrom, Worker.age <= ageto,
    #                                  Worker.pricefrom >= pricefrom, Worker.pricefrom <= priceto).all()
    #
    # print(worker)

    # get_workers = (sess.query(Worker, Properties)
    #                .filter(Worker.age >= agefrom, Worker.age <= ageto, Worker.pricefrom >= pricefrom,
    #                        Worker.pricefrom <= priceto)
    #                .filter(Worker.id == Properties.worker_id)
    #                .filter(Properties.bed == '1')
    #                .all())
    # for i in get_workers:
    #     workers.append(i[0])
    # print(workers)
    # print(type(workers[0]))
    return 'ok'
