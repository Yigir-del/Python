import sys
# Bu satır, Python'un 'sys' modülünü içeri aktarır. 'sys' modülü, Python yorumlayıcısının çeşitli fonksiyonlarına erişim sağlar.
# Burada 'sys.argv' komut satırından gelen parametreleri almak için kullanılıyor.

from PyQt5 import QtWidgets, QtGui
# PyQt5 kütüphanesinden 'QtWidgets' ve 'QtGui' modüllerini içeri aktarıyoruz.
# - 'QtWidgets' kullanıcı arayüzü bileşenlerini sağlar, örneğin pencereler, etiketler, düğmeler vb.
# - 'QtGui' modülü, resim işleme (pixmap) ve grafiksel öğelerle çalışmak için gereklidir.

def Pencere():
    # 'Pencere' fonksiyonunu tanımlıyoruz. Bu fonksiyon PyQt5 penceresini başlatacak olan kodu içeriyor.

    app = QtWidgets.QApplication(sys.argv)
    # PyQt5 uygulamasını başlatmak için 'QApplication' sınıfından bir nesne oluşturuluyor.
    # 'sys.argv' komut satırından gelen parametreleri alır. Burada bu parametreler kullanılmasa da uygulamanın çalışması için gereklidir.

    pencere = QtWidgets.QWidget()
    # 'QWidget', PyQt5'te bir pencereyi temsil eder. Bu satırda bir pencere nesnesi oluşturuyoruz.
    # Bu pencere daha sonra kullanıcıya gösterilecek olan ana arayüz olacaktır.

    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    # Burada iki tane etiket (label) nesnesi oluşturuluyor. 'QLabel', üzerinde metin veya resim gösterebileceğimiz bir bileşendir.
    # Etiketler 'pencere' nesnesine bağlı olacak, yani pencere içinde gösterilecekler.

    etiket2.setPixmap(QtGui.QPixmap("Prenses.png"))
    # Bu satır, 'etiket2' etiketine bir resim atar. 'QPixmap' sınıfı, resimleri yüklemek için kullanılır.
    # 'Prenses.png' adlı resim dosyasını 'etiket2' etiketine yükleriz.
    # Burada 'Prenses.png' dosyasının bulunduğunuz dizinde olması gerektiğini unutmamalısınız.

    etiket2.move(20, 100)
    # Bu satır, 'etiket2' etiketinin konumunu ayarlar. Bu etiket pencere içinde (x: 20, y: 100) koordinatlarına yerleştirilir.

    etiket1.setText("Burasi bir yazidir.")
    # 'etiket1' etiketine bir metin atarız. Burada, "Burasi bir yazidir." metnini 'etiket1' etiketine yazdırıyoruz.

    etiket1.move(200, 20)
    # Bu satır, 'etiket1' etiketinin konumunu ayarlar. Bu etiket pencere içinde (x: 200, y: 20) koordinatlarına yerleştirilir.

    pencere.setWindowTitle("PyQt5 Ders 1")
    # Bu satır, oluşturduğumuz pencerenin başlık çubuğunda görünen metni ayarlar.
    # Pencerenin başlığında "PyQt5 Ders 1" yazacaktır.

    pencere.setGeometry(100, 100, 700, 700)
    # 'setGeometry' fonksiyonu, pencerenin ekran üzerindeki konumunu ve boyutlarını belirler.
    # Burada pencere, (x: 100, y: 100) koordinatından başlayıp, genişliği 700 piksel ve yüksekliği 700 piksel olacak şekilde ayarlanır.

    pencere.show()
    # Bu satır, pencereyi ekranda görüntüler. Eğer bu satır olmasaydı, pencere oluşturulmuş olurdu fakat ekranda görünmezdi.

    sys.exit(app.exec_())
    # Bu satır, uygulamanın olay döngüsünü başlatır. 'app.exec_()' fonksiyonu, uygulamanın çalışmasını sağlar.
    # Uygulama kapandığında düzgün bir şekilde çıkmak için 'sys.exit()' fonksiyonu kullanılır.

Pencere()
# Son olarak, 'Pencere' fonksiyonunu çağırıyoruz. Bu, yukarıda tanımladığımız fonksiyonu çalıştırarak pencereyi açar ve içeriklerini gösterir.
