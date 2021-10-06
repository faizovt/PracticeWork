import pandas as pd
import datetime
from hero import *

DateBegin = "30-06-2019"
TimeBegin = "23:31"
TimeEnd = "01:15"

Time1 = datetime.time(hour=17, minute=25)
Time2 = datetime.time(hour=17, minute=35)
mw = 0.25

chem_data = pd.DataFrame({'HEATCUST': 999,
                          'DATETIME': ["23:40","23:58","00:22"],
                          'TEMP': [1569, 1641, None],
                          'VALO2_PPM': [None, 645, None],
                          'VALC': [None, 0.08, 0.06],
                          'VALSI': [None, 0.13, 0.09],
                          'VALMN': [None, 0.02, 0.02],
                          'VALP': [None, 0.1, 0.05],
                          'VALS': [None, 0.11, 0.11],
                          'VALCU': [None, 0.18, 0.18],
                          'VALCR': [-1, 0.048, 0.123],
                          'VALMO': [None, 0.011, 0.006],
                          'VALNI': [0.12, 0.01, 0.01],
                          'VALAS': [None, 0.01, 0.01],
                          'VALSN': [None, 0, 0.01],
                          'VALN': [None, 0.01, 0.01],
                          'VALZN': [None, 0.001, 0.005],
                          })
#chem_data = pd.DataFrame({})



transformer = pd.DataFrame({'STARTTIME': Time2,
                            'DURATION': ["00:10", "00:15", "00:20"],
                            'MW': mw})
#transformer = pd.DataFrame({})
Pipe = ConvertData()
Pipe.set_all(date_begin=DateBegin, time_begin=TimeBegin, time_end=TimeEnd, chem_data=chem_data, transformer=transformer)
print(Pipe.printdata())
Pipe.writedata()
