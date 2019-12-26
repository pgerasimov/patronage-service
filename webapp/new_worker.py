from webapp import Worker, db
from webapp.get_exp_age import get_exp


def add_new_worker(all_args, client_age):
    properties_map = {'recomendations': 0, 'diabet': 0, 'insult': 0, 'alzheimer': 0,
                      'dcp': 0, 'bed': 0, 'oncology': 0, 'hygiene': 0, 'injections': 0, 'dropper': 0, 'lfk': 0,
                      'cooking': 0, 'buyfood': 0, 'cleaning': 0, 'walking': 0}

    for item in all_args:
        if item in properties_map.keys():
            properties_map[item] = 1

    exp = get_exp(all_args['experience'])

    new_worker = Worker(
        surname=all_args['surname'],
        name=all_args['name'],
        age=all_args['age'], bio=all_args['bio'],
        phone=all_args['phone'],
        email=all_args['email'],
        address=all_args['address'],
        pricefrom=int(all_args['pricefrom']),
        priceto=int(all_args['priceto']),
        experience=exp,
        shedule=all_args['shedule'],
        gender=all_args['sex'],
        recomendations=properties_map['recomendations'],
        diabet=properties_map['diabet'],
        insult=properties_map['insult'],
        alzheimer=properties_map['alzheimer'],
        dcp=properties_map['dcp'],
        bed=properties_map['bed'],
        oncology=properties_map['oncology'],
        hygiene=properties_map['hygiene'],
        injections=properties_map['injections'],
        dropper=properties_map['dropper'],
        lfk=properties_map['lfk'],
        cooking=properties_map['cooking'],
        buyfood=properties_map['buyfood'],
        cleaning=properties_map['cleaning'],
        walking=properties_map['walking'],
        patient_age=client_age,
        medical=all_args.get('medical', 0))
    db.session.add(new_worker)
    db.session.commit()

    return '200'
