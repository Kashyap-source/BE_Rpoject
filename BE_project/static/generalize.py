import pandas as pd
import math

hb = pd.read_csv('../haberman.csv', header=None)
hb.columns = ['Age', 'Year of Operation', 'No of Positive Nodes', 'Survival']
cols = hb.columns.values
def employ_generalization(d, attr, hb):


    di = {}
    for i in range(d):
        di[i+1] = []
        split = 0
        c = 0
    for i in range(d):
        lower_bound = hb[attr].min() + math.ceil(split)
        di[i+1].append(lower_bound)
        split += ( hb[attr].max() - hb[attr].min() )/ d
        di[i+1].append(math.ceil(hb[attr].min() + split))
        split += 1

    return di

def generalize(d, attr, data):
    di = employ_generalization(d, attr, data)
    print(di)
    data.reset_index(inplace=True, drop=True)
    for i in range(len(data[attr])):
        val = data[attr].loc[i]

        for k in di:
            if val >= di[k][0] and val <= di[k][1]:
                if abs(val-di[k][0]) < abs(val-di[k][1]):
                    data[attr].loc[i] = di[k][0]
                else:
                    data[attr].loc[i] = di[k][1]
                    break
    return data[attr]


l = []
for i in range(len(cols)-1):
    attr = generalize(2, cols[i], hb)
    l.append(attr)


generalized_haberman = pd.DataFrame(l)
generalized_haberman_trans = generalized_haberman.T
generalized_haberman_trans['Survival'] = hb.Survival
generalized_haberman_trans.to_csv("Generalized Haberman.csv")
