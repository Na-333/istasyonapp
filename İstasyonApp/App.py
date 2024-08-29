import time
import tkinter
import customtkinter
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import pywinstyles

baglanti = sqlite3.connect("OPET.db")
cs = baglanti.cursor()

customtkinter.set_appearance_mode("light")


def adminpencere():

    cs.execute("Select * from yakit where id=1")
    yakitbilgi=cs.fetchone()
    benzinstok = str(yakitbilgi[1])
    dizelstok=str(yakitbilgi[2])
    benzinfiyat=yakitbilgi[3]
    dizelfiyat=yakitbilgi[4]



    adminpen=customtkinter.CTk()
    adminpen.geometry("800x400")
    adminpen.resizable(False,False)
    adminpen.title("Admin Paneli")
    adminpen.iconbitmap("login_icon.ico")

    backimage = customtkinter.CTkImage(light_image=Image.open("oilback.png"),size=(800,400))
    labelback = customtkinter.CTkLabel(adminpen, image=backimage, text="")
    labelback.pack()
    solframe = customtkinter.CTkLabel(adminpen,text="",fg_color="#ffffff",width=300,height=300)
    solframe.place(x=25,y=50)
    sagframe = customtkinter.CTkLabel(adminpen, text="", fg_color="#ffffff", width=300, height=300)
    sagframe.place(x=475,y=50)
    pywinstyles.set_opacity(solframe, value=0.5)
    pywinstyles.set_opacity(sagframe,value=0.5)

    benzinlabel = customtkinter.CTkLabel(solframe, text="Benzin Stoğu:",font=("Calibri",14))
    benzinlabel.place(x=10, y=20)
    dizellabel = customtkinter.CTkLabel(solframe, text="Dizel Stoğu:", font=("Calibri", 14))
    dizellabel.place(x=10, y=50)
    benzinentry = customtkinter.CTkEntry(solframe,width=80,height=5)
    benzinentry.place(x=90,y=20)
    dizelentry = customtkinter.CTkEntry(solframe, width=80, height=5)
    dizelentry.place(x=90, y=50)
    benzin_fiyat_label=customtkinter.CTkLabel(solframe,text="Benzin Fiyatı:",font=("Calibri",14))
    dizel_fiyat_label = customtkinter.CTkLabel(solframe, text="Dizel Fiyatı:", font=("Calibri", 14))
    benzin_fiyat_label.place(x=10,y=80)
    dizel_fiyat_label.place(x=10,y=110)
    benzinfiyat_entry=customtkinter.CTkEntry(solframe,width=80,height=5)
    benzinfiyat_entry.place(x=90,y=80)
    dizelfiyat_entry = customtkinter.CTkEntry(solframe, width=80, height=5)
    dizelfiyat_entry.place(x=90, y=110)
    benzinentry.insert(0,benzinstok[0:7])
    dizelentry.insert(0,dizelstok[0:7])
    benzinfiyat_entry.insert(0,benzinfiyat)
    dizelfiyat_entry.insert(0,dizelfiyat)

    adminmevsifrelabel=customtkinter.CTkLabel(sagframe,text="Mevcut Şifre:",font=("calibri",14))
    adminmevsifrelabel.place(x=10,y=20)
    adminnewsifrelabel = customtkinter.CTkLabel(sagframe, text="Yeni Şifre:", font=("calibri", 14))
    adminnewsifrelabel.place(x=10, y=50)
    adminnewkadlabel = customtkinter.CTkLabel(sagframe, text="Yeni K_Adı:", font=("calibri", 14))
    adminnewkadlabel.place(x=10, y=80)

    adminmevsifentry=customtkinter.CTkEntry(sagframe,width=80,height=5)
    adminmevsifentry.place(x=90,y=20)
    adminnewsifentry = customtkinter.CTkEntry(sagframe, width=80, height=5)
    adminnewsifentry.place(x=90, y=50)
    adminnewkadentry = customtkinter.CTkEntry(sagframe, width=80, height=5)
    adminnewkadentry.place(x=90, y=80)

    def adminbilgiguncelle():

        cs.execute("select * from admin where id=1")
        adminbilgi=cs.fetchone()
        adm_sif=adminbilgi[2]
        if adminmevsifentry.get()==adm_sif:
            cs.execute("UPDATE admin SET kullanici=? , sifre=? WHERE id=?",(adminnewkadentry.get(),adminnewsifentry.get(),1))
            baglanti.commit()

            messagebox.showinfo("Succession","Giriş Bilgileri Başarıyla Güncellendi")
        else:
            messagebox.showinfo("Failed","İşlem Başarısız! Girilen Bilgiler Doğru Değil.")

    def yakitguncelle():
        

        cs.execute(f"UPDATE yakit SET benzin_stok = {benzinentry.get()},dizel_stok ={dizelentry.get()},benzin_fiyat={benzinfiyat_entry.get()},dizel_fiyat={dizelfiyat_entry.get()} WHERE id=1")
        baglanti.commit()

    yakitbilgi_button=customtkinter.CTkButton(solframe,text="KAYDET",width=120,height=30,command=yakitguncelle)
    yakitbilgi_button.place(x=10,y=150)
    admingunbuton = customtkinter.CTkButton(sagframe, text="KAYDET", width=120, height=30, command=adminbilgiguncelle)
    admingunbuton.place(x=10, y=120)

    adminpen.mainloop()





def main():
    def check():
        cs.execute("select * from admin where id=1")
        kayit = cs.fetchone()
        kullanıci_tablo = kayit[1]
        sifre_tablo = kayit[2]
        if kullanıci_tablo == k_ad_entry.get() and sifre_tablo == sifre_entry.get():
            pencere.destroy()
            adminpencere()

        else:
            messagebox.showinfo("Uyarı", "Giriş Başarısız")

    pencere = customtkinter.CTk()
    pencere.geometry("400x500")
    pencere.title("Alfa Oil - Login")
    pencere.resizable(False,False)
    pencere.iconbitmap("login_icon.ico")

    login_resim=customtkinter.CTkImage(light_image=Image.open("login2.png"),dark_image=Image.open("login.png"),size=(150,150))
    login_label=customtkinter.CTkLabel(pencere,image=login_resim,text="")
    login_label.place(x=125,y=30)
    k_ad_entry=customtkinter.CTkEntry(pencere,width=120,height=6,text_color="#00b1c3",bg_color="white")
    k_ad_entry.place(x=140,y=180)
    sifre_entry=customtkinter.CTkEntry(pencere,width=120,height=6,text_color="#00b1c3",bg_color="white",show="*")
    sifre_entry.place(x=140,y=210)
    kullanıcıad_label=customtkinter.CTkLabel(pencere,text="Kullancı Adı:",font=("calibri",14),text_color="#00b1c3")
    kullanıcıad_label.place(x=40,y=180)
    sifre_label=customtkinter.CTkLabel(pencere,text="Şifre:",font=("calibri",14),text_color="#00b1c3")
    sifre_label.place(x=40,y=210)
    login_buton=customtkinter.CTkButton(pencere,text="Giriş Yap",bg_color="white",font=("calibri",15),width=120,fg_color="#c60c0f",command=check)
    login_buton.place(x=140,y=240)
    pywinstyles.set_opacity(k_ad_entry,color="white")
    pywinstyles.set_opacity(sifre_entry,color="white")
    pywinstyles.set_opacity(login_buton,color="white")
    k_ad_entry.insert(0,"fahrisozer")
    sifre_entry.insert(0,"as1234")

    pencere.mainloop()