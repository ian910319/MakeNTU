import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas
import numpy as np
import math
from enum import IntEnum
from random import random
import csv

class situation(IntEnum):
    none =0
    rest =20
    walk =60
    active =80
    fall =100##########################################3333333




def radialHeatMap(filePath, numOfRound =7, numPerRound =6*60*24):
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='polar')

    ax.set_xticks(np.arange(0,2.0*np.pi,np.pi/12.0))

    ax.set_ylim(0,numOfRound)
    ax.set_yticks(range(numOfRound))

    try:
        data =pandas.read_csv(str(filePath)).values
    except:
        print("Could not open {} to draw radial heat map.".format(filePath))
        return

    value =[[] for i in range(numPerRound)]

    count =0
    #situationInHour =0
    subArray =[]

    for i in range(numPerRound*numOfRound):
        try:
            event =data[i]
            
            if event[0] == "rest":
                subArray.append(situation.rest)
            elif event[0] == "walk":
                subArray.append(situation.walk)
            elif event[0] == "active":
                subArray.append(situation.active)
            elif event[0] == "fall":
                subArray.append(situation.fall)
        except:
            subArray.append(situation.none)
        finally:
            '''if countick >= 360:
                subArray.append((situationInHour/360))
                situationInHour =0
                count +=1
                countick =0'''
            
            count +=1
            
            if count >= numPerRound:
                for i in range(numPerRound):
                    value[i].append(subArray[i])
                    
                count,  subArray =0, []
                
            #countick +=1
    
    #print(value)

    rad = np.linspace(0, numOfRound, numOfRound+1)
    a = np.linspace(0, 2 * np.pi, numPerRound+1)
    r, th = np.meshgrid(rad, a)

    plt.subplot(projection ="polar")

    plt.pcolormesh(th, r, value, cmap ='Wistia')################################3

    plt.plot(a, r, ls='none', color = 'k')
    plt.grid()
    plt.colorbar()
    plt.savefig("flutter/health_monitoring_app/assets/images/graph.png", bbox_inches='tight')

    #plt.show()

if __name__ == "_main_":
    with open("situation.csv", 'w', newline ='') as f:
        writer = csv.DictWriter(f, fieldnames =["sitution", "time"])
        writer.writeheader()
    
        for i in range(51):
            r =int(4*random())%4
            for j in range(360):
                if r == 0:
                    writer.writerow(dict(sitution= "rest"))
                elif r == 1:
                    writer.writerow(dict(sitution= "active"))
                elif r == 2:
                    writer.writerow(dict(sitution= "fall"))
                elif r == 3:
                    writer.writerow(dict(sitution= "walk"))
        
    radialHeatMap(filePath ="situation.csv")