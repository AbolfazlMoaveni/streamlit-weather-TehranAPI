import streamlit as st
import requests
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://api.open-meteo.com/v1/forecast?latitude=32&longitude=53&hourly=temperature_2m&timezone=auto"
def WeatherPrint(temp1):
    st.write(f'Timezone: {temp1['timezone'].partition('/')[2]}')
    st.json(data)
    DayHours = 24
    LogList=[]
    TempList=[]
    for i in range(168):
        DayList=[]
        AppendList = []
        DateTime=str(temp1['hourly']['time'][i]).partition('T')
        temperature=temp1['hourly']['temperature_2m'][i]
        AppendList.append(DateTime[2]) 
        AppendList.append(str(temperature))
        TempList.append(AppendList)
        if i%23 == 0 and i!=0:
            LogBlock=[DateTime[0],TempList]
            # st.write(LogBlock)
            LogList.append(LogBlock)
            TempList = []
    st.write(LogList)
    df=pd.DataFrame(LogList)
    st.dataframe(df)
    PltShowToday(LogList)


    #df.to_csv('output.csv',index=False)
    # we continue here


def PltShowToday(logl):
    # st.write(logl[0][1][i][1] for i in range(24))
    # st.write(x)
    x = [logl[0][1][i][1] for i in range(24)]
    xpoints= np.array(range(24))
    ypoints= np.array(x)
    # st.write(xpoints)
    # st.write(ypoints)
    fig,ax=plt.subplots()
    ax.plot(xpoints,ypoints)
    st.pyplot(fig)
    

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        WeatherPrint(data)
        
    else:
        st.write("not successful")
except requests.exceptions.RequestException as e:
    
    st.warning(f'error : {response.status_code} - {e}')