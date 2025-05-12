# casi in cui si interrompe

# casi di base / di arresto
def countdow(n:int) ->None:
    if n<0:  #1
        print("essrore")

    elif n==0:  #2
        print(0)
#caso recursivo
    else:
        print(n)
        countdow(n-1)

countdow(5)
countdow(-5)
countdow(0)
