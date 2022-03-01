from random import random
from flask import Flask, flash, request, redirect, url_for, current_app,send_from_directory,render_template, session
import numpy as np
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from wtforms import Form,StringField,TextAreaField,validators
from werkzeug.utils import secure_filename
from functools import wraps
import base64
import pandas as pd
from wtforms.fields.html5 import TelField,IntegerField
from datetime import datetime
from app import app
from app import metnecevir
import easyocr
import pytesseract
from PIL import Image


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return decorated_function
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["yetki"]==1:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("index"))

    return decorated_function

try:
    mydb = mysql.connector.connect(
        host="yatagroup.com",
        user="hypegena",
        password="&or496tD",
        database="hypegena_sprbkn"
    )
    print(mydb)
    
    mycursor2 = mydb.cursor(buffered=True)
    mycursor3 = mydb.cursor(buffered=True)
except Exception as e:
    print(e)
    mydb=False

def connection_db():
    mydb = mysql.connector.connect(
        host="yatagroup.com",
        user="hypegena",
        password="&or496tD",
        database="hypegena_sprbkn"
    )
    return mydb

with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)
app.secret_key = 'super secret key'
adi_soyadi = " "
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
tc_kimlik_no = " "
database_url = ""
kayit_tarihi = datetime.now()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# mail=session["username"]
app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)
img1 = []


    

@app.route("/update", methods=['GET', 'POST'])

def update():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    form1=İndexForm1(request.form)
    form2=İndexForm2(request.form)
    tc=""
    isim_soyisim=""
    telefon=""
    meslek=""
    sicil_numarasi=""
    plaka=""
    kamu_durumu=""
    giriş_tarihi=""
    cikis_tarihi=""
    yemek_durumu=""
    grup_durumu=""
    resepsiyon_notu=""
    oda_numarasi=""

    if request.method == 'POST':

        if request.form.get("button") == "kimlik_sorgulama":

            try:
                sorgulanan_tc = form1.tc_sorgulama_input.data
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute(
                    "SELECT kisisel_bilgiler.tcno,kisisel_bilgiler.ad_soyad,kisisel_bilgiler.tel,kisisel_bilgiler.meslek,kisisel_bilgiler.sicil_numarasi," +
                    "kisisel_bilgiler.plaka,kisisel_bilgiler.kamu_durumu,kayit_formu.giris_tarihi," +
                    "kayit_formu.cikis_tarihi,kayit_formu.yemek_durumu,kayit_formu.grup_durumu,kayit_formu.resepsiyon_notu,kayit_formu.oda_numarasi " +
                    "FROM kayit_formu " +
                    "INNER JOIN kisisel_bilgiler ON kayit_formu.kisiID = kisisel_bilgiler.kisiID " +
                    "WHERE tcno='"+sorgulanan_tc+"'")

                myresult = mycursor.fetchall()
                mycursor.close()
                for i in myresult:
                    form2.tc_no.data = i[0]
                    form2.isim_soyisim.data = i[1]
                    form2.telefon.data = i[2]
                    form2.meslek.data = i[3]

                    form2.sicil_numarasi.data = i[4]
                    form2.plaka.data = i[5]
                    kamu_durumu = i[6]
                    form2.date1.data = i[7]
                    form2.date2.data = i[8]
                    yemek_durumu = i[9]
                    grup_durumu = i[10]
                    form2.resepsiyon_not.data = i[11]
                    form2.oda_numarasi.data = i[12]
                flash("Kimlik Kontrolü Yapildi",'info')
                return render_template("update.html",form1=form1,form2=form2,
                kamu_durumu=kamu_durumu,yemek_durumu=yemek_durumu, grup_durumu=grup_durumu)
            except Exception as e:
                return render_template("update.html")

        elif request.form.get("button") == "güncelle":

            try:

                isim_soyisim = form2.isim_soyisim.data
                tc = form2.tc_no.data
                meslek = form2.meslek.data
                telefon = form2.telefon.data
                plaka = form2.plaka.data
                oda = form2.oda_numarasi.data
                date1 = form2.date1.data
                date2 = form2.date2.data
                grup_durum = request.form.get("group_durum")
                yemek_durum = request.form.get("yemek_durum")
                fiyat_grubu = request.form.get("fiyat_grubu")
                resepsiyon = form2.resepsiyon_not.data
                sicil_numarasi = form2.sicil_numarasi.data
                try:
                    mycursor = mydb.cursor(buffered=True)
                    mycursor.execute("update kisisel_bilgiler set ad_soyad='"+str(isim_soyisim)+"',tcno='"+str(tc)+"',meslek='"+str(meslek)+"'," +
                                    "tel='"+str(telefon)+"',plaka='"+str(plaka)+"',kamu_durumu='"+str(fiyat_grubu)+"',sicil_numarasi='"+str(sicil_numarasi)+"' where tcno='"+str(tc)+"'")
                    mydb.commit()
                    mycursor.close()
                    
                except Exception as e:
                    print(e,"1111")
                try:
                    mycursor2 = mydb.cursor(buffered=True)
                    mycursor2.execute(
                        "select kisiID from kisisel_bilgiler where tcno='"+str(tc)+"'")
                    new_id = mycursor2.fetchone()
                    new_id = new_id[0]
                    mycursor2.close()

                except Exception as e:
                    print(e,"2222")

                try:
                    mycursor = mydb.cursor(buffered=True)
                    mycursor.execute("update kayit_formu set giris_tarihi='"+str(date1)+"',cikis_tarihi='"+str(date2)+"',oda_numarasi='"+str(oda)+"',kisiID="+str(new_id)+"," +
                                    "resepsiyon_notu='"+str(resepsiyon)+"',grup_durumu="+str(grup_durum)+",yemek_durumu="+str(yemek_durum)+" where kisiID="+str(new_id)+"")
                    mydb.commit()
                    mycursor.close()
                    flash("Kimlik Güncellemesi Yapildi",'info')
                    return redirect(url_for("update"))
                except Exception as e:
                    flash("Kimlik Güncellemesi Yapılamadı",'info')
                    print(e,"33333")

            except Exception as e:
                print(e)
    else:
        return render_template("update.html",form1=form1,form2=form2)
    return render_template("update.html",form1=form1,form2=form2)



