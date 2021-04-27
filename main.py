import sys
from statistics import mean, median
import pandas as pd


class Data():
    def __init__(self, path):
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
        flat_list = []
        for sublist in list_of_districts:
            for item in sublist:
                flat_list.append(item)
        return(flat_list)

    def set_districts_data(self, districts):
        rows = districts
        right_districts = self.df.loc[self.df['denominazione_region'].isin(rows)]
        right_districts = right_districts.values
        file = open("data.py", "w")
        file.write(str(right_districts))
        file.close()



class districts(Data):
    def __init__(self, path):
        self.dataset = Data(path)
        Data.__init__(self,path)

    def filter_districts(self, letters):
        all_dist = self.dataset.get_all_districts()
        sorted_dist = sorted(all_dist)
        sorted_dist = list(dict.fromkeys(sorted_dist))
        list_to_use = []
        for i in sorted_dist:
            indi = 0
            for j in letters:
                if i[0] == j:
                    indi = 1
                else:
                    continue
            if indi == 1:
                list_to_use.append(i)
                continue
            else:
                continue
        self.dataset.set_districts_data(list_to_use)

    def print_details(self, features, statistic_functions):
        list1 = self.df
        print("Question 1:")
        for fea in features:
            curr_mean = statistic_functions[0](list1[fea])
            curr_median = statistic_functions[1](list1[fea])
            print(fea + ":" + " " + str(curr_mean) + ", " + str(curr_median))

    def determine_day_type(self):
        a_dict = self.df
        a_dict['day_type'] = 0
        val_healed = (a_dict['resigned_healed']).values
        val_got_sick = (a_dict['new_positives']).values
        length = len(val_healed)
        place = 0
        for i in range(length):
            if (val_healed[i]) > (val_got_sick[i]):
                a_dict.loc[i, "day_type"] = 1
            else:
                continue
            place = place + 1
        return a_dict



def main(argv):
#    path = sys.argv[1]
    statistic_functions = [mean, median]
    features = ['hospitalized_with_symptoms', 'intensive_care', 'total_hospitalized', 'home_insulation']
    our_districts = ['Calabria','Lombardia', 'Umbria', 'Veneto']
    letters = {'T', 'C', 'L', 'U'}
    path = 'C:\\Users\Yael\Documents\intro_to_DS\hw2\dpc-covid19-ita-regioni.csv'
    data1 = Data(path)
    data1.load_data()
    data1.get_all_districts()
    data1.set_districts_data(our_districts)
    dist1 = districts(path)
    dist1.filter_districts(letters)
    dist1.print_details(features, statistic_functions)
    dist1.determine_day_type()






if __name__ == '__main__':
    main(sys.argv)

