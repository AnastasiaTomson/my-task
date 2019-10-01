'''
Дан мас­сив, со­дер­жа­щий 2018 по­ло­жи­тель­ных целых чисел,
не пре­вы­ша­ю­щих 15 000. Не­об­хо­ди­мо умень­шить все чётные
эле­мен­ты мас­си­ва на зна­че­ние ми­ни­маль­но­го эле­мен­та,
крат­но­го 3, и вы­ве­сти изменённый мас­сив по од­но­му эле­мен­ту в стро­ке. 
Если в ис­ход­ном мас­си­ве нет эле­мен­тов, крат­ных 3, 
все эле­мен­ты нужно вы­ве­сти без из­ме­не­ния.
'''

a= []
n = 5
min = 15000
for i in range(n):
    a.append(int(input()))
    if a[i] < min and a[i] % 2 == 1:
        min = a[i]
for x in range(n):
    if a[x] % 2 == 0:
        a[x] -= min
print(' '.join(map(str, a)))
