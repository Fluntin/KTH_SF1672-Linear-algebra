def get_data():
    data_sample = "Stonepastures.txt"
    text_data = open(data_sample, 'r', encoding="utf8").read()
    text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')  
    
    to_change=['.',',','!','?',';','"',"'","“","”","(",")","-",":"]
    #add split row to the raw text file.
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
            text_data.insert(int(elment)+next_index, key)
            next_index+=1
    #print(text_data)

    return(text_data)

def get_set (raw_text):
    set_text=list(set(raw_text))
    set_text.sort()
    #print(set_text)
    return(set_text)

def get_location(raw_text,set_text):
    location_word=dict()
    for element in set_text:
        index=list()
        location_word[element]=index
    
    for i in range (0,len(raw_text)):
        location_word[raw_text[i]].append(i)
    
    next_word=dict()
    for element in set_text:
        index=list()
        next_word[element]=index
        
    for key in location_word:
        for element in location_word[key]:
            try:
                next_word[key].append(raw_text[int(element)+1])
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
            if i in next_word[j]:
               probability=next_word[j].count(i)/len(next_word[j])
               line.append(probability)
            else:
                line.append(0) 
        markov_matrix.append(line)
    
    return(markov_matrix)
                
        
def main():
    raw_text=get_data()
    set_text=get_set(raw_text)
    next_word=get_location(raw_text,set_text)
    markov_matrix=initial_matrix(set_text,next_word)
    
    
    for element in markov_matrix:
        print(sum(element))
    #print(markov_matrix)
    
    #print(raw_text)
    #print(next_word)
    #print(len(raw_text))
    #print(len(set_text))

    print("done")
    
    
    
    
main()