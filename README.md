## Genel Bakış
###### •FoliumFuzion.py, çeşitli ekonomik ve demografik göstergelere ilişkin verileri toplayan ve bu verileri interaktif haritalar üzerinde görselleştiren bir Python betiğidir. Bu betik, kullanıcıların ticaret dengesi, nüfus dağılımı, enflasyon, gayri safi yurtiçi hasıla (GDP) ve CO2 emisyonları gibi önemli verileri hızlıca elde edip haritalar üzerinde görselleştirmesini sağlar. 
###### •Projede kullanılan veriler ‘theglobaleconomy’ sitesinden alınmıştır. 
###### •Ana veriler haritada görselleştirilebilir, haritada kullanılan veriler ‘ana_veriler.xlsx’ adlı dosyadan alınır ve siteden veriler kazınarak güncel verilere de erişilebilir, daha fazla veri kısmındaki veriler ise sadece siteden verileri kazırlar.
###### •‘ana_veriler.xlsx’ adlı Excel dosyasına kendi çektiğiniz verileri doğru bir şekilde yerleştirdiğiniz takdirde bu verileri de haritaya ekleme imkanına erişebilirsiniz.
###### •Kod içerisinde dosya konumları yer almaktadır eğer kodu kendi cihazınızda kullanmayı arzu ederseniz bu dosya konumlarını kendi dosya konumlarınız ile değiştiriniz.
###### •Projede yer alan 'html' uzantılı dosyaları folium kütüphanesi oluşturmuştur, kodu kendi cihanızında etkinleştirmek için 'html' uzantılı dosyaları indirmeniz gerekmez bu dosyalar kod çalıştırıldığında folium betikliği tarafından oluşturulur.

