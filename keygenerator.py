from random import getrandbits,randrange,randint
from math import gcd ## gcd == ebob

class PaillierKeyGenerator:
    def generate_paillier_key_pairs(self):
        q = generate_random_primary_number()
        p = generate_random_primary_number()

        n = p * q 
        
        lambda_val = self.ekok(p-1, q-1)
        
        g = random.randint(n**2,n**3) ## n**2 den büyük rastgele bir g sayısı seçilecekti,  n**2 den n**3 e kadar olabilir.


    def generate_random_primary_number(self,numbers_of_test = 3,bits = 1024):
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
    
    def ekok(a,b): return a * b / gcd(a,b)

        

k=PaillierKeyGenerator()     
print(k.generate_random_primary_number())
