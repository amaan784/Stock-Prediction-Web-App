# importing necessary packages
# streamlit fbprophet yfinance plotly

# the web framework
import streamlit as st 

# for forecasting / prediction
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
# import pystan

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
st.title("The Stock Prediction App")
st.subheader("A Web Application for Stock Prediction\n")

# choosing stocks that we want to display / deal with 
# choosing from https://finance.yahoo.com/
# displaying them in ascending order
unsortedStocksList = ("JNJ", "GOOG", "AAPL", "BRK-A", "AMZN", "MSFT", "JPM", "NFLX", "META", "BAC", "GME", "MCD", "KO")
stocks = sorted(unsortedStocksList)
stocks = tuple(stocks)

# creating a dropdown box for user selection
dropdown_box_selection = st.selectbox("\nSelect a stock for prediction\n", stocks)

# creating a slider for selecting number of years of stock data
# calculating the no. of days based on the slider selection
n_years = st.slider("\nYears of prediction", 1, 10)
period = n_years * 365
    
@st.cache
def load_stock_data(stock_code):
    """
        The "@st.cache" helps for the data to be present already if the data was selected before and is being selected again
        
        The function loads stock data through the yahoo finance library 
        
        Args:
            stock_code (string): a code or abbreviation for identifying a stock
            
        Returns: the data retrieved from yahoo finance
    """
    # this will give a pandas dataframe for a particular stock with the speicifed start date and end date
    data = yf.download(stock_code, START, TODAY)
    # the reset_index method will not create a new DataFrame. 
    # Instead, it will directly modify and overwrite the original DataFrame
    data.reset_index(inplace=True)
    return data

# loads the data and has placeholders for before and after loading the data
# loads the data through load_stock_data() which we made
stock_data_state = st.text("Load data...")
stock_data = load_stock_data(dropdown_box_selection)    
stock_data_state.text("Data Loaded!")


# writes a subheading
# displays the stock data as a pandas dataframe
st.subheader("\nDisplaying first 5 rows for the Stock Data")
st.write(stock_data.head())
st.subheader("Displaying last 5 rows for the Stock Data")
st.write(stock_data.tail())


def plot_data():
    """
        Creates scatter plots for a particular stock
        The y axis contains the opening and closing price and the x axis contains the date/time
    """
    # creating a plotly graph object figure
    figure = go.Figure()
    
    # plotting 2 scatter plot lines on one graph
    # the first box contains the graph and is the plot
    # the second box is the slider
    # we have appropriate labels and titles
    figure.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Open'], name='Open Price'))
    figure.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name='Closing Price'))
    figure.layout.update(title_text="Scatter Plots", xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)
    
# calls the plot_data() function which we made for plotting the data
plot_data()

# Forecasting
df_train = stock_data['Date', 'Close']
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

# if __name__ == '__main__':
#   main()