@app.route('/uploads/<name>')
@login_required
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route("/file_select", methods=['GET', 'POST'])
@login_required
def file_select():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    id_list = []
    tc_kimlik_no_list = []
    file_url_list = []
    kayit_date_list = []
    if request.method == 'POST':
        if request.form.get("button") == "value":
            date1 = (request.form.get("date1"))

            date2 = (request.form.get("date2"))
            try:
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute(
                    "SELECT * FROM file WHERE kayit_date >='"+date1+"' and kayit_date<'"+date2+"'")
                
                myresult = mycursor.fetchall()
                mycursor.close()
                for i in myresult:
                    id_list.append(i[0])
                    tc_kimlik_no_list.append((i[1]))
                    file_url_list.append(str(i[2]))
                    kayit_date_list.append((str(i[3])))
                flash("Dosya Yüklemeleri Listelendi",'info')
                
            except Exception as e:
                flash("Dosya Yüklemeleri Listelenemedi",'info')

    return render_template("upload_file.html", id_list=id_list, tc_kimlik_no_list=tc_kimlik_no_list, file_url_list=file_url_list, kayit_date_list=kayit_date_list)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload_file", methods=['GET', 'POST'])
@login_required
def upload_file():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    return_durum = ""
    if request.method == 'POST':

        if request.form.get("button") == "value":

            if 'file' not in request.files:
                return_durum = "LÜTFEN DOSYA SEÇİNİZ "
                return redirect(request.url)
            file = request.files['file']
            tc = request.form.get("tc_kimlik_no")
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return_durum = "LÜTFEN DOSYA SEÇİNİZ"
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save("./app/static/uploads/"+filename)
                file_url = "./static/uploads/"+filename
                datenow = datetime.now()

                try:
                    mycursor = mydb.cursor(buffered=True)
                    mycursor.execute(
                        "insert into file(tc_no,file_url,kayit_date)values(%s,%s,%s)", (tc, file_url, str(datenow)))
                    mydb.commit()
                    mycursor.close()
                    return_durum = "DOSYA YÜKLEME BAŞARILI"
                    flash("Dosya Yüklemesi Başarılı",'info')
                except Exception as e:
                    flash("Dosya Yüklenmesi Başarısız",'info')
                    

    return render_template("upload_file.html", return_durum=return_durum)

class İndexForm1(Form):
    tc_sorgulama_input=StringField("Sorgulanacak T.C. Kimlik Numarası",validators=[validators.DataRequired(message="Lütfen Boş Geçmeyiniz!")])
    
class İndexForm2(Form):
    isim_soyisim=StringField("İsim-Soyisim",validators=[validators.DataRequired(message="Lütfen Boş Geçmeyiniz!")])
    tc_no=StringField("T.C Kimlik Numarası",validators=[validators.DataRequired(message="Lütfen Boş Geçmeyiniz!")])
    meslek=StringField("Kurum Veya Meslek")
    telefon=TelField("Telefon Numarası",validators=[validators.DataRequired(message="Lütfen Boş Geçmeyiniz!")])
    plaka=StringField("Plaka",validators=[validators.DataRequired(message="Lütfen Bu Alanı Boş Geçmeyiniz!")])
    oda_numarasi=IntegerField("Oda Numarası",validators=[validators.DataRequired(message="Lütfen Bu Alanı Boş Geçmeyiniz!")])
    isim_soyisim2=StringField("2. İsim-Soyisim")
    tc_no2=StringField("2. Misafir T.C No")
    isim_soyisim3=StringField("3. İsim-Soyisim")
    tc_no3=StringField("3. Misafir T.C No") 
    isim_soyisim4=StringField("4. İsim-Soyisim")
    tc_no4=StringField("4. Misafir T.C No")
    date1=StringField("Giriş Tarihi",validators=[validators.DataRequired(message="Lütfen Bu Alanı Boş Geçmeyiniz!")])
    date2=StringField("Çıkış Tarihi",validators=[validators.DataRequired(message="Lütfen Bu Alanı Boş Geçmeyiniz!")])
    sicil_numarasi=StringField("Sicil Numarası")
    resepsiyon_not=TextAreaField("Resepsiyon Notu",validators=[validators.DataRequired(message="Lütfen Bu Alanı Boş Geçmeyiniz!")])
