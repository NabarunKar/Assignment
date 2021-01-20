with open("lower.txt") as f1:
    with open("upper.txt" ,"w") as f2:
        for i in f1:
            res=str(i)
            
            f2.write(res.upper())
