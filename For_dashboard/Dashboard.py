import streamlit as st
import pandas as pd

import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import os
import io
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request



SCOPES = ['https://www.googleapis.com/auth/drive.file']
CLIENT_SECRET_FILE = "/Users/sishanyang/Desktop/client_secret.json"
CREDENTIALS_FILE = "/Users/sishanyang/Desktop/credentials.json"  # 存储凭证的文件路径

# 检查凭证是否存在且有效
if os.path.exists(CREDENTIALS_FILE):
    creds = None
    # 如果有凭证文件，则加载它
    creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)
    # 如果凭证过期，则重新授权
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
else:
    # 如果没有凭证，则执行授权流程
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    # 保存凭证以便以后使用
    with open(CREDENTIALS_FILE, 'w') as token:
        token.write(creds.to_json())

# 使用授权的凭证建立服务
service = build('drive', 'v3', credentials=creds)
file_id = '1e1oBzeg8Wlq7DO6_PHjqdYWpLDjewWfU'
file = service.files().get(fileId=file_id).execute()
request = service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)

done = False
while done is False:
    status, done = downloader.next_chunk()
fh.seek(0)
df = pd.read_csv(fh)


# 启用深色主题
alt.themes.enable("dark")


# 设置页面配置（必须是第一个 Streamlit 命令）
st.set_page_config(
    page_title="Land Restoration in Assaba, Sahel",
    page_icon="🏜️💦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Filters
st.sidebar.header("Filter Data")
year_filter = st.sidebar.slider("Select Year", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].max()))
land_type_filter = st.sidebar.selectbox("Select Land Type", df['land_type'].unique())

# Filter Data Based on Sidebar Inputs
filtered_df = df[(df['year'] == year_filter) & (df['land_type'] == land_type_filter)]

# 检查筛选后的 DataFrame 是否为空
if filtered_df.empty:
    st.warning("No data found for the selected filters.")
else:
    # Display the filtered DataFrame
    st.subheader(f"Filtered Data for {land_type_filter} in {year_filter}")
    st.write(filtered_df)

    # GPP vs Rainfall (Scatter Plot)
    st.subheader("GPP vs Rainfall")
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['rainfall'], filtered_df['gpp'])
    ax.set_xlabel("Rainfall")
    ax.set_ylabel("GPP")
    ax.set_title("GPP vs Rainfall")
    st.pyplot(fig)

    # Statistical Summary
    st.subheader("Statistical Summary")
    st.write(filtered_df.describe())

    # Rainfall Distribution (Histogram)
    st.subheader("Rainfall Distribution")
    fig = plt.figure(figsize=(8, 6))
    sns.histplot(filtered_df['rainfall'], bins=10, kde=True)
    plt.title("Rainfall Distribution")
    st.pyplot(fig)

    # Show Correlation Matrix
    st.subheader("Correlation Heatmap")
    corr = filtered_df.corr()
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    st.pyplot(fig)
