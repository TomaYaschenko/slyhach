my_dict={"Derjach Pavlo":[7,8,9],'Naumov Max':[10,12,9,19],'Sergob Serg':
         [6,10,2,11,12]}
def ser(x):
    return sum(x)/len(x)
m_x=['',0]
m_n=['',15]
for k,v in my_dict.items():
    if ser(v)>m_x[1]:
        m_x[0],m_x[1]=k,ser(v)

    if ser(v)<m_n[1]:
        m_n[0],m_n[1]=k,ser(v)
print(m_x)
print(m_n)
        
    
