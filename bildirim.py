#BU MODÜL İLE BİLGİSAYAR ÜZERİNDE BİLDİRİM GÖNDEREBİLİRSİN VEYA ÇOK SAYIDA FARKLI İŞLEM YTGULAYABİLİRSİN

from plyer import notification
from plyer import battery
#from plyer import gps# MASAÜSTÜNDE DESTEKLENMİYOR ANDROİD CİHAZLAR İÇİN DAHA İŞLEVSEL.

from plyer import filechooser#DOSYA SEÇMEMİZE YARAYAN BİR MODÜL.

dosyalar = filechooser.open_file()
print(dosyalar)

#from plyer import audio#SEÇİLEN YOLDAKİ SES DOSYASINI BİZİM İÇİN OYNATIR.

#audio.play(filepath="")




#def print_location(**kwargs):
#    print(**kwargs)

#gps.configure(on_location=print_location)
#gps.start()

info=battery.status
print(info)

notification.notify(
    title="Merhaba",
    message=f"Şarjınız={info}",
    app_name="Nasılsın",
    timeout=5
)