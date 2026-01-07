import pandas
#alıştırma1: Devamsızlığı 0 olan öğrencileri listeleyin
veri={
    "İsim":["Ali","Ayşe","Fatma","Ahmet"],
    "Yaş":[25,30,22,35],
    "vize": [70, 80, 90, 60],
    "final": [80, 50, 90, 40],
    "bölüm": ["Bilgisayar","Elektrik","Makina","İnşaat"],
    "devamsızlık": [0, 2, 9, 5]}
df=pandas.DataFrame(veri)
print(df[df["devamsızlık"]==0])
print("---------------------------------------------------")
#Alıştırma 2: Her bölümün en yüksek not alan öğrencisini bulun. 
grup=df.groupby("bölüm")
for isim, grup_df in grup:
    en_yuksek_not_alan=grup_df.loc[grup_df[["vize","final"]].sum(axis=1).idxmax()]
    print(f"Bölüm: {isim}")
    print(en_yuksek_not_alan)
    print("---------------------------------------------------")
#Alıştırma 3: Vize ve final notu arasındaki farkı hesaplayan yeni bir sütun ekleyin. 
df["not_farkı"]=abs(df["vize"]-df["final"])
print(df)
#Alıştırma 4: Ortalaması 75-85 arasında olan öğrencileri between() ile filtreleyin. 
ortalama_not=df[["vize","final"]].mean(axis=1)
filtrelenmis_df=df[ortalama_not.between(75,85)]
print(filtrelenmis_df)
print("---------------------------------------------------")
#Alıştırma 5: Kendi sınıfınızın notlarını içeren bir CSV dosyası oluşturun ve analiz edin. 
df.to_csv("sinif_notlari.csv", index=False)
print("Sınıf notları 'sinif_notlari.csv' dosyasına kaydedildi.")
#Alıştırma 6: Öğrenci sayısına göre bölümleri sıralayın (en kalabalıktan en aza). 
bolum_sayilari=df["bölüm"].value_counts().sort_values(ascending=False)
print(bolum_sayilari)