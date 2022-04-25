spisok_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
znak = '"'
a = int(spisok_1[1])
a = f'{a:02.0f}'
spisok_1[1] = znak + a + znak
spisok_1[3] = znak + spisok_1[3] + znak
a = list(spisok_1[8])
b = int(a[1])
b = f'{b:02.0f}'
a[1] = b
spisok_1[8] = znak + a[0] + a[1] + znak
spisok_2= ' '.join(spisok_1)
print(spisok_2)