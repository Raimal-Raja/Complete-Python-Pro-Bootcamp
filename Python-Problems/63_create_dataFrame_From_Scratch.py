import pandas as pd
data_dic = {
    'students':["Raimal","Raja",'Kolhi'],
    'score':[78,98,99]
}

data = pd.DataFrame(data_dic)
data.to_csv(r'C:\Users\Professor\Desktop\Complete-Python-Pro-Bootcamp\Complete-Python-Pro-Bootcamp\Python-Problems\dataFrame.csv')