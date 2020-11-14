import pandas as pd

class Mode:
    CASES = "Cases"
    DEATH = "Deaths"


def load_relevant_data(pak_data=True,mode=Mode.CASES):
    
    # BASE_PATH : 
    
    BASE_PATH = "C:\\Users\\shariq\\OneDrive\\Data Analysis Git\\Pakistan Corona Analysis\\pakistan corona dataset"
    if pak_data and mode == Mode.CASES:
        PATH = BASE_PATH + "\\PK COVID-19.csv"
    elif pak_data and mode == Mode.DEATH:
        PATH = BASE_PATH + "\\PK COVID-19.csv"
    elif not pak_data and mode == Mode.CASES:
        PATH = BASE_PATH + "\\PK COVID-19.csv"
    elif pak_data and mode == Mode.DEATH:
        PATH = BASE_PATH + "\\PK COVID-19.csv"

    return pd.read_csv(PATH)

def get_province_names():
    df = load_relevant_data()
    return df['Province'].unique()

def get_travel_history():
    df = load_relevant_data(pak_data=False)
    return df['Travel_history'].unique()


# travel_history = {'China':'CH', 'Iran/Taftan':'IR', 'Local':"LO", 'Syria':"SY", 'UK':"UK", 'USA':"USA", 'KSA':"KSA",
       'International':"IN", 'Dubai':'DU', 'India':'IN'}


pk_state_abbrev = {'Islamabad Capital Territory':'ISL', 'Sindh':'SND', 'Gilgit-Baltistan':'GB',
       'Baluchistan':"BLH", 'Punjab':"PUN", 'Khyber Pakhtunkhwa':"KP",
       'Azad Jummu Kashmir':'AJK','Federal Administration Tribal Area':'FATA'}


abbrev_pk_state = dict(map(reversed,pk_state_abbrev()))

if __name__ == "__main__":
    print('')
    print('Azad Jummu Kashmir  ', abbrev_pk_state['Azad Jummu Kashmir'] == 'AJK')
    print('Number of entries ', 8 = len(pk_state_abbrev))    