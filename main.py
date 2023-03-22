import os
import requests
import pandas as pd
import string

os.chdir('data')


front_url = "https://www.desinventar.net/DesInventar/report_spreadsheet.jsp?bookmark=1&countrycode="
back_url = "&maxhits=100&lang=EN&frompage=/definestats.jsp&bSum=Y&_stat=fichas.fechano&nlevels=1&_variables=1,fichas.evento,fichas.fechano,fichas.fechames,fichas.fechadia,fichas.muertos,fichas.heridos,fichas.desaparece,fichas.damnificados,fichas.afectados,fichas.reubicados,fichas.evacuados,fichas.valorus,fichas.valorloc"
back_url_pac = "&maxhits=100&lang=EN&frompage=/definestats.jsp&bSum=Y&_stat=fichas.fechano&nlevels=1&_variables=1,fichas.evento,lev0_name_en,lev0_cod,fichas.fechano,fichas.fechames,fichas.fechadia,fichas.muertos,fichas.heridos,fichas.desaparece,fichas.damnificados,fichas.afectados,fichas.reubicados,fichas.evacuados,fichas.valorus,fichas.valorloc"


country_codes = ['alb','ago','atg','arg','brb','blz','btn','bol','bfa','khm','chl','col','com','cri','dji','dma','dom','ecu','egy','slv','gnq','swz','eth','gmb','gha','grd','gtm','gin','gnb','guy',
                'hnd','ng_oy','idn','irq','irn','jam','jor','ken','xkx','lao','lbn','lbr','mdg','mwi','mdv','mli','mus','mex','mng','mne','mar','moz','mmr','npl','nic','ner','019','pac','pak',
                'pse','pan','pry','per','rwa','kna','lca','vct','sen','srb','syc','sle','esp','lka','syr','033','tls','tgo','tto','tun','tur','uga','tza','ury','005','ven','vnm','yem','zmb']

col = ["Serial","Type","Year","Month","Day","Deaths","Injured","Missing","Directly Affected","Indirectly Affected","Relocated","Evacuated","Losses (USD)","Losses (Local)",'na']
col_pac = ["Serial","Type","Country","Country Code","Year","Month","Day","Deaths","Injured","Missing","Directly Affected","Indirectly Affected","Relocated","Evacuated","Losses (USD)","Losses (Local)",'na']

def get_csv(country_code):

    # generate url (pac needs country column)
    if country_code == 'pac':
        url = front_url + "pac" + back_url_pac
    else:
        url = front_url + country_code + back_url


    # 'get' url with requests library
    r = requests.get(url, allow_redirects = True)

    # save content with name 
    file_name = country_code + '.xls'
    open(file_name, 'wb').write(r.content)

    # convert to .csv file
    os.rename(file_name, country_code + '.csv')

def clean_col(country_code):

    # put into pandas dataframe
    df = pd.read_csv(country_code + ".csv",on_bad_lines='skip',skiprows = 4, sep = '\t')

    # remove unecessary column
    df.drop("DataCards", inplace=True, axis=1)

    # rename columns
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

    # remove unecessary column
    df.drop("na", inplace=True, axis=1)

    #update csv file with new dataframe
    df.to_csv(country_code + ".csv")


def translate_file(country_code):

    # put csv into dataframe
    df = pd.read_csv(country_code + ".csv",on_bad_lines='skip')

    # change dir
    os.chdir('..')
    os.chdir('transl_dict')

    type_ind = df.columns.get_loc("Type")

    # iterate through .csv files to translate all strings under "Type"
    for i in range(len(df)):

        # see if type is made up of latin alphabets
        # initialise translation dataframe from /transl_dict/ based on first letter/language
        first_char = str(df.iloc[i,type_ind])[0]
        if first_char in list(string.ascii_letters):
            first_char = first_char.lower()
            df_transl = pd.read_csv(first_char + ".csv",on_bad_lines='skip')
        else:
            df_transl = pd.read_csv('not_lat.csv',on_bad_lines='skip')

        # iterate through translation dataframe to see if there are matches for the disaster type in a different language
        # if yes, swap with English translation
        for j in range(len(df_transl)):
            if df_transl.iloc[j,0] == df.iloc[i,type_ind]:
                df.iloc[i,type_ind] = df_transl.iloc[j,1]
                break


    # change back dir + push dataframe to csv file
    os.chdir('..')
    os.chdir('data')
    df.to_csv(country_code + ".csv")





for country_code in country_codes:
    get_csv(country_code)
    clean_col(country_code)
    translate_file(country_code)


# 18mins 

# comment

