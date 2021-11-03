# delit the inside dictionary c item
dic= {
    1: 'NAVGURUKUL',
    2: 'IN',  
        3:{    
            'A' : 'WELCOME',
            'B' : 'To',
            'C' : 'DHARAMSALA'
        }
    }
del dic[3]["C"]
print(dic)
