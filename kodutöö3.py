# Viktorija Safronova ITT20
# 07.03.2021
# Kodune töö 3


# Pangakonto tehingud

summad = [] 


fail = open('konto.txt','r')
for rida in fail:
    summad.append(float(rida))
fail.close()


for summa in summad:
    if summa > 0:
        print(summa)
        

print("--------------------------------------------------------------")

# Jukebox

laulud = []
laulu_nr = []
jkn = 1

kaust = input("Palun sisesta kausta nimi: ")
fail = open('jukebox.txt', encoding='UTF-8')

for rida in fail:
    rida = rida.rstrip()
    laulud.append(rida)
    print(jkn,'. ', rida,sep='')
    laulu_nr.append(jkn)
    jkn += 1
    
fail.close()
    
loo_nr = int(input("Palun sisesta soovitud laulu nr: "))
for i in range(len(laulu_nr)):
    if loo_nr == laulu_nr[i]:
        print("Esitatake laulu ",laulud[i])
        

print("---------------------------------------------------------------")

# Ülikooli vastuvõetute harjutus

oppeaastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
i = 0
vastuvoetud = []

fail = open('rebased.txt', encoding='UTF-8')
for rida in fail:    
    vastuvoetud.append(int(rida))
fail.close()


oppeaasta = int(input("Palun sisestage, millise aasta andmeid vajate :"))

for i in range(len(oppeaastad)): 
    if oppeaasta == oppeaastad[i]: 
        print(oppeaasta,". aastal oli vastuvõetuid ",vastuvoetud[i],sep='')
        
    
print("-------------------------------------------------------------")