import pandas
data = pandas.read_csv('example_csv.csv',index_col=0)
print(data)
data = data.drop(columns=['城市'])
print(data)
data['sum']=data['年龄']+data['数字']
print(data)