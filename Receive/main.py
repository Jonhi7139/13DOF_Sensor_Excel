from openpyxl import Workbook
from Receiver import*

wb=Workbook()
ws=wb.active
ws.append(("ax","ay","az","gx","gy","gz","tempI","time","tempO","humidity","pressure","Gas","mx","my","mz"))

x=Receiver('COM13', 9600,"<fffffffQfffIhhh",58)
c=0
while x.ser.is_open:
    d=x.store()
    if d is not None:
        c=c+1
        print(c)
        ws.append(d)
        if(c>=10000):
            x.ser.close()
            wb.save("DOFData.xlsx")
            break                 