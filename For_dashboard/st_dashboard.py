# import streamlit as st
# import pandas as pd

# import altair as alt
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pydeck as pdk

# import os
# import io


# # page setting
# st.set_page_config(
#     page_title="Land Restoration in Assaba, Sahel",
#     page_icon="🏜️💦",
#     layout="wide",
#     initial_sidebar_state="expanded")

# # read dataset
# @st.cache_data
# def load_data():
#     try:
#         df = pd.read_csv('clean_data.csv', index_col=0)
#         print("CSV file loaded successfully.")
#         return df
#     except FileNotFoundError:
#         st.error("Error: clean_data.csv not found.")
#         st.stop()
#     except Exception as e:
#         st.error(f"An error occurred while reading the CSV file: {e}")
#         st.stop()

# # 加载数据
# df = load_data()

# # 检查'year'列是否存在于索引中
# if 'year' in df.index.names:
#     print("'year' is in the index. Resetting index...")
#     df = df.reset_index()

# # 检查'year'列是否存在
# if 'year' not in df.columns:
#     st.error("Error: 'year' column not found in the CSV.")
#     st.stop()

# # dark mode
# alt.themes.enable("default")

# # 打印数据的前几行
# st.write(df.head())

# # Sidebar Filters
# st.sidebar.header("Filter Data")
# year_filter = st.sidebar.slider("Select Year", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].max()))
# land_type_filter = st.sidebar.selectbox("Select Land Type", df['land_type'].unique())

# # Filter Data Based on Sidebar Inputs
# filtered_df = df[(df['year'] == year_filter) & (df['land_type'] == land_type_filter)]

# # Check if there's data for the selected year
# if filtered_df.empty:
#     st.warning("No data available for the selected filters.")

# else:
#     # Display the filtered DataFrame
#     st.subheader(f"Filtered Data for {land_type_filter} in {year_filter}")
#     st.write(filtered_df)

#     # 显示当前选择年份数据的地图
# if filtered_df.empty:
#     st.warning(f"There is no data for this land type in {year_filter}.")
# else:
#     st.subheader(f"GPP in {year_filter}")

#     # Pydeck 图层定义
#     map_style = "mapbox://styles/mapbox/light-v9"
#     layer = pdk.Layer(
#         "ScatterplotLayer",  # 使用散点图层
#         filtered_df,
#         pickable=True,  # 可以点击
#         opacity=1,
#         get_position='[actual_lon, actual_lat]',  # 经度和纬度
#         get_radius='value * 500',  # 圆的大小
#         get_fill_color="[gpp * 30, 50, 100, 150]",  # 根据 value 颜色填充
#         get_line_color=[255, 255, 255],  # 圆圈边界颜色
#     )

#     # 设置 Pydeck 地图的视角
#     view_state = pdk.ViewState(
#         latitude=filtered_df['actual_lat'].mean(),
#         longitude=filtered_df['actual_lon'].mean(),
#         zoom=4,
#         pitch=0
#     )

#     # 使用 pydeck 创建地图
#     r = pdk.Deck(
#         layers=[layer],
#         initial_view_state=view_state,
#         map_style=map_style,
#         tooltip={"text": "GPP: {gpp}"}  # 鼠标悬停时显示的内容
#     )

#     # 在 Streamlit 中展示地图
#     st.pydeck_chart(r)
