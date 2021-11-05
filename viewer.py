import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go
import yfinance as yf

input_string = input("Enter stock symbol separated by space")
bruh = input_string.split()
for stock in bruh:
  try:
    name = yf.Ticker(stock).info['shortName']
  except:
    print(f"{stock.upper()} - Stock doesn't exist, skipped.")
    continue

  df = yf.download(stock, start='2021-04-01')
  df.to_csv('test.csv')

  trace1 = {
      'x': df.index,
      'open': df.Open,
      'close': df.Close,
      'high': df.High,
      'low': df.Low,
      'type': 'candlestick',
      'name': stock.upper(),
      'showlegend': False
  }

  # Calculate and define moving average of 30 periods
  avg_20 = df.Close.rolling(window=20, min_periods=1).mean()

  # Calculate and define moving average of 50 periods
  avg_50 = df.Close.rolling(window=50, min_periods=1).mean()

  # Calculate and define moving average of 50 periods
  avg_200 = df.Close.rolling(window=200, min_periods=1).mean()


  trace2 = {
      'x': df.index,
      'y': avg_20,
      'type': 'scatter',
      'mode': 'lines',
      'line': {
          'width': 1,
          'color': 'red'
              },
      'name': '20MA'
  }


  trace3 = {
      'x': df.index,
      'y': avg_50,
      'type': 'scatter',
      'mode': 'lines',
      'line': {
          'width': 1,
          'color': 'blue'
      },
      'name': '50MA'
  }

  trace4 = {
      'x': df.index,
      'y': avg_200,
      'type': 'scatter',
      'mode': 'lines',
      'line': {
          'width': 1,
          'color': 'green'
      },
      'name': '200MA'
  }

  data = [trace1, trace2, trace3,trace4]
  # Config graph layout
  layout = go.Layout({
      'title': {
          'text': f'{stock}',
          'font': {
              'size': 15
          }
      }
  })


  fig = go.Figure(data=data, layout=layout)
  fig.update_layout(title_text=f"{name}({stock.upper()})")
  fig.show()
