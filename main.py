from gemoetry.bangunruang import BangunRuang
from gemoetry.persegipanjang import PersegiPanjang
from gemoetry.segitiga import Segitiga

print('Use OOP')

p1 = PersegiPanjang(10,5)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(11,7)
print(s1.info())
print(s1.hitung_luas())

b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

#Polymorphism: kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
