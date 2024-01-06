# Emlak Tahmin Uygulaması:
- İstanbul Beyoğlundaki evlerin fiyatlarını tahmin eden makine öğrenmesi projesi.
- Projede önce örnek ev verileri çekildi.
- Daha sonra bu veriler üzerinde ön işleme yapıldı (one hot encoding, vs.).
- Daha sonra işlenmiş veriler üzerinden makine öğrenmesi algoritmaları eğitildi.
- 7 Farklı algoritma eğitildi (catboost, gbm, knn, pcr, pls, rf).
- Daha sonra içlerinden en verimli sonucu veren algoritma seçildi (Random Forest).
- Daha sonra bu algoritma üzerinden modelin servislemesi yapıldı.

![servisleme](https://github.com/eyp091/Emlak_Tahmin/blob/main/resimler/emlak_tehmin.png)

- En son gerekli parametreler girilir ve evin fiyatı tahmin edilir.
