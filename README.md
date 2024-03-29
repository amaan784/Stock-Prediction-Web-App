[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stock-forecast-streamlit.herokuapp.com/)

# Stock-Prediction-Web-App
A Stock Forecast / Prediction Web Application made using Streamlit

### Instructions to run-

Required Python Version is 3.8.8 (fbprphet doesnt run on the latest python version)-

`pip install -r requirements.txt`

`streamlit run main.py`

Or open in browser-

https://stock-forecast-streamlit.herokuapp.com/

### Difference between Forecast and Prediction

Forecasting is an estimation of a future events which one can make by incorporating and casting forward data related to the past in a pre-determined and systematic manner. Prediction is an estimate of future events made by subjective considerations.

[Source: Key Differences](https://keydifferences.com/difference-between-forecasting-and-prediction.html#:~:text=Forecasting%20is%20an%20estimation%20of,events%20made%20by%20subjective%20considerations.)

### Notes: 
- The graphs in the app are interactive (except the forecast components one).
- The default stock for prediction is AAPL (Apple).
- The default prediction year is 1.
- The forecast part takes time to run since the computation by fbprophet is complicated.
    
### Key Learning:
> Always watch out for the python version of packages and environements (hosting the site and installing fbprophet took a lot of time because of this)

### TODO (maybe):
- view the csv file (present in the unused stock data folder) from the NASDAQ site (https://www.nasdaq.com/market-activity/stocks/screener)
- display all / most stock names in the selection or just allow a search. Use a pandas dataframe for it.
- explore more of fbprophet / prophet

### Sources-

[Streamlit Tutorial by Python Engineer](https://www.youtube.com/watch?v=0E_31WqVzCY)

[Yahoo Finance Website](https://finance.yahoo.com/)

[Streamlit Documentation](https://docs.streamlit.io/)

[Facebook Prophet Documentation](https://facebook.github.io/prophet/docs/quick_start.html#python-api)

Hosting Streamlit help-

- [Streamlit Hosting Tutorial by Data Professor](https://youtu.be/zK4Ch6e1zq8)

- https://github.com/edkrueger/covid-forecast (done by creating a pipenv environment)

- https://github.com/HansikaSachdeva/Stock-Prediction-Web-App

- https://github.com/michaeltuijp/streamlit-crypto-forecaster


