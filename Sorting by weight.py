"""TASK:
Imagine that you have a certain number of stones
n (3 ≤ n ≤ 100) of known weight w1, w2, w3, ...,
where wi are positive integers from 1 to 1000000 inclusive.
Write a script that will distribute the stones into two heaps so
that the difference in the weights of these two heaps is minimal.
The number of stones and weights should be generated randomly.
The script itself should return a number equal to the minimum
weight difference of the two heaps. """



"""ЗАДАЧА:
Представьте, что у вас имеется некоторое количество камней
n (3 ≤ n ≤ 100) известного веса w1, w2, w3, ...,
где wi – это целые положительные числа от 1 до 1000000 включительно.
Напишите скрипт, который распределит камни в две кучи так,
чтобы разность весов этих двух куч была минимальной.
Количество камней и веса должны генерироваться случайным образом.
Сам скрипт должен возвращать число, равное минимальной разности
весов двух куч. """



from random import randint


def stones_sort():
    # Количество циклов №3 и №4
    W = 5
    # Количество циклов №5
    W5 = 10

    # Ограничение циклов для №5
    N5 = 500_000
    # Ограничение циклов для №6
    N6 = 500_000

    ########################### СОРТИРОВКА № 0 ###################################

    N = randint(3, 100)
    lsk1 = []
    lsk2 = []
    n = 1
    for i in range(1, N + 1):
        i = randint(1, 1_000_000)
        if n % 2 != 0:
            lsk1.append(i)
            n += 1
        else:
            lsk2.append(i)
            n += 1

    print()
    print(f'СОРТИРОВКА №0: (Случайное деление на две кучи камней из одной):')
    print(f'Всего камней: {N} шт.')
    lsk1.sort()
    lsk2.sort()
    print('№1:', lsk1)
    print('№2:', lsk2)
    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D0 = m1 - m2
    print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
    print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
    print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D0): ,})##### ')
    T = (D0 / (m1 + m2)) * 100
    print(f'Точность сортировки камней: {abs(T): .2f} %')

    ########################### СОРТИРОВКА № 1 ###################################

    lsk1.sort()
    lsk2.sort()
    lsd = []
    ls_ch = []
    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D1 = m1 - m2
    k1 = 0
    k2 = 0
    n_k = 0

    if m1 > m2 and len(lsk1) >= 2:
        while D1 > 0:
            ls_ch.append(lsk1[0])
            lsk2.append(lsk1[0])
            lsk1.remove(lsk1[0])
            m1 = sum(lsk1)
            m2 = sum(lsk2)
            D1 = m1 - m2
            lsd.append(abs(D1))
            n_k += 1
            k1 = 1

        if len(lsd) >= 2 and len(ls_ch) >= 2 and abs(D1) != min(lsd) and k1 > 0:
            lsk1.append(ls_ch[(len(ls_ch) - 1)])
            lsk2.remove(ls_ch[(len(ls_ch) - 1)])
            n_k += 1
            #print(f'Было перемещение камня <{ls_ch[(len(ls_ch) - 1)]}> '
                  #f'из <Кучи №2> обратно в <Кучу №1> ')

    elif m1 < m2 and len(lsk2) >= 2:
        while D1 < 0:
            ls_ch.append(lsk2[0])
            lsk1.append(lsk2[0])
            lsk2.remove(lsk2[0])
            m1 = sum(lsk1)
            m2 = sum(lsk2)
            D1 = m1 - m2
            lsd.append(abs(D1))
            k2 = 1
            n_k += 1

        if len(lsd) >= 2 and len(ls_ch) >= 2 and abs(D1) != min(lsd) and k2 > 0:   #len(lsd) > 0 and len(ls_ch) > 0 and abs(D1) != min(lsd):
            lsk2.append(ls_ch[(len(ls_ch) - 1)])
            lsk1.remove(ls_ch[(len(ls_ch) - 1)])
            n_k += 1
            #print(f'Было перемещение камня <{ls_ch[(len(ls_ch) - 1)]}>'
                  #f' из <Кучи №1> обратно в <Кучу №2> ')

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D1 = m1 - m2

    if abs(D1) < abs(D0):
        print()
        print('СОРТИРОВКА №1: (Перемещение камней из большей кучи в меньшую '
              'и обратно)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D1 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D1): ,})##### ')
        T = (D1 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .2f} %')

    elif len(lsd) == 1 and len(ls_ch) == 1 and k1 > 0 and abs(D1) > abs(D0):
        lsk1.append(ls_ch[0])
        lsk2.remove(ls_ch[0])
        print()
        print('СОРТИРОВКА №1: (Перемещение камней из большей кучи в меньшую '
              'и обратно)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D1 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D1): ,})##### ')
        T = (D1 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .2f} %')

    elif len(lsd) == 1 and len(ls_ch) == 1 and k2 > 0 and abs(D1) > abs(D0):
        lsk2.append(ls_ch[0])
        lsk1.remove(ls_ch[0])
        print()
        print('СОРТИРОВКА №1: (Перемещение камней из большей кучи в меньшую '
              'и обратно)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D1 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D1): ,})##### ')
        T = (D1 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .2f} %')

    elif abs(D1) == abs(D0) and k1 == 0 and k2 == 0:
        print()
        print('СОРТИРОВКА №1: (Перемещение камней из большей кучи в меньшую '
              'и обратно)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D1 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D1): ,})##### ')
        T = (D1 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .2f} %')

    ########################### СОРТИРОВКА № 2 ###################################

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D2 = m1 - m2
    ls_ni = []
    ls_ng = []
    K = 0.499
    A = abs(D2) * 0.5
    B = abs(D2) * 0.5
    n_k = 0
    n_z = 0
    k1 = 0
    k2 = 0

    if m1 > m2 and len(lsk1) >= 2:
        while K <= 1 and n_z != 1:
            K += 0.001
            while B <= (abs(D2) * K + 1):
                A -= 1
                B += 1
                n_k += 1
                for i in lsk1:
                    if A <= i <= B:
                        ls_ni.append(i)
                        n_k += 1
                        n_z = 1
                        k1 = 1
                        break

    elif m1 < m2 and len(lsk2) >= 2:
        while K <= 1 and n_z != 1:
            K += 0.001
            while B <= (abs(D2) * K + 1):
                A -= 1
                B += 1
                n_k += 1
                for g in lsk2:
                    if A <= g <= B:
                        ls_ng.append(g)
                        n_k += 1
                        n_z = 1
                        k2 = 1
                        break

    if k1 > 0 and ls_ni[0] in lsk1:
        a2 = ls_ni[0]
        lsk2.append(a2)
        lsk1.remove(a2)

    elif k2 > 0 and ls_ng[0] in lsk2:
        b2 = ls_ng[0]
        lsk1.append(b2)
        lsk2.remove(b2)

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D2 = m1 - m2

    if abs(D2) < abs(D1):
        print()
        print('СОРТИРОВКА №2: (Перемещение одного камня из большей кучи в меньшую)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D2 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D2): ,})##### ')
        T = (D2 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .4f} %')

    elif k1 > 0 and abs(D2) > abs(D1):
        a2 = ls_ni[0]
        lsk1.append(a2)
        lsk2.remove(a2)
        print()
        print('СОРТИРОВКА №2: (Перемещение одного камня из большей кучи в меньшую)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D2 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D2): ,})##### ')
        T = (D2 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .4f} %')

    elif k2 > 0 and abs(D2) > abs(D1):
        b2 = ls_ng[0]
        lsk2.append(b2)
        lsk1.remove(b2)
        print()
        print('СОРТИРОВКА №2: (Перемещение одного камня из большей кучи в меньшую)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D2 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D2): ,})##### ')
        T = (D2 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .4f} %')

    elif abs(D2) == abs(D1) and k1 == 0 and k2 == 0:
        print()
        print('СОРТИРОВКА №2: (Перемещение одного камня из большей кучи в меньшую)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D2 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D2): ,})##### ')
        T = (D2 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .4f} %')

    ########################### СОРТИРОВКА № 3 ###################################

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D3 = m1 - m2
    ls_cikl = []
    n_k = 0
    n_min = 0

    print()
    print('Идет сортировка №3: .............................................')
    while True:
        n_min += 1
        A = abs(D3) * 0.5
        B = abs(D3) * 0.5
        ls_d1 = []
        ls_d2 = []
        n_z = 0
        K = 0.499
        z1 = 0
        z2 = 0
        if m1 > m2:
            while K <= 1 and n_z != 1:
                K += 0.001
                while B <= (abs(D3) * K + 1):
                    A -= 1
                    B += 1
                    n_k += 1
                    for i in lsk1:
                        for g in lsk2:
                            if (i-g) > 0 and A <= (i-g) <= B:
                                ls_d1.append(i)
                                ls_d2.append(g)
                                n_k += 1
                                z1 = 1
                                n_z = 1
                                break
        elif m1 < m2:
            while K <= 1 and n_z != 1:
                K += 0.001
                while B <= (abs(D3) * K + 1):
                    A -= 1
                    B += 1
                    n_k += 1
                    for g in lsk2:
                        for i in lsk1:
                            if (g - i) > 0 and A <= (g-i) <= B:
                                ls_d1.append(i)
                                ls_d2.append(g)
                                n_k += 1
                                z2 = 1
                                n_z = 1
                                break

        if z1 > 0 and ls_d1[0] in lsk1 and ls_d2[0] in lsk2 and ls_d1[0] != ls_d2[0]:
            a3 = ls_d1[0]
            b3 = ls_d2[0]
            lsk1.remove(a3)
            lsk2.remove(b3)
            lsk2.append(a3)
            lsk1.append(b3)

        elif z2 > 0 and ls_d1[0] in lsk1 and ls_d2[0] in lsk2 and ls_d1[0] != ls_d2[0]:
            b3 = ls_d2[0]
            a3 = ls_d1[0]
            lsk2.remove(b3)
            lsk1.remove(a3)
            lsk1.append(b3)
            lsk2.append(a3)

        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D3 = m1 - m2
        ls_cikl.append(abs(D3))

        if n_min >= W:
            if abs(D3) == min(ls_cikl):
                break

    ls_cikl = set(ls_cikl)
    ls_cikl = list(ls_cikl)
    ls_cikl.sort(reverse=True)

    print('Варианты разницы весов (D3):', ls_cikl)
    #print(f'К: {K: .3f}')

    if abs(D3) < abs(D2):
        print()
        print('СОРТИРОВКА №3: (Перемещение одного камня из каждой кучи в другую)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D3): ,})##### ')
        T = (D3 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif abs(D3) == abs(D2):
        print()
        print('СОРТИРОВКА №3: (Перемещение одного камня из каждой кучи в другую)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        print('№1:', lsk1)
        print('№2:', lsk2)
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D3): ,})##### ')
        T = (D3 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    ########################### СОРТИРОВКА № 4 ###################################

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D4 = m1 - m2
    ls_cikl = []
    n_min = 0
    n_k = 0

    print()
    print('Идет сортировка №4: .............................................')
    while True:
        n_min += 1
        A = abs(D4) * 0.5
        B = abs(D4) * 0.5
        ls_i1 = []
        ls_i2 = []
        ls_g1 = []
        ls_g2 = []
        n_z = 0
        K = 0.499
        mk1 = 0
        mk2 = 0

        if m1 > m2 and len(lsk2) >= 2:
            while K <= 1 and n_z != 1:
                K += 0.001
                while B <= (abs(D4) * K + 1):
                    A -= 1
                    B += 1
                    n_k += 1
                    for i1 in lsk1:
                        for g1 in lsk2:
                            for g2 in lsk2:
                                if (i1 - (g1 + g2)) > 0 and \
                                        A <= (i1 - (g1 + g2)) <= B:
                                    ls_i1.append(i1)
                                    ls_g1.append(g1)
                                    ls_g2.append(g2)
                                    n_k += 1
                                    mk1 = 1
                                    n_z = 1
                                    break

        elif m1 < m2 and len(lsk1) >= 2:
            while K <= 1 and n_z != 1:
                K += 0.001
                while B <= (abs(D4) * K + 1):
                    A -= 1
                    B += 1
                    n_k += 1
                    for g1 in lsk2:
                        for i1 in lsk1:
                            for i2 in lsk1:
                                if (g1 - (i1 + i2)) > 0 and\
                                        A <= (g1 - (i1 + i2)) <= B:
                                    ls_g1.append(g1)
                                    ls_i1.append(i1)
                                    ls_i2.append(i2)
                                    n_k += 1
                                    mk2 = 1
                                    n_z = 1
                                    break
        ls_i1 = set(ls_i1)
        ls_i1 = list(ls_i1)
        ls_g1 = set(ls_g1)
        ls_g1 = list(ls_g1)

        if mk1 > 0 and len(ls_g1) >= 2 and len(ls_i1) != 0 and ls_i1[0] in lsk1 and\
                ls_g1[0] in lsk2 and ls_g1[1] in lsk2 and ls_g1[0] != ls_g1[1] and \
                ls_i1[0] != ls_g1[0]:
            a4 = ls_i1[0]
            c4 = ls_g1[0]
            d4 = ls_g1[1]
            lsk2.append(a4)
            lsk1.remove(a4)
            lsk1.append(c4)
            lsk1.append(d4)
            lsk2.remove(c4)
            lsk2.remove(d4)

        if mk2 > 0 and len(ls_i1) >= 2 and len(ls_g1) != 0 and ls_i1[0] in lsk1 and\
                ls_i1[1] in lsk1 and ls_g1[0] in lsk2 and ls_i1[0] != ls_i1[1] and \
                ls_g1[0] != ls_i1[0]:
            a4 = ls_i1[0]
            b4 = ls_i1[1]
            c4 = ls_g1[0]
            lsk1.append(c4)
            lsk2.remove(c4)
            lsk2.append(a4)
            lsk2.append(b4)
            lsk1.remove(a4)
            lsk1.remove(b4)

        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D4 = m1 - m2
        ls_cikl.append(abs(D4))

        if n_min >= W:
            if abs(D4) == min(ls_cikl):
                break

    ls_cikl = set(ls_cikl)
    ls_cikl = list(ls_cikl)
    ls_cikl.sort(reverse=True)
    print('Варианты разницы весов (D4):', ls_cikl)
    #print(f'К: {K: .3f}')

    if abs(D4) < abs(D3):
        print()
        print('СОРТИРОВКА №4: (Перемещение двух камней одной кучи и'
              ' одного камня другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D4 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D4): ,})##### ')
        T = (D4 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif abs(D4) == abs(D3):
        print()
        print('СОРТИРОВКА №4: (Перемещение двух камней одной кучи и'
              ' одного камня другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D4 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D4): ,})##### ')
        T = (D4 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    ########################### СОРТИРОВКА № 5 ###################################

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D5 = m1 - m2
    ls_cikl = []
    n_min = 0
    n_k = 0

    print()
    print('Идет сортировка №5: .............................................')
    while n_k <= N5:
        n_min += 1
        A = abs(D5) * 0.5
        B = abs(D5) * 0.5
        ls_i1 = []
        ls_i2 = []
        ls_g1 = []
        ls_g2 = []
        n_z = 0
        K = 0.499
        mk1 = 0
        mk2 = 0
        global zk1, zk2
        zk1 = 0
        zk2 = 0
        n_k += 1

        if m1 > m2 and len(lsk1) >= 2 and len(lsk2) >= 2:
            while K <= 1 and n_z != 1:
                K += 0.001
                while B <= (abs(D5) * K + 0.5):
                    A -= 1
                    B += 1
                    n_k += 1
                    for i1 in lsk1:
                        for i2 in lsk1:
                            for g1 in lsk2:
                                for g2 in lsk2:
                                    if ((i1 + i2) - (g1 + g2)) > 0 and\
                                            A <= ((i1 + i2) - (g1 + g2)) <= B:
                                        ls_i1.append(i1)
                                        ls_i2.append(i2)
                                        ls_g1.append(g1)
                                        ls_g2.append(g2)
                                        n_k += 1
                                        n_z = 1
                                        mk1 = 1
                                        break

        elif m1 < m2 and len(lsk1) >= 2 and len(lsk2) >= 2:
            while K <= 1 and n_z != 1:
                K += 0.001
                while B <= (abs(D5) * K + 0.5):
                    A -= 1
                    B += 1
                    n_k += 1
                    for g1 in lsk2:
                        for g2 in lsk2:
                            for i1 in lsk1:
                                for i2 in lsk1:
                                    if ((g1 + g2) - (i1 + i2)) > 0 and\
                                            A <= ((g1 + g2) - (i1 + i2)) <= B:
                                        ls_g1.append(g1)
                                        ls_g2.append(g2)
                                        ls_i1.append(i1)
                                        ls_i2.append(i2)
                                        n_k += 1
                                        n_z = 1
                                        mk2 = 1
                                        break
        ls_i1 = set(ls_i1)
        ls_i1 = list(ls_i1)
        ls_i2 = set(ls_i2)
        ls_i2 = list(ls_i2)
        ls_g1 = set(ls_g1)
        ls_g1 = list(ls_g1)
        ls_g2 = set(ls_g2)
        ls_g2 = list(ls_g2)

        if mk1 > 0 and len(ls_i1) >= 2 and len(ls_g1) >= 2 and ls_i1[0] in lsk1 and\
                ls_i1[1] in lsk1 and ls_g1[0] in lsk2 and ls_g1[1] in lsk2 and\
                ls_i1[0] != ls_g1[0] and ls_i1[0] != ls_g1[1] and\
                ls_i1[1] != ls_g1[0] and ls_i1[1] != ls_g1[1]:
            a5 = ls_i1[0]
            b5 = ls_i1[1]
            c5 = ls_g1[0]
            d5 = ls_g1[1]
            lsk2.append(a5)
            lsk2.append(b5)
            lsk1.remove(a5)
            lsk1.remove(b5)
            lsk1.append(c5)
            lsk1.append(d5)
            lsk2.remove(c5)
            lsk2.remove(d5)
            zk1 = 1

        elif mk2 > 0 and len(ls_i1) >= 2 and len(ls_g1) >= 2 and ls_i1[0] in lsk1 and\
                ls_i1[1] in lsk1 and ls_g1[0] in lsk2 and ls_g1[1] in lsk2 and\
                ls_i1[0] != ls_g1[0] and ls_i1[0] != ls_g1[1] and\
                ls_i1[1] != ls_g1[0] and ls_i1[1] != ls_g1[1]:
            a5 = ls_i1[0]
            b5 = ls_i1[1]
            c5 = ls_g1[0]
            d5 = ls_g1[1]
            lsk1.append(c5)
            lsk1.append(d5)
            lsk2.remove(c5)
            lsk2.remove(d5)
            lsk2.append(a5)
            lsk2.append(b5)
            lsk1.remove(a5)
            lsk1.remove(b5)
            zk2 = 1

        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D5 = m1 - m2
        ls_cikl.append(abs(D5))

        if n_min >= W5:
            if abs(D5) == min(ls_cikl):
                break

    ls_cikl = set(ls_cikl)
    ls_cikl = list(ls_cikl)
    ls_cikl.sort(reverse=True)

    print('Варианты разницы весов (D5):', ls_cikl)
    #print(f'К: {K: .3f}')
    #print('D4:', abs(D4))
    #print('D5:', abs(D5))

    if n_k >= N5:
        print()
        print('Сортировка №5 прервана: превышение допустимого количества циклов.')
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D4): ,})##### ')
        T = (D4 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif abs(D5) < abs(D4):
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D5 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
        T = (D5 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif z1 > 0 and abs(D5) > abs(D4):
        a5 = ls_i1[0]
        b5 = ls_i1[1]
        c5 = ls_g1[0]
        d5 = ls_g1[1]
        lsk2.remove(a5)
        lsk2.remove(b5)
        lsk1.append(a5)
        lsk1.append(b5)
        lsk1.remove(c5)
        lsk1.remove(d5)
        lsk2.append(c5)
        lsk2.append(d5)
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D5 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
        T = (D5 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif z2 > 0 and abs(D5) > abs(D4):
        a5 = ls_i1[0]
        b5 = ls_i1[1]
        c5 = ls_g1[0]
        d5 = ls_g1[1]
        lsk1.remove(c5)
        lsk1.remove(d5)
        lsk2.append(c5)
        lsk2.append(d5)
        lsk2.remove(a5)
        lsk2.remove(b5)
        lsk1.append(a5)
        lsk1.append(b5)
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D5 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
        T = (D5 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif abs(D5) == abs(D4) and z1 == 0 and z2 == 0:
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D5 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
        T = (D5 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')

    elif (z1 != 0 and abs(D5) == abs(D4)) or (z2 != 0 and abs(D5) == abs(D4)):
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        lsk1.sort()
        lsk2.sort()
        print('№1:', lsk1)
        print('№2:', lsk2)
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        D5 = m1 - m2
        print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
        print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
        T = (D5 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')
    else:
        print()
        print('СОРТИРОВКА №5: (Перемещение двух камней одной кучи и'
              ' двух камней из другой)')
        print(f'Циклов: {n_k}')
        print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
        print('### Сортировка не улучшила предыдущий результат. ###')
        print('### Все остается без изменений. ###')
        m1 = sum(lsk1)
        m2 = sum(lsk2)
        print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D4): ,})##### ')
        T = (D4 / (m1 + m2)) * 100
        print(f'Точность сортировки камней: {abs(T): .6f} %')


    ########################### СОРТИРОВКА № 6 ###################################

    m1 = sum(lsk1)
    m2 = sum(lsk2)
    D6 = m1 - m2
    if abs(D5) > abs(D4):
        D5 = D4

    Sort_6 = 1
    if abs(D5) >= 100 and Sort_6 == 1:
        ls_cikl = []
        n_min = 0
        n_k = 0
        print()
        print('Идет сортировка №6: .............................................')
        while n_k <= N6:
            n_min += 1
            A = abs(D6) * 0.5
            B = abs(D6) * 0.5
            ls_i1 = []
            ls_i2 = []
            ls_i3 = []
            ls_g1 = []
            ls_g2 = []
            ls_g3 = []
            li = 0
            lg = 0
            n_z = 0
            K = 0.499
            mk1 = 0
            mk2 = 0
            n_k += 1

            if m1 > m2 and len(lsk1) >= 3 and len(lsk2) >= 3:
                while K <= 1 and n_z != 1 and lg != 3:
                    K += 0.001
                    while B <= (abs(D6) * K + 0.5) and lg != 3:
                        A -= 1
                        B += 1
                        n_k += 1
                        for i1 in lsk1:
                            for i2 in lsk1:
                                for i3 in lsk1:
                                    for g1 in lsk2:
                                        for g2 in lsk2:
                                            for g3 in lsk2:
                                                if ((i1 + i2 + i3) - (g1 + g2 + g3)) > 0 and \
                                                        A <= ((i1 + i2 + i3) - (g1 + g2 + g3)) <= B:
                                                    ls_i1 = list(ls_i1)
                                                    ls_g1 = list(ls_g1)
                                                    ls_i1.append(i1)
                                                    ls_i1 = set(ls_i1)
                                                    li = len(ls_i1)
                                                    ls_i2.append(i2)
                                                    ls_i3.append(i3)
                                                    ls_g1.append(g1)
                                                    ls_g1 = set(ls_g1)
                                                    lg = len(ls_g1)
                                                    ls_g2.append(g2)
                                                    ls_g3.append(g3)
                                                    n_k += 1
                                                    n_z = 1
                                                    mk1 = 1
                                                    break

            elif m1 < m2 and len(lsk1) >= 3 and len(lsk2) >= 3:
                while K <= 1 and n_z != 1 and li != 3:
                    K += 0.001
                    while B <= (abs(D6) * K + 0.5) and li != 3:
                        A -= 1
                        B += 1
                        n_k += 1
                        for g1 in lsk2:
                            for g2 in lsk2:
                                for g3 in lsk2:
                                    for i1 in lsk1:
                                        for i2 in lsk1:
                                            for i3 in lsk1:
                                                if ((g1 + g2 + g3) - (i1 + i2 + i3)) > 0 and \
                                                        A <= ((g1 + g2 + g3) - (i1 + i2 + i3)) <= B:
                                                    ls_i1 = list(ls_i1)
                                                    ls_g1 = list(ls_g1)
                                                    ls_i1.append(i1)
                                                    ls_i1 = set(ls_i1)
                                                    li = len(ls_i1)
                                                    ls_i2.append(i2)
                                                    ls_i3.append(i3)
                                                    ls_g1.append(g1)
                                                    ls_g1 = set(ls_g1)
                                                    lg = len(ls_g1)
                                                    ls_g2.append(g2)
                                                    ls_g3.append(g3)
                                                    n_k += 1
                                                    n_z = 1
                                                    mk2 = 1
                                                    break
            ls_i1 = set(ls_i1)
            ls_i1 = list(ls_i1)
            ls_i2 = set(ls_i2)
            ls_i2 = list(ls_i2)
            ls_i3 = set(ls_i3)
            ls_i3 = list(ls_i3)
            ls_g1 = set(ls_g1)
            ls_g1 = list(ls_g1)
            ls_g2 = set(ls_g2)
            ls_g2 = list(ls_g2)
            ls_g3 = set(ls_g3)
            ls_g3 = list(ls_g3)

            if mk1 > 0 and len(ls_i1) >= 3 and len(ls_g1) >= 3 and \
                    ls_i1[0] in lsk1 and ls_i1[1] in lsk1 and ls_i1[2] in lsk1 and \
                    ls_g1[0] in lsk2 and ls_g1[1] in lsk2 and ls_g1[2] in lsk2 and \
                    ls_i1[0] != ls_g1[0] and ls_i1[0] != ls_g1[1] and ls_i1[0] != ls_g1[2] and \
                    ls_i1[1] != ls_g1[0] and ls_i1[1] != ls_g1[1] and ls_i1[1] != ls_g1[2] and \
                    ls_i1[2] != ls_g1[0] and ls_i1[2] != ls_g1[1] and ls_i1[2] != ls_g1[2]:
                a6 = ls_i1[0]
                b6 = ls_i1[1]
                ab6 = ls_i1[2]
                c6 = ls_g1[0]
                d6 = ls_g1[1]
                cd6 = ls_g1[2]
                lsk2.append(a6)
                lsk2.append(b6)
                lsk2.append(ab6)
                lsk1.remove(a6)
                lsk1.remove(b6)
                lsk1.remove(ab6)
                lsk1.append(c6)
                lsk1.append(d6)
                lsk1.append(cd6)
                lsk2.remove(c6)
                lsk2.remove(d6)
                lsk2.remove(cd6)

            elif mk2 > 0 and len(ls_i1) >= 3 and len(ls_g1) >= 3 and \
                    ls_i1[0] in lsk1 and ls_i1[1] in lsk1 and ls_i1[2] in lsk1 and \
                    ls_g1[0] in lsk2 and ls_g1[1] in lsk2 and ls_g1[2] in lsk2 and \
                    ls_i1[0] != ls_g1[0] and ls_i1[0] != ls_g1[1] and ls_i1[0] != ls_g1[2] and \
                    ls_i1[1] != ls_g1[0] and ls_i1[1] != ls_g1[1] and ls_i1[1] != ls_g1[2] and \
                    ls_i1[2] != ls_g1[0] and ls_i1[2] != ls_g1[1] and ls_i1[2] != ls_g1[2]:
                a6 = ls_i1[0]
                b6 = ls_i1[1]
                ab6 = ls_i1[2]
                c6 = ls_g1[0]
                d6 = ls_g1[1]
                cd6 = ls_g1[2]
                lsk1.append(c6)
                lsk1.append(d6)
                lsk1.append(cd6)
                lsk2.remove(c6)
                lsk2.remove(d6)
                lsk2.remove(cd6)
                lsk2.append(a6)
                lsk2.append(b6)
                lsk2.append(ab6)
                lsk1.remove(a6)
                lsk1.remove(b6)
                lsk1.remove(ab6)

            m1 = sum(lsk1)
            m2 = sum(lsk2)
            D6 = m1 - m2
            ls_cikl.append(abs(D6))

            if len(ls_cikl) == 2:
                break

        ls_cikl = set(ls_cikl)
        ls_cikl = list(ls_cikl)
        ls_cikl.sort(reverse=True)

        print('Варианты разницы весов (D6):', ls_cikl)
        #print(f'К: {K: .3f}')
        #print('D5:', abs(D5))
        #print('D6:', abs(D6))

        if n_k >= N6:
            print()
            print('Сортировка №6 прервана: превышение допустимого количества циклов.')
            print()
            print('СОРТИРОВКА №6: (Перемещение двух камней одной кучи и'
                  ' двух камней из другой)')
            print(f'Циклов: {n_k}')
            print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
            print('### Сортировка не улучшила предыдущий результат. ###')
            print('### Все остается без изменений. ###')
            m1 = sum(lsk1)
            m2 = sum(lsk2)
            print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
            T = (D5 / (m1 + m2)) * 100
            print(f'Точность сортировки камней: {abs(T): .6f} %')

        elif abs(D6) < abs(D5):
            print()
            print('СОРТИРОВКА №6: (Перемещение трех камней одной кучи и'
                  ' трех камней из другой)')
            print(f'Циклов: {n_k}')
            print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
            lsk1.sort()
            lsk2.sort()
            print('№1:', lsk1)
            print('№2:', lsk2)
            m1 = sum(lsk1)
            m2 = sum(lsk2)
            D6 = m1 - m2
            print(f'Куча камней №1: {len(lsk1)} шт., Вес: {m1}:')
            print(f'Куча камней №2: {len(lsk2)} шт., Вес: {m2}:')
            print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D6): ,})##### ')
            T = (D6 / (m1 + m2)) * 100
            print(f'Точность сортировки камней: {abs(T): .6f} %')

        else:
            print()
            print('СОРТИРОВКА №6: (Перемещение трех камней одной кучи и'
                  ' трех камней из другой)')
            print(f'Циклов: {n_k}')
            print(f'Всего камней: {len(lsk1) + len(lsk2)} шт.')
            print('### Сортировка не улучшила предыдущий результат. ###')
            print('### Все остается без изменений. ###')
            T = (D5 / (m1 + m2)) * 100
            print(f'--- РАЗНОСТЬ ВЕСОВ: #####({abs(D5): ,})##### ')
            print(f'Точность сортировки камней: {abs(T): .6f} %')

    print()
    print('                  ******* СОРТИРОВКА КАМНЕЙ ЗАВЕРШЕНА! *******')


if __name__ == '__main__':
    stones_sort()