## Özellikler
###### •	Veri Toplama: Çeşitli ekonomik göstergelere ilişkin verileri otomatik olarak toplar.
###### •	Veri Görselleştirme: Toplanan verileri Folium kütüphanesi kullanarak interaktif haritalar üzerinde görselleştirir.
###### •	Kullanıcı Dostu Menü: Kullanıcıların işlem yapmasını kolaylaştıran basit ve anlaşılır bir menü arayüzü sunar.
## Kurulum
FoliumFuzion.py dosyasını çalıştırabilmek için öncelikle gerekli Python kütüphanelerinin yüklü olması gerekir. Aşağıdaki komutu kullanarak bu kütüphaneleri yükleyebilirsiniz:
pip install requests beautifulsoup4 pandas folium re time webbrowser folium.plugins
## Kullanım
#### 1.	Betik Çalıştırma: Betiği çalıştırmak için terminalde şu komutu kullanın:
python FoliumFuzion.py
#### 2.	Menü Kullanımı: Betiği çalıştırdıktan sonra, aşağıdaki seçeneklerden birini seçerek işlem yapabilirsiniz:
###### o	1: Trade Balance İndikatörü - Ticaret dengesi verilerini toplar, harita üzerinde gösterir ve verileri Excele aktarmayı olanaklı kılar
###### o	2: Nüfus Dağılımı - Nüfus dağılımı verilerini toplar ve harita üzerinde görselleştirir. Ülke sınırları ‘world.json’ adlı json dosyasından erişilmektedir, kodun bu kısmı diğerlerine göre biraz farklı gibi görünse de aynı şekilde çalışır.
###### o	3: Enflasyon - Enflasyon verilerini toplar, analiz eder , harita üzerinde gösterir ve verileri Excele aktarmayı olanaklı kılar
###### o	4: GDP - Gayri safi yurtiçi hasıla (GDP) verilerini toplar analiz eder , harita üzerinde gösterir ve verileri Excele aktarmayı olanaklı kılar
###### o	5: CO2 Emisyonları - CO2 emisyon verilerini toplar ve harita üzerinde görselleştirir.
###### o	6: Tüm Ana Verileri Haritada Görselleştir - Tüm ana verileri tek bir harita üzerinde toplar.
###### o	7: Daha Fazla Veri - Ekstra veriler toplar, analiz eder ve verilerin Excele aktarılmasını olanaklı kılar. Dilerseniz bu verileri ana_veriler exceline yerleştirip kodda da gerekli düzenlemeleri yaparak bu verileri de haritaya aktarabilirsiniz.
###### o	8: Çıkış - Programdan çıkış yapar.
#### Sınıflar ve Fonksiyonlar
Aşağıda, FoliumFuzion.py dosyasında tanımlı tüm fonksiyonlar ve bunların açıklamaları verilmiştir:
###### 1. __init__()
•	Açıklama: Indicators sınıfının başlatıcı fonksiyonudur. Sınıfın gerekli başlangıç değişkenlerini tanımlar.
###### 2. program()
•	Açıklama: Ana programın kontrol akışını yöneten fonksiyon. Kullanıcının yaptığı seçimlere göre diğer fonksiyonları çağırır.
###### 3. menu()
•	Açıklama: Kullanıcıya bir menü sunarak yapılacak işlemi seçmesini sağlar.
###### 4. kontrol(secim)
•	Açıklama: Kullanıcının yaptığı seçimleri doğrular ve geçersiz seçimlerde hata mesajı döner.
###### 5. nufus_dagilim()
•	Açıklama: Nüfus dağılımı verilerini toplar ve analiz eder.
###### 6. trade_balance()
•	Açıklama: Ticaret dengesi verilerini toplar ve bu verileri harita üzerinde görselleştirir.
###### 7. trade_balance_harita()
•	Açıklama: Ticaret dengesi verilerini harita üzerinde görselleştirir.
###### 8. trade_balance_renk()
•	Açıklama: Ticaret dengesi verilerini renklendirir.
###### 9. trade_balance_yari_cap()
•	Açıklama: Ticaret dengesi verilerini yarıçap kullanarak görselleştirir.
###### 10. trade_balance_ekrana_getir()
•	Açıklama: Ticaret dengesi verilerini ekrana yazdırır.
###### 11. inflation()
•	Açıklama: Enflasyon verilerini toplar ve analiz eder.
###### 12. inflation_harita()
•	Açıklama: Enflasyon verilerini harita üzerinde görselleştirir.
###### 13. enflasyon_renk()
•	Enflasyon verilerini renklendirir.
###### 14. enflasyon_radius()
•	Açıklama: Enflasyon verilerini yarıçap kullanarak görselleştirir.
###### 15. inflation_ekrana_getir()
•	Açıklama: Enflasyon verilerini ekrana yazdırır.
###### 16. gdp()
•	Açıklama: GDP (Gayri Safi Yurtiçi Hasıla) verilerini toplar ve analiz eder.
###### 17. GDP_harita()
•	Açıklama: GDP verilerini harita üzerinde görselleştirir.
###### 18. son_yil_gdp_renk()
•	Açıklama: Son yılın GDP verilerini renklendirir.
###### 19. son_yil_gdp_radius()
•	Açıklama: Son yılın GDP verilerini yarıçap kullanarak görselleştirir.
###### 20. GDP_ekrana_getir()
•	Açıklama: GDP verilerini ekrana yazdırır.
###### 21. CO2_emission()
•	Açıklama: CO2 emisyon verilerini toplar ve analiz eder.
###### 22. CO2_harita()
•	Açıklama: CO2 emisyon verilerini harita üzerinde görselleştirir.
###### 23. CO2_Emission_renk()
•	Açıklama: CO2 emisyon verilerini renklendirir.
###### 24. CO2_Emission_yari_cap()
•	Açıklama: CO2 emisyon verilerini yarıçap kullanarak görselleştirir.
###### 25. CO2_ekrana_getir()
•	Açıklama: CO2 emisyon verilerini ekrana yazdırır.
###### 26. harita()
•	Açıklama: Tüm ana verileri tek bir harita üzerinde toplar ve görselleştirir.
###### 27. daha_fazla_veri()
•	Açıklama: Ekstra veriler toplar ve analiz eder. Bu veriler high_tech_exports, globalization_index, globalization_index’tir.
###### 28. high_tech_exports()
•	Açıklama: Yüksek teknoloji ihracatı verilerini toplar ve analiz eder.
###### 29. globalization_index()
•	Açıklama: Küreselleşme endeksi verilerini toplar ve analiz eder.
###### 30. Gini_inequality_index()
•	Açıklama: Gini eşitsizlik endeksi verilerini toplar ve analiz eder.
###### 31. cikis()
•	Açıklama: Programdan çıkış yapar.
###### 32. menudon()
•	Açıklama: Ana menüye geri döner.
  ## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz, lütfen bu depoyu fork'layın ve pull request gönderin. Hata raporları, özellik istekleri ve iyileştirmeler memnuniyetle karşılanır.
  ## İletişim
Herhangi bir soru ya da sorun için lütfen batuhan.gnd@hotmail.com adresine ulaşın.
