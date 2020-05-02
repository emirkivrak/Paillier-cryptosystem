from random import getrandbits,randrange,randint
from math import gcd ## gcd == ebob

class PrivateKey:

    def __init__(self,lambda_val,micro):
        print("Gizli anahtar oluşturuluyor")
        self.l = lambda_val
        self.m = micro
        print("Gizli anahtar oluşturuldu")

    def printKey(self):
        print("** PRIVATE KEY ** ")
        print("lambda değeri : ",self.l)
        print("mikro değeri  :",self.m)
        print("** PRIVATE KEY **")

class PublicKey:

    def __init__(self,n,g):
        print("Açık anahtar oluşturuluyor")
        self.n = n
        self.g = g
        print("Açık anahtar Oluşturuldu.")
        
        
    def printKey(self):
        print("** PUBLIC KEY ** ")
        print("n değeri : ",self.n)
        print("g değeri  :",self.g)
        print("** PUBLIC KEY **")


class PaillierKeyGenerator:
    def generate_paillier_key_pairs(self):
        print("Anahtar çifti üretme işlemi başlıyor..")
        q = self.generate_random_primary_number()
        p = self.generate_random_primary_number()
        print("p ve q değerleri oluşturuldu.")

        n = p * q
        print("n değeri oluşturuldu.")
        
        lambda_val = self.ekok(p-1,q-1)
        print("lambda değeri oluşturuldu.")
        
        g = randint(n**2,n**3) ## n**2 den büyük rastgele bir g sayısı seçiliyor. üst limit olarak n**3 ün yeterli olacağını düşündüm.
        print("g değeri oluşturuldu.")
        
        """Vikipedia adım 4 deki L fonksiyonu ve işlem"""
        L = lambda x : x-1 // n
        mikro = (L(pow(g,lambda_val,n**2))**-1)  % n
        print("mikro değeri oluşturuldu")

    def generate_random_primary_number(self,numbers_of_test = 3,bits = 1024):
        print("Rastgele '",bits,"' bit asal sayı üretme islemi yapılacak '",numbers_of_test,"' kere test edilecek")
        """Rastgele büyük bir sayı üretip primality teste sokacağız eğer başarılı ise
        generation_successfull değeri true değişken alacak ve fonksiyon geriye sayıyı döndürecek 
        bu fonksiyon iki büyük p ve q asal sayısını üretmek için yazılıyor"""
        generation_succesfull = False 
        
        while(generation_succesfull == False):
            try:
                large_number = getrandbits(bits)
                if(self.rabin_miller(large_number,numbers_of_test)==True):
                    generation_succesfull == True
                    print("Rabin Miller testi başarılı. ")
                    return large_number
                else:
                    continue

            except KeyboardInterrupt:
                print("devam etmekte olan işlemi sonlandırdınız.")
            except:
                print("bir hata meydana geldi.. test düzgün gerçekleşememiş olabilir.")
           

    def rabin_miller(self,n, k):
        """Rabin Miller n-> sayı k -> test sayısı"""
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
    
    def ekok(self,a,b): return a * b // gcd(a,b) ## / yerine // kullanmam gerekti cunkü olusan float overflow error verdiriyor.

        

k=PaillierKeyGenerator()     
k.generate_paillier_key_pairs()
