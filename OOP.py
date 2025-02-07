"""class Araba:
    marka = "reno"
    silindir = 4
    beygir = 110

araba = Araba()
araba.beygir = 120
print(araba.beygir)


class Araba2:
    def __init__(self,marka,silindir,beygir):
        self.marka = marka
        self.silindir = silindir
        self.beygir = beygir
        print("init çalışıyor")


araba2 = Araba2("renoult","4",110)
print(araba2.beygir)
print(araba2.marka)
print(araba2.silindir)
help(Araba2)
"""


class Yazilimci:
    def __init__(self,tecrube,maas,bildigi_diller,yas):
        self.tecrube = tecrube
        self.maas = maas
        self.bildigi_diller = bildigi_diller
        self.yas = yas
        print("Kisi eklendi.")
    
    def goster(self):
        print("""
        Tecrube = {}
        
        Maas = {}
        
        Bildigi diller = {}

        Yas = {}
        """.format(self.tecrube,self.maas,self.bildigi_diller,self.yas))

    def zam_yap(self,miktar):
        print("Zam yapiliyor...")
        self.maas += miktar
    def dil_ekle(self,dil):
        print("Dil ekleniyor...")
        self.bildigi_diller.append(dil)
    def deneyim(self,sure):
        print("Deneyim arttiriliyor")
        self.tecrube += sure

yazilimci = Yazilimci(10,40000,["java","C","javaScript"],30)
yazilimci.goster()
yazilimci.dil_ekle("C#")
yazilimci.goster()
yazilimci.zam_yap(1000)
yazilimci.goster()
    
