class Araba:
    """
    Basit bir Araba sınıfı. Varsayılan marka, silindir sayısı ve beygir gücü ile oluşturulur.
    """
    def __init__(self, marka="Renault", silindir=4, beygir=110):
        self.marka = marka
        self.silindir = silindir
        self.beygir = beygir

    def set_beygir(self, yeni_beygir):
        """Arabanın beygir gücünü günceller."""
        self.beygir = yeni_beygir

araba = Araba()
araba.set_beygir(120)
print(f"Güncellenmiş Beygir Gücü: {araba.beygir}")


class Yazilimci:
    """
    Yazılım geliştiricilerini modelleyen bir sınıf.
    """
    def __init__(self, tecrube: int, maas: float, bildigi_diller: list, yas: int):
        self.tecrube = tecrube
        self.maas = maas
        self.bildigi_diller = bildigi_diller
        self.yas = yas
        print("Yeni bir yazılımcı oluşturuldu.")
    
    def bilgileri_goster(self):
        """Yazılımcının bilgilerini ekrana yazdırır."""
        print(f"""
        Tecrübe: {self.tecrube} yıl
        Maaş: {self.maas} TL
        Bildiği Diller: {', '.join(self.bildigi_diller)}
        Yaş: {self.yas}
        """)

    def zam_yap(self, miktar: float):
        """Maaşa zam yapar."""
        self.maas += miktar
        print(f"Yeni maaş: {self.maas} TL")

    def dil_ekle(self, dil: str):
        """Yazılımcının bildiği dillere yeni bir programlama dili ekler."""
        if dil not in self.bildigi_diller:
            self.bildigi_diller.append(dil)
            print(f"{dil} dili eklendi.")
        else:
            print(f"{dil} dili zaten mevcut.")


# Yazılımcı nesnesi oluşturma
yazilimci = Yazilimci(10, 40000, ["Java", "C", "JavaScript"], 30)
yazilimci.bilgileri_goster()
yazilimci.dil_ekle("C#")
yazilimci.zam_yap(1000)
yazilimci.bilgileri_goster()


class Calisan:
    """
    Çalışanları modelleyen temel sınıf.
    """
    def __init__(self, maas: float, tecrube: int, departman: str):
        self.maas = maas
        self.tecrube = tecrube
        self.departman = departman
    
    def bilgileri_goster(self):
        """Çalışanın bilgilerini ekrana yazdırır."""
        print(f"""
        Departman: {self.departman}
        Tecrübe: {self.tecrube} yıl
        Maaş: {self.maas} TL
        """)
    
    def zam_yap(self, miktar: float):
        """Çalışanın maaşına zam yapar."""
        self.maas += miktar
        print(f"Yeni maaş: {self.maas} TL")


class Yonetici(Calisan):
    """
    Yönetici sınıfı, Çalışan sınıfından türetilmiştir ve ek olarak sorumlu olduğu kişi sayısını içerir.
    """
    def __init__(self, departman: str, tecrube: int, maas: float, sorumlu_kisi: int):
        super().__init__(maas, tecrube, departman)
        self.sorumlu_kisi = sorumlu_kisi

    def bilgileri_goster(self):
        """Yöneticinin bilgilerini ekrana yazdırır."""
        super().bilgileri_goster()
        print(f"Sorumlu Olunan Kişi Sayısı: {self.sorumlu_kisi}")


# Yönetici nesnesi oluşturma
yonetici = Yonetici("Yönetim", 15, 10000, 20)
yonetici.bilgileri_goster()
