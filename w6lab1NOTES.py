import random

#sentence = "Hello, you are looking good today."
#sentence = sentence.split()
#print(sentence)
#sentence[4] = "striking"     #change elements in a list
#print(sentence)


#sentence = "Hello, you are looking good today."
#sentence = sentence.split()
#for word in sentece:
#    print (word)


#abc = ["Red", "Yellow", "Green", "Orange"]
#print (abc)
#myInput = input("Hi")




 
sentence = "Hello, you are looking *adj today."
sentence = sentence.split()
adjectives = ["beautiful", "handsome", "pretty", "warm", "fantastic"]
indexCount = 0
st = ""
for word in sentence:
        if word == "*adj":
            wordChoice = random.choice(adjectives)
            sentence[indexCount] = wordChoice
        indexCount+=1
       
print(sentence)
for word in sentence:
    st += word + " "
print(st)
