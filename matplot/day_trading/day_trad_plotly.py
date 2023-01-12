import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import timedelta, datetime, time
import talib as ta
import pytz


class MovingAverageDayTrading():

    def __init__(self, ticker, stop_loss=0.05, take_profit=0.1):
        self.ticker = ticker
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        # This way, when an instance of the class is created, the self.stop_loss and self.take_profit will be set with default values of 0.05 and 0.1 respectively. These values can be overridden when an instance of the class is created by passing a different value for stop_loss and take_profit.

    def moving_average_timeframes(self):
        
        #  QUERYING DATA --------------------------------------------

        end= datetime.today()
        start = end - timedelta(days=7)
        df = yf.download(self.ticker, start= start ,end= end, interval='1m')
        print(f'--------{df}__________')
        print(df.dtypes)
        print(f'index typeeeee : {df.index.dtype}')
        
        # check the interval of your dataframe by using the df.resample function with the same interval of data you want to work with
        ## df.resample('1min')

        #  SETTING UP DATA: ADDING COLUMNS FOR MA  --------------------------------------

        # Exponential Moving Averages
        df['EMA_20'] = df['Adj Close'].ewm(span=20, adjust=False).mean()
        df['EMA_50'] = df['Adj Close'].ewm(span=50, adjust=False).mean()
        df['EMA_200'] = df['Adj Close'].ewm(span=200, adjust=False).mean()
        # the ewm() method to calculate the EMA, passing in the window size or span, which is the number of periods to use in the moving average. You can also adjust whether or not to apply some decay to the weights by adjusting the adjust parameter. By default is set to True, but it depends on the use case.

        # Simple Moving Averages
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['SMA_200'] = df['Close'].rolling(window=200).mean()

        # Bollinger Bands
        df['BOL_upper'], df['BOL_middle'], df['BOL_lower'] = ta.BBANDS(df["Adj Close"])
        
        # Stochastic Oscillator
        df['STO_slowk'], df['STO_slowd'] = ta.STOCH(df["High"], df["Low"], df["Adj Close"])
        
        # Relative Strength Index
        df['RSI'] = ta.RSI(df["Adj Close"])
        
        # Moving Average Convergence Divergence
        df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df["Adj Close"])
        
        
        # CLEANING DATA ------------------------------------------

        print(df.dtypes)

        # check if the data is sorted correctly by running 
        # df.sort_index(inplace=True)

        # fill the empty spaces with what we want to fill it out
        # df.fillna(method='ffill', inplace=True)

        # convert the index to the correct timezone using the pytz library
        # df.index = df.index.tz_localize('UTC').tz_convert('US/Eastern')

        # filter dataframe to only include rows within trading hours
        start_time = time(9, 30)
        end_time = time(16, 0)
        print(f'HHHHHHHHHHHHHH {type(df.index)}')
        

        
        # Remove any rows with missing values
        # df = df.dropna()
        # Filter the data to only include rows within trading hours
        # df = df[(df.index.hour >= 9) & (df.index.hour <= 16)]
        # Remove any rows for weekends (Saturday and Sunday)
        # df = df[df.index.weekday < 5]
        # Select only the columns of interest
        df = df[['Adj Close', 'EMA_20', 'EMA_50', 'EMA_200', 'SMA_20', 'SMA_50', 'SMA_200', 'BOL_upper','STO_slowk', 'RSI', 'MACD']]

        print(f'SHAPEEEEEEEEEEE  {df.shape}')

        
        if self.stop_loss is None or self.take_profit is None:
            raise ValueError("stop_loss and take_profit values must be set before using them")

        #  RISK MANAGEMENT // CHECKS BEFORE PLOTTING ----------------------------

        # buy = []
        # sell = []
        # for i in range(1, len(df)):
        #     # Check for buy signal
        #     if (df['EMA_20'][i] > df['EMA_50'][i] and df['EMA_20'][i-1] < df['EMA_50'][i-1]) and (df['EMA_20'][i] > df['EMA_200'][i] and df['EMA_20'][i-1] < df['EMA_200'][i-1]) and (df['SMA_20'][i] > df['SMA_50'][i] and df['SMA_20'][i-1] < df['SMA_50'][i-1]) and (df['SMA_20'][i] > df['SMA_200'][i] and df['SMA_20'][i-1] < df['SMA_200'][i-1]):
        #         buy.append((df.index[i], df['Adj Close'][i]))
        #         current_price = df['Adj Close'][i]
        #         stop_loss_price = current_price * (1 - self.stop_loss)
        #         take_profit_price = current_price * (1 + self.take_profit)
                
        #         # Implement stop loss and take profit
        #         for j in range(i, len(df)):
        #             if df['Adj Close'][j] < stop_loss_price:
        #                 sell.append((df.index[j], df['Adj Close'][j]))
        #                 break
        #             elif df['Adj Close'][j] > take_profit_price:
        #                 sell.append((df.index[j], df['Adj Close'][j]))
        #                 break
        #     # Check for sell signal   
        #     elif (df['EMA_20'][i] < df['EMA_50'][i] and df['EMA_20'][i-1] > df['EMA_50'][i-1]) and (df['EMA_20'][i] < df['EMA_200'][i] and df['EMA_20'][i-1] > df['EMA_200'][i-1]) and (df['SMA_20'][i] < df['SMA_50'][i] and df['SMA_20'][i-1] > df['SMA_50'][i-1]) and (df['SMA_20'][i] < df['SMA_200'][i] and df['SMA_20'][i-1] > df['SMA_200'][i-1]):
        #         sell.append((df.index[i], df['Adj Close'][i]))

        # PLOTTING WITH MATPLOTLIB -------------------------------------
        print(df)
        print(f'@@@@@@@@@@{df.columns}@@@@@@@@@@')
        print(df.columns[0])
        
        
        # for timer in df.index.time:
        #     print(timer, "timer")

        # for timer in df.index:
        #     print(timer, "index")
        # filtered_data = df.loc[(df.index.time >= start_time) & (df.index.time <= end_time)]
        print(f'fFFFFFFFFFFFFFFFF {df.index}')
        
        # Specify minimum time gap in nanoseconds. 
        TIME_GAP = 60000000000

        # get an index array where there is a time gap
        gap_idx = np.where(np.diff(df.index.astype(int)) > TIME_GAP)[0]

        df = df.reset_index()

        # use numpy to insert nans
        df = pd.DataFrame(
            columns = df.columns, 
            data = np.insert(df.values, gap_idx+1, values=np.nan, axis=0)
            )

        df = df.set_index('Datetime')

        #Make Graph
        
        # fig = go.Figure()
        fig = make_subplots(rows=1, cols=2)
        fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], mode='lines', name='Asset price'))
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA_20'], mode='lines', name='EMA_20'))
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA_50'], mode='lines', name='EMA_50'))
        fig.add_trace(go.Scatter(x=df.index, y=df['EMA_200'], mode='lines', name='EMA_200'))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], mode='lines', name='SMA_20'))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA_50'))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_200'], mode='lines', name='SMA_200'))
        fig.add_trace(go.Scatter(x=df.index, y=df['BOL_upper'], mode='lines', name='BOL_upper'))
        fig.add_trace(go.Scatter(x=df.index, y=df['STO_slowk'], mode='markers', name='STO_slowk'), row=1, col=2)
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='RSI'), row=1, col=2)
        fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], mode='lines', name='MACD'), row=1, col=2)
        
        # fig.show()


        # fig = px.scatter(df, x=df.index, y=['Adj Close', 'EMA_20', 'EMA_50', 'EMA_200'], title='Moving Average Trading', labels={'x':'Date', 'y':'Price'})
        
        
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=[
                    dict(count=1, label="1m", step="minute", stepmode="todate"),
                    dict(count=1, label="1h", step="hour", stepmode="todate"),
                    dict(count=1, label="1d", step="day", stepmode="todate"),
                    dict(step="all")
                    ]),
                rangebreaks=[
                    dict(bounds=[16, 9.5], pattern="hour"), #hide hours outside of 9am-5pm
                    dict(bounds=["sat", "mon"]), #hide weekends
                    dict(values=["2015-12-25", "2016-01-01"])  # hide Christmas and New Year's
            ]
        )
        
        return fig.show()


if __name__ == '__main__':
    
    average = MovingAverageDayTrading('GOOG', stop_loss=0.03, take_profit=0.15)
    average.moving_average_timeframes()