# -*- coding: utf-8 -*-
"""dashboard

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qyJaj2ENO0ZjeT_vZh2spCHR4PFwt0zF
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#Load data seller_dataset
e_commerce = pd.read_csv("sellers_dataset.csv")

with st.sidebar:
    st.text("Welcome to Dashboard")

state_ES = e_commerce.loc[e_commerce["seller_state"] == "ES"]

state_CE = e_commerce.loc[e_commerce["seller_state"] == "CE"]

def create_max_min_state_ES(sd):
    max_min_state_ES = sd.groupby(state_ES["seller_city"]).agg({"seller_id": "count"}).rename(columns={"seller_id": "Total Sales"}).sort_values(by="Total Sales", ascending=False).reset_index().rename(columns={"seller_city": "Kota"})
    return max_min_state_ES

def create_dist_state_CE(sd):
    dist_state_CE = e_commerce.groupby(state_CE["seller_city"]).agg({"seller_id": "count"}).rename(columns={"seller_id": "Total Sales"}).sort_values(by="Total Sales", ascending=False).reset_index().rename(columns={"seller_city": "Kota"})
    return dist_state_CE

#Streamlit App
st.header('E-Commerce Public Dashboard: Sellers_Dataset')

#Create Dataframe
max_min_state_ES = create_max_min_state_ES(e_commerce)
dist_state_CE = create_dist_state_CE(e_commerce)

st.subheader('Bagaimana demografi sales tertinggi dan terendah pada kota-kota di negara ES?')

top = max_min_state_ES.head(5)
bottom = max_min_state_ES.tail(5)

combine = pd.concat([top, bottom])

fig, ax = plt.subplots(figsize=(10, 3))
sns.barplot(x='Total Sales', y='Kota', data=combine, palette="Blues_r")
plt.xlabel=('Total Sales')
plt.ylabel=('Kota')
plt.title('Total Sales berdasarkan Kota')

for index, value in enumerate(combine['Total Sales']):
  plt.text(value, index, str(value))
st.pyplot(fig)

with st.expander("See Explanation"):
  st.write(
      """Dapat di simpulkan bahwa kota Cachoeiro de Itapemirim, Vila Velha, dan Vitoria sebagai kota dengan sales tertinggi, dengan demikian di harapkan stakeholder dapat melanjutkan strategi marketing lainnya agar dapat meningkatkan sales di 3 kota tersebut sehingga dapat meningkatkan laba pada perusahaan. Kemudian, kota Cariacica/Es, Colatina, Domingos Martins, Muqui, dan Viana merupakan kota dengan sales terendah, dengan demikian di harapkan stakeholder dapat menimbangkan untuk melanjutkan bisnis nya di kota-kota tersebut. Adapun kota yang berada di ambang tengah yaitu kota Serra dan Cariacica, dengan demikian di harapkan stakeholder dapat menimbangkan bisnis nya pada 2 kota tersebut."""
  )

st.subheader('Bagaimana distribusi sales pada kota-kota yang berada pada negara MS?')

#Hitung total sales untuk setiap kota
total_sales_CE = state_CE.groupby("seller_city")["seller_id"].count()

#Hitung persentase sales untuk setiap kota
percentages = total_sales_CE / total_sales_CE.sum()

#Buat diagram lingkaran
fag, ux = plt.subplots(figsize=(10,8))
plt.pie(percentages, labels=total_sales_CE.index, autopct='%1.1f%%')
plt.title("Total Sales di setiap Kota pada negara CE")
st.pyplot(fag)

with st.expander("See Explanation"):
  st.write(
      """Dapat disimpulkan bahwa kota Fortaleza merupakan kota dengan sales tertinggi yaitu sebesar 53.8% dan di ikuti oleh 6 kota lainnya yaitu Juzeiro do Norte, Mucambo, Pacatuba, Varzea Alegre, Caucaia, dan Eusebio dengan masing masing data sales nya sebesar 7.7%. Di harapkan dengan data ini, stakeholder dapat menimbangkan bisnis nya pada 6 kota tersebut dan meningkatkan sales nya pada kota Fortaleza sehingga dapat berdampak baik pada perusahaan."""
  )
