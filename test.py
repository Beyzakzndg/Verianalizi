dolarDun=4.25
dolarBugun=4.29

if dolarDun<dolarBugun:
    print("🔼")
elif dolarDun>dolarBugun:
    print("🔽")
else:
    print("=")
print("------------------------")
kurslar=["C#","Python","C++","Js","Java"]
for kurs in kurslar:
    print(kurs)
print("----------------------------")
sayac=0
while sayac<10:
    print(sayac)
    sayac+=1
print("--------------------------------")
ogrenciBeyza={"Kullanıcı Adı": "Beyzakznd",
              "Şifre": "12345",
              "E-posta":"beyzakznd12@gmail.com"}
ogrenciElif={"Kullanıcı Adı":"Elifzynp",
              "Şifre":"14789",
              "E-posta":"elifzynp@hotmail.com"}
print(ogrenciBeyza["Kullanıcı Adı"])
print(ogrenciElif["Kullanıcı Adı"])