def main(): 
    print("The game is simple, you will be asked a series of questions and you will try to\nprovide the correct answer to each question. Your answers should be word long")
    questions = [
    "what is the capital of France?",
    "What is the capital of Cameroon?",
    "What is the capital of the United States?",
    "What is the capital of Nigeria?",
    "What is the capital of South Africa?",
    "What has keys but can't open locks? ",
    "What has a head, a tail but has no body? ",
    "What has a neck but no head?",
    "What has a thumb and four fingers but is not a hand?",
    "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
    "The more you take, the more you leave behind. What am I?",
    "What has a face and two hands but no arms or legs? ",
    "I'm light as a feather, but even the world's strongest man couldn't hold me for much longer than a minute. What am I?",
    "What has cities, but no houses; forests, but no trees; and rivers, but no water?",
    "What has one eye but can't see?",
    "What has many keys but can't open a single lock?",
    "I'm tall when I'm young and short when I'm old. What am I?",
    "I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
    "I'm full of holes, but I can still hold a lot of water. What am I?",
    "What has keys but can't open locks?",
    "What can travel around the world while staying in a corner?",
    "The person who makes it, sells it. The person who buys it, never uses it. The person who uses it, never knows they're using it. What is it?",
    ]

    answers = [
    "Paris", "Yaounde", "Washington", "Abuja", "Pretoria", "piano", "coin", "bottle", "glove", "echo", "footsteps", "clock", "breath", "map", "needle", "piano", "candle", "fire", "sponge", "keyboard", "stamp", "coffin"
    ]

    score = 0
    response="yes"
    # Loop through the questions and answers
    for i in range(len(questions)):
        if response.lower() == "no":
            print("Thank you for playing my game!")
            break
        else:
            print(questions[i])
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == answers[i].lower():
                print("Correct!")
                score += 1
                print("You scored: ", score, "out of", len(questions))
                response=input("Good guess... Would you like to continue playing the game? (yes/no): ")
            else:
                print("Incorrect! answer is: ", answers[i])
                print("You scored: ", score, "out of", len(questions))
                response=input("Would you like to continue playing the game? (yes/no): ")
        if i == 4:
                print("Welcome to tier 2 of the game where the questions will be harder!")
        elif i == 10:
                print("Welcome to tier 3 of the game where the questions will be even harder!")
        elif i == 15:
                print("Welcome to tier 4 of the game where the questions will be the hardest!")
        elif i == 22:
                print("Congratulations! You have completed the game!")
                print("Thank you for playing my game!")
                break      
print("Welcome to my small guessing game project to test your knowledge!\n")
reply=input("Would you like to play the guessing game? (yes/no): ")
if reply.lower() == "yes":        
    if __name__ == "__main__":
        main()
else:
      print("Thank you for your time and goodbye!")