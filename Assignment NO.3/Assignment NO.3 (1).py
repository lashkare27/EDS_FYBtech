#Assignment NO.3
#Group Member:-1.Agniv Borah_235 2.Rohan Agrawal_236 3.Prathmesh Lashkare_237
#Title:- Performance of Indian Cricketer 
import numpy as np

#Odi Section
arr1= np.loadtxt("odi..csv",delimiter=",",dtype=str,skiprows=1)#odi..csv file converted into array
print("Odi data of Player:-\n",arr1,"\n\n")

mat1=arr1[:,1].astype(int)#Matches played in odi 
print("Total Number of Matches played by each Player in Odi:-\n",mat1,"\n" )
run1=arr1[:,2].astype(int)#Runs in ODI Matches
print("Total Number Of Runs of Each Player in Odi:-\n",run1,"\n")
wckt1=arr1[:,3].astype(int)#Wickets in ODI Matches
print("Total Number Of Wicket Taken by each player in Odi:-\n",wckt1,"\n")
cen1=arr1[:,4].astype(int)#Century in ODI Matches
print("Total Number of Century did by each player in odi:-\n",cen1,"\n")
ha_cen1=arr1[:,5].astype(int)#Half-Century in ODI Matches
print("Total Number of Half-Century did by each player in odi:-\n",ha_cen1,"\n")

mean_odi=np.mean(run1)
print("Mean of Total Runs of ODI:-\n",mean_odi,"\n")
median_odi=np.median(run1)
print("Median of Total Runs of ODI:-\n",median_odi,"\n")
std_odi=np.std(run1)
print("Standard Deviation of Total Runs of ODI:-\n",std_odi,"\n")
var_odi=np.var(run1)
print("Variance of Total Runs of ODI:-\n",var_odi,"\n")

result_odi=np.add(mat1,run1)#Addition of Matches and Runs in ODI
print("Sum of Total Matches and Total Runs:-\n",result_odi,"\n")
result1_odi=np.subtract(run1,mat1)#Subtraction Matches and Runs in ODI
print("Subtarction of Total Matches and Total Runs:-\n",result1_odi,"\n")
result2_odi=np.matmul(mat1,run1)
print("Matrix Multiplication Of Total Matches And Total Runs -\n",result2_odi,"\n")
result3_odi=np.hstack((mat1,run1))#Horizontal stack of Mataches and Runs 
print("Stack Along Rows -\n",result3_odi,"\n")
result4_odi=np.vstack((mat1,run1))#Vertical stack of Matches and Runs 
print("Stack Along Columns -\n",result4_odi,"\n")
result5_odi=np.multiply(mat1,run1)#Multiplication of Matches and Runs in ODI
print("Multiplication of Total Matches and Total Runs -\n", result5_odi,"\n")
result6_odi=np.divide(run1,mat1)#Divsion of Matches and Runs in ODI
print("Division of Total Runs and Total Matches -\n", result6_odi,"\n")

count_odi=wckt1[np.where(wckt1==0)]
print("How many Player has taken zero wickets in Odi :-", {count_odi.size})
count1_odi=cen1[np.where(cen1==0)]
print("How many player not did century in Odi :-",{count1_odi.size})
count2_odi=ha_cen1[np.where(ha_cen1==0)]
print("How many player did Half-century in Odi :-",{count2_odi.size},"\n\n\n\n")

#T20 Section
arr2= np.loadtxt("t20..csv",delimiter=",",dtype=str,skiprows=1)#t20..csv file converted into array
print("T20 data of Player:-\n",arr2)

mat2=arr2[:,1].astype(int)#Matches played in t20 
print("Total Number of Matches played by each Player in T20:-\n",mat2,"\n" )
run2=arr2[:,2].astype(int)#Runs in t20 Matches
print("Total Number Of Runs of Each Player in T20:-\n",run2,"\n")
wckt2=arr2[:,3].astype(int)#Wickets in t20 Matches
print("Total Number Of Wicket Taken by each player in T20:-\n",wckt2,"\n")
cen2=arr2[:,4].astype(int)#Century in t20 Matches
print("Total Number of Century did by each player in T20:-\n",cen2,"\n")
ha_cen2=arr2[:,5].astype(int)#Half-Century in t20 Matches
print("Total Number of Half-Century did by each player in T20:-\n",ha_cen2,"\n")

mean_t20=np.mean(run2)
print("Mean of Total Runs of T20:-\n",mean_t20,"\n")
median_t20=np.median(run2)
print("Median of Total Runs of T20:-\n",median_t20,"\n")
std_t20=np.std(run2)
print("Standard Deviation of Total Runs of T20:-\n",std_t20,"\n")
var_t20=np.var(run2)
print("Variance of Total Runs of T20:-\n",var_t20,"\n")

result_t20=np.add(mat2,run2)#Addition of Matches and Runs in T20
print("Sum of Total Matches and Total Runs:-\n",result_t20,"\n")
result1_t20=np.subtract(run2,mat2)#Subtraction Matches and Runs in T20
print("Subtarction of Total Matches and Total Runs:-\n",result1_t20,"\n")
result2_t20=np.matmul(mat2,run2)
print("Matrix Multiplication Of Total Matches And Total Runs -\n",result2_t20,"\n")
result3_t20=np.hstack((mat2,run2))#Horizontal stack of Mataches and Runs 
print("Stack Along Rows -\n",result3_t20,"\n")
result4_t20=np.vstack((mat2,run2))#Vertical stack of Matches and Runs 
print("Stack Along Columns -\n",result4_t20,"\n")
result5_t20=np.multiply(mat2,run2)#Multiplication of Matches and Runs in T20
print("Multiplication of Total Matches and Total Runs -\n", result5_t20,"\n")
result6_t20=np.divide(run2,mat2)#Divsion of Matches and Runs in T20
print("Division of Total Runs and Total Matches -\n", result6_t20,"\n")

count_t20=wckt2[np.where(wckt2==0)]
print("How many Player has taken zero wickets in T20 :-", {count_t20.size})
count1_t20=cen2[np.where(cen2==0)]
print("How many player not did century in T20 :-",{count1_t20.size})
count2_t20=ha_cen2[np.where(ha_cen2==0)]
print("How many player did Half-century in T20 :-",{count2_t20.size},"\n\n\n\n")
