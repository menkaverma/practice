# dic1={'Fairy':'Menka','Rainy':'Varsha'}
# print(dic1)
# dic1['cloud']='Akash'
# dic1['good luck']='Lucky'
# print(dic1)


alien_0={'x_position':0, 'y_position':25 ,'speed':'fast'}
print(f"Original position is {alien_0['x_position']}")
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position'] + x_increment
print(f"New position is {alien_0['x_position']} ")