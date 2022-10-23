print("selam")
a = "selam moruq"


#değişkenler
sea = "Oguzhan"
ase = 10.45
boy = 180

#değişken yazma
print("değişken yazma")
print("adım", sea,"km", ase,"boyum", boy)


#değisken tipleri
print("değisken tipleri")
print(type(sea))
print(type(ase))
print(type(boy))


#toplama ve karakter sayısı
print("değiskenleri toplama çıkarma ve karakter sayısı olcme")
print(len(sea))
print(ase+boy)
print(ase*boy)
print(ase/boy)
print(boy-ase)

#keyword
print("KEYWORD LİSTESİ")
import keyword
keywordlist = keyword.kwlist
print(keywordlist)


#bellektki yeri
toplama = "10 + 2"
print("BELLEKTEKİ KONUMU")
print( hex ( id (toplama)))

#pi sayısı
pi = 22 / 7
print("Pi Sayısı")
print(pi)


#if ve else
sayı = 13
sayı2 = 22
if sayı > sayı2:
    print("if")  
    pass

else:
     print("else")
     
      
#elif
elif1 = 13
elif2 = 43

if elif1 > 50:
    print("Yuksek")
    pass

elif elif1 >35:
    print("Orta")
    pass

elif elif1 > 10:
    print("Düşük")
    

#2 kere yazdırmaa
ase2 = 45
print(2*123)

while ase2 < pi:
    print(ase2)
    ase2 = ase2 + 0.01
    
    
    
#Ödev
pyisim = "Ayşe Python"
pygun =  "15"
p = "Sn"
u = "öğrencinizin toplam devamsızlığı"
ı = "gündür."
o = "Python Lisesi"

print(p , pyisim , u, pygun, ı, o)


#Ödev 2
pytutar = "10TL"
pyhitap = "Sayın"
pynumara = "17317378129"
pydonem = "12.13.2022"

print(pyhitap, pynumara, "nolu abonemiz", pydonem, "dönemli faturanız", pytutar, "TL'dir.Python Belediyesi")