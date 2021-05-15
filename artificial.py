import csv
from random import random

with open("situation_m.csv", 'w', newline ='') as f:
    writer = csv.DictWriter(f, fieldnames =["sitution", "time"])
    writer.writeheader()
    
    sec =0
    min =0
    hr =0
    day =0

    for i in range(500):
        r =int(50*random())
        if hr>=21 or hr<=5:
            for j in range(int(random()*30*6)):
                if r >= 5:
                    writer.writerow(dict(sitution= "rest", time =str(day)+":"+str(hr)+":"+str(min)+":"+str(sec)))
                else:
                    writer.writerow(dict(sitution= "walk", time =str(day)+":"+str(hr)+":"+str(min)+":"+str(sec)))
                sec +=10

                if(sec >= 60):
                    min +=1
                    sec -=60
                if min >= 60:
                    hr +=1
                    min -=60
                if hr >= 24:
                    day +=1
                    hr -=24
        
        else:
            if r < 2:
                writer.writerow(dict(sitution ="fall", time =str(day)+":"+str(hr)+":"+str(min)+":"+str(sec)))
                sec +=10
                if(sec >= 60):
                    min +=1
                    sec -=60
                if min >= 60:
                    hr +=1
                    min -=60
                if hr >= 24:
                    day +=1
                    hr -=24
                continue
    
            r %= 5
            for j in range(int(random()*30*6)):
                if r == 0 or r==3:
                    writer.writerow(dict(sitution= "rest", time =str(day)+":"+str(hr)+":"+str(min)+":"+str(sec)))
                elif r == 1:
                    writer.writerow(dict(sitution= "active", time =str(day)+":"+str(hr)+":"+str(min)+":"+str(sec)))
                elif r == 2 or r==4:
                    writer.writerow(dict(sitution= "walk", time =str(day)+":"+str(hr)+":"+str(min)+":"+str(sec)))

                sec +=10

                if(sec >= 60):
                    min +=1
                    sec -=60
                if min >= 60:
                    hr +=1
                    min -=60
                if hr >= 24:
                    day +=1
                    hr -=24