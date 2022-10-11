
from pandas import read_csv
url='diabetes_dataset.csv'
data=read_csv(url)
colnames=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
print (data.shape)
