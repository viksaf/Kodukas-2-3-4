# Viktorija Safronova ITT20
# 09.02.2021
# Kodune töö nr 2

#Õunad
import random
mitu_tahab= input("Sisesta mitu õuna soovid: ")
mitu_tahab= int(mitu_tahab)
ounte_kogus= 14

for i in range(0, mitu_tahab):
    yhele= random.randint(1, 2)
    ounte_kogus= ounte_kogus - yhele
    print(yhele)
    print("alles jaab " + str(ounte_kogus))

print("-------------------------------------------------------------")



#Murelikud vanemad
ringide_arv = int(input("Sisesta ringide arv: "))
i = 2
summa = 0
while i <= ringide_arv:
    if i % 2 == 0:
        summa += i
    i += 2
print("Porgandite koguarv on " + str(summa))

print("-------------------------------------------------------------")

#Äratus
äratus = int(input("Sisesta mitu korda äratada: "))
i = 0
while i <äratus:
    print("Tõuse ja sära!")
    i = i + 1
    print(i)