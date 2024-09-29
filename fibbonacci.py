def fibonnaci(nterms):
    n1,n2=0,1
    count=0
    if nterms<=0:
        print("Please enter a positive number")
    elif nterms==1:
        print(n1)
    else:
        while count<nterms:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1

nterm=int(input("Enter the nth terms"))
fibonnaci(nterm)
