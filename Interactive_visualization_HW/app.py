import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

class MetaData(db.Model):
    __tablename__ = 'samples_metadata'

    SAMPLEID = db.Column(db.Integer, primary_key=True)
    EVENT = db.Column(db.String)
    ETHNICITY = db.Column(db.String)
    GENDER = db.Column(db.String)
    AGE = db.Column(db.Integer)
    WFREQ = db.Column(db.Integer)
    BBTYPE = db.Column(db.Integer)
    LOCATION = db.Column(db.String)
    COUNTRY012 = db.Column(db.String)
    ZIP012 = db.Column(db.Integer)
    COUNTRY1319 = db.Column(db.String)
    ZIP1319 = db.Column(db.Integer)
    DOG = db.Column(db.String)
    CAT = db.Column(db.String)
    IMPSURFACE013 = db.Column(db.Integer)
    NPP013 = db.Column(db.Integer)
    MMAXTEMP013 = db.Column(db.Integer)
    PFC013 = db.Column(db.Integer)
    IMPSURFACE1319 = db.Column(db.Integer)
    NPP1319 = db.Column(db.Integer)
    MMAXTEMP1319 = db.Column(db.Integer)
    PFC1319 = db.Column(db.Integer)


    def __repr__(self):
        return '<MetaData %r>' % (self.name)

class Otu(db.Model):
    __tablename__ = 'otu'
    
    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxonomic_unit_found = db.Column(db.String)

    def __repr__(self):
        return '<Otu %r>' % (self.name)



