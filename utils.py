# Импорты

import json
import os

def load_candidates():
    '''
    :return: загружает данные о кандидатах
    '''
    with open(os.path.join('candidates.json'), 'r', encoding='utf-8') as jfile:
        candidates = json.load(jfile)
    return candidates


def get_all():
    '''
    :return: выводит всех кандидатов
    '''
    candidates = load_candidates()
    print(candidates)


def get_by_pk(pk):
    '''
    :param pk: номер пк кндидата
    :return: возвращает кандидатов по номеру пк
    '''
    candidates = load_candidates()
    result = list(filter(lambda item: item['pk'] == pk, candidates))[0]
    return result


def get_by_skill(skill_name):
    '''
    :param skill_name: название умения
    :return: выводит кандидатов по умению
    '''
    candidates = load_candidates()
    result = list(filter(lambda item: skill_name.lower() in item['skills'].lower(), candidates))
    return result


