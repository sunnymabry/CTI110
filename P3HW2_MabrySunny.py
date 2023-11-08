#CTI-110
#P3HW2-Salary
#Sunny Mabry
#November 8th, 2023
#
name=input("Enter employee's name:")
hrs=input("Enter number of hours worked:")
h=float(hrs)
r=input("Enter employee's pay rate:")
r=float(r)
rp= h*r
if h > 40:
    ot=(h-40)
    otp=1.5*r
    gp=rp+otp
else: h <=40
gp=h*r
xer=float(gp)
print("-------------------------------------")
print("Epmloyee's name:", name)
print("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour pay   Gross Pay")
print("-------------------------------------------------------------------------------------")
print(h ,              r,         ot,        otp,           rp,           gp)
