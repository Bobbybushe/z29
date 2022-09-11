import json

file = open('try_csv.csv', 'r')
str_list = file.readlines()
file.close()
slov = {}
spisok = []
spis_shapka = str_list.pop(0)
spis_shapka = spis_shapka[0:-2]
spis_shapka = spis_shapka.split(',')
for i in range(len(str_list)):
    slov = dict(zip(spis_shapka, str_list[i].split(',')))
    spisok.append(slov)
print(spisok)

f = open("new.json","w")
f.write(json.dumps(spisok, indent='/n'))
f.close()