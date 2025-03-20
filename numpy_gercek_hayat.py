"""
🎯 Amaç:
Bu ödevde, NumPy kullanarak gerçek hayattan alınmış bazı verileri oluşturacak, analiz edecek ve görselleştireceksiniz.
"""

import numpy as np
import matplotlib.pyplot as plt


print("📊 BÖLÜM 1: Şirket Maaş Analizi\n")

# Rastgeleliği sabitlemek için tohumlama
np.random.seed(42)

# 500 çalışanın maaşlarını rastgele 3000 $ ile 15000 $ arasında oluştur
maaslar = np.random.randint(3000, 15001, 500)

# Ortalama, maksimum ve minimum maaşı hesapla
ortalama_maas = np.mean(maaslar)
maksimum_maas = np.max(maaslar)
minimum_maas = np.min(maaslar)

# Sonuçları ekrana yazdır
print("*** ENJA ŞİRKETİ MAAŞLARI ***"
      f"\nOrtalama Maaş = {ortalama_maas} $"
      f"\nMaksimum Maaş = {maksimum_maas} $"
      f"\nMinimum Maaş = {minimum_maas} $\n")

# Maaş dağılımını histogram ile görselleştir
plt.figure(figsize=(10, 6))
plt.hist(maaslar, bins=10, edgecolor="black", alpha=0.8)
plt.xlabel("Maaş ($)", fontweight="bold")
plt.ylabel("Çalışan Sayısı\n", fontweight="bold")
plt.title("Enja Şirketi Maaş Dağılımı\n", fontweight="bold")
plt.grid(axis="y")
plt.show()

# 500 çalışanı rastgele 3 farklı departmana atama
# 1 = Mühendislik, 2 = Muhasebe, 3 = Pazarlama
departmanlar = np.random.choice([1, 2, 3], 500)
departman_isimleri = ["Mühendislik", "Muhasebe", "Pazarlama"]
print("\n*** ENJA ŞİRKETİ DEPARTMANLARA GÖRE ORTALAMA MAAŞ ***")


# Departmana göre ortalama maaşı hesaplayan fonksiyon
def ortalama_maas_hesapla(departman_id):
    departman_maaslari = maaslar[departmanlar == departman_id]
    return np.mean(departman_maaslari)


# Her departman için ortalama maaşı hesapla
ortalama_muhendislik_maas = ortalama_maas_hesapla(1)
ortalama_muhasebe_maas = ortalama_maas_hesapla(2)
ortalama_pazarlama_maas = ortalama_maas_hesapla(3)

# Her departman için sonuçları ekrana yazdır
print(f"Ortalama Mühendislik Maaşı = {ortalama_muhendislik_maas:.2f} $"
      f"\nOrtalama Muhasebe Maaşı = {ortalama_muhasebe_maas:.2f} $"
      f"\nOrtalama Pazarlama Maaşı = {ortalama_pazarlama_maas:.2f} $")

# Her departmanın ortalama maaşlarını çubuk grafik ile görselleştir
plt.figure(figsize=(10, 6))
departman_ortalama_maas = [ortalama_muhendislik_maas, ortalama_muhasebe_maas, ortalama_pazarlama_maas]
plt.title("Enja Şirketi Departmanlara Göre Ortalama Maaş\n", fontweight="bold")
plt.xlabel("\nDepartmanlar", fontweight="bold")
plt.ylabel("Ortalama Maaş ($)\n", fontweight="bold")
plt.bar(departman_isimleri, departman_ortalama_maas, color="r", edgecolor="black")
plt.grid(axis="y")
plt.show()


print("\n📈 BÖLÜM 2: Hava Durumu Verilerini Oluşturma ve Analiz Etme")

# 365 gün için rastgele -10°C ile 40°C arasında sıcaklık verileri oluştur
sicaklik_verisi = np.random.uniform(-10, 40, 365)

# Ortalama, minimum ve maksimum sıcaklığı hesapla
ortalama_sicaklik = np.mean(sicaklik_verisi)
minimum_sicaklik = np.min(sicaklik_verisi)
maksimum_sicaklik = np.max(sicaklik_verisi)

# Sonuçları ekrana yazdır: ortalama, minimum ve maksimum sıcaklık
print(f"\n*** Yıllık Sıcaklık Verileri (365 Gün) ***"
      f"\nOrtalama Sıcaklık = {ortalama_sicaklik:.2f}°C"
      f"\nMinimum Sıcaklık = {minimum_sicaklik:.2f}°C"
      f"\nMaksimum Sıcaklık = {maksimum_sicaklik:.2f}°C")

# Yıllık sıcaklık değişimlerini görselleştir
plt.figure(figsize=(10, 6))
plt.plot(sicaklik_verisi, color="b", marker="o", markersize=5, markerfacecolor="yellow")
plt.title("Yıllık Sıcaklık Dalgalanmaları\n", fontweight="bold")
plt.xlabel("Günler", fontweight="bold")
plt.ylabel("Sıcaklık (°C)", fontweight="bold")
plt.grid(axis="y")
plt.show()


print("\n📉 BÖLÜM 3: Ürün Satış Analizi")

# Ürün listesi
urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]

# Her ürün için 30 günlük rastgele satış verisi oluştur ve bir sözlükte sakla
satis_verileri = {urun: np.random.randint(10, 101, 30) for urun in urunler}

# Toplam satışları hesapla
toplam_satis = {urun: np.sum(satis) for urun, satis in satis_verileri.items()}

# Ortalama satışları hesapla
ortalama_satis = {urun: np.mean(satis) for urun, satis in satis_verileri.items()}

# Sonuçları ekrana yazdır
print("\n      ***** ÜRÜNLER ******\n")

for urun in urunler:
    print(f"|{urun.upper()}|")
    print(
        "|---------------------------------|"
        f"\n| Aylık Toplam Satış = {toplam_satis[urun]} $    |"
        f"\n| Aylık Ortalama Satış = {ortalama_satis[urun]:.2f} $ |"
        "\n|---------------------------------|\n\n")

# Ürünlerin toplam satışlarını çubuk grafik ile görselleştir
plt.figure(figsize=(10, 6))
plt.bar(urunler, list(toplam_satis.values()), color="skyblue", edgecolor="black", width=0.6)
plt.xlabel("\nÜrünler", fontweight="bold")
plt.ylabel("Toplam Satış Miktarı\n", fontweight="bold")
plt.title("Aylık Ürün Satış Verileri\n", fontweight="bold")
plt.grid(axis="y")
plt.show()
