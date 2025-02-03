from random import choice 

def get_random_response() -> str:
    random_list: list[str] = [
        "Please try writing someting more descriptive",
        "I dind't understand. Can you rephrase that please?",
        "I can't answer that yet. I am sorry",
    ]
    
    return choice(random_list)

if __name__ == '__main__':
    for i in range(5):
        print (get_random_response())