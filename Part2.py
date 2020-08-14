from random import seed, random
while True: # Collects inputs from the user, stores variables and handles errors
    try: # Saves inputs
        expRet1 = float(input("Enter expected return for fund 1 in %: "))
        expRet2 = float(input("Enter expected return for fund 2 in %: "))
        vol1 = float(input("Enter volatility for fund 1 in %: "))
        vol2 = float(input("Enter volatility for fund 2 in %: "))
        corr = float(input("Enter the correlation coefficient: "))
        riskAversion = float(input("Enter the risk aversion coefficient: "))
        while ((vol1<0)or(vol2<0)): # Limits volatility to larger or equal to 0
            print("Please enter a percentage greater than 0!!!")
            vol1 = float(input("Enter volatility for fund 1 in %: "))
            vol2 = float(input("Enter volatility for fund 2 in %: "))
        while ((corr<-1)or(corr>1)): # Limits correlation to between -1 and 1
            print("Please enter a floating number between -1 and 1!!!")
            corr = float(input("Enter the correlation coefficient: "))
        break
    except ValueError: # Blocks non-integer inputs
        print("Please enter a number (Letters will not work)!!")
# %% creates 100 random floating numbers for fund weights
n = 100
seed(1)
w1 = [random() for i in range(n)]
w2 = [(1-w1[i]) for i in range(n)]
#Verifies Weights
verify = [round(w1[i]+w2[i]) for i in range(n)]
verify = [True if (verify[i]==1) else False for i in range(n)]
# %% computes portfolio expected return, volatility and utility
portExpRet = [((w1[i]*(expRet1/100))+(w2[i]*(expRet2/100))) for i in range(n)]
portVol = [((((w1[i]**2)*((vol1/100)**2))+((w2[i]**2)*((vol2/100)**2))+(2*w1[i]*
             w2[i]*corr*(vol1/100)*(vol2/100)))**(1/2)) for i in range(n)]
portUtil = [(portExpRet[i]-((1/2)*riskAversion*(portVol[i]**2))) for i in range(n)]
#finds the portfolio with the best utility and it's index number
indexNum = portUtil.index(max(portUtil))
# %% prints the table headers
print(' ---------------------------------------------------------------------')
print("Weight 1 (%)".ljust(10), "Weight 2 (%)".ljust(10), "E[R](%)".center(5), 
      "Vol(%)".center(5), "Utility".center(5), "W1+W2=1?".center(5), sep="\t")
print(' ---------------------------------------------------------------------')
for i in range(n): # prints the table contents
    print(str(round(w1[i]*100,2)).center(10), str(round(w2[i]*100,2)).center(10),
          str(round(portExpRet[i]*100,2)).center(5),
          str(round(portVol[i]*100,2)).center(5),
          str(round(portUtil[i],2)).center(5), verify[i], sep="\t", end="\n")
print(' ---------------------------------------------------------------------')
#Prints best portfolio information
print("The best portfolio is: ", "Portfolio #",(indexNum+1))
print("Fund 1 Weight: ", str(round((w1[indexNum]*100), 2)),"%", "\t", 
      "Fund 2 Weight: ", str(round((w2[indexNum]*100), 2)),"%",
      "\nMaximum Utility: ", str(round((portUtil[indexNum]),2)),
      "\nExpected Return: ", str(round((portExpRet[indexNum]*100),2)),"%",
      "\nVolatility: ", str(round((portVol[indexNum]*100),2)),"%")