import random
def passgen(length,lis):
    
    password=''
    for i in range(length):
        rand=random.choice(lis)
        password+=str(random.choice(rand))
    return password

def main():
    length=int(input("Enter the length of the password "))
    level=int(input("Enter the level from 1 to 3 of complexity "))
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    num=[1,2,3,4,5,6,7,8,9,0]
    spe=['!','@','#','$','%','^','&','*','(','',')','_','+','[',']','{','|','}',':','"',';','?','/','>','<','.','₹',"'"]
    lis=[]
    if level==1:
        lis=[a,num]
    elif level==2:
        lis=[a,A,num]
    elif level==3:
        lis=[a,A,num,spe]
    else:
        print("invalid choise")
    print(passgen(length,lis))
    
    y=int(input("Generate new password for enter 1 for yes and 2 for no "))
    if y==1:
        main()


if __name__=="__main__":
    main()