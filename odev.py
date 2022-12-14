liste = ["bir", "iki", "dört"]
liste.append(["üç" , "beş"])
print(liste)

liste = ["1. veri", "2. veri", "3. veri", "4. veri", "5. veri"]
print(liste[0:1])
print(liste[4:5])

liste = [1, 2, 3, 4, 5 ,6 ,7]
print(liste[1:3])
print(liste[0:3])
print(liste[3:7])
print(liste)

liste = [34 , 1, 56 , 334, 23, 2, 3, 19]
liste.sort()
print(liste)
liste.reverse()
print(liste)

listem = ["Merhaba", "Türkiye", "Nasılsın", "Tebrikler"]
print(listem[-1])
print(listem[-3])
print(listem[-4])

harf = ["a", "e", "i", "o", "p", "u"]
print(harf.index("i"))
print(harf.index("p"))


liste1 = ["selam"]
liste2 = ["deneme"]
liste3 = ["dünya"]
liste4 = ["1"]
liste1.append("9")
liste2.append("merhaba")
liste3.append("türkiye")
liste4.append("matematik")
print(liste1, liste2, liste3, liste4)

liste = ["selam", "123", "deneme"]
liste2 = ["türkçe", "kapı"]
liste3 = (liste + liste2)
print(liste3)