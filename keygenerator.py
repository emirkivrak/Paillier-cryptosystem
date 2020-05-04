from random import getrandbits,randrange,randint
from math import gcd ## gcd == ebob
from os import path,mkdir,getcwd,chdir
class PrivateKey:

    def __init__(self,lambda_val,micro):
        print("Gizli anahtar oluşturuluyor")
        self.l = lambda_val
        self.m = micro
        self.export_key_to_file() ## değerler constructor ile alınıyor ve direk fonksiyon çağırılıp key  dosyaları oluşturuluyor.

    def export_key_to_file(self):
        print("Gizli anahtar dışarı aktarma başlıyor.")

        """privatekey.txt dosyasını oluşturup üzerine yazıyoruz.."""
        try:
            with open("keys/privatekey.txt","w") as f:
                f.write(str(self.l))
                f.write("\n")
                f.write(str(self.m))
                print("dosya oluşturuldu && yazma işlemi yapıldı.")

        except IOError:
            print("Dosyaya yazarken bir hata oluştu! Anahtar düzgün işlenememiş olabilir!")

        finally:
            print("Gizli anahtar yazma işlemi bitti. ")



class PublicKey:

    def __init__(self,n_val,g_val):
        print("Açık anahtar oluşturuluyor")
        self.n = n_val
        self.g = g_val
        self.export_key_to_file() 

    def export_key_to_file(self):
        print("Açık anahtar dışa aktarma başlıyor.")

        """publickey.txt dosyasını oluşturup üzerine yazıyoruz.."""
        try:
            with open("keys/publickey.txt","w") as f:
                f.write(str(self.n))
                f.write("\n")
                f.write(str(self.g))
                print("dosya oluşturuldu && yazma işlemi yapıldı.")

        except IOError:
            print("Dosyaya yazarken bir hata oluştu! Anahtar düzgün işlenememiş olabilir!")

        finally:
            print("Açık anahtar yazma işlemi bitti. ")

class PaillierKeyGenerator:
    def generate_paillier_key_pairs(self,anahtar_uzunlugu):
        q = self.generate_random_primary_number(bits = anahtar_uzunlugu)
        p = self.generate_random_primary_number(bits = anahtar_uzunlugu)
        print("p ve q değerleri oluşturuldu.")
        
        n = p * q
        print("n değeri oluşturuldu.")
        
        lambda_val = self.ekok(p-1,q-1)
        print("lambda değeri oluşturuldu.")
        
        g = randint(n**2,n**3) ## n**2 den büyük rastgele bir g sayısı seçiliyor. üst limit olarak n**3 ün yeterli olacağını düşündüm.
        print("g değeri oluşturuldu.")
        
        """Vikipedia adım 4 deki L fonksiyonu ve işlem"""
        ##L = lambda x : x-1 // n
        ##mikro = (L(pow(g,lambda_val,n**2))**-1)  % n
        mikro = 1; ## DİKKAT !! MİKRO DEĞERİ ÜSTTEKİ GİBİ HESAPLANAMADIGI İÇİN İŞLEME DEVAM EDEBİLMEK İÇİN 1 VERDİM ..
        print("mikro değeri oluşturuldu")
        
        public_key = PublicKey(n,g)
        
        private_key = PrivateKey(lambda_val,mikro)
        

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

    def build_and_check_file_integrity(self):
        print("dosya yapısı kontrolü başlıyor ..")
        current_dir = getcwd() ## şu anki dizini aldık
        chdir(current_dir)
        private_key_path = "keys/privatekey.txt"
        public_key_path = "keys/publickey.txt"

        """Önceden key oluşturulup oluşturulmadığına bakıyoruz""" 
        try:
            if(path.exists("public_key_path") or path.exists(private_key_path)):
                print("halihazırda bir anahtar çifti saklama dosyası var içleri kontrol ediliyor...")
                if(path.getsize(private_key_path) != 0 and path.getsize(public_key_path) != 0):
                    ## iki dosyanın içeriği de 0 dan farklı ise muhtemel dolu
                    input("Yeni anahtar Çiftini üzerine yazmak için ENTER a basın işlemi sonlandırmak için CTRL+C")
            else:
                print("Keys dizini veya privatekey.txt ve publickey.txt Dosyaları Oluşturulmamış!")
                print("Dosyalar otomatik oluşturulacak")
        
            """ keys dizinini oluşturuyoruz"""
            try:
                mkdir('keys')
                print("keys dizini oluşturuldu")
            except FileExistsError:
                print("keys dizini oluşturulmuş .. Anahtar üretimine geçiliyor..")
        except:
            print("DOSYA BÜTÜNLÜĞÜ DOĞRULANAMADI, KEY YANLIŞ YERE YAZILIP OKUNABİLİR")

k=PaillierKeyGenerator()     
k.build_and_check_file_integrity()
k.generate_paillier_key_pairs(1024)
