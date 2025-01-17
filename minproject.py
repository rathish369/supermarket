from datetime import datetime
name=input("enter your name:")
lists="""
        rice rs60/kg
        sugar rs40/kg
        salt   rs 10/kg
        oil    rs 180/kg
        maggi  rs 10/piece
        biscuit rs 5/piece
        powder  rs 10/box
        brush    rs20/piece"""
price=0
totalprice=0
finalprice=0
pricelist=[]
qlist=[]
plist=[]
ilist=[]
iteam= {"rice": 60,"sugar": 40, "salt":  10,"oil ":180,"maggi":  10,"biscuit " :5,"powder":  10,"brush "   :20}
option=int(input("if u want to check iteam list press 1"))
if option==1:
    print(lists)
    for i in range(len(iteam)):
        input1=int(input("enter the number 1 if u want to buy anthorwise enter 2"))
        if input1==2:
            break
        elif input1==1:
            iteams=input("enter iteam name")
            quality=int(input("enter how much qulity u need"))
            if iteams in iteam.keys():
                price=quality*(iteam.get(iteams,0))
                pricelist.append((iteam,quality,iteam,price))
                totalprice+=price
                ilist.append(iteams)
                qlist.append(quality)
                plist.append(price)
                gst=(totalprice*5)/100
                finalprice=gst+totalprice
            else:
                print ("iteam not avaible")
        else:
           print("you entered wrong number")
        input2=input("enter yes or else no")
        if input2=="yes":
            pass
        elif  finalprice !=0:
            print(25*"=","shivamarket",25*"=")
            print(28*"=","hydeabad")
            print("Name:",name,30*"",datetime.now())
            print(75*"-")
            for i in range(len(pricelist)):
             print(i,8*"" ,5*"",ilist[i],10*"",qlist[i],10*"",plist[i])
             print(75*"=")
             print(50*"","totalamout:","rs",totalprice)
             print("gst amout",40*"","gst rs",gst)
             print(75*"=")
             print(50*"","finalamout:","rs",finalprice)
             print(75*"=")
             print(50*"","thanksfor shopping")
             print(75*"=")      
        else:
            print("thanks for coming")
print("total amout of our shopping:",finalprice)
