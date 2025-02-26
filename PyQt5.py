import sys
# Bu satır, Python'un 'sys' modülünü içeri aktarır. 'sys' modülü, Python yorumlayıcısının çeşitli fonksiyonlarına erişim sağlar.
# Bu durumda, uygulamanın sonunda 'sys.exit()' fonksiyonunu kullanabilmek için bu modülü import ettik.

from PyQt5 import QtWidgets
# Bu satır, PyQt5 kütüphanesinin QtWidgets modülünü içeri aktarır.
# QtWidgets, PyQt5'teki grafiksel kullanıcı arayüzü bileşenlerini sağlar (örneğin, pencereler, düğmeler, etiketler, vb.).
# Buradaki temel bileşen, pencereyi oluşturabilmemizi sağlayan 'QWidget' sınıfıdır.

def Pencere():
    # 'Pencere' adında bir fonksiyon tanımlıyoruz. Bu fonksiyon, PyQt5 penceresini başlatacak olan kodu içeriyor.

    app = QtWidgets.QApplication(sys.argv)
    # PyQt5'te uygulama başlatmak için 'QApplication' sınıfından bir nesne oluşturulması gerekir.
    # 'sys.argv', komut satırından gelen parametreleri alır, ama burada bu parametreler kullanılmayacak.
    # Bu satır, PyQt5 uygulamasını başlatmak için gerekli olan uygulama nesnesini oluşturur.

    pencere = QtWidgets.QWidget()
    # 'QWidget', PyQt5'te bir pencereyi temsil eder. Bu satırda bir pencere (widget) nesnesi oluşturuyoruz.
    # Bu pencere daha sonra kullanıcıya gösterilecek olan ana arayüz olacaktır.

    pencere.setWindowTitle("PyQt5 Ders 1")
    # Bu satır, oluşturduğumuz pencerenin başlık çubuğunda görünen metni ayarlar.
    # Başlık çubuğunda "PyQt5 Ders 1" metni görünecek.

    pencere.show()
    # Bu satır, pencereyi ekranda görüntüler.
    # Eğer bu satır olmasaydı, pencere oluşturulmuş olurdu ama ekranda görünmezdi.

    sys.exit(app.exec_())
    # Bu satır, uygulamanın olay döngüsünü başlatır. 'app.exec_()' fonksiyonu uygulamanın çalışmasını sağlar.
    # Uygulama kapandığında düzgün bir şekilde çıkmak için 'sys.exit()' fonksiyonu kullanılır.
    # Bu satır, uygulama penceresi kapatılana kadar programın devam etmesini sağlar.

Pencere()
# Son olarak, 'Pencere' fonksiyonunu çağırıyoruz. Bu, yukarıda tanımladığımız fonksiyonu çalıştırarak pencerenin açılmasını sağlar.
