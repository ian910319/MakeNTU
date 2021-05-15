import csv                          ######################
import pandas                       ## only for makeNTU ##
from scatterPlot import *           ######################

timeSlice =10
recordRate =100
whereDataGoes ="processed_data_to_be_trained/test"     ### 注意: 若不想遺失資料請每次編譯前改後面的檔名，否則同名檔案將被覆蓋。資料相同就沒差。 ###

attributeVectorList =[]

def scatterAnalysis(filePath, situa):
    global attributeVectorList
    
    try:
        threeAxisesAccData =pandas.read_csv(str(filePath)).values
    except:
        print("Cannot open the raw data file.")
        return

    sumOfMagSq =0
    maxAmpl =0
    avg =0
    maxSlope =0
    latestTwentyData =[]
    peakList =[]

    counter =0
    
    for singleData in threeAxisesAccData:
        mag =sum(singleData[i]*singleData[i] for i in range(1, 4))**0.5
        
        
        #sum of mag square to compute 標準差
        sumOfMagSq +=mag**2
    
        #maxAmpl
        if mag > maxAmpl:
            maxAmpl =mag#
    
        #peak: a mag greater than 10 before and 10 after can called a peak
        #would do the peak avg finally and compare numbers of peaks gtr or smlr than peak avg
        latestTwentyData.append(mag)
    
        if len(latestTwentyData) >= 20:
            if latestTwentyData[9] == max(latestTwentyData):
                peakList.append(mag)
            
            latestTwentyData.pop(0)
    
        #avg: divided by num finally
        avg +=mag#
        
        #maxSlope
        if counter > 3:
            slope =0.25*recordRate*abs(latestTwentyData[-1]-latestTwentyData[-5])
        if counter > 3 and slope > maxSlope:
            maxSlope =slope#
        
        counter +=1
    
    ############################ when one time slice passed ############################
        
        if counter >= timeSlice*recordRate:
            peakAvg =sum(peakList)/len(peakList)
            peakAboveRate =0
            
            for peak in peakList:
                if peak >= peakAvg:
                    peakAboveRate +=1
    
            peakAboveRate /=len(peakList)#
    
            avg /=counter
    
            stdDiviation =sumOfMagSq/(timeSlice*recordRate)-avg**2#
            
            attributeVectorList.append((maxAmpl, avg, maxSlope, peakAboveRate, stdDiviation, str(situa), singleData[0]))

            sumOfMagSq, maxAmpl, avg, maxSlope, latestTwentyData, peakList =0, 0, 0, 0, [], []
            counter =0
        
    #####################################################################################





def saveData(fileName, fieldnames, dataList):
    count =0
    renewedFileName =str(fileName) + ".csv"
    fileCount =0

    csvfile =None
    writer =None

    for data in dataList:
        if count == 0 or count > 10000:
            if count > 10000:
                fileCount +=1
                renewedFileName =str(fileName) + "({})".format(fileCount) + ".csv"

            count =1

            createNewFile(renewedFileName, fieldnames)
            csvfile =open(renewedFileName, 'a', newline ='')
            writer =csv.DictWriter(csvfile, fieldnames =fieldnames)

        dataOfOneRow =dict()

        for i in range(len(fieldnames)):
            dataOfOneRow[fieldnames[i]] =data[i]

        writer.writerow(dataOfOneRow)


def createNewFile(fileName, fieldnames):
    try:
        with open(fileName, 'w', newline ='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames =fieldnames)
            writer.writeheader()
    except:
        print("One error in creating new file.")
        
        while True:
            pass



#以下請依功能自行解註

if __name__ == "__main__":
    
    dimentionName =["maxAmpl", "avgAmpl", "maxSlope", "peakAboveRate", "stdDiviation"]
    
    scatterAnalysis("raw_data/_rest.xlsx - Raw Data.csv", "rest")      #分析
    scatterAnalysis("raw_data/_walk.xlsx - Raw Data.csv", "walk")      #分析
    scatterAnalysis("raw_data/_active.xlsx - Raw Data.csv", "active")  #分析
    scatterAnalysis("raw_data/_fall.xlsx - Raw Data.csv", "fall")      #分析
    
    #scatterAnalysis("raw_data/110秒已知測資.xls - Raw Data.csv", "100s_unknown")      #分析
    #scatterAnalysis("raw_data/500秒測資.xls - Raw Data.csv", "unknown")          #分析

    plotScatter(attributeVectorList, dimentionName)        #畫圖

    #dimentionName.append("situation")      #存成 .csv
    #saveData(fileName ="Trained", fieldnames =dimentionName, dataList =attributeVectorList)      #存成 .csv
    

    
