import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('data.csv')

data = df['reading score'].tolist()

mean = sum(data)/len(data)

std = statistics.stdev(data)

median = statistics.median(data)

mode = statistics.mode(data)

firstStdStart , firstStdEnd = mean - std, mean + std
secondStdStart , secondStdEnd = mean - (2*std), mean + (2*std)
thirdStdStart , thirdStdEnd = mean - (3*std), mean + (3*std)

graph = ff.create_distplot([data], ['reading score'], show_hist = False)

graph.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = 'lines', name = 'mean'))

graph.add_trace(go.Scatter(x = [firstStdStart, firstStdStart], y = [0, 0.17], mode = 'lines', name = 'std1'))
graph.add_trace(go.Scatter(x = [firstStdEnd, firstStdEnd], y = [0, 0.17], mode = 'lines', name = 'std1'))

graph.add_trace(go.Scatter(x = [secondStdStart, secondStdStart], y = [0, 0.17], mode = 'lines', name = 'std2'))
graph.add_trace(go.Scatter(x = [secondStdEnd, secondStdEnd], y = [0, 0.17], mode = 'lines', name = 'std2'))

graph.show()

listofDatawithinfirstStd = [i for i in data if i > firstStdStart and i < firstStdEnd]
listofDatawithinsecondStd = [i for i in data if i > secondStdStart and i < secondStdEnd]
listofDatawithinthirdStd = [i for i in data if i > thirdStdStart and i < thirdStdEnd]

print('Mean of datsa is {}'.format(mean))
print('Median of data is {}'.format(median))
print('Mode of data is {}'.format(mode))
print('Standard Deviation of data is {}'.format(std))
print('{}% of Data Lies Within First Standard Deviation '.format(len(listofDatawithinfirstStd)*100.0/len(diceResult)))
print('{}% of Data Lies Within Second Standard Deviation '.format(len(listofDatawithinsecondStd)*100.0/len(diceResult)))
print('{}% of Data Lies Within Third Standard Deviation '.format(len(listofDatawithinthirdStd)*100.0/len(diceResult)))