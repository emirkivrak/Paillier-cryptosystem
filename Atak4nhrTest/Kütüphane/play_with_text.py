import binascii
# -*- coding: UTF-8 -*-
##METNİ İNT DEĞERE ÇEVİRME VE O İNT DEĞERİ TEKRAR METNE ÇEVİRME KISMI

def string_to_int(data):
    #Yapılan İşlemler
    #UTF-8 ENCODE İLE UNICODE HALE GETİRİLİYOR.     "ATAKANÇÇTESTÜÜĞĞ" ====>   b'ATAKAN\xc3\x87\xc3\x87TEST\xc3\x9c\xc3\x9c\xc4\x9e\xc4\x9e'  
    #16 LIK HALE ÇEVİRDİK                           ====>b'4154414b414ec387c38754455354c39cc39cc49ec49e'
    #16 LIK HALDEN INT E ÇEVİRDİK                   ====>24442526145367114357973530860057415323702860751750302
    return int(binascii.hexlify(data.encode('utf-8')),16)
    
def int_to_string(data):
    #Yapılan İşlemler
    #ALINAN INT DEĞER 16 LIK DEĞERE DÖNÜŞTÜRÜLÜYOR
    #DÖNÜŞTÜRÜLEN 16 LIK DEĞERİN BAŞINDAKİ 0x İFADESİ KESİLİYOR
    #Unhexlify ile 16 lık değer unicode hale çevriliyor.
    #UNICODE OLAN DEĞER DECODE EDİLEREK STRİNG HALİNE GELİYOR
    return binascii.unhexlify(hex(data)[2:].encode('ascii')).decode('utf-8')



