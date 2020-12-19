def isInt(x): return int(x)==x
def findplace(x,rept):
    reptt=len(str(x))
    while reptt>rept:
        reptt-=1
        x%=10**reptt
    x=int(x//(10**(rept-1)))
    return x
def fact(x):
    for i in range(x-1): x*=i+1
    return x
i=1
ii=0
rept=int(input("How many numbers do you want in this pack? "))
print("\nTitle=Numbers 1-"+str(rept)+"\nDescription=Every number up to "+str(rept)+" is creatable, but not beyond.\nId=numbers\nVersion=3."+str(rept)+"\nNumbers: #FFFFFF\nNot Numbers: #FFFFFF\nNumbers (Not Numbers)\nOperation (Not Numbers)\nNumbers + Numbers = 1 (Numbers)\nOperation + Operation = Subtraction (Not Numbers)\nSubtraction + Operation = Multiplication (Not Numbers)\nMultiplication + Operation = Division (Not Numbers)\nDivision + Operation = Exponentiation (Not Numbers)\nExponentiation + Operation = Factorial (Not Numbers)\n<-"+str(rept)+" + * =  < Negative"+str(rept)+" (Not Numbers)\nNot an integer + * = Not an integer (Not Numbers)\n>"+str(rept)+" + * = >"+str(rept)+" (Not Numbers)\nNumbers - Symbols used to count things.\nOperation - Actions performed on numbers.\nSubtraction - Taking the value of one number from another.\nMultiplication - Adding a number to itself a certian amount of times.\nExponentiation - Multiplying a number with itself a certian amount of times.\nFactorial - The factorial of a number is the product of all whole numbers less than or equal to the number but above zero.\nDivision - Subtracting a number from itself a certian amount of times.\n>"+str(rept)+" - Greater than "+str(rept)+".\n< Negative"+str(rept)+" - Less than negative"+str(rept)+".\nNot an integer - The number is not a whole number.\n0 - The 0th number.")
while i<=rept:
    print(i,"+ Subtraction = Negative",str(i),"(Numbers)")
    print(i,"+ Multiplication = x"+str(i),"(Numbers)")
    print(i,"+ Division = /"+str(i),"(Numbers)")
    print("Negative",i,"+ Multiplication = x Negative",str(i),"(Numbers)")
    print("Negative",i,"+ Division = / Negative",str(i),"(Numbers)")
    print("x"+str(i),"+ Subtraction = x Negative",str(i),"(Numbers)")
    print("/"+str(i),"+ Subtraction = / Negative",str(i),"(Numbers)")
    print(i,"+ Exponentiation = ^"+str(i),"(Numbers)")
    if fact(i)>rept: iii=">"+str(rept)+" (Not Numbers)"
    else: iii=str(fact(i))+" (Numbers)"
    print(i,"+ Factorial =",iii)
    while ii<=i:
        if i+ii>rept:
            iii=str(rept)
            print(i,"+",ii,"= >",iii,"(Not Numbers)")
            print("Negative",i,"+","Negative",ii,"= < Negative",iii,"(Not Numbers)")
        else:
            iii=i+ii
            print(i,"+",ii,"=",iii,"(Numbers)")
            print("Negative",i,"+","Negative",ii,"=","Negative",iii,"(Numbers)")
        ii+=1
    ii=0
    while ii<=rept:
        if ii-i<-rept: iii="< Negative "+str(rept)+" (Not Numbers)"
        else: 
            if ii-i<0: iii="Negative "+str(-1*(ii-i))+" (Numbers)"
            else: iii=str(ii-i)+" (Numbers)"
        print(ii,"+","Negative "+str(i),"=",iii)
        if i*ii>rept:
            iii=str(rept)+" (Not Numbers)"
            print(ii,"+ x"+str(i),"= >",iii)
            print("Negative",ii,"+ x"+str(i),"= < Negative",iii)
            print(ii,"+ x Negative "+str(i),"= < Negative",iii)
            print("Negative",ii,"+ x Negative "+str(i),"= >",iii)
        else:
            iii=str(i*ii)+" (Numbers)"
            print(ii,"+ x"+str(i),"=",iii)
            print("Negative",ii,"+ x"+str(i),"= Negative",iii)
            print(ii,"+ x Negative "+str(i),"= Negative",iii)
            print("Negative",ii,"+ x Negative "+str(i),"=",iii)
        if not isInt(ii/i): iii="Not an integer (Not Numbers)"
        else: iii=str(int(ii/i))+" (Numbers)"
        print(ii,"+ /"+str(i),"=",iii)
        print("Negative",ii,"+ /"+str(i),"= Negative",iii)
        print(ii,"+ / Negative "+str(i),"= Negative",iii)
        print("Negative",ii,"+ / Negative "+str(i),"=",iii)
        if ii*i>rept:
            iii=str(rept)+" (Not Numbers)"
            if int(ii)/2!=ii/2: iii="< Negative "+iii
            else: iii=">"+iii
            print(ii,"+ ^"+str(i),"=",iii)
            print("Negative",ii,"+ ^"+str(i),"=",iii)
        else:
            iii=ii*i
            if int(ii)/2!=ii/2: iii="Negative "+iii
            print(ii,"+ ^"+str(i),"=",iii,"(Numbers)")
            print("Negative",ii,"+ ^"+str(i),"=",iii,"(Numbers)")
        ii+=1
    ii=0
    tth=findplace(i,1)
    th="th"
    if findplace(i,2)!=1:
        if tth==1: th="st"
        elif tth==2: th="nd"
        elif tth==3: th="rd"
    print(i,"- The ",i,th," number.",sep="")
    print("Negative "+str(i)," - The ",i,th," negative number.",sep="")
    print("x"+str(i)," - The ",i,th," number, ready to be multiplied with another number.",sep="")
    print("/"+str(i)," - The ",i,th," number, ready to divide another number.",sep="")
    print("x Negative "+str(i)," - The ",i,th," negative number, ready to be multiplied with another number.",sep="")
    print("/ Negative "+str(i)," - The ",i,th," negative number, ready to divide another number.",sep="")
    print("^"+str(i)," - The ",i,th," negative number, ready to be exponentiated with another number.",sep="")
    i+=1
    
