def euler2():
    sum = 0
    seqm2 = 0
    seqm1 = 1
    seq = 2
    while seq < 4000000:
        if (seq % 2 == 0):
            sum += seq
        seqm2 = seqm1
        seqm1 = seq
        seq = seqm1 + seqm2
    print(sum)
    
        
