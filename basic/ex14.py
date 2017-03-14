from datetime import datetime
def datediff(df1,df2):
    st_date=datetime.strptime(df1,"%d/%m/%Y")
    end_date=datetime.strptime(df2,"%d/%m/%Y")
    print(abs(end_date-st_date).days)



d1=(2014, 7, 2) 
d2=(2014, 7, 11)

df1=str(d1[2])+"/"+str(d1[1])+"/"+str(d1[0])
df2=str(d2[2])+"/"+str(d2[1])+"/"+str(d2[0])

print(df1,df2)

datediff(df1,df2)


    
