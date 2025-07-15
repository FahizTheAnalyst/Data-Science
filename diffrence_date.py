from  datetime import  date, timedelta
year= int(input("enter year:"))
month= int(input("enter month:"))
day= int(input("enter day:"))
date1= date(year,month,day)
dt= date1 - timedelta(5)

print("current date:", date1)

print("5 days before current date:", dt)