from webapp import Worker


def search_worker(options, gender, age, price, patient_age, shedule):
    options_map = {'medical': 0, 'recomendations': 0, 'diabet': 0, 'insult': 0, 'alzheimer': 0, 'dcp': 0, 'bed': 0,
                   'oncology': 0}

    for option in options:
        if option in options_map.keys():
            options_map[option] = 1

    worker = Worker.query.filter(gender=gender).filter(Worker.age >= age[0]).filter(Worker.age <= age[1]).filter(
        Worker.pricefrom >= price[0]).filter(Worker.pricefrom <= age[1]).filter(medical=options_map['medical']).filter(
        patient_age=patient_age).filter(shedule=shedule)

    return worker

    # print(gender)
    # print(age)
    # print(price)
    # print(patient_age)
    # print(shedule)
    #
    # print(options_map)