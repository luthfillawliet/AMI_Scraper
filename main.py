from readdata import readdata
from scraping import AP2T
import time
filepath = "data//datameter.xlsx"
filepathchromedriver = r'chromedriver\chromedriver.exe'
filepathenkripsi = r'C:\Program Files (x86)\PT PLN (PERSERO)\AP2T ENKRIPSI\Token.exe'
urlap2t = 'https://ap2t.pln.co.id/ap2t/Login.aspx'
user_options = "user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data"
link_info_pelanggan = "https://ap2t.pln.co.id/infopelanggannewap2t-dr/"

def main():
    jumlahbaris = readdata.getjumlahbaris(filepath=filepath,sheetname="summary")
    print("Jumlah baris : "+str(jumlahbaris))
    ap2t = AP2T(filepathchromedriver=filepathchromedriver,filepathenkripsi=filepathenkripsi,urlap2t=urlap2t,user_options=user_options)
    for i in range(0,jumlahbaris):
        #print("Baris "+str(i))
        nomormeter = readdata.bacanomormeter(filepath=filepath,sheetname="list",baris=i)
        #print("Nomor Meter : "+str(nomormeter))
        id_pelanggan,nomorgardu = ap2t.get_info_pelanggan(tipe_pencarian="Nomor Meter",nomor_id=str(nomormeter),link_infopelanggan=link_info_pelanggan)
        #write idpel ke excel
        readdata.write_idpel(filepath=filepath,sheetname="list",data=id_pelanggan,column_number=2,row_number=i+2)
        #write nomor gardu ke excel
        readdata.write_nomorgardu(filepath=filepath,sheetname="list",data=nomorgardu,column_number=3,row_number=i+2)
        #print("Id pelanggan :" + id_pelanggan)
        
        
    


if __name__ == "__main__":
    main()