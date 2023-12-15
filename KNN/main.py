# Habib Şako
# İnönü Üniversitesi Mühendislik Fakültesi
# Bilgisayar Mühendisliği 4. Sınıf Öğrencisi
# 13-12-2023 Çarşamba

# K-means algoritmasının en yakın uzaklığa göre kümeleme algoritması
# Uzaklık hesabında öklid formülü kullanılmıştır.

# kütüphaneler
import numpy as np


def k_means(x, k):
    # Rastgele olarak kümelerin seçilmesi
    y = x[np.random.choice(x.shape[0], k, replace=False), :]

    ## noktalar arasındaki uzaklıkların hesaplanıp distances değişkenine atılması ##
    # öklid uzaklığına göre hesaplanması
    distances = np.sqrt(((x - y[:, np.newaxis]) ** 2).sum(axis=2))

    # en küçük değerinin indexsini döndürür bu sayede küme merkezleri oluşur.
    clusters = np.argmin(distances, axis=0)

    # Küme çıktı olarak yazılması yazdırılması
    for i in range(k):
        print(f"Küme {i + 1}: {x[clusters == i]}")

if __name__ == '__main__':
    # x1,x2 değerlerinin ve k değerinin manuel olarak verilmesi
    x = np.array([[4, 2], [6, 4], [5, 1], [10, 6], [11, 8]])
    k = 2
    k_means(x, k)
