def isInt(x): return int(x)==x
def findplace(x,rept):
    reptt=len(str(x))
    while reptt>rept:
        reptt-=1
        x%=10**reptt
    x=int(x//(10**(rept-1)))
    return x
i=1
ii=0
rept=int(input("How many numbers do you want in this pack? "))
print("\nTitle=Numbers 1-"+str(rept)+"\nDescription=Every number up to "+str(rept)+" is creatable, but not beyond.\nId=numbers\nVersion=3."+str(rept)+"\nNumbers: #FFFFFF\nNot Numbers: #FFFFFF\nNumbers (Not Numbers)\nOperation (Not Numbers)\nNumbers + Numbers = 1 (Numbers)\nOperation + Operation = Subtraction (Not Numbers)\nSubtraction + Operation = Multiplication (Not Numbers)\nMultiplication + Operation = Division (Not Numbers)\n<-"+str(rept)+" + * =  < Negative"+str(rept)+" (Not Numbers)\nNot an integer + * = Not an integer (Not Numbers)\n>"+str(rept)+" + * = >"+str(rept)+" (Not Numbers)\nNumbers - Symbols used to count things.\nOperation - Actions performed on numbers.\nSubtraction - Taking the value of one number from another.\nMultiplication - Adding a number to itself a certian amount of times.\nDivision - Subtracting a number from itself a certian amount of times.\n>"+str(rept)+" - Greater than "+str(rept)+".\n< Negative"+str(rept)+" - Less than negative"+str(rept)+".\nNot an integer - The number is not a whole number.\n0 - The 0th number.")
while i<=rept:
    print(i,"+","Subtraction =","Negative "+str(i),"(Numbers)")
    print(i,"+","Multiplication =",str(i)+"x","(Numbers)")
    print(i,"+","Division =",str(i)+"/","(Numbers)")
    while ii<=i:
        if i+ii>rept: iii=">"+str(rept)
        else: iii=i+ii
        print(i,"+",ii,"=",iii,"(Numbers)")
        ii+=1
    ii=0
    while ii<=rept:
        if ii-i<-rept: iii="< Negative "+str(rept)+" (Not Numbers)"
        else: 
            if ii-i<0: iii="Negative "+str(-1*(ii-i))+" (Numbers)"
            else: iii=str(ii-i)+" (Numbers)"
        print(ii,"+","Negative "+str(i),"=",iii)
        if i*ii>rept: iii=">"+str(rept)+" (Not Numbers)"
        else: iii=str(i*ii)+" (Numbers)"
        print(ii,"+",str(i)+"x","=",iii)
        if not isInt(ii/i): iii="Not an integer (Not Numbers)"
        else: iii=str(int(ii/i))+" (Numbers)"
        print(ii,"+",str(i)+"/","=",iii)
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
    print(str(i)+"x"," - The ",i,th," number, ready to be multiplied with another number.",sep="")
    print(str(i)+"/"," - The ",i,th," number, ready to be divided with another number.",sep="")
    i+=1
#add lines for negative numbers too
#operations: exponets (5^3=125), factorials (5!=120), (what is this called?) n + n-1 + n-2 (5+4+3+2+1=15), etc.
