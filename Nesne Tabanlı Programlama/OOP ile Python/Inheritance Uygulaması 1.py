class Kisi:  # Superclass kişi
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def bilgileri_yazdir(self):
        print(self.isim, self.soyisim, self.yas)


class Ogrenci(Kisi):
    def __init__(self, isim, soyisim, yas, sinifi, aldigi_ders_sayisi):
        super().__init__(isim, soyisim, yas)  # Superclass dakileri kulanabilmek için
        self.sinifi = sinifi
        self.aldigi_ders_sayisi = aldigi_ders_sayisi

    # pass  pass i init yokken superclassı kullanmak için kullanılır
    def bilgileri_yazdir(self):  # Overwrite etmek sınıfın içinde varsa superclassa uğramaz
        print(self.isim, self.soyisim, self.yas, self.sinifi, self.aldigi_ders_sayisi)


class Ogretmen(Kisi):
    def __init__(self, isim, soyisim, yas, unvani, maasi):
        super().__init__(isim, soyisim, yas)
        self.unvani = unvani
        self.maasi = maasi

    def bilgileri_yazdir(self):
        print(self.isim, self.soyisim, self.yas, self.unvani, self.maasi)


kisi1 = Kisi("Gül", "Deniz", 40)
ogrenci1 = Ogrenci("Kader", "Yılmaz", 25, 4, 5)
ogretmen1 = Ogretmen("Kadir", "Veli", 32, "Dr", 2000)
kisi1.bilgileri_yazdir()
ogrenci1.bilgileri_yazdir()
ogretmen1.bilgileri_yazdir()
