print("Bu dastur UCHBURCHAKNING YUZIni topib beradi")
def tori():
    a=float(input("1-tomon: "))
    b=float(input("2-tomon: "))
    c=float(input("3-tomon: "))
    p=(a+b+c)/2
    yuz=(p*(p-a)*(p-b)*(p-c))**0.5
    if a+b>c and a+c>b and b+c>a:
        print("Uchburchakning yuzi:",yuz)
    elif a+b<=c or a+c<=b or b+c<=a:
        print("Bunday uchnurchak mavjud emas")
        print("Balki xato kiritgandirsiz")
        print("Yana bir marta kiriting")
        tori()
        
tori()
