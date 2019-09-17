Django Framework ile oluþturulmuþ bir blog sitesidir. Üye olma ve kullanýcý giriþi iþlemleri yapabilir. Kullanýcýlar (tercihe göre) görsel ekleyip metin yazýlarý ile post yayýnlayabilir. Diðer kullanýcýlar bu postlara yorum metni yazabilir. Yayýnlanan postlar veritabanýnda tutulur ve kullanýcý isterse yayýnlanan postu üzerinde deðiþiklik yapabilir veya silebilir.

Kullanýlan teknolojiler:
-Django Framework & Python
-HTML & CSS & JavaScript
-SQLite
-Bootstrap

3. Parti Django Uygulamalarý:
-Crispy Form
-Django Cleanup
-CKEditor (aktif deðil)
-Captcha (aktif deðil)


Navbar



Kullanýcý giriþi yapýlmamýþsa Home/Blog/Login/Register üzerinden yayýnlanan postlarý görüntüleyebilir,üye olabilir, kullanýcý giriþi yapabilir ve baþlýk&içerik için arama yapabilir.


Login & Register



Kullanýcý adý ve þifre doðrulamasýyla kullanýcý giriþi yapabilir.



Üye kaydý yapabilir.


Blog



Kullanýcý giriþi yaptýktan sonra New Post linki aktif olur ve post yayýnlamaya baþlayabilir.



Index sayfa numarasýna göre bir url adresi atanýr.



Yayýnlanmýþ bir post üzerinden “View” butonuna týklayarak postun detay sayfasýna yönlendirilir. “Update” ile güncellemeler yapýp “Delete” ile silebilir.



Her postun detay sayfasýna kendi baþlýk bilgisine göre eþsiz bir url adresi atanýr. Ayný baþlýk bilgisine sahip postlar için sonuna nümerik ifadeler eklenir.
Comment



Post detay sayfasýndan yorum yapýlabilir. Ziyaretçiler bu formu göremez yalnýzca üyeler eriþebilir.



Yapýlan yorumlar postun detay sayfasýnda görüntülenir. Silinen bir posta yapýlan yorumlar da veritabanýndan silinir.



Son paylaþýlan üstte olacak þekilde kronolojik olarak sýralanýr. Her sayfada 5 adet post görüntülenir.


Post Eklemek


Baþlýk, içerik metinleri ve tercihe göre görsel ekleyerek post yayýnlanabilir. Buna yalnýzca kullanýcý giriþi yapmýþ üyeler eriþebilir.



Post ekleme iþlemi baþarýlý olduðunda bir mesaj ile kullanýcýya bildirilir.


