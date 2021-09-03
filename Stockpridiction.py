import streamlit as st
import pandas as pd
from PIL import Image
from streamlit.proto.RootContainer_pb2 import SIDEBAR

st.write("""**Visually** show data on a stock! Data range from Aug 29,2020 - Aug 29, 2021""")

#sidebar header
st.sidebar.header('User Input')
#function to get the users input
def get_input():
    start_date= st.sidebar.text_input("Start date","2020-08-29")
    end_date= st.sidebar.text_input("End date","2021-08-29")
    stock_symbol= st.sidebar.text_input("Stock Symbol","AMZN")
    return start_date,end_date,stock_symbol

#create a function to get the company name
def get_company_name(symbol):
    if symbol=='AMZN':
        return 'Amazon'
    elif symbol=='TSLA':
        return 'Tesla'
    elif symbol=='GOOG':
        return 'ALphabet'
    else:
        'None'

#creating a fucntion to get the proper data according to the compny
def get_data(symbol,start,end):
    #loading data
    if symbol.upper()=='AMZN':
        df = pd.read_csv("C:/Users/91981/Documents/others/WIE/Project2/AMZN.csv")
    elif symbol.upper()=='TSLA':
        df = pd.read_csv("C:/Users/91981/Documents/others/WIE/Project2/TSLA.csv")
    elif symbol.upper()=='GOOG':
        df = pd.read_csv("C:/Users/91981/Documents/others/WIE/Project2/GOOG.csv")
    else:
        df= pd.DataFrame(columns =['Date','Open','High','Low','Close','Adj Close','Volume'])
        #get the datee range
    start = pd.to_datetime(start)
    end=pd.to_datetime(end)
    #seting the start and end index rows both to 0
    start_row=0
    end_row=0
     # starting the date from the top and going according to the dataset
    for i in range(0,len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row=i
            break
    #starting  from the bottom of the dataset 
    for j in range (0,len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row=len(df)-j-1
            break
    #Set the index to be the date
    df=df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

#Geting the users input
start, end, symbol = get_input()
#geting the data
df= get_data(symbol,start,end)
#get the companny name
company_name=get_company_name(symbol.upper())

#display the closed price 
st.header(company_name+"Close Price\n")
st.line_chart(df['Close'])

#display the volume
st.header(company_name+"Volume\n")
st.line_chart(df['Volume'])

#geting the statistics
st.header('Data Statistics')
st.write(df.describe())

        

