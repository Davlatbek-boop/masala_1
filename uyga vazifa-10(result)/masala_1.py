def datatekshir(data):
    spdata=n[0].split(",")
    try: 
        if 0<int(spdata[0])<30 and 0<int(spdata[1])<=12 and 0<int(spdata[2])<=2024 and 0<int(spdata[3])<60 and 0<int(spdata[4])<60:
            return True
        else:
            return False
    except:
        return False
    

data=input("date ni kiriting >>> ")
print(datatekshir(data))


        

