# import pandas as pd
import pandas as pd


# Import CSV into Pandas Dataframe and resolve mixed datatype errors
data = pd.read_csv("Building_Permits.csv", low_memory=False)
print(data.describe())

