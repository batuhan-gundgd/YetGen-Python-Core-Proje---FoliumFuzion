import requests
from bs4 import BeautifulSoup
import pandas as pd
import folium
import re  # Sayı olan değerleri ayıklayıp yazdırmak için
import time
import webbrowser
import folium.plugins


class Indicators():
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()

        if secim == "1":
            print("Trade Balance Verisi Alınıyor...\n")
            time.sleep(2)
            self.trade_balance()
        
        if secim == "2":
            print("Nüfus Dağılım Verisi Alınıyor...")
            time.sleep(2)
            self.nufus_dagilim()

        if secim == "3":
            print("Inflation Verileri Alınıyor...\n")
            time.sleep(2)
            self.inflation()

        if secim == "4":
            print("GDP Verileri Aktarılıyor\n")
            time.sleep(2)
            self.gdp()

        if secim == "5":
            print("CO2 Verisi Alınıyor...\n")
            time.sleep(2)
            self.CO2_emission()

        if secim == "6":
            print("Ana Veriler Yükleniyor...\n")
            time.sleep(2)
            self.harita()
        
        if secim == "7":
            print("Daha Fazla Veri Yükleniyor...\n")
            time.sleep(2)
            self.daha_fazla_veri()

        if secim == "8":
            print("Programdan Çıkılıyor...\n")
            time.sleep(2)
            self.cikis()



    def menu(self):
        def kontrol(secim): # ana veriler icin
            if not re.search("[1-8]",secim):
                raise Exception("Lutfen 1 ve 8 Arasinda Gecerli Bir Secim Yapın!!")
            elif len(secim)!=1:
                raise Exception(("Lutfen 1 ve 8 Arasinda Gecerli Bir Secim Yapın!!"))
        while True:
            try:
                secim=input("\n\nMerhabalar, FoliumFuzion Menusune Hos Geldiniz...\n\nLutfen Yapmak İstediginiz İslemi Seciniz...\n\
[1]Trade Balance İndikatörü\n[2]Nufüs Dağılım Oranı\n[3]Enflasyon\n[4]GDP\n[5]CO2 Emissions\n\
[6]Tüm Ana Verileri Haritada Görselleştir\n[7]Daha Fazla Veriye Erişim Sağla\n[8]Cıkış\nSeçim:  ")
                kontrol(secim)
            except  Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secim                


    def nufus_dagilim(self):
        nufus_dagilim_haritasi = folium.FeatureGroup(name="NüfusDağılımHaritası")
        world_map = folium.Map(tiles="Cartodb dark_matter")
        nufus_dagilim_haritasi.add_child(folium.GeoJson(
                            data=(open(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\world.json"
                                       , "r", encoding="utf-8-sig").read()),
                            style_function= lambda x : {'fillColor':'green'
                            if x["properties"]["POP2005"] < 20000000 else 'white'
                            if 20000000 <= x["properties"]["POP2005"]  <= 50000000 else 'orange'
                            if 50000000 <= x["properties"]["POP2005"] <= 100000000 else 'red'}))
        world_map.add_child(nufus_dagilim_haritasi)
        world_map.add_child(folium.LayerControl())
        world_map.add_child(folium.LatLngPopup()) #
        world_map.add_child(folium.plugins.Geocoder(position="topleft"))
        world_map.add_child(folium.plugins.Fullscreen(position="topright", title="Expand", title_cancel="Exit Expanded View", force_separate_button=True))
        world_map.add_child(folium.plugins.MiniMap(toggle_display=True, show = True, zoom_level_offset=-12))
        world_map.save("nufus_map.html")
        print("Nüfus Dağılım Verisi Haritaya İşlendi")
        n_d = input("Harita Açılsın mı?[E/H]")
        if n_d.upper() == 'E':
            print("Harita Açılıyor")
            time.sleep(2)
            html_file_path = r'C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\nufus_map.html'

    
            webbrowser.open(html_file_path)
        else:
            print("Harita açılmadı.")
            time.sleep(1)
            print("Menuye Donuluyor...")
            self.menudon()


    
    def trade_balance(self):
        tercih = input("Tercihinizi Giriniz...\n[1]Veriyi Haritada Görselleştir\n[2]Güncel Veriye Eriş\n\nTercih:   ")
        if tercih == "1":
             self.trade_balance_harita()
        if tercih == "2":
             self.trade_balance_ekrana_getir()
        else:
            print("Hatalı tercih!")
    
    def trade_balance_harita(self):
        veri = pd.read_excel(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\ana_veriler.xlsx")
        enlemler = list(veri["Enlem"])
        boylamlar = list(veri["Boylam"])
        trade_balance = list(veri["esas"])

        Trade_Balance_Map = folium.FeatureGroup(name="Trade Balance")

        def trade_balance_renk(t_b):
                if t_b > 300:
                    return "green"
                elif t_b > 60:
                    return "white"
                elif t_b > 5:
                    return "yellow"
                elif t_b > -50:
                    return "orange"
                else:
                    return "red"

        def trade_balance_yari_cap(t_b):
                if t_b > 400:
                    return 50000
                elif t_b > 60:
                    return 60000
                elif t_b > 5:
                    return 70000
                elif t_b > -20:
                    return 100000
                else:
                    return 200000
        world_map = folium.Map(tiles="Cartodb dark_matter")
        for enlem, boylam, t_balance in zip(enlemler,boylamlar,trade_balance): #
                Trade_Balance_Map.add_child(folium.Circle(location=(enlem, boylam),
                                                 radius=trade_balance_yari_cap(t_balance),
                                                 color=trade_balance_renk(t_balance),
                                                 fill=trade_balance_renk(t_balance),
                                                 fill_opacity=0.5))
            
        world_map.add_child(Trade_Balance_Map)
        world_map.add_child(folium.LayerControl())
        world_map.add_child(folium.LatLngPopup()) #
        world_map.add_child(folium.plugins.Geocoder(position="topleft"))
        world_map.add_child(folium.plugins.Fullscreen(position="topright", title="Expand", title_cancel="Exit Expanded View", force_separate_button=True))
        world_map.add_child(folium.plugins.MiniMap(toggle_display=True, show = True, zoom_level_offset=-12))
        world_map.save("trade_balance_map.html")
        time.sleep(2)
        print("Trade Balance Verisi Haritaya İşlendi... ")
        t_b = input("Harita Açılsın mı?[E/H]")
        if t_b.upper() == 'E':
                print("Harita Açılıyor")
                time.sleep(2)
                html_file_path = r'C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\trade_balance_map.html'

    
                webbrowser.open(html_file_path)
        elif t_b.upper() == "H":
             print("Menuye Donuluyor...")
             time.sleep(1)
             self.menudon()

        else:
                print("Harita açılmadı.")
                time.sleep(2)
                self.menudon()


        
        
    def trade_balance_ekrana_getir(self):
            print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
            time.sleep(2)
            url = "https://www.theglobaleconomy.com/rankings/trade_balance_dollars/"


            response = requests.get(url)
            response.raise_for_status()#    HTTP isteği başarılı mı kontrol eder

            parser = BeautifulSoup(response.content, 'html.parser')

            ülkeler = ["Albania","Algeria","Angola","Antigua-and-Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan",
"Bahrain","Bangladesh","Belarus","Belgium","Belize","Bhutan","Bolivia","Bosnia-and-Herzegovina","Brazil","Bulgaria",
"Cambodia","Canada","Cape-Verde","Chile","China","Colombia","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Denmark","Dominican-Republic","Dominica",
"Ecuador","El-Salvador","Estonia","Ethiopia",
"Finland","France",
"Georgia","Germany","Greece","Grenada","Guatemala",
"Honduras","Hong-Kong","Hungary",
"Iceland","India","Indonesia","Ireland","Israel","Italy",
"Japan",
"Kazakhstan","Kuwait",
"Latvia","Lebanon","Lesotho","Lithuania","Luxembourg",
"Malaysia","Mauritius","Mexico","Moldova","Mongolia","Montenegro","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Nigeria","Macedonia","Norway",
"Pakistan","Panama","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Romania","Russia","Rwanda",
"Saint-Lucia","Samoa","Saudi-Arabia","Serbia","Seychelles","Singapore","Slovakia","Slovenia","Solomon-Islands","South-Africa","South-Korea","Spain","Sri-Lanka","Saint-Vincent-and-the-Grenadines","Suriname","Sweden","Switzerland",
"Tajikistan","Thailand","Turkey",
"United-Kingdom","USA","Ukraine","Uruguay","Uzbekistan",
"Vietnam",
]

            frames = []
            for i in range(len(ülkeler)):
                try:
                    table = parser.find("a", {"href":f"/{ülkeler[i]}/trade_balance_dollars/"}).parent.parent.find_all("td")
                    bilgi12 = table[1].string
                    bilgi22 = table[0].a.string
                    bilgi3 = table[2].string
                    item_str1 = str(bilgi12)
                    item_str2 = str(bilgi3)
                    cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                    cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                    frames.append({
                        'Country Name': bilgi22,
                        'Trade Balance': cleaned_item1,
                        'Global Rank': cleaned_item2
                    })
                except AttributeError:
                    continue
            frame = pd.DataFrame(frames)
            print(frame)
        
            x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
            if x.upper() == "E":
                dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                try:
                    frame.to_excel(f"{dosya_konum}"\
                                           ,sheet_name="Trade_Balance",index=False)
                    print("Veriler Excele Başarıyla İşlendi...")
                    time.sleep(2)
                    self.menudon()
                except FileNotFoundError:
                    print("Dosya dizini hatalı girildi")
            elif x.upper() == "H":
                print("Ana Menuye Donuluyor")
                time.sleep(2)
                self.menudon()
            else:
                print("Hatalı komut!!")



    def inflation(self):
        tercih = input("Tercihinizi Giriniz...\n[1]Veriyi Haritada Görselleştir\n[2]Güncel Veriyi Ekrana Getir\nTercih: ")
        if tercih == "1":
            self.inflation_harita()
        if tercih == "2":
             self.inflation_ekrana_getir()
        else:
            print("Hatalı tercih!")
    
    def inflation_harita(self):
        veri = pd.read_excel(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\ana_veriler.xlsx")

        enlemler = list(veri["Enlem"])
        boylamlar = list(veri["Boylam"])
        enflasyon_oranlari = list(veri["esas_enflasyon"])

        inflation_Map = folium.FeatureGroup(name="Inflation")

        def enflasyon_renk(enflasyon):
                if enflasyon < 2:
                    return "green"
                elif enflasyon < 5:
                    return "orange"
                elif enflasyon < 20:
                    return "red"
                else:
                    return "darkred"

        def enflasyon_radius(enflasyon):
                if enflasyon < 2:
                    return 40000
                elif enflasyon < 5:
                    return 100000
                elif enflasyon < 10:
                    return 125000
                else:
                    return 150000

        world_map = folium.Map(tiles="Cartodb positron")

        for enlem, boylam, enflasyon in zip(enlemler, boylamlar, enflasyon_oranlari):
                inflation_Map.add_child(folium.Circle(
            location=(enlem, boylam),
            radius=enflasyon_radius(enflasyon),
            color=enflasyon_renk(enflasyon),
            fill_color=enflasyon_renk(enflasyon),
            fill_opacity=0.3))

        world_map.add_child(inflation_Map)
        world_map.add_child(folium.LayerControl())
        world_map.add_child(folium.LatLngPopup()) #
        world_map.add_child(folium.plugins.Geocoder(position="topleft"))
        world_map.add_child(folium.plugins.Fullscreen(position="topright", title="Expand", title_cancel="Exit Expanded View", force_separate_button=True))
        world_map.add_child(folium.plugins.MiniMap(toggle_display=True, show = True, zoom_level_offset=-12))
        world_map.save("inflation_map.html") ###
        time.sleep(2)
        print("Inflation Verisi Haritaya İşlendi... ")
        inf = input("Harita Açılsın mı?[E/H]")
        if inf.upper() == 'E':
                print("Harita Açılıyor")
                time.sleep(2)
                html_file_path = r'C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\inflation_map.html'

        
                webbrowser.open(html_file_path)
        elif inf.upper() == "H":
            print("Ana Menuye Donuluyor...")
            time.sleep(1)
            self.menudon()
        else:
            print("Harita açılmadı.")
            time.sleep(2)
            self.menudon()
        
    def inflation_ekrana_getir(self):
        print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
        time.sleep(2)
        url3 = "https://www.theglobaleconomy.com/rankings/inflation/"


        response = requests.get(url3)
        response.raise_for_status() #    HTTP isteği başarılı mı kontrol eder
        parser = BeautifulSoup(response.content, 'html.parser')

        enflasyon_ülkeler = ["Algeria","Angola","Antigua-and-Barbuda","Armenia","Australia","Austria","Azerbaijan",
"Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Botswana","Brazil","Brunei","Bulgaria","Burkina-Faso","Burundi",
"Central-African-Republic","Cambodia","Canada","Chad","Chile","China","Colombia","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Denmark","Dominican-Republic","Djibouti","Dominica",
"Ecuador","El-Salvador","Estonia","Ethiopia",
"Finland","France",
"Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea",
"Haiti","Honduras","Hong-Kong","Hungary",
"Iceland","India","Indonesia","Iran","Ireland","Israel","Italy","Ivory-Coast",
"Jamaica","Japan","Jordan",
"Kazakhstan","Kenya","Kuwait","Kyrgyzstan",
"Laos","Latvia","Lebanon","Lesotho","Libya","Lithuania","Luxembourg",
"Madagascar","Malawi","Malaysia","Mali","Malta","Mauritius","Mexico","Moldova","Mongolia","Montenegro","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Niger","Nigeria","Macedonia","Norway",
"Oman",
"Pakistan","Palau","Palestine","Papua-New-Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Republic-of-the-Congo","Romania","Rwanda",
"Sao-Tome-and-Principe","Saint-Lucia","Samoa","Saudi-Arabia","Serbia","Sierra-Leone","Singapore","Slovakia","Slovenia","Solomon-Islands","South-Africa","South-Korea","Spain","Sri-Lanka","Saint-Vincent-and-the-Grenadines","Sweden","Switzerland",
"Tanzania","Thailand","Tonga","Trinidad-and-Tobago","Tunisia","Turkey",
"United-Kingdom","USA","Uganda","Ukraine","Uruguay",
"Vietnam",
"Zambia"]

        frames1 = []
        for i in range(len(enflasyon_ülkeler)):
            try:
                table1 = parser.find("a", {"href":f"/{enflasyon_ülkeler[i]}/Inflation/"}).parent.parent.find_all("td")
                bilgi12 = table1[1].string
                bilgi22 = table1[0].a.string
                bilgi3 = table1[2].string
                item_str1 = str(bilgi12)
                item_str2 = str(bilgi3)
                cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                frames1.append({
                    'Country Name': bilgi22,
                    'Inflation Rate': cleaned_item1,
                    'Global Rank': cleaned_item2
                })
            except AttributeError:
                continue
        frame = pd.DataFrame(frames1)
        print(frame)
        
        x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
        if x.lower() == "e":
                    dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                    try:
                        frame.to_excel(f"{dosya_konum}"\
                                           ,sheet_name="Trade_Balance",index=False)
                        print("Veriler Excele Başarıyla İşlendi...")
                        time.sleep(2)
                        self.menudon()
                    except :
                        print("Dosya dizini hatalı girildi")
        elif x.lower() == "h":
                print("Ana Menuye Donuluyor")
                time.sleep(2)
                self.menudon()
        else:
                    print("Hatalı komut!!")
        
        
    def gdp(self):
        tercih = input("Tercihinizi Giriniz...\n[1]Veriyi Haritada Görselleştir\n[2]Güncel Veriyi Ekrana Getir\nTercih: ")
        
        if tercih == "1":
            self.GDP_harita()
        elif tercih == "2":
            self.GDP_ekrana_getir()
        else:
            print("Hatalı tercih!")
    
    def GDP_harita(self):
        veri = pd.read_excel(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\ana_veriler.xlsx")

        enlemler = list(veri["Enlem"])
        boylamlar = list(veri["Boylam"])
        son_yil_gdp = list(veri["esas_gdp"])

        gdp_Map = folium.FeatureGroup(name="GDP")

        def son_yil_gdp_renk(son_gdp): 
            if son_gdp >= 10000:
                return "green"
            elif 1000 <= son_gdp < 10000:
                return "orange"
            else:
                return "red"

        def son_yil_gdp_radius(son_gdp): 
            if son_gdp > 10000:
                return 80000
            elif son_gdp > 5000:
                return 40000
            elif son_gdp > 1000:
                return 20000
            else:
                return 10000

        world_map = folium.Map(zoom_start=4, tiles="Cartodb dark_matter")

        for enlem, boylam, son_gdp in zip(enlemler, boylamlar, son_yil_gdp):
            gdp_Map.add_child(folium.Circle(
                location=(enlem, boylam),
                radius=son_yil_gdp_radius(son_gdp),
                color=son_yil_gdp_renk(son_gdp),
                fill_color=son_yil_gdp_renk(son_gdp),
                fill_opacity=0.6
            ))

        world_map.add_child(gdp_Map)
        world_map.add_child(folium.LayerControl())
        world_map.add_child(folium.LatLngPopup()) #
        world_map.add_child(folium.plugins.Geocoder(position="topleft"))
        world_map.add_child(folium.plugins.Fullscreen(position="topright", title="Expand", title_cancel="Exit Expanded View", force_separate_button=True))
        world_map.add_child(folium.plugins.MiniMap(toggle_display=True, show = True, zoom_level_offset=-12))
        world_map.save("world_map_gdp.html")
        t_b = input("Harita Açılsın mı?[E/H]")
        if t_b.upper() == 'E':
            print("Harita Açılıyor")
            time.sleep(2)
            html_file_path = r'C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\world_map_gdp.html'

        
            webbrowser.open(html_file_path)

        elif t_b.upper() == "H":
            print("Ana Menuye Donuluyor...")
            time.sleep(1)
            self.menudon()

        else:
            print("Harita açılmadı.")
            time.sleep(2)
            self.menudon()

    def GDP_ekrana_getir(self):
        print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
        time.sleep(2)
        url3 = "https://www.theglobaleconomy.com/rankings/GDP_current_USD/"

        response = requests.get(url3)
        response.raise_for_status()
        parser = BeautifulSoup(response.content, 'html.parser')

        ülkeler = ["Albania","Algeria","Andorra","Angola","Antigua-and-Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan",
                   "Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bolivia","Bosnia-and-Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina-Faso","Burma-Myanmar",
                   "Central-African-Republic","Cambodia","Cameroon","Canada","Cape-Verde","Chile","China","Colombia","Comoros","Costa-Rica","Croatia","Cyprus","Czech-Republic",
                   "Democratic-Republic-of-the-Congo","Denmark","Djibouti","Dominican-Republic","Dominica",
                   "Ecuador","Egypt","El-Salvador","Equatorial-Guinea","Estonia","Ethiopia",
                   "Fiji","Finland","France",
                   "Guinea-Bissau","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guyana",
                   "Haiti","Honduras","Hong-Kong","Hungary",
                   "Iceland","India","Indonesia","Iran","Ireland","Israel","Italy","Ivory-Coast",
                   "Jamaica","Japan","Jordan",
                   "Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan",
                   "Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Lithuania","Luxembourg",
                   "Macao","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Mongolia","Montenegro","Morocco","Mozambique",
                   "Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Niger","Nigeria","Macedonia","Norway",
                   "Oman",
                   "Pakistan","Palau","Palestine","Panama","Papua-New-Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto-Rico",
                   "Republic-of-the-Congo","Romania","Russia","Rwanda",
                   "Sao-Tome-and-Principe","Saint-Lucia","Samoa","Saudi-Arabia","Senegal","Serbia","Seychelles","Sierra-Leone","Singapore","Slovakia","Slovenia","Solomon-Islands","Somalia","South-Africa","South-Korea","Spain","Sri-Lanka","Saint-Vincent-and-the-Grenadines","Sweden","Sudan","Suriname","Swaziland","Sweden","Switzerland",
                   "Tajikistan","Tanzania","Thailand","Togo","Trinidad-and-Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu",
                   "United-Arab-Emirates","United-Kingdom","USA","Uganda","Ukraine","Uruguay","Uzbekistan",
                   "Vanuatu","Vietnam",
                   "Zambia","Zimbabwe"]

        frames1 = []
        for ülke in ülkeler:
            try:
                table1 = parser.find("a", {"href": f"/{ülke}/GDP_current_USD/"}).parent.parent.find_all("td")
                bilgi12 = table1[1].string
                bilgi22 = table1[0].a.string
                bilgi3 = table1[2].string
                item_str1 = str(bilgi12)
                item_str2 = str(bilgi3)
                cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                frames1.append({
                    'Country Name': bilgi22,
                    'GDP': cleaned_item1,
                    'Global Rank': cleaned_item2
                })
            except AttributeError:
                continue

        frame = pd.DataFrame(frames1)
        print(frame)

        x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
        if x.lower() == "e":
            dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
            try:
                frame.to_excel(f"{dosya_konum}", sheet_name="GDP", index=False)
                time.sleep(2)
                print("Veriler Excele Başarıyla İşlendi...")
            except Exception as e:
                print(f"Dosya dizini hatalı girildi veya dosya oluşturulamadı: {e}")
        elif x.lower() == "h":
            print("Ana Menüye Dönülüyor")
            time.sleep(2)
            self.menudon()
        else:
            print("Hatalı komut!!")
            time.sleep(2)
            self.menudon()

    
    def CO2_emission(self):
        tercih = input("Tercihinizi Giriniz...\n[1]Veriyi Haritada Görselleştir\n[2]Güncel Veriyi Ekrana Getir\nTercih: ")
        
        if tercih == "1":
            self.CO2_harita()
        elif tercih == "2":
            self.CO2_ekrana_getir()
        else:
            print("Hatalı tercih!")
    
    def CO2_harita(self):
        veri = pd.read_excel(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\ana_veriler.xlsx")
        enlemler = list(veri["Enlem"])
        boylamlar = list(veri["Boylam"])
        CO2_Emission = list(veri["esas_CO2"])

        total_CO2_Emission_Map = folium.FeatureGroup(name="CO2 Emission-2020")

        def CO2_Emission_renk(emission):
            if emission is None:
                return "black"
            elif emission < 8000:
                return "green"
            elif emission < 50000:
                return "yellow"
            elif emission < 200000:
                return "orange"
            else:
                return "red"

        def CO2_Emission_yari_cap(vaka):
                    if vaka > 400:
                        return 50000
                    elif vaka > 60:
                        return 60000
                    elif vaka > 5:
                        return 70000
                    elif vaka > -20:
                        return 100000
                    elif vaka == None:
                        return 150000
                    else:
                        return 200000
        world_map = folium.Map(tiles="Cartodb dark_matter")
        for enlem, boylam, emission in zip(enlemler,boylamlar,CO2_Emission): #
            total_CO2_Emission_Map.add_child(folium.Circle(location=(enlem, boylam),
                                                    radius=CO2_Emission_yari_cap(emission),
                                                    color=CO2_Emission_renk(emission),
                                                    fill=CO2_Emission_renk(emission),
                                                    fill_opacity=0.5))
                
        world_map.add_child(total_CO2_Emission_Map)
        world_map.add_child(folium.LayerControl())
        world_map.add_child(folium.LatLngPopup()) #
        world_map.add_child(folium.plugins.Geocoder(position="topleft"))
        world_map.add_child(folium.plugins.Fullscreen(position="topright", title="Expand", title_cancel="Exit Expanded View", force_separate_button=True))
        world_map.add_child(folium.plugins.MiniMap(toggle_display=True, show = True, zoom_level_offset=-12))
        world_map.save("emissions_map.html")
        time.sleep(2)
        print("CO2 Emission Verisi Haritaya İşlendi... ")
        co2 = input("Harita Açılsın mı?[E/H]")
        if co2.upper() == 'E':
                    print("Harita Açılıyor")
                    time.sleep(2)
                    html_file_path = r'C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\emissions_map.html'

        
                    webbrowser.open(html_file_path)
        
        elif co2.upper() == "H":
            print("Ana Menuye Donuluyor...")
            time.sleep(1)
            self.menudon()

        else:
                    print("Harita açılmadı.")
                    time.sleep(2)
                    self.menudon()


    def CO2_ekrana_getir(self):
            print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
            time.sleep(2)
            url = "https://www.theglobaleconomy.com/rankings/Carbon_dioxide_emissions/"

            response = requests.get(url)
            response.raise_for_status()#    HTTP isteği başarılı mı kontrol eder
            parser = BeautifulSoup(response.content, 'html.parser')

            ülkeler = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua-and-Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan",
"Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia-and-Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina-Faso","Burma-Myanmar","Burundi",
"Central-African-Republic","Cambodia","Cameroon","Canada","Cape-Verde","Chad","Chile","China","Colombia","Comoros","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Democratic-Republic-of-the-Congo","Denmark","Djibouti","Dominican-Republic","Dominica",
"Ecuador","Egypt","El-Salvador","Equatorial-Guinea","Eritrea","Estonia","Ethiopia",
"Fiji","Finland","France",
"Guinea-Bissau","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guyana",
"Haiti","Honduras","Hungary",
"Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Ivory-Coast",
"Jamaica","Japan","Jordan",
"Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan",
"Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg",
"Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Mongolia","Montenegro","Morocco","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Niger","Nigeria","North-Korea","Macedonia","Norway",
"Oman",
"Pakistan","Palau","Panama","Papua-New-Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Republic-of-the-Congo","Romania","Russia","Rwanda",
"Sao-Tome-and-Principe","Saint-Lucia","Samoa","Saudi-Arabia","Senegal","Serbia","Seychelles","Sierra-Leone","Singapore","Slovakia","Slovenia","Solomon-Islands","Somalia","South-Africa","South-Korea","Spain","Sri-Lanka","Saint-Vincent-and-the-Grenadines","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria",
"Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad-and-Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu",
"United-Arab-Emirates","United-Kingdom","USA","Uganda","Ukraine","Uruguay","Uzbekistan",
"Vanuatu","Venezuela","Vietnam",
"Yemen",
"Zambia","Zimbabwe"]

            frames1 = []
            for i in range(len(ülkeler)):
                table = parser.find("a", {"href":f"/{ülkeler[i]}/Carbon_dioxide_emissions/"}).parent.parent.find_all("td")
                bilgi1 = table[1].string
                bilgi2 = table[0].a.string
                bilgi3 = table[2].string
                item_str1 = str(bilgi1)
                item_str2 = str(bilgi3)
                cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                frames1.append({
                            'Country Name': bilgi2,
                            'CO2 Emissions': cleaned_item1,
                            'Global Rank': cleaned_item2})
            frame = pd.DataFrame(frames1)
            print(frame)
        
            x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
            if x.lower() == "e":
                dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                try:
                    frame.to_excel(f"{dosya_konum}", sheet_name="GDP", index=False)
                    print("Veriler Excele Başarıyla İşlendi...")
                    time.sleep(2)
                    self.menudon()
                except Exception as e:
                    print(f"Dosya dizini hatalı girildi veya dosya oluşturulamadı: {e}")
            elif x.lower() == "h":
                print("Ana Menüye Dönülüyor")
                time.sleep(2)
                self.menudon()
            else:
                print("Hatalı komut!!")
                time.sleep(2)
                self.menudon()



    def harita(self):#islem sonunda harita acılsın mı? Ana verilerin hepsini haritaya işler
        veri = pd.read_excel(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\ana_veriler.xlsx")
        enlemler = list(veri["Enlem"])
        boylamlar = list(veri["Boylam"])
        trade_balance = list(veri["esas"])
        enflasyon_oranlari = list(veri["esas_enflasyon"])
        son_yil_gdp = list(veri["esas_gdp"])
        CO2_Emission = list(veri["esas_CO2"])

        Trade_Balance_Map = folium.FeatureGroup(name="Trade Balance")
        inflation_Map = folium.FeatureGroup(name="Inflation")
        gdp_Map = folium.FeatureGroup(name="GDP")
        total_CO2_Emission_Map = folium.FeatureGroup(name="CO2 Emission-2020")
        nufus_dagilim_haritasi = folium.FeatureGroup(name="NüfusDağılımHaritası")


        def trade_balance_renk(t_b):
                if t_b is None:
                    return "black"
                elif t_b > 300:
                    return "green"
                elif t_b > 60:
                    return "white"
                elif t_b > 5:
                    return "yellow"
                elif t_b > -50:
                    return "orange"
                else:
                    return "red"

        def trade_balance_yari_cap(t_b):
                if t_b > 400:
                    return 50000
                elif t_b > 60:
                    return 60000
                elif t_b > 5:
                    return 70000
                elif t_b > -20:
                    return 100000
                elif t_b == None:
                    return 150000
                else:
                    return 200000
                
        def enflasyon_renk(enflasyon):
                if enflasyon < 2:
                    return "green"
                elif enflasyon < 5:
                    return "orange"
                elif enflasyon < 20:
                    return "red"
                else:
                    return "darkred"

        def enflasyon_radius(enflasyon):
                if enflasyon < 2:
                    return 40000
                elif enflasyon < 5:
                    return 100000
                elif enflasyon < 10:
                    return 125000
                else:
                    return 150000

        def son_yil_gdp_renk(son_gdp): 
            if son_gdp >= 10000:
                return "green"
            elif 1000 <= son_gdp < 10000:
                return "orange"
            else:
                return "red"

        def son_yil_gdp_radius(son_gdp): 
            if son_gdp > 10000:
                return 80000
            elif son_gdp > 5000:
                return 40000
            elif son_gdp > 1000:
                return 20000
            else:
                return 10000

        def CO2_Emission_renk(emission):      
            if emission < 8000:
                return "green"
            elif emission < 50000:
                return "yellow"
            elif emission < 200000:
                return "orange"
            else:
                return "red"

        def CO2_Emission_yari_cap(vaka):
            if vaka > 400:
                return 50000
            elif vaka > 60:
                return 60000
            elif vaka > 5:
                return 70000
            elif vaka > -20:
                return 100000
            else:
                return 200000


        
        world_map = folium.Map(tiles="Cartodb dark_matter")



        for enlem, boylam, emission in zip(enlemler,boylamlar,trade_balance): 
                Trade_Balance_Map.add_child(folium.Circle(location=(enlem, boylam),
                                                 radius=trade_balance_yari_cap(emission),
                                                 color=trade_balance_renk(emission),
                                                 fill=trade_balance_renk(emission),
                                                 fill_opacity=0.5))
                
        for enlem, boylam, enflasyon in zip(enlemler, boylamlar, enflasyon_oranlari):
                inflation_Map.add_child(folium.Circle(
            location=(enlem, boylam),
            radius=enflasyon_radius(enflasyon),
            color=enflasyon_renk(enflasyon),
            fill_color=enflasyon_renk(enflasyon),
            fill_opacity=0.3))
                
        for enlem, boylam, son_gdp in zip(enlemler, boylamlar, son_yil_gdp):
            gdp_Map.add_child(folium.Circle(
                location=(enlem, boylam),
                radius=son_yil_gdp_radius(son_gdp),
                color=son_yil_gdp_renk(son_gdp),
                fill_color=son_yil_gdp_renk(son_gdp),
                fill_opacity=0.6))
            
        for enlem, boylam, emission in zip(enlemler,boylamlar,CO2_Emission): 
            total_CO2_Emission_Map.add_child(folium.Circle(location=(enlem, boylam),
                                                    radius=CO2_Emission_yari_cap(emission),
                                                    color=CO2_Emission_renk(emission),
                                                    fill=CO2_Emission_renk(emission),
                                                    fill_opacity=0.5))

        nufus_dagilim_haritasi.add_child(folium.GeoJson(
                            data=(open(r"C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\world.json"
                                       , "r", encoding="utf-8-sig").read()),
                            style_function= lambda x : {'fillColor':'green'
                            if x["properties"]["POP2005"] < 20000000 else 'white'
                            if 20000000 <= x["properties"]["POP2005"]  <= 50000000 else 'orange'
                            if 50000000 <= x["properties"]["POP2005"] <= 100000000 else 'red'}))
                
        world_map.add_child(Trade_Balance_Map)
        time.sleep(1)
        print("Trade Balance Verisi Haritaya İşlendi... ")
        world_map.add_child(inflation_Map)
        time.sleep(1)
        print("Inflation Verisi Haritaya İşlendi... ")
        world_map.add_child(gdp_Map)
        time.sleep(1)
        print("GDP Verisi Haritaya İşlendi...")
        world_map.add_child(total_CO2_Emission_Map)
        time.sleep(1)
        print("CO2 Emission Verisi Haritaya İşlendi... ")
        time.sleep(1)
        world_map.add_child(nufus_dagilim_haritasi)
        print("Nüfus Dağılım Verisi Haritaya İşlendi")

        world_map.add_child(folium.LayerControl())
        world_map.add_child(folium.LatLngPopup()) #
        world_map.add_child(folium.plugins.Geocoder(position="topleft"))
        world_map.add_child(folium.plugins.Fullscreen(position="topright", title="Expand", title_cancel="Exit Expanded View", force_separate_button=True))
        world_map.add_child(folium.plugins.MiniMap(toggle_display=True, show = True, zoom_level_offset=-12))
        world_map.save("mapx.html")

        n_d = input("Harita Açılsın mı?[E/H]: ")

        if n_d.upper() == 'E':
                    print("Harita Açılıyor")
                    time.sleep(2)
                    html_file_path = r'C:\Users\batuh\OneDrive\Masaüstü\Python Core Veri Projesi\mapx.html'
                    #Düzenlemeler için kendi oluşturdunuz path'i giriniz
                    webbrowser.open(html_file_path)
                    time.sleep(2)
                    self.menudon()
        else:
                    print("Harita açılmadı.")
                    time.sleep(2)
                    self.menudon()
       

    def daha_fazla_veri(self):
        print("Güncel Verilere Erişildi...")
        time.sleep(2)
        tercih = input("[1]High Tech Exports\n[2]Globalization Index\n[3]Gini Inequality Index\nTercih: ")
        if tercih == "1":
             self.high_tech_exports()
        elif tercih == "2":
             self.globalization_index()
        elif tercih == "3":
             self.Gini_inequality_index()

        
    def high_tech_exports(self):
        print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
        time.sleep(2)
        url = "https://www.theglobaleconomy.com/rankings/High_tech_exports/"

        response = requests.get(url)
        response.raise_for_status()#    HTTP isteği başarılı mı kontrol eder
        parser = BeautifulSoup(response.content, 'html.parser')

        ülkeler = ["Albania","Andorra","Angola","Antigua-and-Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan",
"Bahamas","Bahrain","Barbados","Belgium","Belize","Benin","Bermuda","Bolivia","Bosnia-and-Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina-Faso","Burma-Myanmar","Burundi",
"Central-African-Republic","Cambodia","Canada","Cape-Verde","Chile","China","Colombia","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Democratic-Republic-of-the-Congo","Denmark","Dominican-Republic",
"Ecuador","Egypt","El-Salvador","Estonia","Ethiopia",
"Fiji","Finland","France",
"Georgia","Germany","Greece","Grenada","Guatemala","Guyana",
"Hong-Kong","Hungary",
"Iceland","India","Indonesia","Ireland","Israel","Italy","Ivory-Coast",
"Jamaica","Japan","Jordan",
"Kazakhstan","Kenya","Kuwait","Kyrgyzstan",
"Latvia","Lebanon","Lesotho","Lithuania","Luxembourg",
"Macao","Madagascar","Malawi","Malaysia","Maldives","Malta","Mauritania","Mauritius","Mexico","Moldova","Mongolia","Montenegro","Morocco","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Niger","Nigeria","Macedonia","Norway",
"Oman",
"Pakistan","Panama","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Romania","Rwanda",
"Sao-Tome-and-Principe","Senegal","Serbia","Singapore","Slovakia","Slovenia","South-Africa","South-Korea","Spain","Sri-Lanka","Suriname","Sweden","Switzerland",
"Tajikistan","Tanzania","Thailand","Togo","Trinidad-and-Tobago","Tunisia","Turkey",
"United-Arab-Emirates","United-Kingdom","USA","Ukraine","Uruguay","Uzbekistan",
"Vietnam",
"Zambia","Zimbabwe"]

        frames1 = []
        for i in range(len(ülkeler)):
                table = parser.find("a", {"href":f"/{ülkeler[i]}/High_tech_exports/"}).parent.parent.find_all("td")
                bilgi1 = table[1].string
                bilgi2 = table[0].a.string
                bilgi3 = table[2].string
                item_str1 = str(bilgi1)
                item_str2 = str(bilgi3)
                cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                frames1.append({
                            'Country Name': bilgi2,
                            'High Tech Exports': cleaned_item1,
                            'Global Rank': cleaned_item2})
        frame = pd.DataFrame(frames1)
        print(frame)
        
        x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
        if x.lower() == "e":
                dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                try:
                    frame.to_excel(f"{dosya_konum}", sheet_name="high_tech_exports", index=False)
                    print("Veriler Excele Başarıyla İşlendi...")
                    time.sleep(2)
                    self.menudon()
                except Exception as e:
                    print(f"Dosya dizini hatalı girildi veya dosya oluşturulamadı: {e}")
        elif x.lower() == "h":
                print("Ana Menüye Dönülüyor")
                time.sleep(2)
                self.menudon()
        else:
                print("Hatalı komut!!")

    def globalization_index(self):
        print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
        time.sleep(2)
        url = "https://www.theglobaleconomy.com/rankings/kof_overall_glob/"

        response = requests.get(url)
        response.raise_for_status()
        #    HTTP isteği başarılı mı kontrol eder
        parser = BeautifulSoup(response.content, 'html.parser')

        ülkeler = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua-and-Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan",
"Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia-and-Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina-Faso","Burma-Myanmar","Burundi",
"Central-African-Republic","Cambodia","Cameroon","Canada","Cape-Verde","Chad","Chile","China","Colombia","Comoros","Costa-Rica","Croatia","Cuba","Cyprus","Czech-Republic",
"Democratic-Republic-of-the-Congo","Denmark","Djibouti","Dominican-Republic","Dominica",
"Ecuador","Egypt","El-Salvador","Equatorial-Guinea","Eritrea","Estonia","Ethiopia",
"Faroe-Islands","Fiji","Finland","France",
"Guinea-Bissau","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guyana",
"Haiti","Honduras","Hong-Kong","Hungary",
"Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Ivory-Coast",
"Jamaica","Japan","Jordan",
"Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan",
"Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg",
"Macao","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Niger","Nigeria","Macedonia","Norway",
"Oman",
"Pakistan","Palau","Panama","Papua-New-Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Republic-of-the-Congo","Romania","Russia","Rwanda",
"Sao-Tome-and-Principe","Samoa","San-Marino","Saudi-Arabia","Senegal","Serbia","Seychelles","Sierra-Leone","Singapore","Slovakia","Slovenia","Solomon-Islands","Somalia","South-Africa","South-Korea","Spain","Sri-Lanka","Sudan","Suriname","Sweden","Switzerland","Syria",
"Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad-and-Tobago","Tunisia","Turkey","Turkmenistan",
"United-Arab-Emirates","United-Kingdom","USA","Uganda","Ukraine","Uruguay","Uzbekistan",
"Vanuatu","Venezuela","Vietnam",
"Yemen",
"Zambia","Zimbabwe"]

        frames1 = []
        for i in range(len(ülkeler)):
                table = parser.find("a", {"href":f"/{ülkeler[i]}/kof_overall_glob/"}).parent.parent.find_all("td")
                bilgi1 = table[1].string
                bilgi2 = table[0].a.string
                bilgi3 = table[2].string
                item_str1 = str(bilgi1)
                item_str2 = str(bilgi3)
                cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                frames1.append({
                            'Country Name': bilgi2,
                            'Globalization Index(0-100)': cleaned_item1,
                            'Global Rank': cleaned_item2})
        frame = pd.DataFrame(frames1)
        print(frame)
        
        x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
        if x.lower() == "e":
                dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                try:
                    frame.to_excel(f"{dosya_konum}", sheet_name="globalization_index", index=False)
                    print("Veriler Excele Başarıyla İşlendi...")
                    time.sleep(2)
                    self.menudon()
                except Exception as e:
                    print(f"Dosya dizini hatalı girildi veya dosya oluşturulamadı: {e}")
        elif x.lower() == "h":
                print("Ana Menüye Dönülüyor")
                time.sleep(2)
                self.menudon()
        else:
                print("Hatalı komut!!")
            
    def Gini_inequality_index(self):
        print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
        time.sleep(2)
        url = "https://www.theglobaleconomy.com/rankings/gini_inequality_index/"

        response = requests.get(url)
        response.raise_for_status()
        #    HTTP isteği başarılı mı kontrol eder
        parser = BeautifulSoup(response.content, 'html.parser')

        ülkeler = ["Argentina","Armenia","Austria",
"Belgium","Benin","Bolivia","Brazil","Bulgaria","Burkina-Faso",
"Central-African-Republic","Cameroon","Colombia","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Denmark","Dominican-Republic",
"Ecuador","El-Salvador","Estonia",
"Finland","France",
"Guinea-Bissau","Georgia","Greece",
"Hungary",
"India","Indonesia","Iran","Ireland","Israel","Italy","Ivory-Coast",
"Jamaica",
"Kazakhstan","Kenya","Kyrgyzstan",
"Latvia","Lithuania","Luxembourg",
"Malaysia","Mali","Moldova","Montenegro",
"Netherlands","Niger",
"Panama","Paraguay","Peru","Philippines","Poland","Portugal",
"Romania",
"Senegal","Serbia","Slovakia","Slovenia","Sweden",
"Thailand","Togo","Tonga","Tunisia","Turkey",
"United-Kingdom","USA","Uruguay"]

        frames1 = []
        for i in range(len(ülkeler)):
                table = parser.find("a", {"href":f"/{ülkeler[i]}/gini_inequality_index/"}).parent.parent.find_all("td")
                bilgi1 = table[1].string
                bilgi2 = table[0].a.string
                bilgi3 = table[2].string
                item_str1 = str(bilgi1)
                item_str2 = str(bilgi3)
                cleaned_item1 = re.sub(r'[\r\n\t\s]+', '', item_str1)
                cleaned_item2 = re.sub(r'[\r\n\t\s]+', '', item_str2)
                frames1.append({
                            'Country Name': bilgi2,
                            'Gini Inequality Index': cleaned_item1,
                            'Global Rank': cleaned_item2})
        frame = pd.DataFrame(frames1)
        print(frame)
        
        x = input("Güncel Veriler Excele Aktarılsın mı?[E/H]\n")
        if x.lower() == "e":
                dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                try:
                    frame.to_excel(f"{dosya_konum}", sheet_name="gini_inequality_index", index=False)
                    print("Veriler Excele Başarıyla İşlendi...")
                    time.sleep(2)
                    self.menudon()
                except Exception as e:
                    print(f"Dosya dizini hatalı girildi veya dosya oluşturulamadı: {e}")
        elif x.lower() == "h":
            print("Ana Menüye Dönülüyor")
            time.sleep(2)
            self.menudon()
        else:
                print("Hatalı komut!!")
         
    
          
    def cikis(self):
        self.dongu=False
        exit()


    def menudon(self):
        print("Ana Menüye Hoş Geldiniz...")
        while True:
            x=input("Menüye Dönmek için 7'ye Çıkmak için 5'e Basiniz\n  ")
            if x == "7":
                print("Menuye Donuluyor")
                time.sleep(2)
                break
                self.program()
            elif x =="5":
                self.cikis()
                break
            else:
                print("Lutfen Geçerli Bir Deger Giriniz.")





Sistem=Indicators()
while Sistem.dongu:
    Sistem.program()
