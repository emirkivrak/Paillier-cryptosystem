import binascii
from random import getrandbits, randrange
import math


depolayici={'p':0,
            'q':0,
            'n':0,
            'lambda':0,
            'nü':0,
            'public':0,
            'private':0,
            'nkare':0
            }

# -*- coding: UTF-8 -*-

"BÜYÜK SAYILARDA İŞLEMLER PATLADIĞI İÇİN KULLANILAN FONKSİYONLAR"
def invmod(a, p, maxiter=1000000):
    """The multiplicitive inverse of a in the integers modulo p:
         a * b == 1 mod p
       Returns b.
       (http://code.activestate.com/recipes/576737-inverse-modulo-p/)"""
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in range(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

def modpow(base, exponent, modulus):
    """Modular exponent:
         c = b ^ e mod m
       Returns c.
       (http://www.programmish.com/?p=34)"""
    result = 1
    while exponent > 0:
        if exponent & 1 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result




##METNİ İNT DEĞERE ÇEVİRME VE O İNT DEĞERİ TEKRAR METNE ÇEVİRME KISMI

def string_to_int(data):
    # Yapılan İşlemler
    # UTF-8 ENCODE İLE UNICODE HALE GETİRİLİYOR.     "ATAKANÇÇTESTÜÜĞĞ" ====>   b'ATAKAN\xc3\x87\xc3\x87TEST\xc3\x9c\xc3\x9c\xc4\x9e\xc4\x9e'
    # 16 LIK HALE ÇEVİRDİK                           ====>b'4154414b414ec387c38754455354c39cc39cc49ec49e'
    # 16 LIK HALDEN INT E ÇEVİRDİK                   ====>24442526145367114357973530860057415323702860751750302
    return int(binascii.hexlify(data.encode('utf-8')), 16)


def int_to_string(data):
    # Yapılan İşlemler
    # ALINAN INT DEĞER 16 LIK DEĞERE DÖNÜŞTÜRÜLÜYOR
    # DÖNÜŞTÜRÜLEN 16 LIK DEĞERİN BAŞINDAKİ 0x İFADESİ KESİLİYOR
    # Unhexlify ile 16 lık değer unicode hale çevriliyor.
    # UNICODE OLAN DEĞER DECODE EDİLEREK STRİNG HALİNE GELİYOR
    return binascii.unhexlify(hex(data)[2:].encode('ascii')).decode('utf-8')


def anahtar_cifti_olustur(bits):
    "P VE Q ASAL SAYILARI BULMAK İSTEDİĞİMİZ KEYİN BİT SAYISININ YARISI KADARDIR. P = 512BIT Q = 512BIT  N=1024 BIT"
    "P VE Q ASAL SAYILARI EŞİT UZUNLUKTA SEÇİLMİŞLERDİR."
    print("P DEĞİŞKENİ OLUŞTURULUYOR...")
    depolayici['p'] = asal_sayi_olustur(int(bits/2))
    print("P=",depolayici['p'])
    print("Q DEĞİŞKENİ OLUŞTURULUYOR...")
    depolayici['q'] = asal_sayi_olustur(int(bits/2))
    print("Q=", depolayici['p'])
    print("PUBLİC KEY OLUŞTURULUYOR...")
    public_key()
    private_key()


def asal_sayi_olustur(bits=512,numbers_of_test=3):
    """Rastgele büyük bir sayı üretip primality teste sokacağız eğer başarılı ise
       generation_successfull değeri true değişken alacak ve fonksiyon geriye sayıyı döndürecek
       bu fonksiyon iki büyük p ve q asal sayısını üretmek için yazılıyor"""
    large_number=0
    while(1):
        large_number = getrandbits(bits)
        if (rabin_miller(large_number, numbers_of_test) == True):
            break
    return large_number



def rabin_miller(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def public_key():
    "P VE Q EŞİT UZUNLUKTADIR"
    "n=p*q"
    "lambda=()"
    if(depolayici['q']!=0,depolayici['p']!=0):
        depolayici['n']= depolayici['p']*depolayici['q']
        depolayici['g']=depolayici['n']+1
        depolayici['nkare']=depolayici['n']*depolayici['n']
    print('PUBLIC KEY : ',depolayici['n'],depolayici['g'])

def private_key():
    depolayici['lambda']=(depolayici['p']-1) * (depolayici['q'] -1)
    depolayici['nü']=invmod(depolayici['lambda'],depolayici['n'])
    print('PRIVATE KEY : ',depolayici['lambda'],depolayici['nü'])

def encrypt(plain):
    while True:
        r = asal_sayi_olustur((round(math.log(depolayici['n'], 2))))
        if r > 0 and r < depolayici['n']:
            break
    x = pow(r, depolayici['n'], depolayici['nkare'])
    cipher = (pow(depolayici['g'], plain, depolayici['nkare']) * x) % (depolayici['nkare'])
    return cipher

def decrypt(cipher):
    x = pow(cipher, depolayici['lambda'], depolayici['nkare']) - 1
    plain = ((x//depolayici['n'])*depolayici['nü']) %depolayici['n']
    return plain



anahtar_cifti_olustur(1024)
print(depolayici)
chipher = encrypt(string_to_int('TEST YAPIYORUM BROO'))
print('SIFRELI TEXT',chipher)
print('ÇÖZÜLMÜŞ TEXT ==>',int_to_string(decrypt(chipher)))

