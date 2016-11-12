def dicegame(score):
    result = 0
    
  
    if len(score)<=5:
        score_dict = dict((i, score.count(i)) for i in score)
    
        
        if score_dict.get(1)>=3:
            result+=1000
            score_dict[1]-=3
        
        for n in score_dict:
            if score_dict.get(n)>=3:
                result+=n*100
                score_dict[n]-=3
        
        if 1 in score_dict:
            result+=score_dict[1]*100
        
        if 5 in score_dict:
            result+=score_dict[5]*100
    else:
        print "Invalid Length"
        
    
    
    return result


print dicegame([1,1,1,45])