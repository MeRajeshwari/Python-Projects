import pandas as pd

full_student_data = pd.read_csv("studata.csv", header=0, sep=",")

Corr_Matrix = round(full_student_data.corr(),2)

print(Corr_Matrix)
    