import random
print("hello human, I am the magic 8 ball!")
responses = ["yes","no","ask again later","definitley","of course","hell no"]
question_words = ["am","will","what","which","when","is"]


while True:
    question  =  input("Ask any question! Enter stop to end: ").lower()
    first_word = question.split()[0]

    if question  ==  "stop":
        break
    elif '?' in question and first_word in question_words:
        print(random.choice(responses))
    else:
        print("display: sorry, that is not a question!")