file = []
tc_gelen = ""
@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    global tc_gelen
    form1=İndexForm1(request.form)
   
    form2=İndexForm2(request.form)
    # global adi_soyadi, tc_kimlik_no, img1, database_url, meslek, sicil, plaka, fiyat_grubu, telefon
    adi_soyadi=""
    file_on_url=""
    file_arka = []
    file_kamu_url=""
    kamu_karti = []
    file_kamu=[]
    grub_usernames= []
    tc_no_array = []
    meslek=""
    database_url=""
    
    if request.method == 'POST':
      
        if request.form.get("button") == "kimlik_sorgulama" and form1.validate():
         
            try:
                mycursor2 = mydb.cursor(buffered=True)
                sorgulanan_tc=form1.tc_sorgulama_input.data
                mycursor2.execute("select * from kisisel_bilgiler where tcno='" +
                                sorgulanan_tc+"' ORDER BY kisiID ASC")
                datalar = mycursor2.fetchall()
                mycursor2.close()
                
                for data in datalar:
                    form2.isim_soyisim.data = data[1]
                    form2.tc_no.data = data[2]  
                    form2.telefon.data = data[4]
                    form2.plaka.data = data[5]
                    form2.meslek.data = data[3]
                    fiyat_grubu = data[6]
                    database_url = data[9]
                    form2.sicil_numarasi.data = data[8]
                print(database_url)

                print(datalar)
                if len(database_url)>5:
                    flash("Kimlik Kontrolü Yapildi",'info')
                    # print(adi_soyadi,tc_kimlik_no)
                    kimlik_goruntule="KİMLİK GÖRÜNTÜLEMEK İÇİN TIKLA"
                
                    return render_template("index.html",form1=form1,form2=form2, database_url=database_url, 
                                            fiyat_grubu=fiyat_grubu,kimlik_goruntule=kimlik_goruntule) 

                else:
                    form2.meslek.data = "MİSAFİR"
                    kimlik_goruntule="KİMLİK BULUNAMADI"
                    return render_template("index.html",form1=form1,form2=form2,kimlik_goruntule=kimlik_goruntule) 
            except Exception as e:
                print(e)
                kimlik_goruntule="KİMLİK SORGULANAMADI"
                return render_template("index.html",form1=form1,form2=form2,kimlik_goruntule=kimlik_goruntule) 
        
        
        if request.form.get("button") == "kimlik_oku":
            print("kimlik oku")
            file_on = request.files['file_on']
            file_arka = request.files['file_arka']
            if file_on and allowed_file(file_on.filename):
                now_save=datetime.now()
                
                file_on.save("./app/static/kimlik_on/"+str(now_save)+".jpg")
                file_on_url = "./app/static/kimlik_on/"+str(now_save)+".jpg"
                a=pytesseract.image_to_string(Image.open("./app/static/kimlik_on/"+str(now_save)+".jpg"), lang="tur")
                print("----------------------")
                print(a)
                print("----------------------")


                reader = easyocr.Reader(['tr'])
                result = reader.readtext("./app/static/kimlik_on/"+str(now_save)+".jpg")

                print("-------------------------")
                # img1 = cv2.imread('on.jpeg')
                tc_kimlik_no = (result[4][1])
                print("ön yüz "+str(tc_kimlik_no))
                adi = result[10][1]
                soyadi = result[7][1]
                adi_soyadi = adi+" "+soyadi
                print(adi_soyadi)
                print(tc_kimlik_no)

                form2.isim_soyisim.data=adi_soyadi
                form2.tc_no.data=tc_kimlik_no


            
        # if request.form.get("button") == "kimlik_getir":
        #     print("burda")
        #     file_on = request.files['file_on']
        #     file_arka = request.files['file_arka']
        #     if file_on and allowed_file(file_on.filename):
        #         now_save=datetime.now()

        #         file_on.save("./app/static/kimlik_on/"+str(now_save)+".jpg")
        #         file_on_url = "./app/static/kimlik_on/"+str(now_save)+".jpg"
                
                


        #         reader = easyocr.Reader(['tr'])
        #         result = reader.readtext("./app/static/kimlik_on/"+str(now_save)+".jpg")

        #         print("-------------------------")
        #         # img1 = cv2.imread('on.jpeg')
        #         tc_kimlik_no = (result[4][1])
        #         print("ön yüz "+str(tc_kimlik_no))
        #         adi = result[10][1]
        #         soyadi = result[7][1]
        #         adi_soyadi = adi+" "+soyadi
        #         print(adi_soyadi)
        #         print(tc_kimlik_no)
        #         print("-------------------------")
        #         print("ön arka yüklendi")
        #         database_url='./static/database_ıd/'+str(tc_kimlik_no)+'.png'








        #         file_on=cv2.imread(str(file_on_url))
        #         cv2.imwrite('./app/static/database_ıd/'+str(tc_kimlik_no)+'.png', file_on)

              
           

        #     if file_arka and allowed_file(file_arka.filename):

                
        #         file_arka.save("./app/static/kimlik_arka/"+str(tc)+".jpg")
        #         file_arka_url = "./app/static/kimlik_arka/"+str(tc)+".jpg"
        #         file_arka=cv2.imread(str(file_arka_url))
        #         # vis=cv2.imread(str(file_arka_url))
        #         print("file arka yüklendi")
        #     try:
        #         # file exists
        #             vis = np.concatenate((file_on, file_arka), axis=1)
        #             cv2.imwrite('./app/static/database_ıd/'+str(tc)+'.png', vis)
        #             database_url='./static/database_ıd/'+str(tc)+'.png'
        #     except Exception as e:
        #         print(e)
        

        
        if request.form.get("button") == "kaydet" and form2.validate():

            isim_soyisim = form2.isim_soyisim.data
            tc = form2.tc_no.data
            tc_gelen=tc
            meslek = form2.meslek.data
            telefon = form2.telefon.data
            plaka = form2.plaka.data
            oda = form2.oda_numarasi.data
            date1 = form2.date1.data
            date2 = form2.date2.data
            grup_durum = request.form.get("group_durum")
            isim_soyisi2 = form2.isim_soyisim2.data
            isim_soyisi3 = form2.isim_soyisim3.data
            isim_soyisi4 = form2.isim_soyisim4.data
            print(isim_soyisi2)
            print(isim_soyisi3)
            print(isim_soyisi4)
            tc_no2 = form2.tc_no2.data
            tc_no3 = form2.tc_no3.data
            tc_no4 = form2.tc_no4.data

            

            yemek_durum = request.form.get("yemek_durum")
            fiyat_grubu = request.form.get("fiyat_grubu")
           
            print("fiyat gurubu "+ fiyat_grubu)
            print(type(fiyat_grubu))
            resepsiyon = form2.resepsiyon_not.data
            kayit_tarihi = datetime.now()
            sicil_numarasi = "0"
            sicil_numarasi = form2.sicil_numarasi.data
            mail = session["username"]
            print("yükle")
           

            if len(isim_soyisi2)>3:
                if len(tc_no2)>3:
                    tc_no_array.append(tc_no2)
                    grub_usernames.append(isim_soyisi2)
            if len(isim_soyisi3)>3:
                if len(tc_no3)>3:
                    tc_no_array.append(tc_no3)
                    grub_usernames.append(isim_soyisi3)
            if len(isim_soyisi4)>3:
                if len(tc_no4)>3:
                    tc_no_array.append(tc_no4)
                    grub_usernames.append(isim_soyisi4)

               
            

            print((grub_usernames))


            tarih = kayit_tarihi
            oda_numarasi = oda
            ad_soyad = isim_soyisim
            vd_no = tc
            tahsilat_sekli = "KK"
            tutar_sayi = " "
            vd_ad = " "
            tutar_yazi="" 
            
            aciklama = str(date1)+ " ile "+str(date2) + " Tarihleri arasında konaklama ücreti."
            görevli_isim = "RESEPSİYON"
            try:
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("insert into makbuz(tarih,oda_numarasi,ad_soyad,vd_no,tahsilat_sekli,tutar_sayi,tutar_yazi,aciklama,görevli_adi)" +
                                "values('"+str(tarih)+"','"+str(oda_numarasi)+"','"+str(ad_soyad)+"','"+str(vd_no)+"','"+str(tahsilat_sekli)+"','"+str(tutar_sayi)+"','"+str(tutar_yazi)+"','"+str(aciklama)+"','"+str(görevli_isim)+"')")
                mydb.commit()
                mycursor.close()

                

            except Exception as e:
                print("Makbuz database insert yapılmadı")
                print(e)

          
            

            try:
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("insert into kisisel_bilgiler(ad_soyad,tcno,meslek,tel,plaka,kamu_durumu," +
                                "mail,sicil_numarasi,data_url)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (isim_soyisim, tc, meslek, telefon, plaka, fiyat_grubu, mail, sicil_numarasi, database_url))
                mydb.commit()
                mycursor.close()
            except Exception as e:
                flash("Kayit başarılı degil.","info")
                print(e)
            try:
                mycursor2 = mydb.cursor(buffered=True)
                mycursor2.execute(
                    "select kisiID from kisisel_bilgiler where tcno='"+tc+"'")
                new_id = mycursor2.fetchone()
                new_id = new_id[0]
                mycursor2.close()

            except Exception as e:
                flash("Kayit başarılı degil.","info")
                print(e)
                
            
            try:
                mycursor3 = mydb.cursor(buffered=True)
                sql = 'insert into kayit_formu(giris_tarihi,cikis_tarihi,oda_numarasi,kisiID,resepsiyon_notu,grup_durumu,yemek_durumu,kayit_tarihi) values(%s,%s,%s,%s,%s,%s,%s,%s)'
                val = (date1, date2, oda, new_id, resepsiyon,
                       grup_durum, yemek_durum, kayit_tarihi)
                mycursor3.execute(sql, val)
                mydb.commit()
                mycursor3.close()
                print("kayit başaılı")
                flash("Kayit Basarili","info") 
            except Exception as e:
                
                flash("Kayit başarılı degil.","info")
          

            print(grub_usernames)
            print("---------------------------")
            print(len(grub_usernames))
            print("---------------------------")
            try:

                for i in range(len(grub_usernames)):
                    try:
                        mycursor = mydb.cursor(buffered=True)
                        mycursor.execute("insert into kisisel_bilgiler(ad_soyad,tcno,meslek,tel,plaka,kamu_durumu," +
                                        "mail,sicil_numarasi,data_url)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (grub_usernames[i], tc_no_array[i], "MİSAFİR","-", "-", "1", "-", "-", "-"))
                        mydb.commit()
                        mycursor.close()
                        print("GRUP KİŞİSEL BİLGİLER EKLENDİ")
                    except Exception as e:
                        flash("GRUP Kayit başarılı degil.","info")
                        print("1")
                        print(e)
                    try:
                        mycursor2 = mydb.cursor(buffered=True)
                        mycursor2.execute(
                            "select kisiID from kisisel_bilgiler where tcno='"+tc_no_array[i]+"'")
                        new_id = mycursor2.fetchone()
                        new_id = new_id[0]
                        mycursor2.close()

                    except Exception as e:
                        print("2")
                        print(e)
                    
                    try:
                        mycursor3 = mydb.cursor(buffered=True)
                        sql = 'insert into kayit_formu(giris_tarihi,cikis_tarihi,oda_numarasi,kisiID,resepsiyon_notu,grup_durumu,yemek_durumu,kayit_tarihi) values(%s,%s,%s,%s,%s,%s,%s,%s)'
                        val = (date1, date2, oda, new_id, "g",
                            "1", "1", kayit_tarihi)
                        mycursor3.execute(sql, val)
                        print("GRUP KAYIT FORMU EKLENDİ")
                        mydb.commit()
                        
                        mycursor3.close()

                    except Exception as e:
                        print("3")
                        print(e)
                        flash("GRUP Kayit başarılı degil.","info")
            except Exception as e:
                print(e)
            
            #######################################################################################################
            return redirect(url_for("index"))
    
    else:
        return render_template("index.html",form1=form1,form2=form2)
    return render_template("index.html",form1=form1,form2=form2)

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    global dataframe_rapor
    print("profile",dataframe_rapor)
    twitter_kullanici_adi = session["username"]

    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute(
            "select*from users WHERE name_surname = '"+str(twitter_kullanici_adi)+"' ")
        myresult = mycursor.fetchall()
        mycursor.close()
        for i in myresult:
            twitter_kullanici_adi = i[3]
            name_surname = i[4]
    except:
        pass

    # username=request.form.get("twitter_user_one") # veritabani sorguları olacak cache'den gelecek giriş yapılan kullanici
    # user_pass=request.form.get("pass")# veritabani sorguları olacak cache'den gelecek giriş yapılan kullanici
    # mail=request.form.get("mail")
    if request.method == 'POST':
        mail = session["username"]

        old_pass = request.form.get("password_current")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select*from users where mail='" +
                         str(mail)+"' and pass='"+str(old_pass)+"'")
        myresult = mycursor.fetchall()
        mycursor.close()
        if myresult:
            newpass1 = request.form.get("password")
            newpass2 = request.form.get("password_confirmation")
            if newpass1 == newpass2:
                mycursor2 = mydb.cursor(buffered=True)
                mycursor2.execute("update users SET pass='" +
                                  newpass1+"' where mail='"+mail+"'")
                mydb.commit()
                mycursor2.close()
                flash("Şifre Değiştirildi",'info')
            else:
                flash("Şifre Değiştirelemedi",'info')

    new_name = request.form.get("name")
    mail = request.form.get("email")

    if request.method == 'POST':
        if request.form.get("button") == "value":

            try:
                sql = "UPDATE users SET mail = '" + \
                    str(mail)+"' WHERE name_surname = '" + \
                    str(twitter_kullanici_adi)+"' "
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute(sql)
                session["username"] = mail
                twitter_kullanici_adi = session["username"]
                mydb.commit()
                mycursor.close()

            except Exception as e:
                pass
    return render_template("profile.html", mail=mail, twitter_kullanici_adi=twitter_kullanici_adi)


@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

dataframe_rapor = []


date1 = ""
date2 = ""

@app.route("/raporlar", methods=['GET', 'POST'])
@login_required
def raporlar():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    
    raporlar_return_array = []
    raporlar_yedek_array=[]
    global dataframe_rapor,date1,date2
    # global id_list,isim_soyisim_list,tc_list,plaka_list,giris_list,cikis_list,yemek_durum_list,resepsiyon_not_list,oda_numarasi_list,date1,date2
    id_list = []
    isim_soyisim_list = []
    tc_list = []
    telefon_list = []
    plaka_list = []
    giris_list = []
    cikis_list = []
    kamu_durum_list = []
    yemek_durum_list = []
    resepsiyon_not_list = []
    oda_numarasi_list = []
    toplam_kayit=""

    if request.method == 'POST':
        if request.form.get("button") == "value":
            try:
                date1 = request.form.get("date1")
                date2 = request.form.get("date2")




                
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute(
                    "SELECT kayit_formu.kayitID,kisisel_bilgiler.ad_soyad,kisisel_bilgiler.tcno,kisisel_bilgiler.tel," +
                    "kisisel_bilgiler.plaka,kisisel_bilgiler.kamu_durumu,kayit_formu.giris_tarihi," +
                    "kayit_formu.cikis_tarihi,kayit_formu.yemek_durumu,kayit_formu.resepsiyon_notu,kayit_formu.oda_numarasi ,kayit_formu.grup_durumu " +
                    "FROM kayit_formu " +
                    "INNER JOIN kisisel_bilgiler ON kayit_formu.kisiID = kisisel_bilgiler.kisiID " +
                    "WHERE kayit_formu.kayit_tarihi>='"+date1+"' and kayit_formu.kayit_tarihi<'"+date2+"'")
                
                myresult = mycursor.fetchall()
                mycursor.close()
                toplam_kayit="Toplam "+ str((len(myresult))) +" Kayıt Buldundu"
                for i in myresult:
                    id_list.append(i[0])
                    isim_soyisim_list.append((i[1]))
                    tc_list.append(str(i[2]))
                    telefon_list.append((str(i[3])))
                    plaka_list.append(str(i[4]))
                    giris_list.append(str(i[6]))
                    cikis_list.append(str(i[7]))
                    kamu_durum_list.append((i[5]))
                   
                    
                    yemek_durum_list.append(str(i[8]))
                    resepsiyon_not_list.append(str(i[9]))
                    oda_numarasi_list.append(str(i[10]))

                    raporlar_return_array.append([str(i[2]),str(i[5]),str(i[11])])
                dataframe_rapor = pd.DataFrame(raporlar_return_array, columns = ['TC', 'Kamu Durumu','Grup Durumu'])
                print(kamu_durum_list)
                print(kamu_durum_list[0])

                print(type(kamu_durum_list[0]))
                if len(myresult)>0:
                    flash("Rapor Görüntülendi",'info')
                    # print(dataframe_rapor)
                else:
                    flash("Rapor Bulunamadı",'info')
            except Exception as e:
                print(e)
                flash("Rapor Görüntülenemedi",'info')   
                
                
                
        if request.form.get("button") == "yedek_value":

            try:
                date1 = request.form.get("date1")
                date2 = request.form.get("date2")




                
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute(
                    "SELECT kayit_formu.kayitID,kisisel_bilgiler.ad_soyad,kisisel_bilgiler.tcno,kisisel_bilgiler.tel," +
                    "kisisel_bilgiler.plaka,kisisel_bilgiler.kamu_durumu,kayit_formu.giris_tarihi," +
                    "kayit_formu.cikis_tarihi,kayit_formu.yemek_durumu,kayit_formu.resepsiyon_notu,kayit_formu.oda_numarasi ,kayit_formu.grup_durumu " +
                    "FROM kayit_formu " +
                    "INNER JOIN kisisel_bilgiler ON kayit_formu.kisiID = kisisel_bilgiler.kisiID " +
                    "WHERE kayit_formu.kayit_tarihi>='"+date1+"' and kayit_formu.kayit_tarihi<'"+date2+"'")
                
                myresult = mycursor.fetchall()
                mycursor.close()
                toplam_kayit="Toplam "+ str((len(myresult))) +" Kayıt Buldundu"
                for i in myresult:
                    id_list.append(i[0])
                    isim_soyisim_list.append((i[1]))
                    tc_list.append(str(i[2]))
                    telefon_list.append((str(i[3])))
                    plaka_list.append(str(i[4]))
                    giris_list.append(str(i[6]))
                    cikis_list.append(str(i[7]))
                    kamu_durum_list.append((i[5]))
                   
                    
                    yemek_durum_list.append(str(i[8]))
                    resepsiyon_not_list.append(str(i[9]))
                    oda_numarasi_list.append(str(i[10]))

                    raporlar_return_array.append([str(i[2]),str(i[5]),str(i[11])])
                    raporlar_yedek_array.append([str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6]),str(i[7]),str(i[8]),str(i[9]),str(i[10])])

                dataframe_rapor = pd.DataFrame(raporlar_return_array, columns = ['TC', 'Kamu Durumu','Grup Durumu'])
                
                dataframe_yedek = pd.DataFrame(raporlar_yedek_array, columns = ['ID', 'İSİM SOYİSİM', 'TC', 'TELEFON', 'PLAKA','GIRIS TARİHİ','CIKIS TARİHİ','KAMU DURUMU','YEMEK DURUMU','RESEPSİYON NOTU','ODA NUMARASI'])
                dataframe_date_name = datetime.now()
                dataframe_yedek.to_csv("./app/static/yedekler/"+str(dataframe_date_name)+".csv")
                
                dataframe_yedek_path=("./static/yedekler/"+str(dataframe_date_name)+".csv")


                
                
                flash("Rapor Yedeklendi",'info')
                new_url="http://etresepsiyon.gsb.gov.tr:5000/"+str(dataframe_yedek_path)
                return redirect(new_url, code=302)
                    # print(dataframe_rapor)
                
            except Exception as e:
                flash("Yedek Oluşturulamadi",'info')
                print(e)
        if request.form.get("button") == "rapor_value":
            try:

                date1 = request.form.get("date1")
                date2 = request.form.get("date2")
                print(dataframe_rapor)
                toplam_kayit=len(dataframe_rapor)
                kamu_personeli=dataframe_rapor[dataframe_rapor['Kamu Durumu']=="0"]
                toplam_kamu_personeli=len(kamu_personeli)
                kamu_harici=dataframe_rapor[dataframe_rapor['Kamu Durumu']=="1"]
                toplam_kamu_harici=len(kamu_harici)
                print(toplam_kayit)
                print(toplam_kamu_personeli)
                print(toplam_kamu_harici)
                grup=dataframe_rapor[dataframe_rapor['Grup Durumu']=="1"]
                toplam_grup=len(grup)
                tekil=dataframe_rapor[dataframe_rapor['Grup Durumu']=="0"]
                toplam_tekil=len(tekil)



                return render_template("chart.html",toplam_tekil=toplam_tekil,toplam_grup=toplam_grup,date1=str(date1),date2=str(date2),toplam_kayit=toplam_kayit,toplam_kamu_personeli=toplam_kamu_personeli,toplam_kamu_harici=toplam_kamu_harici)
            except Exception as e:
                print(e)
                return render_template("raporlar.html",toplam_kayit=toplam_kayit,date1=date1,date2=date2, id_list=id_list, isim_soyisim_list=isim_soyisim_list, tc_list=tc_list, telefon_list=telefon_list, plaka_list=plaka_list, giris_list=giris_list, cikis_list=cikis_list, kamu_durum_list=(kamu_durum_list), yemek_durum_list=yemek_durum_list, resepsiyon_not_list=resepsiyon_not_list, oda_numarasi_list=oda_numarasi_list)

           
    return render_template("raporlar.html",toplam_kayit=toplam_kayit,date1=date1,date2=date2, id_list=id_list, isim_soyisim_list=isim_soyisim_list, tc_list=tc_list, telefon_list=telefon_list, plaka_list=plaka_list, giris_list=giris_list, cikis_list=cikis_list, kamu_durum_list=(kamu_durum_list), yemek_durum_list=yemek_durum_list, resepsiyon_not_list=resepsiyon_not_list, oda_numarasi_list=oda_numarasi_list)
