from src.utils import load_file, executed_last_operations, format_operation


def test_load_file():
    assert load_file('/home/vk/CP_3/tests/test_operations1.json') is None
    assert len(load_file('/home/vk/CP_3/tests/test_operations.json')) > 0
    assert isinstance(load_file('/home/vk/CP_3/tests/test_operations.json'), list)
    assert load_file('/home/vk/CP_3/tests/test_operations.json') == [{'date': '2019-08-26T10:50:58.294041',
                                                                      'description': 'Перевод организации',
                                                                      'from': 'Maestro 1596837868705199',
                                                                      'id': 441945886,
                                                                      'operationAmount': {'amount': '31957.58',
                                                                                          'currency': {'code': 'RUB',
                                                                                                       'name': 'руб.'}},
                                                                      'state': 'EXECUTED',
                                                                      'to': 'Счет 64686473678894779589'},
                                                                     {'date': '2019-10-30T01:49:52.939296',
                                                                      'description': 'Перевод с карты на счет',
                                                                      'from': 'Visa Gold 7756673469642839',
                                                                      'id': 509645757,
                                                                      'operationAmount': {'amount': '23036.03',
                                                                                          'currency': {'code': 'RUB',
                                                                                                       'name': 'руб.'}},
                                                                      'state': 'EXECUTED',
                                                                      'to': 'Счет 48943806953649539453'},
                                                                     {'date': '2018-12-29T21:45:18.495053',
                                                                      'description': 'Перевод организации',
                                                                      'from': 'Счет 77977573135347241529',
                                                                      'id': 547682597,
                                                                      'operationAmount': {'amount': '66263.93',
                                                                                          'currency': {'code': 'RUB',
                                                                                                       'name': 'руб.'}},
                                                                      'state': 'EXECUTED',
                                                                      'to': 'Счет 33062909508148771891'},
                                                                     {'date': '2019-06-14T19:37:49.044089',
                                                                      'description': 'Перевод со счета на счет',
                                                                      'from': 'Счет 73222753239048295679',
                                                                      'id': 811920303,
                                                                      'operationAmount': {'amount': '63150.74',
                                                                                          'currency': {'code': 'USD',
                                                                                                       'name': 'USD'}},
                                                                      'state': 'EXECUTED',
                                                                      'to': 'Счет 78544755774551298747'},
                                                                     {'date': '2019-06-14T19:37:49.044089',
                                                                      'description': 'Перевод со счета на счет',
                                                                      'from': 'Счет 73222753239048295679',
                                                                      'id': 811920303,
                                                                      'operationAmount': {'amount': '63150.74',
                                                                                          'currency': {'code': 'USD',
                                                                                                       'name': 'USD'}},
                                                                      'state': 'EXECUTED'},
                                                                     {'date': '2019-06-14T19:37:49.044089',
                                                                      'description': 'Перевод со счета на счет',
                                                                      'id': 811920303,
                                                                      'operationAmount': {'amount': '63150.74',
                                                                                          'currency': {'code': 'USD',
                                                                                                       'name': 'USD'}},
                                                                      'state': 'EXECUTED',
                                                                      'to': 'Счет 78544755774551298747'}]


def test_executed_last_operations():
    file = load_file('/home/vk/CP_3/tests/test_operations.json')
    count = 2

    assert executed_last_operations(file, count) == [{'date': '2019-10-30T01:49:52.939296',
                                                      'description': 'Перевод с карты на счет',
                                                      'from': 'Visa Gold 7756673469642839',
                                                      'id': 509645757,
                                                      'operationAmount': {'amount': '23036.03',
                                                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                                                      'state': 'EXECUTED',
                                                      'to': 'Счет 48943806953649539453'},
                                                     {'date': '2019-08-26T10:50:58.294041',
                                                      'description': 'Перевод организации',
                                                      'from': 'Maestro 1596837868705199',
                                                      'id': 441945886,
                                                      'operationAmount': {'amount': '31957.58',
                                                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                                                      'state': 'EXECUTED',
                                                      'to': 'Счет 64686473678894779589'}]

    assert executed_last_operations(file) == [{'date': '2019-10-30T01:49:52.939296',
                                               'description': 'Перевод с карты на счет',
                                               'from': 'Visa Gold 7756673469642839',
                                               'id': 509645757,
                                               'operationAmount': {'amount': '23036.03',
                                                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 48943806953649539453'},
                                              {'date': '2019-08-26T10:50:58.294041',
                                               'description': 'Перевод организации',
                                               'from': 'Maestro 1596837868705199',
                                               'id': 441945886,
                                               'operationAmount': {'amount': '31957.58',
                                                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 64686473678894779589'},
                                              {'date': '2019-06-14T19:37:49.044089',
                                               'description': 'Перевод со счета на счет',
                                               'from': 'Счет 73222753239048295679',
                                               'id': 811920303,
                                               'operationAmount': {'amount': '63150.74',
                                                                   'currency': {'code': 'USD', 'name': 'USD'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 78544755774551298747'},
                                              {'date': '2019-06-14T19:37:49.044089',
                                               'description': 'Перевод со счета на счет',
                                               'from': 'Счет 73222753239048295679',
                                               'id': 811920303,
                                               'operationAmount': {'amount': '63150.74',
                                                                   'currency': {'code': 'USD', 'name': 'USD'}},
                                               'state': 'EXECUTED'},
                                              {'date': '2019-06-14T19:37:49.044089',
                                               'description': 'Перевод со счета на счет',
                                               'id': 811920303,
                                               'operationAmount': {'amount': '63150.74',
                                                                   'currency': {'code': 'USD', 'name': 'USD'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 78544755774551298747'},
                                              {'date': '2018-12-29T21:45:18.495053',
                                               'description': 'Перевод организации',
                                               'from': 'Счет 77977573135347241529',
                                               'id': 547682597,
                                               'operationAmount': {'amount': '66263.93',
                                                                   'currency': {'code': 'RUB', 'name': 'руб.'}},
                                               'state': 'EXECUTED',
                                               'to': 'Счет 33062909508148771891'}]


def test_format_operation():
    data = load_file('/home/vk/CP_3/tests/test_operations.json')
    filter_data = executed_last_operations(data)

    assert format_operation(filter_data) == ['\n'
                                             '30.10.2019 - Перевод с карты на счет\n'
                                             'Visa Gold 7756 67** **** 2839 -> Счет **9453\n'
                                             '23036.03 руб.',
                                             '\n'
                                             '26.08.2019 - Перевод организации\n'
                                             'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                             '31957.58 руб.',
                                             '\n'
                                             '14.06.2019 - Перевод со счета на счет\n'
                                             'Счет 7322 27** **** 5679 -> Счет **8747\n'
                                             '63150.74 USD',
                                             '\n'
                                             '14.06.2019 - Перевод со счета на счет\n'
                                             'Счет 7322 27** **** 5679 -> Снятие наличных \n'
                                             '63150.74 USD',
                                             '\n'
                                             '14.06.2019 - Перевод со счета на счет\n'
                                             'Пополнение вклада  -> Счет **8747\n'
                                             '63150.74 USD',
                                             '\n'
                                             '29.12.2018 - Перевод организации\n'
                                             'Счет 7797 75** **** 1529 -> Счет **1891\n'
                                             '66263.93 руб.']
