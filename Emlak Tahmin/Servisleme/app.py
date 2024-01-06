import pandas as pd 
import numpy as np
import streamlit as st 
import joblib
from predict_cost import predict

#Arayüz
st.markdown("## Emlak Fiyat Tahmini")
st.write("----------------------------")

#Veri giriş kolonu oluşturma
metrekare = st.number_input("Evin Metrekaresi")
# oda_sayisi = st.number_input("Evin Oda Sayısı")
# bulundugu_kat = st.number_input("Bulunduğu Kat")
# isitma_tipi = st.number_input("Isıtma Tipi")
# aidat = st.number_input("Aidat")
# balkon_sayisi = st.number_input("Balkon Sayısı")
# binanin_yasi = st.number_input("Binanın Yaşı")
# esya_durumu = st.number_input("Eşya Durumu")
# kira_getirisi = st.number_input("Kira Getirisi")
# banyo_sayisi = st.number_input("Banyo Sayısı")
# krediye_uygunluk = st.number_input("Krediye Uygunluk")
oda_sayisi = st.selectbox("Evin Oda Sayısı", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
bulundugu_kat = st.selectbox("Bulunduğu Kat", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
#isitma_tipi = st.selectbox("Isıtma Tipi", [1, 2, 3, 4, 5, 6])
aidat = st.number_input("Aidat")
balkon_sayisi = st.selectbox("Balkon Sayısı", [0, 1, 2, 3])
binanin_yasi = st.number_input("Binanın Yaşı")
#esya_durumu = st.selectbox("Eşya Durumu", [0,1])
#kira_getirisi = st.number_input("Kira Getirisi")
banyo_sayisi = st.selectbox("Banyo Sayısı", [0, 1, 2, 3])
#krediye_uygunluk = st.selectbox("Krediye Uygunluk", [0,1])

#Tahmin butonu
if st.button("Ev Fiyatını Tahmin Et"):
    ev = np.array([[metrekare, oda_sayisi, bulundugu_kat,  aidat, balkon_sayisi, binanin_yasi,
                                banyo_sayisi]])
    fiyat = predict(ev)
    st.text(fiyat[0])