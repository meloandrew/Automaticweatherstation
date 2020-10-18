import pandas as pd

class DataProcessing():
    def __init__(self):
        super().__init__()

    def Run(self, raw_data) -> dict:
        table: pd.DataFrame = pd.DataFrame(raw_data, dtype = "float64")
        
        if table is None:
            return {}
        
        table = table.drop(table.columns[[0, 1, 6]], axis=1)

        table = table.rename(columns = {
            'field1': "Temp", 
            "field2": "Hum", 
            "field3": "Press", 
            "field4":"Wind"
            }, 
            inplace = False)
        
        agg_table = pd.DataFrame(table.agg("mean", axis="rows")).T

        return agg_table
    pass