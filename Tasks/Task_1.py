duration = int(input('Введите кол-во секунд: '))
s = duration % 60
m = duration // 60 % 60
h = duration // 3600 % 24
d = duration // 86400
#вывод значения по форме
if d == 0 and h == 0 and m == 0:
    print(s, 'сек')
elif d == 0 and s == 0 and h == 0:
    print(m, 'мин')
elif d == 0 and s == 0 and s == 0:
    print(h, 'час')
elif h == 0 and m == 0 and s == 0:
    print(d, 'дн')
elif d == 0 and h == 0 and s !=0:
    print(m, 'Мин', s, 'сек')
elif d == 0 and m == 0 and s !=0:
    print(h, 'час', s, 'сек')
elif m == 0 and h == 0 and s !=0:
    print(d, 'дн', s, 'сек')
elif h == 0 and s == 0 and m !=0:
    print(d, 'дн', m, 'мн')
elif m == 0 and s == 0 and m !=0:
    print(d, 'дн', h, 'час')
elif d != 0 and h != 0 and s == 0 and m == 0:
    print(d, 'дн', h,'час', s, 'сек')
elif d != 0 and h == 0 and s !=0 and m != 0:
    print(d, 'дн', m, 'мин', s, 'сек')
elif d != 0 and h != 0 and s == 0 and m != 0:
    print(d, 'дн', h, 'час', m, 'мин')
elif d == 0 and h !=0 and s != 0 and m !=0:
    print(h, 'час', m, 'мин', s, 'сек')
else:
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')