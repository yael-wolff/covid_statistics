import sys
from statistics import mean, median
import pandas as pd


class Data():
    def __init__(self, path, ):
        self.path = path
        df = pd.read_csv(path)
        self.df = df
        self.data = df.to_dict(orient='list')

    def load_data(self):
        dictionary_data = self.data
        file = open("data.py", "w")
        file.write(str(dictionary_data))
        file.close()

    def get_all_districts(self):
        columns = ['denominazione_region']
        list_of_districts = pd.DataFrame(self.df, columns=columns)
        list_of_districts = list_of_districts.values
        return(list_of_districts)

    def set_districts_data(self, districts):
        rows = districts
        right_districts = pd.DataFrame(self.df, index=rows)
        file = open("data.py", "w")
        file.write(str(right_districts))
        file.close()





def main(argv):
#    path = sys.argv[1]
    districts = ['Calabria', 'Umbria', 'Veneto']
    path = 'C:\\Users\Yael\Documents\intro_to_DS\hw2\dpc-covid19-ita-regioni.csv'
    data1 = Data(path)
    data1.load_data()
    data1.get_all_districts()
    data1.set_districts_data(districts)






if __name__ == '__main__':
    main(sys.argv)

#C://Users/Yael/Documents/intro_to_DS/hw2/main.py