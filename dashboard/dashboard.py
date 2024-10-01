import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.markdown("# Proyek Analisis Data")
st.sidebar.markdown("Nama : Kevin Junus Ketti")
st.sidebar.markdown("Email : kevinketti218@gmail.com")
st.sidebar.markdown("ID Dicoding : kevinjunusketti")
st.sidebar.markdown("---")

st.header("Analisis Data E-Commerce Public Dataset")

df_all_data = pd.read_csv('./dashboard/MainData.csv')

df_all_data['order_purchase_timestamp'] = pd.to_datetime(df_all_data['order_purchase_timestamp'])

st.sidebar.markdown("### Filter")

year = st.sidebar.selectbox("Pilih Tahun untuk Analisis", df_all_data['order_purchase_timestamp'].dt.year.unique())

group_month = df_all_data['order_purchase_timestamp'].dt.to_period("M")
monthly_order = df_all_data.loc[df_all_data['order_purchase_timestamp'].dt.year == year].groupby(group_month).order_id.nunique()

month_mapping = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
monthly_order.index = monthly_order.index.month.map(month_mapping)

month = st.sidebar.selectbox("Pilih Bulan untuk Analisis", range(1, 13), format_func=lambda x: month_mapping[x])

jumlah_terbanyak = monthly_order.max()
bulan_terbanyak = monthly_order.idxmax()
colors = ['blue' if month != bulan_terbanyak else 'green' for month in monthly_order.index]

plt.figure(figsize=(10, 6))
monthly_order.plot(kind="bar", color=colors)
st.subheader(f'Jumlah Pesanan Bulanan di Tahun {year}')
plt.xlabel('Bulan')
plt.xticks(rotation=25)
plt.ylabel('Jumlah Pesanan')
st.pyplot(plt)

st.markdown(f"\nJumlah terbanyak pada bulan **{bulan_terbanyak}** dengan jumlah produk terjual: **{jumlah_terbanyak}**.")

st.markdown("---")

df_filter = df_all_data.loc[(df_all_data['order_purchase_timestamp'].dt.year == year) & 
                            (df_all_data['order_purchase_timestamp'].dt.month == month)]    
top_ten_product_category = df_filter.groupby(by="product_category_name_english").order_id.nunique().sort_values(ascending=False).head(10)
       
plt.figure(figsize=(8, 8))
top_ten_product_category.plot.pie(
    y='Number of Orders', 
    labels=top_ten_product_category.index, 
    autopct='%1.1f%%', 
    legend=False
)
st.subheader(f"Top 10 Kategori Terlaris di Bulan {month_mapping[month]} {year}")
plt.ylabel("")
    
plt.legend(top_ten_product_category.index, loc='center left', bbox_to_anchor=(1.2, 0.5))
st.pyplot(plt)
st.markdown("---")

df_all_data['year'] = df_all_data['order_purchase_timestamp'].dt.year
avg_review_per_year = df_all_data.groupby('year')['review_score'].mean()

plt.figure(figsize=(8, 6))
avg_review_per_year.plot()
st.subheader(f'Perkembangan Skor Review Rata-rata Tiap Tahun')
plt.xlabel('Year')
plt.xticks(ticks=[2016, 2017, 2018], labels=['2016', '2017', '2018'])
plt.ylabel('Average Review Score')
st.pyplot(plt)

df_year = df_all_data[df_all_data['order_purchase_timestamp'].dt.year == year]

df_year['month'] = df_year['order_purchase_timestamp'].dt.month
avg_review_per_month = df_year.groupby('month')['review_score'].mean()

plt.figure(figsize=(8, 6))
avg_review_per_month.plot(kind='line', marker='o')
st.subheader(f'Perkembangan Skor Review Rata-rata di Tahun {year}')
plt.xlabel('Month')
plt.xticks(ticks=range(1, 13), labels=[month_mapping[m] for m in range(1, 13)], rotation=45)
plt.ylabel('Average Review Score')
st.pyplot(plt)


st.markdown("---")
st.markdown("Dikembangkan oleh Kevin Junus Ketti | Email: kevinketti218@gmail.com")
