from webapp import Worker, Properties, db


def add_new_worker(all_args, properties, client_age):
    properties_map = {'medical': 0, 'recomendations': 0, 'diabet': 0, 'insult': 0, 'alzheimer': 0,
                      'dcp': 0, 'bed': 0, 'oncology': 0, 'hygiene': 0, 'injections': 0, 'dropper': 0, 'lfk': 0,
                      'cooking': 0, 'buyfood': 0, 'cleaning': 0, 'walking': 0}

    for item in properties:
        if item in properties_map.keys():
            properties_map[item] = 1

    new_worker = Worker(surname=all_args['surname'], name=all_args['name'], mname=all_args['mname'],
                        age=all_args['age'], bio=all_args['bio'], phone=all_args['phone'],
                        email=all_args['email'], pricefrom=all_args['pricefrom'], priceto=all_args['priceto'],
                        experience=all_args['experience'], shedule=all_args['shedule'], gender=all_args['sex'])

    db.session.add(new_worker)
    db.session.commit()

    new_worker_properties = Properties(medical=properties_map['medical'],
                                       recomendations=properties_map['recomendations'],
                                       diabet=properties_map['diabet'], insult=properties_map['insult'],
                                       alzheimer=properties_map['alzheimer'], dcp=properties_map['dcp'],
                                       bed=properties_map['bed'],
                                       oncology=properties_map['oncology'], hygiene=properties_map['hygiene'],
                                       injections=properties_map['injections'],
                                       dropper=properties_map['dropper'],
                                       lfk=properties_map['lfk'], cooking=properties_map['cooking'],
                                       buyfood=properties_map['buyfood'],
                                       cleaning=properties_map['cleaning'], walking=properties_map['walking'],
                                       patient_age=client_age, worker_id=new_worker.id)
    db.session.add(new_worker_properties)
    db.session.commit()

    return '200'
