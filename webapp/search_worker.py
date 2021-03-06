from sqlalchemy import create_engine, text

from webapp import Worker


def search_worker(options, priceto, pricefrom, agefrom, ageto, gender, shedule):
    engine = create_engine('sqlite:///webapp.db')
    connection = engine.connect()

    priceto = priceto if priceto != '' else '10000'
    pricefrom = pricefrom if pricefrom != '' else '1'
    agefrom = agefrom if agefrom != '' else '1'
    ageto = ageto if ageto != '' else '999'

    request = 'AND'
    workers = []

    options_map = {'medical': 0, 'recomendations': 0, 'diabet': 0, 'insult': 0, 'alzheimer': 0, 'dcp': 0, 'bed': 0,
                   'oncology': 0, 'patient_age': 0}

    for option in options:
        if option in options_map.keys():
            options_map[option] = 1

    for key, value in options_map.items():
        if value != 0:
            request = f'{request} {key} = 1 AND'

    request = request[:-4]

    if len(gender) == 2 or not gender:
        pass
    else:
        request = f'{request} AND gender = "{gender[0]}"'

    if shedule:
        request = f'{request} AND shedule = {shedule[0]}'

    result = connection.execute(text(
        f'SELECT Worker.id '
        f'FROM Worker '
        f'WHERE pricefrom >= {pricefrom} AND priceto <= {priceto} AND age >= {agefrom} AND age <= {ageto} {request}'))

    for i in result:
        workers.append(Worker.query.filter(Worker.id == i[0]).all())

    return workers
