import random
inp=[["Bangalore","Bangalore",0],	["Bangalore","Hyderabad",569],	["Bangalore","Kochi",547],	["Bangalore","Chennai",334],["Bangalore","Mumbai",981],
     ["Bangalore","Panjim",590],     ["Bangalore","Bhopal",1441],	["Bangalore","Gir",1814],	["Bangalore","Shimla",2525]	,["Bangalore","Srinagar",2976],
["Hyderabad","Bangalore",569],	["Hyderabad","Hyderabad",0],		["Hyderabad","Kochi",1122],	["Hyderabad","Chennai",626],
     ["Hyderabad","Mumbai",708]	,["Hyderabad","Panjim",656], ["Hyderabad","Bhopal",850]	,["Hyderabad","Gir",1495],	["Hyderabad","Shimla",1934],
     ["Hyderabad","Srinagar",2385],
["Kochi","Bangalore",547]	,	["Kochi","Hyderabad",1122]	,	["Kochi","Kochi",0]	,	["Kochi","Chennai",690]	,["Kochi","Mumbai",1430],
     ["Kochi","Panjim",776]	,["Kochi","Bhopal",1987],	["Kochi","Gir",2262],	["Kochi","Shimla",2938],	["Kochi","Srinagar",3386],
["Chennai","Bangalore",334],		["Chennai","Hyderabad",626],		["Chennai","Kochi",690],	["Chennai","Chennai",0],
     ["Chennai","Mumbai",1334],	["Chennai","Panjim",944],	["Chennai","Bhopal",1474],	["Chennai","Gir",2167],	["Chennai","Shimla",2859],
     ["Chennai","Srinagar",3010],
["Mumbai","Bangalore",981]	,	["Mumbai","Hyderabad",708]	,	["Mumbai","Kochi",1430],	["Mumbai","Chennai",1334],	["Mumbai","Mumbai",0],
     ["Mumbai","Panjim",570],	["Mumbai","Bhopal",776],	["Mumbai","Gir",841]	,["Mumbai","Shimla",1720],	["Mumbai","Srinagar",2167],
["Panjim","Bangalore",590]	,	["Panjim","Hyderabad",656]	,	["Panjim","Kochi",776],	["Panjim","Chennai",944],	["Panjim","Mumbai",570],
     ["Panjim","Panjim",0],	["Panjim","Bhopal",1231]	,["Panjim","Gir",1401],	["Panjim","Shimla",2189]	,["Panjim","Srinagar",2636],
["Bhopal","Bangalore",1441]	,	["Bhopal","Hyderabad",850]	,	["Bhopal","Kochi",1987]	,["Bhopal","Chennai",1474]	,["Bhopal","Mumbai",776],
     ["Bhopal","Panjim",1231],	["Bhopal","Bhopal",0]	,["Bhopal","Gir",949],	["Bhopal","Shimla",1140],	["Bhopal","Srinagar",1591],
["Gir","Bangalore",1814]	,	["Gir","Hyderabad",1495]	,	["Gir","Kochi",2262],	["Gir","Chennai",2167],	["Gir","Mumbai",841],
     ["Gir","Panjim",1401]	,["Gir","Bhopal",949]	,["Gir","Gir",0]	,	["Gir","Shimla",1612],	["Gir","Srinagar",2089],
["Shimla","Bangalore",2825]	,	["Shimla","Hyderabad",1934]	,	["Shimla","Kochi",2938],	["Shimla","Chennai",2559]	,["Shimla","Mumbai",1720],
     ["Shimla","Panjim",2189],	["Shimla","Bhopal",1140],	["Shimla","Gir",1612]	,["Shimla","Shimla",0],	["Shimla","Srinagar",640],
     ["Srinagar","Bangalore",2976],	["Srinagar","Hyderabad",2385],	["Srinagar","Kochi",3386],	["Srinagar","Chennai",3010],	["Srinagar","Mumbai",2167],
     ["Srinagar","Panjim",2636],	["Srinagar","Bhopal",1591],	["Srinagar","Gir",2059],	["Srinagar","Shimla",640]	,["Srinagar","Srinagar",0]]
n=100

#print(random.choice(inp))


#print(random.sample(inp,10))
k=random.sample(inp,10)

inp=sorted(inp,key= lambda inp:inp[2])
for i in range(len(inp)-99):
  print(k)
print("The  list in sorted manner :")
k=sorted(k,key= lambda k:k[2])
print(k)

 
