import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# local files 
from helper import Mode,abbrev_pk_state,load_relevant_data 

TEST_DATE = ['2/26/2020', '2/29/2020', '3/2/2020', '3/6/2020', '3/7/2020',
       '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020',
       '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020',
       '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020',
       '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020',
       '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020',
       '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020',
       '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020',
       '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020',
       '4/19/2020']

def plot_daily_count_states(states =['Islamabad Capital Territory', 'Sindh', 'Gilgit-Baltistan',
                                    'Baluchistan', 'Punjab', 'Khyber Pakhtunkhwa',
                                    'Azad Jummu Kashmir', 'Federal Administration Tribal Area'],
                                    day = TEST_DATE,
                                    mode = Mode.CASES,filename = None  ):
                                    COLUMN = "Province"
                                    df = load_relevant_data(False,mode).groupby(COLUMN).sum().reset_index()
                                    plot_data(df,states,day,mode,COLUMN,filename)


def plot_travel_history(Travel_history = ['Travel_history'],day = TEST_DATE,mode = Mode.CASES,filename = None):
    COLUMN = 'Travel_history'
    df = load_relevant_data(False,mode).groupby(COLUMN).sum().reset_index()
    plot_data(df,states,day,mode,COLUMN,filename)
    

def plot_data(df,places,day,mode,column,filename):
    n = len(places)
    color = plt.cm.Reds(np.linspace(0.35,0.65,n))

    values = []
    for index,place in enumerate(places):
        cumulative_data = df[df[column] == places]
        start_column = cumulative_data.column.get_loc('4/19/2020')
        counts = cumulative_data.iloc[:,start_column:].diff(axis = 1)
        values.append(int(counts[day]))

    plt.bar(places,values,color = colors)
    label_figure(day,mode,filename)


def label_figure(day,mode,filename):
    plt.title(f'{mode},{dau}')
    plt.ylabel(f"{mode}")
    filename  = filename if filename else f'{mode}_{day.replace("/","-")}.png'
    plt.savefig(filename)
    plt.close()