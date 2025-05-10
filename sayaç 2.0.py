import time

while True:

    saat=int(input("Kaç saat : "))
    dk=int(input("Kaç dakika : "))
    sn=int(input("Kaç saniye : "))


    while saat>=0:
        sn-=1

        if sn==-1:
            dk-=1
            sn+=60

        else:
            time.sleep(1)
            print(f"{saat} saat, {dk} dakika, {sn} saniye kadlı.")


        if dk==-1:
            saat-=1
            dk+=60

        if saat==0 and dk==0 and sn==0:
            print("Süre bitti")
            break