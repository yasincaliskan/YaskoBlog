

Django Framework ile oluþturulmuþ bir blog sitesidir. Üye olma ve kullanýcý giriþi iþlemleri yapýlabilir. Kullanýcýlar (tercihe göre) görsel ekleyip metin yazýlarý ile post yayýnlayabilir. Diðer kullanýcýlar bu postlara yorum metni yazabilir. Yayýnlanan postlar veritabanýnda tutulur ve kullanýcý isterse yayýnlanan post üzerinde deðiþiklik yapabilir veya silebilir.

## Kullanýlan teknolojiler:

 - Django Framework & Python
 - HTML & CSS & JavaScript
 - SQLite
 - Bootstrap

## 3. Parti Django Uygulamalarý:

 - Crispy Form
 - Django Cleanup
 - *CKEditor (aktif deðil)*
 - *Captcha (aktif deðil)*

## **Navbar**

![enter image description here](https://lh3.googleusercontent.com/zJJT1Sl6HQOswTuhgDXPUcRHffXRg50u09knbHRDr8_X1wXaOzzOgbSUW2zPGyzzGaDSnoh1p40)

Kullanýcý giriþi yapýlmamýþsa Home/Blog/Login/Register üzerinden yayýnlanan postlarý görüntüleyebilir, üye olabilir, kullanýcý giriþi yapabilir ve baþlýk&içerik için arama yapabilir.

## **Login & Register**

![enter image description here](https://lh3.googleusercontent.com/w5P-IWOuBl5XTWezzwNUPjZIByvT9IOgiHpAZX3J6XFYKTpNxQKCbg1JwInvJIf43X7G1SiFV8Y)

Kullanýcý adý ve þifre doðrulamasýyla kullanýcý giriþi yapabilir.

![enter image description here](https://lh3.googleusercontent.com/diyK7YPhsPFZbOY3iEC9cXuikfpJqocyvdjoIWcfCzgngqhGMTtrahHVqvSyPWLladQdihw7yrQ)

Üye kaydý yapabilir.

## **Blog**

![enter image description here](https://lh3.googleusercontent.com/qE1_xqq1t5-ZZC-erXlWBhHw3IqAQQ667Z4Wf4UOLcbfi7Mt7s0acTXeRVKhNOtYT9mvLvIa0-I)

Kullanýcý giriþi yaptýktan sonra New Post linki aktif olur ve post yayýnlamaya baþlayabilir.

![enter image description here](https://lh3.googleusercontent.com/3SGSfbRpWY8bmjCPxnaAC6qiq930BTjymko6vE2ZK6FvSQ4B3jEfrJj431R_VM-eINdfz3TbQHY)
![enter image description here](https://lh3.googleusercontent.com/AM5yVnxoPDZCGNec8A2cXcQTT9LjYyDmyyE1oURbgS8ZFOKHtlasVDSEMtuxHWOkq7iOh-HcEvY)

Index sayfa numarasýna göre bir url adresi atanýr.

![enter image description here](https://lh3.googleusercontent.com/L6JooNNQdv6sSdxQepchjWXrbJzgkamGNped185OUCyayBwns75w1Z4QlVCMrbnsJH4E-OPBiXw)

Yayýnlanmýþ bir post üzerinden “View” butonuna týklayarak postun detay sayfasýna yönlendirilir. “Update” ile güncellemeler yapýp “Delete” ile silebilir.

![enter image description here](https://lh3.googleusercontent.com/ow8K7oRR9BzTZeLdUwLONvK_n45XTU0LuxBOAdXWbuLDEcpsIWJqTBeo_WGyQgKtpfy3ielvxP4)

Her postun detay sayfasýna kendi baþlýk bilgisine göre eþsiz bir url adresi atanýr. Ayný baþlýk bilgisine sahip postlar için sonuna nümerik ifadeler eklenir.

## **Comment**

![enter image description here](https://lh3.googleusercontent.com/V8gip_7cPjlR_1TLc4jYYymVGyj8N64Ann6HO4yTh4Ix33lVUpkWOUxLuXmaqkhW0fa2vzxtqok)

Post detay sayfasýndan yorum yapýlabilir. Ziyaretçiler bu formu göremez yalnýzca üyeler eriþebilir.

![enter image description here](https://lh3.googleusercontent.com/IlPs1pFaN3TgoAJGcThQETGJjkHZPg54Fy1IjDy_yo4MR6kGQhwYvJo90z25lQww3QcjlrnJIek)

Yapýlan yorumlar postun detay sayfasýnda görüntülenir. Silinen bir posta yapýlan yorumlar da veritabanýndan silinir.

![enter image description here](https://lh3.googleusercontent.com/hLnJrl5QPi3CXh00RHK-ZHv3PXqdMlyx__awq3LJ2SYWuTLhiL-pQCs8-Cp9jS5wzedQ0w6Cu3s)

Son paylaþýlan üstte olacak þekilde kronolojik olarak sýralanýr ve her sayfada 5 adet post görüntülenir.

## **Post Eklemek**

![enter image description here](https://lh3.googleusercontent.com/_LOcLpAIhoI5Nt82-KmcB9DnaySxzPeB1mni3VhhafcsfB2gYxypkvjj1J-QHaZvY1tSgXHchSk)

Baþlýk, içerik metinleri ve tercihe göre görsel ekleyerek post yayýnlanabilir. Buna yalnýzca kullanýcý giriþi yapmýþ üyeler eriþebilir.

![enter image description here](https://lh3.googleusercontent.com/fy0rsAPrnBrf_8Wym1UZGgK4_Mi_y99wQZfdxmTajAFHoFA4x-fWGl7QhBp46eaQiU5v7G1YYTA)

Post ekleme iþlemi baþarýlý olduðunda bir mesaj ile kullanýcýya bildirilir.