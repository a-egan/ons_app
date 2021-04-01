import requests
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly as pl
import streamlit as st

st.title("UK Labour Market Statistics Dashboard")
st.header("""
    A brief overview of the latest ONS labour market stats.
    """)
st.markdown(
    """
    Created by [Anthony Egan](https://uk.linkedin.com/in/anthony-egan-51b538150)
    """
)


@st.cache
def grab_ONS_time_series_data(dataset_id, timeseries_id):
    """ This function grabs specified time series from the ONS API. """
    api_endpoint = "https://api.ons.gov.uk/"
    api_params = {
        "dataset": dataset_id,
        "timeseries": timeseries_id}
    url = (api_endpoint
           + "/".join([x+"/"+y for x, y in zip(api_params.keys(),
                                               api_params.values())][::-1])
           + "/data")
    return requests.get(url).json()


# 1. Unemployment rate (aged 16 and over, seasonally adjusted)
data = grab_ONS_time_series_data("LMS", "MGSX")

# Check we have the right time series
title_text = data["description"]["title"]
st.header(title_text)
# Put the data into a dataframe and convert types
# Note that you"ll need to change months if you"re
# using data at a different frequency
df = pd.DataFrame(pd.io.json.json_normalize(data["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# Display data in streamlit
st.write("Chart")
st.line_chart(df["value"])

agree1 = st.checkbox("Show unemployment rate data table")
if agree1:
    st.write("Table")
    df = df.rename(columns={"label": "period"})
    st.write(df[["period", "value"]])

# Source
st.write("Source:", df["sourceDataset"][0])
# Update Date
st.write("Last updated:", df["updateDate"][-1])

# 2.Employment rate (aged 16 to 64, seasonally adjusted)
data = grab_ONS_time_series_data("LMS", "LF24")

# Check we have the right time series
title_text = data["description"]["title"]
st.header(title_text)
# Put the data into a dataframe and convert types
# Note that you"ll need to change months if you"re
# using data at a different frequency
df = pd.DataFrame(pd.io.json.json_normalize(data["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# Display data in streamlit
st.write("Chart")
st.line_chart(df["value"])
agree2 = st.checkbox("Show employment rate data table")
if agree2:
    st.write("Table")
    df = df.rename(columns={"label": "period"})
    st.write(df[["period", "value"]])

# Source
st.write("Source:", df["sourceDataset"][0])
# Update Date
st.write("Last updated:", df["updateDate"][-1])


# 3.LFS: Economic inactivity rate: UK: All: Aged 16-64: %: SA

data = grab_ONS_time_series_data("LMS", "LF2S")

# Check we have the right time series
title_text = data["description"]["title"]
st.header(title_text)
# Put the data into a dataframe and convert types
# Note that you"ll need to change months if you"re
# using data at a different frequency
df = pd.DataFrame(pd.io.json.json_normalize(data["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# Display data in streamlit
st.write("Chart")
st.line_chart(df["value"])
agree3 = st.checkbox("Show inactivity rate data table")
if agree3:
    st.write("Table")
    df = df.rename(columns={"label": "period"})
    st.write(df[["period", "value"]])

# Source
st.write("Source:", df["sourceDataset"][0])
# Update Date
st.write("Last updated:", df["updateDate"][-1])

# 4.UK Vacancies (thousands) - Total

data = grab_ONS_time_series_data("UNEM", "AP2Y")

# Check we have the right time series
title_text = data["description"]["title"]
st.header(title_text)
# Put the data into a dataframe and convert types
# Note that you"ll need to change months if you"re
# using data at a different frequency
df = pd.DataFrame(pd.io.json.json_normalize(data["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# Display data in streamlit
st.write("Chart")
st.line_chart(df["value"])
agree4 = st.checkbox("Show vacancies data table")
if agree4:
    st.write("Table")
    df = df.rename(columns={"label": "period"})
    st.write(df[["period", "value"]])

# Source
st.write("Source:", df["sourceDataset"][0])
# Update Date
st.write("Last updated:", df["updateDate"][-1])

# 5. Regional unemployment rates
st.header("Regional unemployment rates (seasonally adjusted)")

# 1 - East data data
data_East = grab_ONS_time_series_data("LMS", "YCNH")
geo = "East"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_East["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df2 = df.rename(columns={"value": geo})


# 2 - East Midlands data

data_EM = grab_ONS_time_series_data("LMS", "YCNF")
geo = "East Midlands"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df3 = df.rename(columns={"value": geo})

# 3 - London data

data_EM = grab_ONS_time_series_data("LMS", "YCNI")
geo = "London"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df4 = df.rename(columns={"value": geo})

# 4 - North East data

data_EM = grab_ONS_time_series_data("LMS", "YCNC")
geo = "North East"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df5 = df.rename(columns={"value": geo})

# 5 - North West data

data_EM = grab_ONS_time_series_data("LMS", "YCND")
geo = "North West"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df6 = df.rename(columns={"value": geo})

# 6 - Northern Ireland data

data_EM = grab_ONS_time_series_data("LMS", "ZSFB")
geo = "Northern Ireland"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df7 = df.rename(columns={"value": geo})

# 7 - Scotland data

data_EM = grab_ONS_time_series_data("LMS", "YCNN")
geo = "Scotland"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df8 = df.rename(columns={"value": geo})

# 8 - South East data

data_EM = grab_ONS_time_series_data("LMS", "YCNJ")
geo = "South East"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df9 = df.rename(columns={"value": geo})

# 9 - South West data

data_EM = grab_ONS_time_series_data("LMS", "YCNK")
geo = "South West"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df10 = df.rename(columns={"value": geo})


# 10 - Wales data

data_EM = grab_ONS_time_series_data("LMS", "YCNM")
geo = "Wales"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df11 = df.rename(columns={"value": geo})


# 11 - West Midlands data

data_EM = grab_ONS_time_series_data("LMS", "YCNG")
geo = "West Midlands"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df12 = df.rename(columns={"value": geo})

# 12 - Yorks & the Humber data

data_EM = grab_ONS_time_series_data("LMS", "YCNE")
geo = "Yorks & the Humber"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df13 = df.rename(columns={"value": geo})


# Merge geo dataframes
df_all = df2.join(df3, lsuffix="_left", rsuffix="_right").join(
    df4, lsuffix="_left", rsuffix="_right").join(df5, lsuffix="_left", rsuffix="_right").join(df6, lsuffix="_left", rsuffix="_right").join(df7, lsuffix="_left", rsuffix="_right").join(df8, lsuffix="_left", rsuffix="_right").join(df9, lsuffix="_left", rsuffix="_right").join(df10, lsuffix="_left", rsuffix="_right").join(df11, lsuffix="_left", rsuffix="_right").join(df12, lsuffix="_left", rsuffix="_right").join(df13, lsuffix="_left", rsuffix="_right")


# Toggle feature

loc = st.multiselect(label="Toggle the regions and nations you wish to see.",
                     options=("East", "East Midlands", "London", "North East", "North West", "Northern Ireland",
                              "Scotland", "South East", "South West", "Wales", "West Midlands", "Yorks & the Humber"),
                     default=("East", "East Midlands", "London", "North East", "North West", "Northern Ireland", "Scotland", "South East", "South West", "Wales", "West Midlands", "Yorks & the Humber"))

# print chart and table

st.write("Chart")
st.line_chart(
    df_all[loc])
# df_all[["East", "East Midlands", "London", "North East", "North West", "Northern Ireland", "Scotland", "South East", "South West", "Wales", "West Midlands", "Yorks & the Humber"]])

agree5 = st.checkbox("Show regional unemployment data table")
if agree5:
    st.write("Table (unemployment rate by month)")
    st.write(df_all[["East", "East Midlands", "London", "North East", "North West", "Northern Ireland",
                     "Scotland", "South East", "South West", "Wales", "West Midlands", "Yorks & the Humber"]])

# Source
st.write("Source:", df["sourceDataset"][0])
# Update Date
st.write("Last updated:", df["updateDate"][-1])


# 4 Unemployment rates by age band
st.header("Unemployment rates by age band (seasonally adjusted)")

# 2 - 16-24

data_EM = grab_ONS_time_series_data("LMS", "MGWY")
geo = "16-24"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df22 = df.rename(columns={"value": geo})

# 3 - 25-49

data_EM = grab_ONS_time_series_data("LMS", "MGXB")
geo = "25-49"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!
df23 = df.rename(columns={"value": geo})

# 4 - 50+

data_EM = grab_ONS_time_series_data("LMS", "YBVW")
geo = "50+"

# Put the data into a dataframe and convert types
df = pd.DataFrame(pd.io.json.json_normalize(data_EM["months"]))

# Put the data in a standard datetime format
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)
df = df.set_index("date")

# ! -- change label to geo tag --!

df24 = df.rename(columns={"value": geo})

# Merge age band dataframes
df_all2 = df22.join(df23, lsuffix="_left", rsuffix="_right").join(
    df24, lsuffix="_left", rsuffix="_right")


# Toggle feature

loc2 = st.multiselect(label="Toggle the age bands you wish to see.",
                      options=("16-24", "25-49", "50+"),
                      default=("16-24", "25-49", "50+"))

# print chart and table

st.write("Chart")
st.line_chart(
    df_all2[loc2])


agree5 = st.checkbox("Show unemployment rates by age data table")
if agree5:
    st.write("Table")
    df_all2 = df_all2.rename(columns={"label_left": "period"})
    st.write(df_all2[["period", "16-24", "25-49", "50+"]])

# Source
st.write("Source:", df["sourceDataset"][0])
# Update Date
st.write("Last updated:", df["updateDate"][-1])
