import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv('reviews_courses.csv', parse_dates=['Timestamp'])

data['Month'] = data['TimeStamp'].dt.strftime('%Y - %m')
month_average = data.groupby(['Month']).mean(numeric_only=True)

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: true
  },
  title: {
    text: 'Atmosphere Temperature by Altitude',
    align: 'left'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model',
    align: 'left'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Altitude'
    },
    labels: {
      format: '{value} km'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Temperature'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} | {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Średnia wartość',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]

  }]
}
"""

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(
        a = wp, text = "Analiza ocen kursów", classes = "text-h3 text-center q-pa-md"
    )

    p1 = jp.QDiv(
        a = wp, text = "Poszczególne wykresy z analizą kursów", classes = "text-h4"
    )

    hc = jp.HighCharts(
        a = wp, options = chart_def
    )

# Zmiana tytułu
    hc.options.title.text = "Średnia ocen kursów według MIESIĄCA"
    hc.options.subtitle.text = "Dane z pliku CSV"
  
    list_1 = [1, 2, 3]
    list_2 = [12, 1, 20]

# Zmiana daty
# X axis
    hc.options.xAxis.categories = list(month_average.index)
# Y axis
    hc.options.series[0].data = list(month_average['Rating'])

    return wp

jp.justpy(app)