#Tasks:
#
#    1.) Turn your compliment generator into a random sentece generator
#        a.) Change your starting sentence (to your choice). In addition to have a place
#                for an adjective to be inserted, make a place for a noun.
#        b.) Create a list of nouns.
#        c.) Add another if statement inside the for loop
#        
#    2.) Can you do this for more parts of speech?
#
#    Tips: If your word ends on a period or other punctuation, instead of
#        if word == "*adj":
#        try
#        if "*adj" in word: 
#
#
#  Side note to self: The reason I was able to swap multiple words in a sentence was bc of different indexCount positions. 
#



#1) PART ONE --- 
import random
sentenceGen = "For dinner, I ate *noun and it was *adj."
sentenceGen = sentenceGen.split()
nouns = ["caesar salad", "filet mignon", "pepperoni pizza", "cheeseburger", "brocolli cheddar soup"]
adjectives  = ["delicious", "alright", "spicy", "disgusting", "mouth-watering", "hot", "nutritious"]
indexCountA = 0
indexCountB = 0
st = ""
for word in sentenceGen:
    if "*adj" in word:
        wordChoice = random.choice(adjectives)
        sentenceGen[indexCountA] = wordChoice
    indexCountA += 1
    if word == "*noun":
        wordChoice = random.choice(nouns)
        sentenceGen[indexCountB] = wordChoice
    indexCountB += 1
print(sentenceGen)
for word in sentenceGen:
    st += word + " "
print(st)


#2.) PART TWO --- 
sentenceGen = "For *food, *who ate *noun and it was *adj."
sentenceGen = sentenceGen.split()
nouns = ["caesar salad", "filet mignon", "pepperoni pizza", "cheeseburger", "brocolli cheddar soup"]
adjectives  = ["delicious", "alright", "spicy", "disgusting", "mouth-watering", "hot", "nutritious"]
foods = ["breakfast", "lunch", "dinner"]
who = ["I", "we", "Tom", "Stacey", "Samatha"]
indexCountA = 0
indexCountB = 0
indexCountC = 0
indexCountD = 0
st = ""
for word in sentenceGen:
    if "*adj" in word:
        wordChoice = random.choice(adjectives)
        sentenceGen[indexCountA] = wordChoice
    indexCountA += 1
    if word == "*noun":
        wordChoice = random.choice(nouns)
        sentenceGen[indexCountB] = wordChoice
    indexCountB += 1
    if "*food" in word:
        wordChoice = random.choice(foods)
        sentenceGen[indexCountC] = wordChoice
    indexCountC += 1
    if word == "*who":
        wordChoice = random.choice(who)
        sentenceGen[indexCountD] = wordChoice
    indexCountD += 1
    
print(sentenceGen)
for word in sentenceGen:
    st += word + " "
print(st)
