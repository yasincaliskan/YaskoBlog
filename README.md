

Django Framework ile olu�turulmu� bir blog sitesidir. �ye olma ve kullan�c� giri�i i�lemleri yap�labilir. Kullan�c�lar (tercihe g�re) g�rsel ekleyip metin yaz�lar� ile post yay�nlayabilir. Di�er kullan�c�lar bu postlara yorum metni yazabilir. Yay�nlanan postlar veritaban�nda tutulur ve kullan�c� isterse yay�nlanan post �zerinde de�i�iklik yapabilir veya silebilir.

## Kullan�lan teknolojiler:

 - Django Framework & Python
 - HTML & CSS & JavaScript
 - SQLite
 - Bootstrap

## 3. Parti Django Uygulamalar�:

 - Crispy Form
 - Django Cleanup
 - *CKEditor (aktif de�il)*
 - *Captcha (aktif de�il)*

## **Navbar**

![enter image description here](https://lh3.googleusercontent.com/zJJT1Sl6HQOswTuhgDXPUcRHffXRg50u09knbHRDr8_X1wXaOzzOgbSUW2zPGyzzGaDSnoh1p40)

Kullan�c� giri�i yap�lmam��sa Home/Blog/Login/Register �zerinden yay�nlanan postlar� g�r�nt�leyebilir, �ye olabilir, kullan�c� giri�i yapabilir ve ba�l�k&i�erik i�in arama yapabilir.

## **Login & Register**

![enter image description here](https://lh3.googleusercontent.com/w5P-IWOuBl5XTWezzwNUPjZIByvT9IOgiHpAZX3J6XFYKTpNxQKCbg1JwInvJIf43X7G1SiFV8Y)

Kullan�c� ad� ve �ifre do�rulamas�yla kullan�c� giri�i yapabilir.

![enter image description here](https://lh3.googleusercontent.com/diyK7YPhsPFZbOY3iEC9cXuikfpJqocyvdjoIWcfCzgngqhGMTtrahHVqvSyPWLladQdihw7yrQ)

�ye kayd� yapabilir.

## **Blog**

![enter image description here](https://lh3.googleusercontent.com/qE1_xqq1t5-ZZC-erXlWBhHw3IqAQQ667Z4Wf4UOLcbfi7Mt7s0acTXeRVKhNOtYT9mvLvIa0-I)

Kullan�c� giri�i yapt�ktan sonra New Post linki aktif olur ve post yay�nlamaya ba�layabilir.

![enter image description here](https://lh3.googleusercontent.com/3SGSfbRpWY8bmjCPxnaAC6qiq930BTjymko6vE2ZK6FvSQ4B3jEfrJj431R_VM-eINdfz3TbQHY)
![enter image description here](https://lh3.googleusercontent.com/AM5yVnxoPDZCGNec8A2cXcQTT9LjYyDmyyE1oURbgS8ZFOKHtlasVDSEMtuxHWOkq7iOh-HcEvY)

Index sayfa numaras�na g�re bir url adresi atan�r.

![enter image description here](https://lh3.googleusercontent.com/L6JooNNQdv6sSdxQepchjWXrbJzgkamGNped185OUCyayBwns75w1Z4QlVCMrbnsJH4E-OPBiXw)

Yay�nlanm�� bir post �zerinden �View� butonuna t�klayarak postun detay sayfas�na y�nlendirilir. �Update� ile g�ncellemeler yap�p �Delete� ile silebilir.

![enter image description here](https://lh3.googleusercontent.com/ow8K7oRR9BzTZeLdUwLONvK_n45XTU0LuxBOAdXWbuLDEcpsIWJqTBeo_WGyQgKtpfy3ielvxP4)

Her postun detay sayfas�na kendi ba�l�k bilgisine g�re e�siz bir url adresi atan�r. Ayn� ba�l�k bilgisine sahip postlar i�in sonuna n�merik ifadeler eklenir.

## **Comment**

![enter image description here](https://lh3.googleusercontent.com/V8gip_7cPjlR_1TLc4jYYymVGyj8N64Ann6HO4yTh4Ix33lVUpkWOUxLuXmaqkhW0fa2vzxtqok)

Post detay sayfas�ndan yorum yap�labilir. Ziyaret�iler bu formu g�remez yaln�zca �yeler eri�ebilir.

![enter image description here](https://lh3.googleusercontent.com/IlPs1pFaN3TgoAJGcThQETGJjkHZPg54Fy1IjDy_yo4MR6kGQhwYvJo90z25lQww3QcjlrnJIek)

Yap�lan yorumlar postun detay sayfas�nda g�r�nt�lenir. Silinen bir posta yap�lan yorumlar da veritaban�ndan silinir.

![enter image description here](https://lh3.googleusercontent.com/hLnJrl5QPi3CXh00RHK-ZHv3PXqdMlyx__awq3LJ2SYWuTLhiL-pQCs8-Cp9jS5wzedQ0w6Cu3s)

Son payla��lan �stte olacak �ekilde kronolojik olarak s�ralan�r ve her sayfada 5 adet post g�r�nt�lenir.

## **Post Eklemek**

![enter image description here](https://lh3.googleusercontent.com/_LOcLpAIhoI5Nt82-KmcB9DnaySxzPeB1mni3VhhafcsfB2gYxypkvjj1J-QHaZvY1tSgXHchSk)

Ba�l�k, i�erik metinleri ve tercihe g�re g�rsel ekleyerek post yay�nlanabilir. Buna yaln�zca kullan�c� giri�i yapm�� �yeler eri�ebilir.

![enter image description here](https://lh3.googleusercontent.com/fy0rsAPrnBrf_8Wym1UZGgK4_Mi_y99wQZfdxmTajAFHoFA4x-fWGl7QhBp46eaQiU5v7G1YYTA)

Post ekleme i�lemi ba�ar�l� oldu�unda bir mesaj ile kullan�c�ya bildirilir.