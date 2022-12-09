"""
Интерактивная играпро ведра, в которой необходимо за наименьшее количество шагов
оставить в ведре 4 литра воды
"""


bucket3 = 0
bucket5 = 0
counter_steps = 0


def status_buckets():
    print(f'В 3-л. ведре осталось {bucket3} литров, а в 5-л. осталось {bucket5} литров')


def action_general():
    status_buckets()
    if action_start == 1:
        action_pour()
    if action_start == 2:
        action_transfuse()
    if action_start == 3:
        action_pour_out()


def action_pour():
    global bucket3, bucket5
    action_middle = int(input('1. Налить воду в 3-л. ведро\n'
                              '2. Налить воду в 5-л. ведро\n'))
    assert action_middle != ''
    assert 0 < action_middle < 3
    if action_middle == 1:
        assert (bucket3 + 3) <= 3, 'Ведро и так уже преисполнено'
        bucket3 += 3
    else:
        assert (bucket5 + 5) <= 5, 'Ведро и так уже преисполнено'
        bucket5 += 5
    status_buckets()


def action_transfuse():
    global bucket3, bucket5
    action_middle = int(input('1. Перелить воду из 5-л. в 3-л. ведро\n'
                              '2. Перелить воду из 3-л. в 5-л. ведро\n'))
    assert action_middle != ''
    assert 0 < action_middle < 3
    if action_middle == 1:
        while bucket3 < 3 and bucket5 > 0:
            bucket3 += 1
            bucket5 -= 1
    else:
        while bucket5 < 5 and bucket3 > 0:
            bucket5 += 1
            bucket3 -= 1
    status_buckets()


def action_pour_out():
    global bucket3, bucket5
    action_middle = int(input('1. Вылить воду из 3-л. ведра\n'
                              '2. Вылить воду из 5-л. ведра\n'))
    assert action_middle != ''
    assert 0 < action_middle < 3
    if action_middle == 1:
        bucket3 = 0
    else:
        bucket5 = 0
    status_buckets()


while bucket5 != 4:
    assert -1 < bucket3 < 4
    assert -1 < bucket5 < 6
    action_start = int(input('1. Налить в ведро воду \n'
                             '2. Перелить из ведра воду\n'
                             '3. Вылить воду\n'))
    action_general()
    counter_steps += 1

print(f'Поздравляю, количество шагов, которое тебе понадобилось для решения задачи - {counter_steps}')
