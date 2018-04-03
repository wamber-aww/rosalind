def countNt(string):
    nt = {}
    for i in string:
        if i not in nt:
            nt[i] = 1
        else:
            nt[i] += 1
    
    print nt['A'], nt['C'], nt['G'], nt['T']
