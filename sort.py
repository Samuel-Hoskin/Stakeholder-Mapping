import pandas as pd

path = "data.csv"

df = pd.read_csv(path)



for i in range(len(df)):

   

    if df.loc[i,'Influence'] <= 2:

        if df.loc[i,'Interest'] <= 2:

            df.loc[i,'Style'] = 'Ignore'

        else:

            df.loc[i,'Style'] = 'Keep Informed'

   

    elif df.loc[i,'Influence'] <= 3.5:

        df.loc[i,'Style'] = 'Keep Onside'

       

    else:

        if df.loc[i,'Interest'] <= 2:

            df.loc[i,'Style'] = 'Watch'

        elif df.loc[i,'Interest'] <= 3.5:

            df.loc[i,'Style'] = 'Keep Satisfied'

        else:

            df.loc[i,'Style'] = 'Constant Active Management'


df.to_csv('data.csv', index=False)