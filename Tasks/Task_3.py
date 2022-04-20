pct = 0
while pct <= 100:
    if 11 <= pct <= 19:
        print(pct, 'процентов')
    elif pct % 10 == 1:
        print(pct, 'процент')
    elif 2<= pct % 10 <= 4:
        print(pct, 'процента')
    else:
        print(pct, 'процентов')
    pct += 1