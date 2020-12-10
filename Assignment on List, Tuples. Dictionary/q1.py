list_of_words=['Africa' , 'Ball' , 'Cactus' , 'Doll' , 'Escape' , 'Fire' , 'Game']

ls=[]
print ("Our initial list: ",list_of_words)

for i in range(0,len(list_of_words)):

    ls.append(list_of_words[i][:1])



print("New list: ",ls)