@app.route("/chart", methods=['GET', 'POST'])
@login_required
def chart():
    

    return render_template("chart.html")

@app.route("/forms", methods=['GET', 'POST'])
@login_required
def forms():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    twitter_kullanici_adi = session["username"]
    result_mail = ""
    if request.method == 'POST':

        if request.form.get("button") == "value":
            name_suname = request.form.get("isim_soyisim")
            telefon = request.form.get("telefon")
            konu = request.form.get("konu")
            baslik = request.form.get("baslik")
            mesaj = request.form.get("mesaj")
            to = ['yildizemre2@hotmail.com', 'yildizemre2@gmail.com']
            subject = baslik
            body = name_suname+"n"+telefon+" "+konu+"\n"+mesaj

            account = 'ali.gkky196@gmail.com'
            password = 'Ali19671570'

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.ehlo()

            server.starttls()

            server.login(account, password)
            mail = MIMEText(body, 'html', 'utf-8')
            mail['From'] = account
            mail['Subject'] = subject
            mail['To'] = ','.join(to)
            mail = mail.as_string()

            try:
                server.sendmail(account, to, mail)
                result_mail = ('Mail gönderimi başarılı')
                flash("Mail gönderimi başarılı",'info')

            except:
                result_mail = ('Mail gönderimi başarısız')
                flash("Mail gönderimi başarısız",'info')

    return render_template("forms.html", result_mail=result_mail, twitter_kullanici_adi=twitter_kullanici_adi)


