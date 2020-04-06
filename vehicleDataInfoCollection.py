import csv
import numpy as np
import pandas as pd
import tkinter as tk

#import gmaps
#import googlemaps
#import datetime as dt
df = pd.read_csv('vehicles.csv')
df.year.apply(str)
finaldf = df
a = []
b = []
c = []
with open('MassachusettsEE1.csv', newline='') as csvfile:
	spamreader = csv.DictReader(csvfile)
	for row in spamreader:
		a.append(row['Address'])
		b.append(row['ZipFinal'])
		c.append((row['Address'],row['ZipFinal']))
	ab = np.array(c)
	print(ab[0,0])
	print(ab[0,1])
	#directions_results[]
	#for i in ab
		#directions_driving[i] = gmaps.directions(ab[i,0],ab[i,1],mode="driving",arrival_time=dt.datetime(2020,09,11,9,0)
		#directions_transit[i] = gmaps.directions(ab[i,0],ab[i,1],mode="transit",arrival_time=dt.datetime(2020,09,11,9,0)
		#directions_bicycling[i] = gmaps.directions(ab[i,0],ab[i,1],mode="bicycling",arrival_time=dt.datetime(2020,09,11,9,0)
		#directions_walking[i] = gmaps.directions(ab[i,0],ab[i,1],mode="walking",arrival_time=dt.datetime(2020,09,11,9,0)
	#print(ab.ndim)
	
	
	
	#asfd = np.hstack((a,b))
	#AB = np.hstack((aa,bb))
	#print(np.hstack((aa,bb)))
	#for rows in a:
	#	print(a)
	csvfile.close









root = tk.Tk()
root.title("Vehicle Selection")

