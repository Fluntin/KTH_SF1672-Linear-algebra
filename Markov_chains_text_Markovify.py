import markovify
with open("Lord of the Rings.txt", 'r', encoding="utf8") as f:
    data = f.read() 
data_model = markovify.Text(data)
for i in range(3):
    print(data_model.make_sentence())    
for i in range(3):
    print(data_model.make_short_sentence(100))