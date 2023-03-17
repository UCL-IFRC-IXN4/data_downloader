import os
import requests
import pandas as pd

os.chdir('data')


front_url = "https://www.desinventar.net/DesInventar/report_spreadsheet.jsp?bookmark=1&countrycode="
back_url = "&maxhits=100&lang=EN&frompage=/definestats.jsp&bSum=Y&_stat=fichas.fechano&nlevels=1&_variables=1,fichas.evento,fichas.fechano,fichas.fechames,fichas.fechadia,fichas.muertos,fichas.heridos,fichas.desaparece,fichas.damnificados,fichas.afectados,fichas.reubicados,fichas.evacuados,fichas.valorus,fichas.valorloc"
back_url_pac = "&maxhits=100&lang=EN&frompage=/definestats.jsp&bSum=Y&_stat=fichas.fechano&nlevels=1&_variables=1,fichas.evento,lev0_name_en,lev0_cod,fichas.fechano,fichas.fechames,fichas.fechadia,fichas.muertos,fichas.heridos,fichas.desaparece,fichas.damnificados,fichas.afectados,fichas.reubicados,fichas.evacuados,fichas.valorus,fichas.valorloc"


country_codes = ['alb','ago','atg','arg','brb','blz','btn','bol','bfa','khm','chl','col','com','cri','dji','dma','dom','ecu','egy','slv','gnq','swz','eth','gmb','gha','grd','gtm','gin','gnb','guy',
                'hnd','ng_oy','idn','irq','irn','jam','jor','ken','xkx','lao','lbn','lbr','mdg','mwi','mdv','mli','mus','mex','mng','mne','mar','moz','mmr','npl','nic','ner','019','pac','pak',
                'pse','pan','pry','per','rwa','kna','lca','vct','sen','srb','syc','sle','esp','lka','syr','033','tls','tgo','tto','tun','tur','uga','tza','ury','005','ven','vnm','yem','zmb']

col = ["Serial","Event","Year","Month","Day","Deaths","Injured","Missing","Directly Affected","Indirectly Affected","Relocated","Evacuated","Losses (USD)","Losses (Local)",'na']
col_pac = ["Serial","Event","Country","Country Code","Year","Month","Day","Deaths","Injured","Missing","Directly Affected","Indirectly Affected","Relocated","Evacuated","Losses (USD)","Losses (Local)",'na']

def get_csv(country_code):
    if country_code == 'pac':
        url = front_url + "pac" + back_url_pac
    else:
        url = front_url + country_code + back_url

    r = requests.get(url, allow_redirects = True)
    file_name = country_code + '.xls'
    open(file_name, 'wb').write(r.content)
    os.rename(file_name, country_code + '.csv')

def clean_col(country_code):
    df = pd.read_csv(country_code + ".csv",on_bad_lines='skip',skiprows = 4, sep = '\t')

    df.drop("DataCards", inplace=True, axis=1)
    if country_code == 'pac':
        df.columns = col_pac
    else:
        df.columns = col
    
    # merge columns [Year,Month,Day] into single column [Date (YMD)]
    day_ind = df.columns.get_loc("Day")	
    df.insert(day_ind+1,"Date (YMD)","NA")
    for i in range(len(df)):
        df.iloc[i,day_ind+1] = str(df.iloc[i,day_ind-2]) + '/' + str(df.iloc[i,day_ind-1]) + '/' + str(df.iloc[i,day_ind]) 
    df.drop("Year", inplace=True, axis=1)
    df.drop("Month", inplace=True, axis=1)
    df.drop("Day", inplace=True, axis=1)

    df.drop("na", inplace=True, axis=1)

    #print(df.head())
    df.to_csv(country_code + ".csv")

for country_code in country_codes:
    get_csv(country_code)
    clean_col(country_code)








