#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Kullanıcıdan ad, yaş ve doğum yılı alma
ad = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
dogum_yili = int(input("Doğum yılınızı girin: "))

# Bilgileri ekrana yazdırma
print(f"Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")

# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Aritmetik işlemler
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız (0'a bölme hatası)"

# Sonuçları ekrana yazdırma
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")


# In[ ]:




