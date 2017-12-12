# -*- coding: utf-8 -*-

def read_json(name):
    import os.path
    from json import loads
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(curr_dir, 'json_files', name)
    with open(file_path) as lang_file:
        data = lang_file.read()
    return loads(data)


CPV_CODES = read_json('cpv.json')
CPV_CODES.append('99999999-9')
DK_CODES = read_json('dk021.json')
FUNDERS = [(i['scheme'], i['id']) for i in read_json('funders.json')['data']]
# DKPP_CODES = read_json('dkpp.json')
ORA_CODES = [i['code'] for i in read_json('OrganisationRegistrationAgency.json')['data']]
WORKING_DAYS = read_json('working_days.json')

ATC_CODES = read_json('atc.json')
INN_CODES = read_json('inn.json')
