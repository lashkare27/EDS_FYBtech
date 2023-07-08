#Title:ICC Test Batting Figures
#Group Member:-1.Prathmesh Lashkare_237
#              2.Jayantika Karna_229
#              3.Akash Jarad_228
#Assignment No.4
import pandas as pd

data= pd.read_csv("ICC_Test.csv",encoding='unicode_escape')
print("data of test data of player:-\n",data.to_string())

#Q1.Print All players name?
print("All player name:-\n",data['Player'])

#Q2.Find Player who had did maximum centuries in test matches?
print("Find Player who had did maximum centuries in test matches:-",data['Player'][data['Centuries'].max()],"\n","Number Of  Century:-",data['Centuries'].max(),"\n\n")

#Q3.Find Player who had did maximum Half-centuries in test matches?
print("Find Player who had did maximum Half-centuries in test matches:-",data['Player'][data['Fifties'].max()],"\n","Number of Half-Centuru:-",data['Fifties'].max(),"\n\n")

#Q4.Find median of all players Batting Average?
print("Find median of all players Batting Average:-",data['Batting Average'].median(),"\n\n")

#Q5.Find mean of all players Batting Average?
print("Find median of all players Batting Average:-",data['Batting Average'].mean(),"\n\n")

#Q6.show player name who had debut before 1900 and also count this player?
d1=data['Player'][data['Debut Year']<=1900]
print("show player name who had debut before 1900:-\n",d1,"\n")
print("Count:-",len(d1),"\n\n")

#Q7. show player name who had played upto 1900 and also count this player?
d2=data['Player'][data['Upto year played']<=1900]
print("show player name who had played upto 1900:-\n",d2,"\n")
print("Count:-",len(d2),"\n\n")

#Q8. show player name who had played from india and also count this player?
d3=data['Player'][data['Country']=='India']
print("show player name who had played from india:-\n",d3,"\n")
print("Count:-",len(d3),"\n\n")

#Q9. show player name who had played from England and also count this player?
d4=data['Player'][data['Country']=='England']
print("show player name who had played from England:-\n",d4,"\n")
print("Count:-",len(d4),"\n\n")

#Q10. show player name who had played from Australia and also count this player?
d5=data['Player'][data['Country']=='Australia']
print("show player name who had played from Australia:-\n",d5,"\n")
print("Count:-",len(d5),"\n\n")

#Q11. show player name who had played from South Africa and also count this player?
d6=data['Player'][data['Country']=='South Africa']
print("show player name who had played from South Africa:-\n",d6,"\n")
print("Count:-",len(d6),"\n\n")

#Q12. show player name who had played from Pakistan and also count this player?
d7=data['Player'][data['Country']=='Pakistan']
print("show player name who had played from Pakistan:-\n",d7,"\n")
print("Count:-",len(d7),"\n\n")

#Q13. show player name who had played from New zealand
d8=data['Player'][data['Country']=='New zealand']
print("show player name who had played from New zealand:-\n",d8,"\n")
print("Count:-",len(d8),"\n\n")

#Q14. show player name who had played from West-indies and also count this player?
d9=data['Player'][data['Country']=='West-indies']
print("show player name who had played from West-indies:-\n",d9,"\n")
print("Count:-",len(d9),"\n\n")

#Q15. find player name who had not out most of time in test?
print("find player name who had not out most of time in test:-",data['Player'][data['Not Outs'].max()])
print("How Many Time the player had not out most of time:-",data['Not Outs'].max(),"\n\n")

#Q16. find player name who had did higest score in test?
print("find player name who had did higest score in test:-",data['Player'][data['Highest Score'].max()])
print("Highest Score:-",data['Highest Score'].max(),"\n\n")

#Q17. Show Player who had did zero centuries in test matches?
print("Show Player who had did zero centuries in test matches:-\n",data['Player'][data['Centuries']==0])
print("Centuries:-",data['Centuries'].min(),"\n\n")

#Q18. show Player who had did zero Half-centuries in test matches?
print("Show Player who had did zero centuries in test matches:-\n",data['Player'][data['Fifties']==0])
print("Half-Centuries:-",data["Fifties"].min(),"\n\n")

#Q19. Show Player name who had Debut 1901 to 1950 in between them?
print("Show Player name who had Debut 1901 to 1950 in between them:-\n",data['Player'][(data['Debut Year']>=1901) & (data['Debut Year']<=1950)])
print("Count:-",len(data['Player'][(data['Debut Year']>=1901) & (data['Debut Year']<=1950)]),"\n\n")

#Q20.Show Player name who had Debut after the 1950 ?
print("Show Player name who had Debut after the 1950:-\n",data["Player"][(data['Debut Year']>=1951)])
print("Count:-",len(data["Player"][(data['Debut Year']>=1951)]),"\n\n")

#Q21. show player name who had played upto 1900?
print("show player name who had played upto 1900:-\n",data['Player'][data["Upto year played"]<=1900])
print("Count:-",len(data['Player'][data["Upto year played"]<=1900]),"\n\n")

#Q22. Find mean of all players Centuries?
print("Find mean of all players Centuries:-",data["Centuries"].mean())

#Q.23 Find mean of all players Half Centuries?
print("Find mean of all players Half Centuries:-",data["Fifties"].mean(),"\n\n")

#Q.24 Describe the Country Column
print("Describe the Country Column:-\n",data["Country"].describe())

#Q.25 Describe the data set
print("Describe the data set:-\n",data.describe(),"\n\n")