class Samples(db.Model):
    __tablename__ = 'samples'

    otu_id = db.Column(db.Integer, primary_key=True)
    BB_940	= db.Column(db.Integer)
    BB_941	= db.Column(db.Integer)
    BB_943	= db.Column(db.Integer)
    BB_944	= db.Column(db.Integer)
    BB_945	= db.Column(db.Integer)
    BB_946	= db.Column(db.Integer)
    BB_947	= db.Column(db.Integer)
    BB_948	= db.Column(db.Integer)
    BB_949	= db.Column(db.Integer)
    BB_950	= db.Column(db.Integer)
    BB_952	= db.Column(db.Integer)
    BB_953	= db.Column(db.Integer)
    BB_954	= db.Column(db.Integer)
    BB_955	= db.Column(db.Integer)
    BB_956	= db.Column(db.Integer)
    BB_958	= db.Column(db.Integer)
    BB_959	= db.Column(db.Integer)
    BB_960	= db.Column(db.Integer)
    BB_961	= db.Column(db.Integer)
    BB_962	= db.Column(db.Integer)
    BB_963	= db.Column(db.Integer)
    BB_964	= db.Column(db.Integer)
    BB_966	= db.Column(db.Integer)
    BB_967	= db.Column(db.Integer)
    BB_968	= db.Column(db.Integer)
    BB_969	= db.Column(db.Integer)
    BB_970	= db.Column(db.Integer)
    BB_971	= db.Column(db.Integer)
    BB_972	= db.Column(db.Integer)
    BB_973	= db.Column(db.Integer)
    BB_974	= db.Column(db.Integer)
    BB_975	= db.Column(db.Integer)
    BB_978	= db.Column(db.Integer)
    BB_1233	= db.Column(db.Integer)
    BB_1234	= db.Column(db.Integer)
    BB_1235	= db.Column(db.Integer)
    BB_1236	= db.Column(db.Integer)
    BB_1237	= db.Column(db.Integer)
    BB_1238	= db.Column(db.Integer)
    BB_1242	= db.Column(db.Integer)
    BB_1243	= db.Column(db.Integer)
    BB_1246	= db.Column(db.Integer)
    BB_1253	= db.Column(db.Integer)
    BB_1254	= db.Column(db.Integer)
    BB_1258	= db.Column(db.Integer)
    BB_1259	= db.Column(db.Integer)
    BB_1260	= db.Column(db.Integer)
    BB_1264	= db.Column(db.Integer)
    BB_1265	= db.Column(db.Integer)
    BB_1273	= db.Column(db.Integer)
    BB_1275	= db.Column(db.Integer)
    BB_1276	= db.Column(db.Integer)
    BB_1277	= db.Column(db.Integer)
    BB_1278	= db.Column(db.Integer)
    BB_1279	= db.Column(db.Integer)
    BB_1280	= db.Column(db.Integer)
    BB_1281	= db.Column(db.Integer)
    BB_1282	= db.Column(db.Integer)
    BB_1283	= db.Column(db.Integer)
    BB_1284	= db.Column(db.Integer)
    BB_1285	= db.Column(db.Integer)
    BB_1286	= db.Column(db.Integer)
    BB_1287	= db.Column(db.Integer)
    BB_1288	= db.Column(db.Integer)
    BB_1289	= db.Column(db.Integer)
    BB_1290	= db.Column(db.Integer)
    BB_1291	= db.Column(db.Integer)
    BB_1292	= db.Column(db.Integer)
    BB_1293	= db.Column(db.Integer)
    BB_1294	= db.Column(db.Integer)
    BB_1295	= db.Column(db.Integer)
    BB_1296	= db.Column(db.Integer)
    BB_1297	= db.Column(db.Integer)
    BB_1298	= db.Column(db.Integer)
    BB_1308	= db.Column(db.Integer)
    BB_1309	= db.Column(db.Integer)
    BB_1310	= db.Column(db.Integer)
    BB_1374	= db.Column(db.Integer)
    BB_1415	= db.Column(db.Integer)
    BB_1439	= db.Column(db.Integer)
    BB_1441	= db.Column(db.Integer)
    BB_1443	= db.Column(db.Integer)
    BB_1486	= db.Column(db.Integer)
    BB_1487	= db.Column(db.Integer)
    BB_1489	= db.Column(db.Integer)
    BB_1490	= db.Column(db.Integer)
    BB_1491	= db.Column(db.Integer)
    BB_1494	= db.Column(db.Integer)
    BB_1495	= db.Column(db.Integer)
    BB_1497	= db.Column(db.Integer)
    BB_1499	= db.Column(db.Integer)
    BB_1500	= db.Column(db.Integer)
    BB_1501	= db.Column(db.Integer)
    BB_1502	= db.Column(db.Integer)
    BB_1503	= db.Column(db.Integer)
    BB_1504	= db.Column(db.Integer)
    BB_1505	= db.Column(db.Integer)
    BB_1506	= db.Column(db.Integer)
    BB_1507	= db.Column(db.Integer)
    BB_1508	= db.Column(db.Integer)
    BB_1510	= db.Column(db.Integer)
    BB_1511	= db.Column(db.Integer)
    BB_1512	= db.Column(db.Integer)
    BB_1513	= db.Column(db.Integer)
    BB_1514	= db.Column(db.Integer)
    BB_1515	= db.Column(db.Integer)
    BB_1516	= db.Column(db.Integer)
    BB_1517	= db.Column(db.Integer)
    BB_1518	= db.Column(db.Integer)
    BB_1519	= db.Column(db.Integer)
    BB_1521	= db.Column(db.Integer)
    BB_1524	= db.Column(db.Integer)
    BB_1526	= db.Column(db.Integer)
    BB_1527	= db.Column(db.Integer)
    BB_1530	= db.Column(db.Integer)
    BB_1531	= db.Column(db.Integer)
    BB_1532	= db.Column(db.Integer)
    BB_1533	= db.Column(db.Integer)
    BB_1534	= db.Column(db.Integer)
    BB_1535	= db.Column(db.Integer)
    BB_1536	= db.Column(db.Integer)
    BB_1537	= db.Column(db.Integer)
    BB_1539	= db.Column(db.Integer)
    BB_1540	= db.Column(db.Integer)
    BB_1541	= db.Column(db.Integer)
    BB_1542	= db.Column(db.Integer)
    BB_1543	= db.Column(db.Integer)
    BB_1544	= db.Column(db.Integer)
    BB_1545	= db.Column(db.Integer)
    BB_1546	= db.Column(db.Integer)
    BB_1547	= db.Column(db.Integer)
    BB_1548	= db.Column(db.Integer)
    BB_1549	= db.Column(db.Integer)
    BB_1550	= db.Column(db.Integer)
    BB_1551	= db.Column(db.Integer)
    BB_1552	= db.Column(db.Integer)
    BB_1553	= db.Column(db.Integer)
    BB_1554	= db.Column(db.Integer)
    BB_1555	= db.Column(db.Integer)
    BB_1556	= db.Column(db.Integer)
    BB_1557	= db.Column(db.Integer)
    BB_1558	= db.Column(db.Integer)
    BB_1561	= db.Column(db.Integer)
    BB_1562	= db.Column(db.Integer)
    BB_1563	= db.Column(db.Integer)
    BB_1564	= db.Column(db.Integer)
    BB_1572	= db.Column(db.Integer)
    BB_1573	= db.Column(db.Integer)
    BB_1574	= db.Column(db.Integer)
    BB_1576	= db.Column(db.Integer)
    BB_1577	= db.Column(db.Integer)
    BB_1581	= db.Column(db.Integer)
    BB_1601	= db.Column(db.Integer)

    def __repr__(self):
        return '<Samples %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():

    db.create_all()

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/names")
def sample_names():

    results = db.session.query(Samples.metadata.tables['samples']).all()

    df1 = pd.DataFrame(results)
    df = df1.columns.values.tolist()
    return jsonify(df)

