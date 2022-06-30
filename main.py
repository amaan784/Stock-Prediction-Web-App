# importing necessary packages
# streamlit fbprophet yfinance plotly

# the web framework
import streamlit as st 

# for forecasting / prediction
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import pystan
# yahoo finance package for getting stock data
import yfinance as yf

# a plotting package
from plotly import graph_objs as go

# date time package 
from datetime import date

# setting up a start date and getting the current date
# this is for the stocks
START = "2012-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# giving the web app a title
st.title("Stock Prediction Web Application")

# choosing stocks that we want to display / deal with 
# choosing from https://finance.yahoo.com/
# displaying them in ascending order
unsortedStocksList = ("JNJ", "GOOG", "AAPL", "BRK-A", "AMZN", "MSFT", "JPM", "NFLX", "META", "BAC", "GME", "MCD", "KO")
stocks = sorted(unsortedStocksList)
stocks = tuple(stocks)

# creating a dropdown box for user selection
dropdown_box = st.selectbox("Select a stock for prediction", stocks)

# creating a slider for selecting number of years of stock data
