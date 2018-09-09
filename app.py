from flask import Flask,render_template,request,redirect
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.embed import components
import quandl
from datetime import datetime, timedelta
import pandas as pd
import bokeh
import os

bv = bokeh.__version__

app = Flask(__name__)

quandl.ApiConfig.api_key = os.environ["QUANDLKEY"]
google_analytics_tracking_id = os.environ["GOOGLE_ANALYTICS_CODE"]


@app.route('/')
def index_start():
    return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():

    a=datetime.now()
    b=datetime.now() - timedelta(365)
    currdate=str(a.year)+'-'+str(a.month)+'-'+str(a.day)
    pastdate=str(b.year)+'-'+str(b.month)+'-'+str(b.day)

    if request.method == 'POST':
        r = request.form['stock_name'].upper()
        data = quandl.get_table('WIKI/PRICES', ticker = str(r), 
                            qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                            date = { 'gte': pastdate, 'lte': currdate }, 
                            paginate=True)
        new=data.set_index('date')
        clean_data = new.pivot(columns='ticker')
        
        clean_data.index=pd.to_datetime(clean_data.index)
        
        p = figure(x_axis_type="datetime", plot_width=500, plot_height=350)
        p.xaxis.axis_label = "Date"
        p.yaxis.axis_label = "Price"
        p.line(clean_data.adj_close.index.name, str(r), source=ColumnDataSource(clean_data.adj_close[pastdate:currdate]))

        script, div = components(p)
        return render_template('display.html', bv=bv,ticker=str(r),script=script, div=div,GANALYTICS_TRACK_ID=google_analytics_tracking_id)
    else:
       #request was a GET 
        return render_template('userinfo.html',GANALYTICS_TRACK_ID=google_analytics_tracking_id)

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html',GANALYTICS_TRACK_ID=google_analytics_tracking_id)

if __name__ == "__main__":
    app.run(port=33507)
