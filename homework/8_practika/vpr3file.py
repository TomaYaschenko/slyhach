from sys import argv
file=open(argv[1])
for i in file:
    first,second=map(lambda s: s.split(),i.split(';'))
    first=list(map(int,first))
    second=list(map(int,second))
    avg=sum(first)//len(first)
    m_d=sum(first)%len(first)
    if [avg,m_d]==second:
        print('True')
    else:
        print('False')
    print(first,second)
    
       
