Django Framework ile olu�turulmu� bir blog sitesidir. �ye olma ve kullan�c� giri�i i�lemleri yapabilir. Kullan�c�lar (tercihe g�re) g�rsel ekleyip metin yaz�lar� ile post yay�nlayabilir. Di�er kullan�c�lar bu postlara yorum metni yazabilir. Yay�nlanan postlar veritaban�nda tutulur ve kullan�c� isterse yay�nlanan postu �zerinde de�i�iklik yapabilir veya silebilir.

Kullan�lan teknolojiler:
-Django Framework & Python
-HTML & CSS & JavaScript
-SQLite
-Bootstrap

3. Parti Django Uygulamalar�:
-Crispy Form
-Django Cleanup
-CKEditor (aktif de�il)
-Captcha (aktif de�il)


Navbar



Kullan�c� giri�i yap�lmam��sa Home/Blog/Login/Register �zerinden yay�nlanan postlar� g�r�nt�leyebilir,�ye olabilir, kullan�c� giri�i yapabilir ve ba�l�k&i�erik i�in arama yapabilir.


Login & Register



Kullan�c� ad� ve �ifre do�rulamas�yla kullan�c� giri�i yapabilir.



�ye kayd� yapabilir.


Blog



Kullan�c� giri�i yapt�ktan sonra New Post linki aktif olur ve post yay�nlamaya ba�layabilir.



Index sayfa numaras�na g�re bir url adresi atan�r.



Yay�nlanm�� bir post �zerinden �View� butonuna t�klayarak postun detay sayfas�na y�nlendirilir. �Update� ile g�ncellemeler yap�p �Delete� ile silebilir.



Her postun detay sayfas�na kendi ba�l�k bilgisine g�re e�siz bir url adresi atan�r. Ayn� ba�l�k bilgisine sahip postlar i�in sonuna n�merik ifadeler eklenir.
Comment



Post detay sayfas�ndan yorum yap�labilir. Ziyaret�iler bu formu g�remez yaln�zca �yeler eri�ebilir.



Yap�lan yorumlar postun detay sayfas�nda g�r�nt�lenir. Silinen bir posta yap�lan yorumlar da veritaban�ndan silinir.



Son payla��lan �stte olacak �ekilde kronolojik olarak s�ralan�r. Her sayfada 5 adet post g�r�nt�lenir.


Post Eklemek


Ba�l�k, i�erik metinleri ve tercihe g�re g�rsel ekleyerek post yay�nlanabilir. Buna yaln�zca kullan�c� giri�i yapm�� �yeler eri�ebilir.



Post ekleme i�lemi ba�ar�l� oldu�unda bir mesaj ile kullan�c�ya bildirilir.