mainframe = tk.Frame(root)
mainframe.grid(column=0,row=0, sticky=(tk.N,tk.W,tk.E,tk.S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkMake = tk.StringVar(root)
tkModel = tk.StringVar(root)
tkYear = tk.StringVar(root)
userVehicle = tk.StringVar(root)
tkStartZip = tk.StringVar(root)
tkEndLoc = tk.StringVar(root)

tkMakeChoice = sorted(df.make.unique())
tkModelChoice = sorted(df.model.unique())	
tkYearChoice = sorted(df.year.unique())
finalChoice = []
s=[]
passDict = {}
#print("old year list: ", tkYearChoice)

def doneButton():
	print('making final dataframe')
	
	print( tkMake.get() )
	df1 = df.query('make == @tkMake.get() ')
	print( tkModel.get() )
	df2 = df1.query('model == @tkModel.get() ')
	print( tkYear.get() )
	df3 = df2.query('year == @tkYear.get() ')
	df4 = df3.query('mpgData == "Y"')
	index = 0
	# print(df3)
	#finaldf = df.query('make == @tkMake & model == @tkModel & year == @tkYear')
	finaldf = df4[['displ','cylinders','trany','fuelType']]
	for row in finaldf.itertuples(index=False,name='Printables'): #index=False
		print(row)
		finalChoice.append(row)
		print()
		print()
		#print(finalChoice[0].Index)
		print(finalChoice[0].displ)
	print('***************************')
	# for i in finalChoice:
		# s[i]=(finalChoice[i].displ+'L. '+finalChoice[i].cylinders+' cylinders '+finalChoice[i].trany+' '+finalChoice[i].fuelType)
	if not finalChoice:
		print('no options!')
	#print(finalChoice[1],'Liters ',finalChoice[2],' cylinders',finalChoice[3],finalChoice[4])
	# print(finaldf)
	# printdf = finaldf.to_string
	# print(printdf)
	#print(printdf.to_string)
	##apply printdf.groupby to list the remainings into last user selection.
	##after picking last option, gather relevant mpg data (if possible)
	##NEW WINDOW
	##apply mpg data to chosen user zipcode (enterable)
	##plot driving route, calculate mpg
	
	popupMenu4 = tk.OptionMenu(mainframe, userVehicle, *finalChoice)
	tk.Label(mainframe, text="Found vehicles with MPG data! Make your final selection based on your engine displacement in liters, number of cylinders, transmission and fuel type:").grid(row = 3, column = 2)
	popupMenu4.grid(row = 4, column =2)

popupMenu1 = tk.OptionMenu(mainframe, tkMake, *tkMakeChoice)
tk.Label(mainframe, text="Choose vehicle make").grid(row = 1, column = 1)
popupMenu1.grid(row = 2, column =1)
B = tk.Button(root, text="Done", command=doneButton, state='disabled')


#callbacks on change dropdown value
def change_make_dropdown(*args):
	print( tkMake.get() )
	newdf1 = df.query('make == @tkMake.get()')
	#print(newdf1)
	tkModelChoice = sorted(newdf1.model.unique())
	
	popupMenu2 = tk.OptionMenu(mainframe, tkModel, *tkModelChoice)
	tk.Label(mainframe, text="Choose vehicle model").grid(row = 1, column = 2)
	popupMenu2.grid(row = 2, column =2)
	#adjust_model_dropdown(tkMake.get())
	
def change_model_dropdown(*args):
	print( tkModel.get() )
	newdf2 = df.query('make == @tkMake.get() & model == @tkModel.get()')
	#print(newdf2)
	tkYearChoice = sorted(newdf2.year.unique())
	#print("new year list: ", tkYearChoice)
	
	popupMenu3 = tk.OptionMenu(mainframe, tkYear, *tkYearChoice)
	tk.Label(mainframe, text="Choose vehicle year").grid(row = 1, column = 3)
	popupMenu3.grid(row = 2, column =3)
	
def change_year_dropdown(*args):
	print( tkYear.get() )
	# newdf3 = df.query('make == @tkMake.get() & model == @tkModel.get() & year == @tkYear.get()')
	B['state']='normal'
	# finaldf = newdf3
	# df = pd.read_csv('vehicles.csv')

def final_pick_dropdown(*args):
	s = userVehicle.get()[1:-1]
	print( s )
	g = s.split(', ')
	print('premod: ',g)
	g[2] = g[2][1:-1]
	g[3] = g[3][1:-1]
	print('postmod: ',g)
	
	df1 = df.query('make == @tkMake.get() ')
	df2 = df1.query('model == @tkModel.get() ')
	df3 = df2.query('year == @tkYear.get() ')
	df4 = df3.query('mpgData == "Y"')
	df5 = df4.query('displ == @g[0] ')
	df6 = df5.query('cylinders == @g[1] ')
	df7 = df6.query('trany == @g[2] ')
	df8 = df7.query('fuelType == @g[3] ')
	print('END RESULT: ', df8)
	mapStart(df8)
	#finaldf = df4[['displ','cylinders','trany','fuelType']]
def mapStart(vehicleDataFrame):
	#createNewWindow()
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()
	
	popupMenu5 = tk.OptionMenu(newWindow, tkModel, *tkModelChoice)
	tk.Label(mainframe, text="Choose vehicle model").grid(row = 1, column = 2)
	popupMenu5.grid(row = 2, column =2)
	
	
# link function to change dropdown
tkMake.trace('w', change_make_dropdown)
tkModel.trace('w', change_model_dropdown)
tkYear.trace('w', change_year_dropdown)
userVehicle.trace('w', final_pick_dropdown)

# def refresh():
	# popupMenu1['menu'].delete(0, 'end)
	# popupMenu1['menu'].delete(0, 'end)
	# popupMenu1['menu'].delete(0, 'end)
#with open('APIkey.txt') as f:
#    apiKey = f.readline()
#    f.close
#gmaps = googlemaps.Client(key=apiKey)

#data1 = np.genfromtxt('MassachusettsEE.csv', delimiter = ',')


#newdf = df.query('make=="Honda"')
#print(df)
#print(newdf)
B.pack()
root.mainloop()
# create dictionaries
#makes, models,
