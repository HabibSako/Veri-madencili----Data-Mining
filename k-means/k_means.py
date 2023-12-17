# Habib Şako
# İnönü Üniversitesi Mühendislik Fakültesi
# Bilgisayar Mühendisliği 4. Sınıf Öğrencisi
# 15-12-2023 Cuma

# K-means algoritması
# Uzaklık hesabında öklid formülü kullanılmıştır.

## kullanıcı dosya seçim işlemi için kütüphaneler
# import openpyxl
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

## Excel Tablosunun Kullanıcıdan Alınması
# #dosya seçim pencerisinin açılması
# root = Tk()
# root.withdraw()
## excel dosyasını alma
# file_path = askopenfilename(filetypes=[("Excel", "*.xlsx")])
# data = pd.read_excel(file_path)

## Excel Tablosunun Otomatik Alınması 
#data = pd.read_excel('data.xlsx')

import numpy as np


def k_means(cluster, k):

    # Küme merkezlerinin rastgele seçilmesi
    centers = cluster[np.random.choice(cluster.shape[0], k, replace=False)]

    while True:
        #  k adet küme oluşturulduktan sonra her bir veri noktasının hangi küme etiketiyle etiketlendiğini belirlemek için kullanılır.
        # sum(axis=2) ifadesi, her bir veri noktasının her bir kümenin merkezine olan uzaklıklarının toplamını hesaplar.
        # centers[:, np.newaxis] işlemi center dizisindeki her bir elemanın tek bir sütunda yer aldığı bir matris oluşturur.
        # sonuç olarak cluster matrisinden centers matrisi çıkartılır ve tüm veri kümelerinin küme merkezine olan uzaklığı hesaplanır.
        labels = np.argmin(np.sqrt(((cluster - centers[:, np.newaxis]) ** 2).sum(axis=2)), axis=0)

        # k adet küme oluşturulduktan sonra her bir kümenin merkezini hesaplamak için kullanılır.
        new_centers = np.array([cluster[labels == i].mean(axis=0) for i in range(k)])

        # Eğer küme merkezleri değişmediyse döngüden çık
        # np.allclose() fonksiyonu merkezleri tutan dizilerin eleman olarak eşit olup olmadığını kontrol eder.
        if np.allclose(centers, new_centers):
            break
        centers = new_centers
    return centers, labels


if __name__ == '__main__':

    # Veri kümesi x1 ve x2 değerleri
    cluster = np.array([[1, 2], [3, 4], [5, 0], [2, 7], [9, 10], [0, 0]])

    # k değeri
    k = 2

    # K-Means algoritmasının çağrılması
    centers, labels = k_means(cluster, 2)

    # Küme merkezleri
    print("Küme merkezleri: ", centers)

    # Her bir verinin hangi kümede olduğunu gösteren etiketler
    print("Etiketler: ", labels)
