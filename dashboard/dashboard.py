import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_order_by_season_df(df):
    order_by_season_df = df.groupby('season_day').agg({
        'count_day': 'mean'
    })
    return order_by_season_df

def create_order_by_hour_df(df):
    order_by_hour_df = df.groupby('time_group', observed=False)[
            ['casual_hour', 'registered_hour']
        ].sum()
    return order_by_hour_df

all_df = pd.read_csv('dashboard/main_data.csv')
all_df.sort_values(by="dteday", inplace=True)

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

order_by_season_df = create_order_by_season_df(main_df)
order_by_hour_df = create_order_by_hour_df(main_df)

st.header('Dicoding Collection Dashboard :sparkles:')


# visualisasi berdasarkan pertanyaan pertama
st.subheader('Total Pelanggan Berdasarkan Musim')
col1, col2 = st.columns(2)
 
with col1:
    total_musim = main_df.season_day.nunique()
    st.metric("Total Musim", value=total_musim)
 
with col2:
    total_cust = main_df.count_day.sum()
    st.metric("Total Pelanggan", value=total_cust)
    

season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
colors = ['#77DD77', '#FFB347', '#FF6961', '#AEC6CF']


# Plot
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(season_labels, order_by_season_df['count_day'].values, color=colors)
plt.grid(axis='y', linestyle='--', alpha=0.7)
ax.bar_label(bars, fmt='%.0f', fontsize=10, fontweight='bold')
st.pyplot(fig)


# visualisasi berdasarkan pertanyaan kedua
st.subheader('Total Pelanggan Harian')
col1, col2 = st.columns(2)
 
with col1:
    total_casual = main_df.casual_hour.sum()
    st.metric("Pelanggan Casual", value=total_casual)
 
with col2:
    total_register = main_df.registered_hour.sum()
    st.metric("Pelanggan Terdaftar", value=total_register)
    
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(order_by_hour_df.index, order_by_hour_df['casual_hour'], marker='o', linestyle='-', label='Casual', color='blue')
ax.plot(order_by_hour_df.index, order_by_hour_df['registered_hour'], marker='s', linestyle='-', label='Registered', color='red')
ax.set_xticks(range(len(order_by_hour_df.index)))
ax.set_xticklabels(order_by_hour_df.index, rotation=45)
ax.legend()
ax.grid(True)
st.pyplot(fig)