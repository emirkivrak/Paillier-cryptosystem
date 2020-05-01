from random import getrandbits,randrange

class PaillierKeyGenerator:
    
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
                    print("Test başarıyla tamamlandı rastgele sayı : ")
                else:
                    continue

            except KeyboardInterrupt:
                print("devam etmekte olan işlemi sonlandırdınız.")
            ##except:
              ##  print("bir hata meydana geldi.. test düzgün gerçekleşememiş olabilir.")
            return large_number
                    


    def rabin_miller(self,n, k):

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
k=PaillierKeyGenerator()     
print(k.generate_random_primary_number())
