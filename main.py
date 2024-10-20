import re
import long_response as long



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
        
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello, how can I assist you today? ', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I am well ! thank you for asking, what about you,how are you? ', ['how', 'are', 'you', 'doing'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('my name is talkytech, and i am a chatbot, well what is your name? ' ,['is','your','name'], single_response=True)
    response('namaste',['namaste'],single_response=True)
    response('Good night, and good luck on your future endeavors',['good night','gn'],single_response=True)
    response('good morning! have a great day',['good morning','gm'],single_response=True)
    response('tum ho humare',['shayari','shayri'], single_response=True)
    response('haan mujhe hindi aati hai! kaise madad kar sakta hu aapki',['hindi'],single_response=True )
    response('kya chahiye ? kuch poochna hai ya bas baat karna hai',['bolo'],single_response=True)
    response('main bas yahan tumse baat kar raha hu. aap kya kar rahe ho?',['kar','kya','rahe','ho'],single_response=True)
    response('I can understand and communicate in english and hindi both',['language'],single_response=True)
    response('a computer program designed to simulate conversation with human users, especially over the internet.',['what','chatbot'],single_response=True)
    response('that\'s great!',['fine'],single_response=True)      
    response('nice name!',['my','name','i am'],single_response=True)
             # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_CHATBOT,['chatbot','work','of'], required_words=['work','chatbot'])
   
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('TALKY TECH : ' + get_response(input('YOU : ')))