@app.route("/otu")
def taxid():
    """Return emoji score and emoji char"""


    results = db.session.query(Otu.otu_id, Otu.lowest_taxonomic_unit_found)


    otuid = [result[0] for result in results]
    taxunit = [result[1] for result in results]

    return jsonify(taxunit)


# Add id number to url after metadata to get metadata for ID
@app.route("/metadata/<sample1>")
def meta_data(sample1):
    """Return emoji score and emoji id"""

    
    results = db.session.query(MetaData.SAMPLEID,MetaData.AGE,MetaData.BBTYPE,MetaData.ETHNICITY,MetaData.GENDER,MetaData.LOCATION).filter(MetaData.SAMPLEID == sample1)
    
    meta = []
    
    for result in results:
       meta.append({
        "id" : result[0],
        "age" : result[1],
        "bbtype" : result[2],
        "ethnicity" : result[3],
        "gender" : result[4],
        "location" : result[5]

       })
    return jsonify(meta)

@app.route('/wfreq/<sample2>')
def wfreq(sample2):
     results = db.session.query(MetaData.SAMPLEID,MetaData.WFREQ).filter(MetaData.SAMPLEID == sample2)
    
     wfreq_value = [result[1] for result in results]
    
     return jsonify(wfreq_value)

@app.route('/samples/<sample3>')
def sample_list(sample3):
     results = db.session.query(Samples.metadata.tables['samples']).all()
    
     results_df = pd.DataFrame(results)

     result_filter = results_df[['otu_id',sample3]]
     results_2 = result_filter[result_filter[sample3] > 0]
     test = results_2.sort_values(sample3, ascending=False)
     top10 = test.head(10)

     idlist = top10[sample3].tolist()
     otulist = top10['otu_id'].tolist()
     
    # Format the data for Plotly
     plot_trace = [{
            "values": idlist,
            "labels": otulist,
            "type": 'pie'
     }]
   
     return jsonify(plot_trace)

    #  list_dict = {
    #     "otu_ids" : otulist,
    #     "sample_values": idlist

    #  }
    
    #  return jsonify(list_dict)



if __name__ == '__main__':
    app.run(debug=True)
