# importing libraries
import spacy

# loaded the language model
nlp = spacy.load('en_core_web_md')

# created a doc object by processing the input text
tokens = nlp('skirt table blouse')

# iterated over each token in the doc
for token1 in tokens:

    # iterated over each token again to compare with other tokens
    for token2 in tokens:

        # checked if both tokens have vectors
        if token1.has_vector and token2.has_vector:

            # calculated the similarity between the tokens
            similarity = token1.similarity(token2)
        else:

            # if either token doesn't have a vector, assigned a similarity of 0.0
            similarity = 0.0

        # printed the tokens and their similarity scores
        print(token1.text, token2.text, similarity)

print("""
1.  Cat - monkey, the similarities between cat and monkey is 0.5351813.
It is above 50% because although they are both animals they are not the same animal

Cat - banana, the similarity score between cat and banana is 0.28
It is quite low because cat and banana have nothing in
common because a cat is an animal and a banana is a fruit

Monkey - banana, the similarities between cat and banana is 0.45207784.
The similarity rate is quite high because monkeys like eating bananas so the model was able to connect the two together
even tho it's an animal and fruit

MY OWN EXAMPLE:

for my own example I used the code above to check the similarity scores between skirt, table, blouse

skirt - table, the similarity score between skirt and table is 0.19
It is quite low because skirt and table heave nothing in
common because a table is a piece of furniture and a skirt is a piece of clothing item

blouse - skirt, the similarities between skirt and blouse is 0.99
These two items' similarity score is quite high because they are both articles of clothing 

table - blouse, the similarity score between blouse and table is 0.19
It is quite low because skirt and table heave nothing in
common because a table is a piece of furniture and a blouse is a piece of clothing item

2. The main difference between the two models is the size and complexity of their word vectors.
When I run the program the with the en_core_web_sm the similarity scores are lower than when you run the program with
the en_core_web_md
""")
