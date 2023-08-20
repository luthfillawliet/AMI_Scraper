from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class AP2T:
    def __init__(self, filepathchromedriver, filepathenkripsi, urlap2t, user_options):

        self.filepathchromedriver = filepathchromedriver
        self.filepathenkripsi = filepathenkripsi
        self.urlap2t = urlap2t
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option('prefs',
        #                                        {"user-data-dir": "C:\\Users\\LENOVO\\AppData\\Local\\Google\\Chrome\\User Data"})
        chrome_options.add_argument(
            user_options)
        self.driver = webdriver.Chrome(
            executable_path=filepathchromedriver, options=chrome_options)
    
    def get_info_pelanggan(self, tipe_pencarian: str, nomor_id: str, link_infopelanggan: str):
        print("Membuka halaman Info Pelanggan")
        print("Tipe Pencarian yang di gunakan : ", tipe_pencarian)
        driver = self.driver
        # Maximize page
        driver.maximize_window()
        # go to ap2t url
        try:
            driver.get(link_infopelanggan)
            time.sleep(2)
            print("Info Pelanggan Berhasil di buka")
            # find edit text input
            edit_text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/form/fieldset/div/div/div[4]/div/div/div/div[2]/div/div/div/div[1]/input"))
            )
            edit_text.send_keys(nomor_id)
            # pilih kategori
            dropdwon_btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/form/fieldset/div/div/div[4]/div/div/div/div[1]/div/div/div/div[1]/div/img"))
            )
            dropdwon_btn.click()
            time.sleep(1)
            # pilih metode pencarian
            categories = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "x-combo-list-item"))
            )
            print("Jumlah Kategori : ", str(len(categories)))
            # Looping untuk get access tiap value dari kategori
            try:
                for i in categories:
                    print(i.text)
                    if (i.text.strip() == tipe_pencarian):
                        i.click()
                        break
                    else:
                        print("Kategori tidak ditemukan")
                # Loading load data
                time.sleep(1)
                btnSearch = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button"))
                )
                btnSearch.click()
                time.sleep(2)
                # Ekstract Id Pelanggan
                element0 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]/div"))
                )
                id_pelanggan = element0.text
                print(id_pelanggan)
                # Klik Tab DIL,sub tab main
                btnDil = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[1]/div[1]/ul/li[2]"))
                )
                btnDil.click()
                # Ekstract Info pelanggan
                # element1 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/input"))
                # )
                # namapelanggan = element1.get_attribute("value")
                # namapelanggan = "Nama Pelanggan : "+namapelanggan+"\n"
                # element2 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/input"))
                # )
                # tarif = element2.get_attribute("value")
                # tarif = "Tarif : "+tarif+"\n"
                # element3 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/input"))
                # )
                # daya = element3.get_attribute("value")
                # daya = "Daya : "+daya+"\n"
                # time.sleep(1)
                # # PNJ
                # element4 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[5]/div/div/div/div[1]/div/div/div/div[1]/input"))
                # )
                # # Nama PNJ
                # element5 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[5]/div/div/div/div[2]/div/div/div/div[1]/input"))
                # )
                # # No Bang
                # element6 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[5]/div/div/div/div[3]/div/div/div/div[1]/input"))
                # )
                # # Ket No bang
                # element7 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[5]/div/div/div/div[4]/div/div/div/div[1]/input"))
                # )
                # # Kabupaten
                # element8 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div/div/div[2]/div/div/div/div[1]/input"))
                # )
                # # Kecamatan
                # element9 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div/div/div[3]/div/div/div/div[1]/input"))
                # )
                # # Desa
                # element10 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div/div/div[4]/div/div/div/div[1]/input"))
                # )
                # alamat = "Alamat : "+element4.get_attribute("value") + " "+element5.get_attribute("value")+" "+element6.get_attribute("value")+" "+element7.get_attribute(
                #     "value")+" ,"+element10.get_attribute("value")+" ,"+element9.get_attribute("value")+" ,"+element8.get_attribute("value")+"\n"
                # Klik tab APP
                tabApp = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/ul/li[4]"))
                )
                tabApp.click()
                element11 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/input"))
                )
                nomor_meter = element11.get_attribute("value")
                nomor_meter = "Nomor kWh Meter : "+nomor_meter+"\n"
                print(nomor_meter)
                # # Get Merk kWh Meter
                # element12 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/input"))
                # )
                # merk_meter = element12.get_attribute("value")
                # merk_meter = "Merk kWh Meter : "+merk_meter+"\n"
                # print(merk_meter)
                # versiKRN = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div[1]/div/div/div/div[1]/input"))
                # )
                # krn = "Versi KRN : "+versiKRN.get_attribute("value")+"\n"
                # # Get Faktor Kali Meter
                # element13 = WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located(
                #         (By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div[6]/div/div/div/div[1]/input"))
                # )
                # fkm = element13.get_attribute("value")
                # fkm = "Faktor Kali Meter : "+fkm+"\n"
                # Merge semua data
                time.sleep(0.5)
                message = "Berhasil Ambil Info Pelanggan"
                time.sleep(1)
                return id_pelanggan
            except Exception as e:
                message = "Kategori gagal di peroleh\nMessage Error : "+str(e)
                print(message)
                return "0"
        except Exception as e:
            message = "Gagal membuka Info Pelanggan"
            print(message)
            print("Error message : ", e)
            return "0"
    

