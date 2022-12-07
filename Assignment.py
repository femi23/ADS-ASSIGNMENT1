import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading the file from Panda
data = pd.read_csv('https://covid19.who.int/who-data/vaccination-data.csv')
data.head()
print(data)

#convert DATE_UPDATED Column to month/Group the data by month.
data['DATE_UPDATED'] = pd.to_datetime(data['DATE_UPDATED'])
data['month'] = pd.DatetimeIndex(data['DATE_UPDATED']).month
vaccination = data.groupby(['month'])[['TOTAL_VACCINATIONS', 'PERSONS_FULLY_VACCINATED','PERSONS_VACCINATED_1PLUS_DOSE']].sum()#.sort_values()
vaccination['month'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']

#conversion of PERSONS_FULLY_VACCINATED/1000 on y-axis for proper visualisation of the graph.
vaccination['fully_vaccinated_by_1m'] = vaccination['PERSONS_FULLY_VACCINATED']/1000000
print(vaccination['fully_vaccinated_by_1m'])

#conversion of PERSONS_VACCINATED_1PLUS_DOSE/1000 on y-axis for proper visualisation on the graph.
vaccination['persons_vaccinated_1plus_dose_by_1m'] = vaccination['PERSONS_VACCINATED_1PLUS_DOSE']/1000000
print(vaccination['persons_vaccinated_1plus_dose_by_1m'])


#Define a function called plt_barchart showing the distributon of Person fully Vaccinated and Persons Vaccinated by at least one dose by Month.
def plt_plotline(month, vac, label, color, xaxis, yaxis, title):
    """
    Constructs all the necessary attributes for the line plot.
    name : x-axis
               month of vaccinations on x-axis
          vac : y-axis
               fully_vaccinated_by_1m and persons_vaccinated_1plus_dose_by_1m
          label : 
              x-axis = fully_vaccinated_by_1m, y-axis = persons_vaccinated_1plus_dose_by_1m
          color :
              used to identify my line plots
          xaxis:
              showing covid-19 vaccination updates by months in 2022
          y-axis:
              showing covid-19 vaccination figures in millions.
          title:
              shows the graph title
    returns the value as line plot
    """
    plt.figure(figsize=(12, 7), dpi=80)
    plt.title(title, fontsize=16)
    for i in range(len(vac)):
        plt.plot(month, vac[i], label=label[i], color=color[i])            
    plt.xlabel(xaxis, fontweight ='bold', fontsize = 12)
    plt.ylabel(yaxis, fontweight ='bold', fontsize = 12)    
    plt.legend(loc='best') 
    plt.savefig('Lineplot.png')
    plt.show()    
    return

#declaring variables for my line plot functions.
month = vaccination['month']
vac = [vaccination['fully_vaccinated_by_1m'],vaccination['persons_vaccinated_1plus_dose_by_1m']] 
label = ["fully_vaccinated", "persons_vaccinated at least one dose"]
color = ['red','blue']
x_label = 'Months(Date last Updated)'
y_label = 'Vaccination_in_1million'
title = 'COVID-19 VACCINATION AROUND THE WORLD'

#line plot showing the distributon of Person fully Vaccinated/persons Vaccinated by at least one dose by Month.
plt_plotline(month, vac, label, color, x_label, y_label, title)


#Grouping data by region showing the distribrution of Total vaccination by Region
region_group = data.groupby('WHO_REGION')[['TOTAL_VACCINATIONS', 'PERSONS_FULLY_VACCINATED', 'PERSONS_VACCINATED_1PLUS_DOSE']].sum()
region_group = region_group.rename_axis('WHO_REGION').reset_index()
print(region_group)

#conversion of TOTAL_VACCINATIONS on y-axis for proper visualisation of the graph.
region_group ['total_vaccination_by_1m'] = region_group['TOTAL_VACCINATIONS']/1000000
print(region_group ['total_vaccination_by_1m'])


#Define a function called plt_barchart and call it to plot a Barchart
def barchart(region, vaccination, xlabel, ylabel, label, color, title):
    """
    Constructs all the necessary attributes for the Bar Chart.
          region : x-axis
               WHO regions grouped on on x-axis
          vaccination : y-axis
               TOTAL_VACCINATIONS
          xaxis:
              showing distribution of covid-19 vaccination in regions
          y-axis:
              showing covid-19 vaccination figures in millions.
            label : 
              showing covid-19 region interpretations.
          color :
              used to uniquely identify the regions
          
          title:
              shows the graph title.
         returns the value as line plot
    """
    plt.figure(figsize=(15,10))
    plt.title(title, fontsize=20)
    for i in range(len(region)):
        
        plt.bar(region[i], vaccination[i],label=label[i],color = color[i])        
        plt.xlabel(xlabel, fontweight ='bold', fontsize = 18)
        plt.ylabel(ylabel, fontweight ='bold', fontsize = 18)
        plt.legend(fontsize=20)
    plt.savefig('Barchart.png')
    plt.show()    
    return

#declaring variables for my functions.
region = region_group['WHO_REGION']
vaccination = region_group['total_vaccination_by_1m']
xlabel = 'WHO_REGIONS' 
ylabel = 'Vaccination_in_1million'
label =['Africa', 'Region of Americas', 'Eastern Med Region', 'European Region', 'OTHER', 'South-East Asia Region','Western Pacific Region']
color = ['red', 'green', 'purple', 'yellow', 'violet', 'pink', 'orange', 'blue']
title = 'Total vaccine doses administered by Region'

#Barchat showing the distributon of Total Vaccination by region
barchart(region, vaccination, xlabel, ylabel,label,color, title)

#Define a function called plt_piechart and call it to plot a Piechart 
def piechart(dataset, explode, labels, title):
    """
    Constructs all the necessary attributes for the Pie Chart.
          dataset : 
               Showing the distribution of persons vaccinated with at least one dose.
          vaccination : y-axis
               TOTAL_VACCINATIONS
          explode:
              showing distribution of a subset of a pie
            label : 
              showing covid-19 region interpretations.
          color :
              used to uniquely identify the regions
          
          title:
              shows the graph title.
         returns the value as line plot
    """
    
    plt.figure(figsize=(12,9))
    plt.pie(dataset,explode, labels=labels, autopct='%2.4f%%')
    plt.title(title, fontsize=16)
    plt.legend(loc='lower left', fontsize=10)
    plt.savefig('Piechart.png')
    plt.show()
    return

#declaring variables for the functions
dataset = region_group['PERSONS_VACCINATED_1PLUS_DOSE']
labels = ['Africa', 'Region of Americas', 'Eastern Med Region', 'European Region', 'OTHER', 'South-East Asia Region','Western Pacific Region']
title = 'Persons vaccinated with at least one dose across the Regions'
explode = 0.2,0,0,0,0,0,0

#piechat showing the distributon of Persons_vaccinated by at least one dose by region.
piechart(dataset, explode, labels, title)





