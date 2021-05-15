import plotly.express as px

def plotScatter(data, dimentionName, situationPos =-1):
    df =dict()
    
    df["situation"] =[]
    for dim in dimentionName:
        df[dim] =[]

    #print(df)
    
    for point in data:
        df["situation"].append(point[situationPos])

        co =0
        
        for dim in dimentionName:
            if co == situationPos or co == len(point)-situationPos:
                co +=1
            
            df[dim].append(point[co])
            co +=1

    fig =px.scatter_matrix(df, dimensions =dimentionName, color ="situation")

    fig.show()



if __name__ == "__main__":
    testData =[]
    for i in range(5):
        testData.append((i, 2*i, i*i, abs((i-4)*i*(i-3)), "run"))
    for i in range(5, 10):
        testData.append((2*i, abs((i-4)*i*(i-3)), i*i, i, "walk"))
    for i in range(10, 15):
        testData.append((abs((i-4)*i*(i-3)), 2*i, i, i*i, "fall"))
        
    plotScatter(data =testData, dimentionName =["one", "two", "three", "four"], situationPos =-1)

