# Made by: Atrin Shahroudi
# Description: This is a interactive dashboard
# I made with streamlit for UI and pandas to handle data. Data Set is from Kaggle

import pandas as pd
import streamlit as st

df = pd.read_csv('co2_data.csv')

all_columns = df.columns
print(all_columns)

st.title('World Wide Co2 per Capita 🌐')

filtered_data = df.copy()
with st.sidebar:
    country_filter = st.selectbox('Select Country', df['Entity'].dropna().unique())
    year_filter = st.multiselect('Select Year', df['Year'].dropna().unique())
    if year_filter:
        filtered_data = filtered_data[filtered_data['Year'].isin(year_filter)]

    if country_filter:
        filtered_data = filtered_data[filtered_data['Entity'] == country_filter]

col1, col2 = st.columns(2)
with col1:
    st.metric('Selected:', country_filter)

with col2:
    st.metric('Data Number:', len(filtered_data))


st.bar_chart(filtered_data, x='Year', y='Annual CO₂ emissions (per capita)')
st.line_chart(filtered_data, x='Year', y='Annual CO₂ emissions (per capita)')

st.write('Global Countries Ranking ⚙️')
st.bar_chart(df, x='Entity', y='Annual CO₂ emissions (per capita)')
st.write('Top 10 Rankings High to Low 🏆')

# My modification start
col3, col4, col5 = st.columns(3)
with col3:
    st.metric('Max', round(df['Annual CO₂ emissions (per capita)'].max(),2))

with col4:
    st.metric('Min', df['Annual CO₂ emissions (per capita)'].min())

with col5:
    st.metric('Average', round(df['Annual CO₂ emissions (per capita)'].mean(), 2))

df = df.sort_values('Annual CO₂ emissions (per capita)', ascending=False)
df = df.sort_values('Year', ascending=False).reset_index(drop=True)
st.dataframe(df.head(10))
# My modification end