import pandas as pd
data=[]
n=int(input('No Of Entries:'))
for i in range(n):
    print(f"\nEntery {i+1}:")
    x=str(input('NAME:'))
    y=int(input('AGE:'))
    z=int(input('PHONE_NO:'))
    data.append([x,y,z])
df=pd.DataFrame(data,columns=['NAME','AGE','PHONE_NO'])    
print(df)

