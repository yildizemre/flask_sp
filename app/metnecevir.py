#matematik kütüphanesini çağırdık.
import math

def cevir(deger):

    def ucHaneOku(sayi): 
        birler = {"0":"","1":"Bir","2":"İki","3":"Üç","4":"Dört","5":"Beş","6":"Altı","7":"Yedi","8":"Sekiz","9":"Dokuz"}
        onlar = {"1":"On","2":"Yirmi","3":"Otuz","4":"Kırk","5":"Elli","6":"Altmış","7":"Yetmiş","8":"Seksen","9":"Doksan","0":""}
        yuz = ["Yüz"]
        
        if len(sayi) == 3:
        
            if sayi[0] == "1":
                oku = yuz[0]+onlar[sayi[1]]+birler[sayi[2]]
                return oku
            if sayi[0] == "0":
                oku = onlar[sayi[1]]+birler[sayi[2]]
                return oku
        
            else:
                oku = birler[sayi[0]]+yuz[0]+onlar[sayi[1]]+birler[sayi[2]]
                return oku
        if  len(sayi) == 1:
            
            if sayi[0] == "0":
                oku = "Sıfır"
                return oku
            else:
                oku = birler[sayi[0]]
                return oku
        if len(sayi) == 2:
            oku = onlar[sayi[0]]+birler[sayi[1]]
            return oku



   
    sayi=deger

    basaSifirEkle = len(sayi)%3
    if basaSifirEkle == 1:
        sayi = "00"+sayi
        
    elif basaSifirEkle == 2:
        sayi = "0"+sayi
    else:
        sayi = sayi


    kacYuzlerVar =  math.ceil(int(len(sayi))/3.0)
    #Uclu grub ların sonucu  gelecek degerler. Mesela 1.000.000 BirMilyon
    ucluGrub = {"0":"","1":"Bin","2":"Milyon","3":"Milyar","4":"Trilyon","5":"Katrilyon"}

    oku = ""

    for i in range(int(kacYuzlerVar)):
        
        if sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)] == "000":
            oku = oku
    
        elif sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)] == "001" and len(sayi) == 6:
            oku = ucluGrub[str(i)] + oku
        # İstisna durumlar yoksa belirttigimiz algoritmik sekilde bunu dondurerek yazdir. ve yazinin sonuna ekle
        # Mesela 535.776 sayisini once YediYuzYetmisAlti okuyup oku degiskenine atadi ve sona ekledi. Sonra
        #BesYuzOtuzBesBin i okudu ve onceki buludugu oku degiskenini bunun sagina ekledi ve 
        #BesYuzOtuzBesBinYediYuzYetmisAlti olustu.
        else:
            oku = ucHaneOku(sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)]) + ucluGrub[str(i)] + oku
    #Enson olarak olusturulan bu oku degeri ekrana yazdiriliyor.
    return oku