@app.route("/login", methods=['GET', 'POST'])
def login():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("pass")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select*from users where mail='" +
                         email+"' and password='"+password+"'")
        myresult = mycursor.fetchall()
        mycursor.close()
        if myresult:
            for i in myresult:
                session["username"]=i[1]
                session["yetki"]=i[5]
            session["logged_in"] = True

            return redirect(url_for("index"))

        else:

            return render_template("login.html")

    return render_template("login.html")

class makbuzPage(Form):
    tarih=StringField("Tarih",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!")])
    oda_numarasi=IntegerField("Oda Numarası:",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!")])
    ad_soyad=StringField("Ad-Soyad Veya Kurum Adı:",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!")])
    vd_no=StringField("V.D No:",validators=[validators.DataRequired(message="Bu Alan Boş Bıkılamaz!")])
    vd_ad=StringField("V.D Ad:",validators=[validators.DataRequired(message="Bu Alan Boş Bıkılamaz!")])
    tahsilat_sekli=StringField("Tahsilat Şekli:",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!")])
    tutar_sayi=IntegerField("Tutar(Sayı):",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!"),validators.AnyOf(values=".",message="Nokta(.),Virgül(,) gibi işaretler kullanmayınız.Sadece Sayısal Değer Yazın.")])
    aciklama=TextAreaField("Açıklama:",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!"),
    validators.Length(min=4,max=250,message="Minimum 4 Maksimum 250 Karakter Kullanabilirsiniz.")])
    görevli_adi=StringField("Görevli Adı-Soyadı:",validators=[validators.DataRequired(message="Bu Alan Boş Bırakılamaz!")])
vd_ad = ""
@app.route("/makbuz_page", methods=['GET', 'POST'])
@login_required
def makbuz_page():
    global mydb

    form1=İndexForm1(request.form)
    

    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    form=makbuzPage(request.form)
    global vd_ad

    if request.form.get("button") == "kimlik_sorgulama":
        print("kimlik sorgulama")

        tc = request.form.get("tc")
        print(tc)


        try:
            
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("select*from makbuz where vd_no="+str(tc)+" ORDER BY makbuzID ASC ")
            result = mycursor.fetchall()
            mycursor.close()
            for i in result:
                islem_no = i[0]
                tarih = i[1]
                oda_numarasi = i[2]
                ad_soyad = i[3]
                vd_no = i[4]
                tahsilat_sekli = i[5]
                tutar_sayi = i[6]
                tutar_yazi = i[7]
                aciklama = i[8]
                görevli_isim = i[9]

            form.tarih.data=tarih 
            form.oda_numarasi.data=oda_numarasi 
            form.ad_soyad.data=ad_soyad 
            form.vd_no.data=vd_no 
            form.tahsilat_sekli.data=tahsilat_sekli
            form.tutar_sayi.data=tutar_sayi
            form.vd_ad.data=vd_ad
             
            
            form.aciklama.data =aciklama 
            form.görevli_adi.data =görevli_isim
        except Exception as e:
            return redirect(url_for("500.html"))
       





    if request.form.get("button") == "makbuz":
        tarih = form.tarih.data
        oda_numarasi = form.oda_numarasi.data
        ad_soyad = form.ad_soyad.data
        vd_no = form.vd_no.data
        tahsilat_sekli = form.tahsilat_sekli.data
        tutar_sayi = form.tutar_sayi.data
        vd_ad = form.vd_ad.data
        tutar_yazi=metnecevir.cevir(str(tutar_sayi)) 
        print(tutar_yazi)
        aciklama = form.aciklama.data
        görevli_isim = form.görevli_adi.data
        try:
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("insert into makbuz(tarih,oda_numarasi,ad_soyad,vd_no,tahsilat_sekli,tutar_sayi,tutar_yazi,aciklama,görevli_adi)" +
                             "values('"+str(tarih)+"','"+str(oda_numarasi)+"','"+str(ad_soyad)+"','"+str(vd_no)+"','"+str(tahsilat_sekli)+"','"+str(tutar_sayi)+"','"+str(tutar_yazi)+"','"+str(aciklama)+"','"+str(görevli_isim)+"')")
            mydb.commit()
            mycursor.close()

            return redirect(url_for("makbuz", id=vd_no))

        except Exception as e:
            print("Makbuz database insert yapılmadı")
            print(e)
    else:
        return render_template("makbuzpage.html",form1=form1,form=form)
    return render_template("makbuzpage.html",form=form,form1=form1)


@app.route("/makbuz/<id>", methods=['GET', 'POST'])
def makbuz(id):
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    global vd_ad
    islem_no = ""
    tarih = ""
    oda_numarasi = ""
    ad_soyad = ""
    vd_no = ""
    tahsilat_sekli = ""
    tutar_sayi = ""
    tutar_yazi = ""
    aciklama = ""
    görevli_isim = ""
    try:
        print(id)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select*from makbuz where vd_no="+id+" ORDER BY makbuzID ASC ")
        result = mycursor.fetchall()
        mycursor.close()
        for i in result:
            islem_no = i[0]
            tarih = i[1]
            oda_numarasi = i[2]
            ad_soyad = i[3]
            vd_no = i[4]
            tahsilat_sekli = i[5]
            tutar_sayi = i[6]
            tutar_yazi = i[7]
            aciklama = i[8]
            görevli_isim = i[9]
    except Exception as e:
        return redirect(url_for("500.html"))
    
    return render_template("makbuz.html",vd_ad=vd_ad, tarih=tarih, islem_no=islem_no, oda_numarasi=oda_numarasi, ad_soyad=ad_soyad, vd_no=vd_no, tahsilat_sekli=tahsilat_sekli, tutar_sayi=tutar_sayi, tutar_yazi=tutar_yazi, aciklama=aciklama, görevli_isim=görevli_isim)


count = 0
imza_array = []






# @app.route("/delete/<id>")
@app.route("/imza", methods=['GET', 'POST'])
def imza():
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()

    global imza_array, count,tc_gelen
    tc_gelen=str(tc_gelen)
    if request.method == 'POST':
        data = request.get_data()
        data = data[22:]
        imza_array.append(data)
        if request.form.get("button") == "imza_kaydet":
            print("1")
            try:
                tc = request.form.get("tc_sorgulama_input")
                
                for i in imza_array:
                    print("2")
                    data_len = (len(str(i)))
                    print(data_len)
                    if data_len:

                        kayit_tarihi = datetime.now()
                        kayit_tarihi = str(kayit_tarihi)[:18]
                        kayıt_txt="./app/static/imza_uploader/"+str(tc)+"_"+kayit_tarihi+".png"
                        with open(kayıt_txt, "wb") as fh:
                            fh.write(base64.decodebytes(i))
                        print("basildi")
                        mycursor = mydb.cursor(buffered=True)
                        mycursor.execute("insert into imza_file(imza_tc,imza_file)values('"+str(tc)+"','"+kayıt_txt+"')")
                        mydb.commit()
                        mycursor.close()
                        imza_array.clear()
                        flash("İmza Kabul Edildi",'info')
                        tc_gelen=""
                        return redirect(url_for("index"))
            except Exception as e:
                print(e)
                flash("İmza Kabul Edilmedi",'info')
    else:
        try:

            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("Select * from imza_file WHERE imza_tc="+str(tc_gelen)+"")
            
            myresult = mycursor.fetchall()
            
            mycursor.close()

            if len(myresult)>0:
                flash("Daha Önce İmza Bulunmaktadır.",'info')
                return redirect(url_for("index"))
        except Exception as e:
            print(e)
        return render_template("imza.html",tc=tc_gelen)

    return render_template("imza.html",tc=tc_gelen)


@app.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("login"))


@app.route("/delete/<id>")
@admin_required
def delete(id):
    global mydb



    if mydb:
        print("Baglandi")
    else:
        mydb=connection_db()
    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("delete from kayit_formu where kayitID ="+id+" ")
        mydb.commit()
        mycursor.close()

    except Exception as e:
        pass

    return redirect(url_for("raporlar"))




