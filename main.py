# the web framework
import streamlit as st 

# for forecasting / prediction
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
# unused packages related to fb prophet
# import pystan
# import prophet
from prophet import Prophet
from prophet.plot import plot_plotly

# yahoo finance API/ package for getting stock data
import yfinance as yf

# a figure / graph plotting package
from plotly import graph_objs as go

# date time package 
from datetime import date


# setting up a start date and getting the current date
# this is for the stocks
START = "2012-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# giving the web app a title and a subheader
st.title("The Stock Forecast App")
st.subheader("A Web Application for Stock Forecast\n")

# choosing stocks that we want to display / deal with 
# choosing from https://finance.yahoo.com/
# since we wanted to display the company names on the dropdown instead of the company stock code 
# so another tuple was created for the full company names with the same indices as the stock codes list
# then the 2 tuples were matched and they formed a dictionary
# for each item in the dictionarys, the key is the company name and the value is the company stock code
# displaying them in ascending order
unsortedStocksCodes = ("JNJ", "GOOG", "AAPL", "BRK-A", "AMZN", "MSFT", "JPM", "NFLX", "META", "BAC", "GME", "MCD", "KO")
unsortedStocksList = ("Johnson & Johnson", "Alphabet Inc Class C", "Apple Inc", "Berkshire Hathaway Inc. Class A", 
                      "Amazon.com, Inc.", "Microsoft Corporation", "JPMorgan Chase & Co", "Netflix Inc", "Meta Platforms Inc", 
                      "Bank of America Corp", "GameStop Corp.", "McDonald's Corp", "Coca-Cola Co")
stocks_dictionary = dict(zip(list(unsortedStocksList), list(unsortedStocksCodes)))
stocks = sorted(unsortedStocksList)
stocks = tuple(stocks)


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


def plot_data(stock_data):
    """
        Creates scatter plots for a particular stock
        The y axis contains the opening and closing price and the x axis contains the date/time
    """
    st.subheader("Plotting Scatter Plots")
    # creating a plotly graph object figure
    figure = go.Figure()
    
    # plotting 2 scatter plot lines on one graph
    # the first box contains the graph and is the plot
    # the second box is the slider
    # we have appropriate labels and titles
    figure.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Open'], name='Open Price'))
    figure.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name='Closing Price'))
    #figure.layout.update(title_text="Plotting Scatter Plots", xaxis_rangeslider_visible=True)
    figure.layout.update(xaxis_rangeslider_visible=True)
    st.plotly_chart(figure)
    
    
def main():
    # creating a dropdown box for user selection
    # whenever the company name is selected in the dropdown, its looked up in the dictionary to find the stocks code
    dropdown_box_selection = st.selectbox("\nSelect a stock for prediction\n", stocks)
    dropdown_box_selection_stock_code = stocks_dictionary[dropdown_box_selection]

    # creating a slider for selecting number of years of stock data
    # calculating the no. of days based on the slider selection
    n_years = st.slider("\nYears of prediction", 1, 10)
    period = n_years * 365

    # for adding space
    for i in range(3):
        st.text("")

    # loads the data and has placeholders for before and after loading the data
    # loads the data through load_stock_data() which we made
    s = "Loading data for " + dropdown_box_selection + "..." 
    stock_data_state = st.text(s)
    stock_data = load_stock_data(dropdown_box_selection_stock_code)    
    s = "Data Loaded for " + dropdown_box_selection + "!"
    stock_data_state.text(s)


    # writes a subheading
    # displays the stock data as a pandas dataframe
    s = "\nDisplaying first 5 rows for the " + "'" + dropdown_box_selection + "'" + " Stock Data"
    st.subheader(s)
    st.write(stock_data.head())
    s = "\nDisplaying last 5 rows for the " + "'" + dropdown_box_selection + "'" + " Stock Data"
    st.subheader(s)
    st.write(stock_data.tail())
    
    # calls the plot_data() function which we made for plotting the data
    plot_data(stock_data)

    # placing placeholders for forecasting
    s = "Forecasting data for " + "'" + dropdown_box_selection + "'" + "..." 
    forecast_state = st.text(s) 

    # Forecasting closing price for stocks using Facebook prophet
    # slicing the colums into a new dataframe and then renaming the columns in it
    # renaming is necessary for the fbprophet package (its a requirement)
    df_train = stock_data[['Date', 'Close']]
    df_train = df_train.rename(columns={'Date': 'ds', 'Close': 'y'})

    # creating a prophet object
    model = Prophet()

    # fitting the data 
    model.fit(df_train)

    # doing the forecast
    # we get a future dataframe
    # the period is the number selected in the slider by the user so we get the prediction for those many years 
    # if the user selects 10 then we get 10 years of prediction from the current date
    future_dataframe = model.make_future_dataframe(periods=period)

    # doing the forecast
    forecast = model.predict(future_dataframe)

    # displaying the last 5 forecast / predicted rows
    s = "\nForecast Data for " + "'" + dropdown_box_selection + "'" + " Stock Data"
    st.subheader(s)
    st.write(forecast.tail())

    # plotting the forecast we got
    st.text("")
    st.subheader('\n\n\nPlotting Forecast Data')
    st.write('ds here means datestamp and y is the stock price')
    figure1 = plot_plotly(model, forecast)
    st.plotly_chart(figure1, )

    # plotting forecast components like trend, weekly, yearly
    st.subheader('\nPlotting Forecast Components')
    figure2 = model.plot_components(forecast)
    st.write(figure2)

    # placing placeholders for forecasting
    s = "Forecasting done for " + "'" + dropdown_box_selection + "'" + "!"
    forecast_state.text(s)


if __name__ == '__main__':
  main()
