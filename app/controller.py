import pandas as pd
import gc

gc.enable


class query():
    def queryterm(self, fname, mname, lname):
        indata = pd.read_csv('data.csv', engine='python')
        indata = indata.drop(['Unnamed: 3', 'Unnamed: 4'], axis=1)

    # print(type(indata), type(tempdata))
        if indata['firstName'].str.contains(fname).any() or indata['middleName'].str.contains(mname).any() or indata['lastName'].str.contains(lname).any():
        
            tempdata = indata[indata['firstName'].str.contains(fname, na=False, case = False)].dropna(thresh=2)
            # print(tempdata)

            return tempdata