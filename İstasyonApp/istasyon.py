import datetime
import customtkinter
import time
import App

kullanicipen = customtkinter.CTk()
kullanicipen.geometry("500x400")
kullanicipen.resizable(False,False)
kullanicipen.title("Alfa - Oil")
kullanicipen.iconbitmap("login_icon.ico")

def kullanıci():
    kullanicipen.destroy()
    App.main()


Adminbuton=customtkinter.CTkButton(kullanicipen,text="Admin",width=80,height=10,command=kullanıci,hover_color="Green")
Adminbuton.place(x=5,y=5)
menü = customtkinter.CTkOptionMenu(kullanicipen,values=["Benzin","Dizel"],button_hover_color="Green")
menü.place(x=175,y=50)
plakalabel=customtkinter.CTkLabel(kullanicipen,text="Plaka:",font=("calibri",14),)
plakalabel.place(x=120,y=100)
plakaentry=customtkinter.CTkEntry(kullanicipen)
plakaentry.place(x=175,y=100)

Tutarlabel=customtkinter.CTkLabel(kullanicipen,text="Tutar:",font=("calibri",14),)
Tutarlabel.place(x=120,y=140)
tutarentry=customtkinter.CTkEntry(kullanicipen)
tutarentry.place(x=175,y=140)

App.cs.execute("select * from yakit where id=1")
bilgi= App.cs.fetchone()
benzinstk = int(bilgi[1])
dizelstk = int(bilgi[2])
bnzfyt = int(bilgi[3])
dzlfyt = int(bilgi[4])
def com():
    alımlitre = (int(tutarentry.get())/bnzfyt)
    if len(plakaentry.get())>8:
        App.messagebox.showerror("Hata!","Lütfen Geçerli Bir Plaka Giriniz.")

    if str(menü.get())=="Benzin":
        if alımlitre>benzinstk:
            App.messagebox.showerror("Hata!","Depoda Yeterli Miktarda Akaryakıt Bulunmamaktadır.")
        else:
            gstr = str(alımlitre)
            App.messagebox.showinfo("Başarılı!",f"Akaryakıt Alımı Başarıyla Tamamlanmıştır.{gstr[0:6]} Litre Benzin Aldınız.")
            yenibnzstok=int(benzinstk-alımlitre)
            App.cs.execute(f"UPDATE yakit SET benzin_stok={yenibnzstok} where id=1")
            App.cs.execute("INSERT INTO satiş(plaka,yakıt_türü,miktar,tutar,zaman) VALUES(?,?,?,?,?)",(plakaentry.get(),"benzin",alımlitre,tutarentry.get(),datetime.datetime.now()))
            App.baglanti.commit()
    else:
        dizellitre=(int(tutarentry.get())/dzlfyt)

        if dizellitre>dizelstk:
            App.messagebox.showerror("Hata!","Depoda Yeterli Miktarda Akaryakıt Bulunmamaktadır.")
        else:
            gstr = str(dizellitre)
            App.messagebox.showinfo("Başarılı!",f"Akaryakıt Alımı Başarıyla Tamamlanmıştır.{gstr[0:6]} Litre Dizel Aldınız.")
            yenidzlstok=int(dizelstk-dizellitre)
            App.cs.execute(f"UPDATE yakit SET dizel_stok={yenidzlstok} where id=1")
            App.cs.execute("INSERT INTO satiş(plaka,yakıt_türü,miktar,tutar,zaman) VALUES(?,?,?,?,?)",(plakaentry.get(),"dizel",dizellitre,tutarentry.get(),datetime.datetime.now()))
            App.baglanti.commit()



alımbuton = customtkinter.CTkButton(kullanicipen,text="Yakıt Al",font=("calibri",14),width=140,height=20,command=com,hover_color="Green")
alımbuton.place(x=175,y=200)

kullanicipen.mainloop()

