#This part is all about getting numbers from input.txt
with open("input.txt", "r") as input_file:#Getting Datas from input.txt
    Datas = input_file.readlines()
    Res = [int(i.strip()) for i in Datas]


#-----------------------------------------------------------------------------------------------------
i=3
ActualSales = []
while i < len(Res): #Getting the Actual Sale Values
    ActualSales.append(Res[i])
    i+=1
AlphaBeta = []
Alpha = [0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50
        , 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05]


#-----------------------------------------------------------------------------------------------------
i=0
k=0
while i < len(Alpha):
    j=0
    while j < len(Alpha):
        AlphaBeta.append([Alpha[i], Alpha[j]])
        j+=1
    i+=1
ForecastT = []
TrendT = []
ActualSalesTRY = [] # Helper for Actual-Forecast Array


#-----------------------------------------------------------------------------------------------------
i=0
j=0
while i < len(AlphaBeta):# This will help because len of ActualSalesTRY and forecastIT will be equal
    j=0
    while j<len(ActualSales):
        ActualSalesTRY.append(ActualSales[j])
        j+=1
    i+=1


#-----------------------------------------------------------------------------------------------------
i=0
j=0
while i < len(AlphaBeta): #We are finding Exponentially Smoothed Forecast(ForecastT) and 
                        #Exponentially smoothed(TrendT)
    k=0
    while k < len(ActualSales):
        if(k==0):
            ForecastT.append([k, (AlphaBeta[i][0]*ActualSales[k])+(1-AlphaBeta[i][0])*(8+10)])
            TrendT.append([k, (AlphaBeta[i][1]*(ForecastT[k][1]-8)+(1-AlphaBeta[i][1])*10)])
        else:
            ForecastT.append([k, (AlphaBeta[i][0]*ActualSales[k])+((1-AlphaBeta[i][0])*(ForecastT[k-1][1]+TrendT[k-1][1]))])
            TrendT.append([k, ((AlphaBeta[i][1]*(ForecastT[k][1]-ForecastT[k-1][1]))+((1-AlphaBeta[i][1])*(TrendT[k-1][1])))])
        k+=1
    i+=1


sumError = []#Error summary
forecastIT = [] #forecast including trend
error = []#Actual-Forecast Array
errorMAPE = []#Actual-Forecast/Actual Array for MAPE
sumErrorMAPE = []#Summary Of Error/Actual for MAPE
sumErrorSqrt = []#Error Squared
errorSqrtFlag=0#Helper of error squared array for fill
#-----------------------------------------------------------------------------------------------------
i=0
k=0
e=0#2-D array of error squared-helper
while i < len(ForecastT):#This loop will help us to find Forecast Including Trend
    forecastIT.append(ForecastT[i][1]+TrendT[i][1])#forecast including trend fill
    if((((i%len(ActualSales))==0)&(i!=0))|((len(ForecastT)-1)==i)):
        e=0
        while e < len(error):#Calculating the error squared
            errorSqrtFlag = (error[e]*error[e]) + errorSqrtFlag#error squared alırken bazı sorunlar yaşıyoruz
            e+=1
        sumError.append(sum(error))#forecast including trend summary array fill
        sumErrorSqrt.append(errorSqrtFlag)
        errorSqrtFlag=0
        sumErrorMAPE.append(sum(errorMAPE))
        error.clear()
        errorMAPE.clear()
    error.append(abs(ActualSalesTRY[(i)]-forecastIT[i]))#Finding error at every one of Sale
    errorMAPE.append(abs(ActualSalesTRY[i]-forecastIT[i])/ActualSalesTRY[i])
    i+=1
    k+=1


#-----------------------------------------------------------------------------------------------------
i=0
flagMSE=0
minSumErrSqrt=min(sumErrorSqrt)
while i<len(sumErrorSqrt): #Helper finding optimum minimized MSE's Alpha and Beta Value
    if(sumErrorSqrt[i]==minSumErrSqrt):
        flagMSE=i
    i+=1
optimalOfMSE = minSumErrSqrt/len(ActualSales)

#-----------------------------------------------------------------------------------------------------
minSumError=min(sumError)
flagMAD=0
i=0
while i < len(sumError): #Helper finding optimum minimized MAD's Alpha and Beta Value
    if(minSumError==sumError[i]):
        flagMAD=i
    i+=1
optimalOfMAD=0
optimalOfMAD = minSumError/len(ActualSales)

#-----------------------------------------------------------------------------------------------------
minSumErrorMAPE = min(sumErrorMAPE)
i=0
flagMAPE=0
while i < len(sumErrorMAPE): #Helper finding optimum minimized MAPE's Alpha and Beta Value
    if(minSumErrorMAPE==sumErrorMAPE[i]):
        flagMAPE=i
    i+=1
optimalOfMAPE = minSumErrorMAPE/len(ActualSales)*100

#1.optimal alpha and beta values minimizing MAD and the 
# related MAD,MSE,MAPE values for this alpha and beta values
print("\n\n --------First Output Part--------")
print("Optimal Alpha for MAD: "+str(AlphaBeta[flagMAD][0])+"\nOptimal Beta for MAD:"+str(AlphaBeta[flagMAD][1])) #Optimal Alpha Beta for MAD
print("Optimal Value of MAD: "+str(optimalOfMAD)) #Optimal MAD
print("MSE with Optimal Alpha and Beta for MAD: "+ str(sumErrorSqrt[flagMAD]/len(ActualSales))) #Calculation of MSE
print("MAPE with Optimal Alpha and Beta for MAD: "+ str(sumErrorMAPE[flagMAD]/len(ActualSales)*100)) #Calculation of MAPE

#2.optimal alpha and beta values minimizing MSE and the 
# related MAD,MSE,MAPE values for this alpha and beta values
print("\n\n --------Second Output Part--------")
print("Optimal Alpha for MSE: "+str(AlphaBeta[flagMSE][0])+"\nOptimal Beta for MSE"+str(AlphaBeta[flagMSE][1]))
print("Optimal Value of MSE: "+str(optimalOfMSE))
print("MAD with Optimal Alpha and Beta for MSE: "+str(sumError[flagMSE]/len(ActualSales)))
print("MAPE with Optimal Alpha and Beta for MSE: "+str(sumErrorMAPE[flagMSE]/len(ActualSales)*100))

#3.optimal alpha and beta values minimizing MAPE and the 
# related MAD,MSE,MAPE values for this alpha and beta values
print("\n\n --------Third Output Part--------")
print("Optimal Alpha for MAPE: "+str(AlphaBeta[flagMAPE][0])+"\nOptimal Beta for MAPE:"+str(AlphaBeta[flagMAPE][1]))
print("Optimal Value of MAPE: "+str(optimalOfMAPE))
print("MAD with Optimal Alpha and Beta for MAPE: "+str(sumError[flagMAPE]/len(ActualSales)))
print("MSE with Optimal Alpha and Beta for MAPE: "+str(sumErrorSqrt[flagMAPE]/len(ActualSales)))
