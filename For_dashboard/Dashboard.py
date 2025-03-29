import streamlit as st
import pandas as pd

import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import io

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.file']
CLIENT_SECRET_FILE = "/Users/sishanyang/Desktop/client_secret.json"
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
creds = flow.run_local_server(port=0)
service = build('drive', 'v3', credentials=creds)
file_id = '1Us4nGXagv8cL5KtA6r1UZ43xFjsoplsr'
file = service.files().get(fileId=file_id).execute()
request = service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)

done = False
while done is False:
    status, done = downloader.next_chunk()
fh.seek(0)
df = pd.read_csv(fh)
df
st.set_page_config(
    page_title="Land Restoration in Assaba, Sahel",
    page_icon="🏜️💦",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
df = pd.read_csv('clean_data.csv', index_col=0)
df
st.title("Assaba Region Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")
year_filter = st.sidebar.slider("Select Year", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].max()))
land_type_filter = st.sidebar.selectbox("Select Land Type", df['land_type'].unique())

# Filter Data Based on Sidebar Inputs
filtered_df = df[(df['year'] == year_filter) & (df['land_type'] == land_type_filter)]

# Display the filtered DataFrame
st.subheader(f"Filtered Data for {land_type_filter} in {year_filter}")
st.write(filtered_df)

# GPP vs Rainfall (Scatter Plot)
st.subheader("GPP vs Rainfall")
fig, ax = plt.subplots()
ax.scatter(filtered_df['rainfall'], filtered_df['gpp'])
ax.set_xlabel("Rainfall")
ax.set_ylabel("GPP")
st.pyplot(fig)

# Population Density Map (If lat/lon is available)
st.subheader("Population Density Map")

# Plotly Map (you can visualize population density on a map if required)
fig = px.scatter_geo(filtered_df, lat='actual_lat', lon='actual_lon', size='popdens', color='popdens',
                     hover_name='land_type', title="Population Density in Assaba Region")
st.plotly_chart(fig)

# Statistical Summary
st.subheader("Statistical Summary")
st.write(filtered_df.describe())

# Rainfall Distribution (Histogram)
st.subheader("Rainfall Distribution")
fig = plt.figure(figsize=(8, 6))
sns.histplot(filtered_df['rainfall'], bins=10, kde=True)
st.pyplot(fig)

# Show Correlation Matrix
st.subheader("Correlation Heatmap")
corr = filtered_df.corr()
fig = plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
st.pyplot(fig)