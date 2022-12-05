import numpy as np
import random

def get_data():
    data_sample = "Harry Potter.txt"
    text_data = open(data_sample, 'r', encoding="utf8").read()
    text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')  
    
    to_change=['.',',','!','?',';','"',"'","“","”","(",")","-",":","`",'|','—']
    log_change=dict()
    for element in to_change:
        index=list()
        for i in range(0,len(text_data)):
            if element in text_data[i]:
                text_data[i]=text_data[i].replace(element,'')
                index.append(i)
        log_change[element]=index
        
    
    next_index=1
    for key in log_change:
        for elment in log_change[key]:
            #text_data.insert(int(elment)+next_index, key)
            next_index+=1
            
    text_data=list(map(str.lower,text_data))
    text_data = list(filter(None, text_data))
    print(text_data)
            

    return(text_data)

def get_set (raw_text):
    set_text=list(set(raw_text))
    set_text.sort()
    return(set_text)

def get_location(raw_text,set_text):
    #Create {word:{empty list]}
    location_word=dict()
    for element in set_text:
        index=list()
        location_word[element]=index
    
    #Goes through each word in original text and uses it as a key -> then appends the index in the list.
    for i in range (0,len(raw_text)):
        location_word[raw_text[i]].append(i)
    #print(location_word)
    
    #Create {word:{empty list]}
    next_word=dict()
    for element in set_text:
        index=list()
        next_word[element]=index
        
    for key in location_word:
        #print(key)
        for element in location_word[key]:
            #print(element)
            try:
                next_word[key].append(raw_text[int(element)+1])
                #print(key)
                #print(next_word[key])
            except IndexError:
                break
                      
    return(next_word)

def initial_matrix (set_text,next_word):
    x_axis=set_text
    y_axis=set_text
    markov_matrix=list()

    for j in y_axis:
        line=list()
        for i in x_axis:
            #print(i)
            if i in next_word[j]:
               #print(i)
               #print(next_word[j])
               probability=next_word[j].count(i)/len(next_word[j])
               #print(probability)
               line.append(probability)
            else:
                line.append(0) 
        markov_matrix.append(line)
    
    #Check columns
    #A=list()
    #for i in range (1,4):
    #    B=list()
    #    for j in range (1,4):
    #        B.append(j)
    #    A.append(B)
    #print(A)
    
    #for i in range (0,3):
    #    sum=0
    #    for j in range (0,3):
    #        sum+=A[j][i]
    #    print(sum)
    
    markov_matrix=np.array(markov_matrix)
    markov_matrix=markov_matrix.transpose()
    
    for i in range (0,len(set_text)):
        sum=0
        for j in range (0,len(set_text)):
            sum+=markov_matrix[j][i]
        #print(sum)
        
    return(markov_matrix)

def get_initial_x(set_text):
    initial_x=random.randint(0,len(set_text))
    print(set_text[initial_x],end=" ")
    x=list()
    for i in range (0,len(set_text)):
        x.append([0])
        
    x[initial_x]=[1]
    #print(x)
    
    return(x)
        
          
def main():
    raw_text=get_data()
    #print(raw_text)
    
    set_text=get_set(raw_text)
    #print(len(set_text))
    #print(set_text)
    
    next_word=get_location(raw_text,set_text)
    
    A=initial_matrix(set_text,next_word)
    
    while True:
        print('Generate a sentance:')
        s=input()
        if s=='t':
            x=np.array(get_initial_x(set_text))
    
            for i in range (0,30):
                x=np.matmul(A,x)
                check=0
                for j in range (0,len(x)):
                    if x[j][0]>=check:
                        check=x[j][0]
                        index=j     
                print(set_text[index],end=" ")
        else:
            break
    
main()