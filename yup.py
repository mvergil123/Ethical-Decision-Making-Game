# The code for the portfolio thingy

# imports
import os, random

# function for the introduction
def intro():
    # clear terminal
    os.system("clear")
    # present intros 
    print("Welcome!")
    print(" ")
    print("This is a choose your own outcome game.")
    print(" ")
    print("I will give you 5 different scenarios and you choose your outcome by typing the number of your desired ethical approach." )
    print(" ")
    print("For each of your answers, you will recieve points based on which one you pick.")
    print(" ")
    print("Press ENTER to begin")
    input(" ")
    os.system("clear")

# function to get your points
def points(score, rando):
    score += rando
    return score

# function to come up with the random number
def random_num():
    num = random.randint(1,100)
    return num

# football story
def football(score):
    # describe the scenario
    print("You are a professional soccer player and you are playing in a match.")
    print("You are in the opponent’s box, about to shoot and you trip on yourself and fall over.") 
    print("The referee marks a penalty kick in favor of your team as from their perspective, the defender tripped you.")
    print("Which approach would you take in this scenario?:")
    print(" ")
    print("1) Confucian")
    print("2) Utilitarianism")
    print("3) Deontology")
    print(" ")
    # get decision
    num = input("Type in your choice: ")
    print(" ")
    allowed = ["1","2","3"]
    while num not in allowed:
        print("Nice try....")
        num = input("Type in your choice: ")
    if num == "1":
        print("You are focused on your relations with the team and respect the referee’s authority so you decide to take the pen.")
    elif num == "2":
        print("You take the pen as you are prioritizing the happiness of your team and the fans.")
    else:
        print("You decide to be honest and tell the referee that you tripped and no penalty kick should be awarded")

    print(" ")

    # generate the points
    won = random_num() 
    print("You recieved", won, "points! Good Job!")    
    new_score = points(score, won)
    print("You now have", new_score, "points!!")

    # clear screen 
    print(" ")
    print("Press ENTER to continue")
    input(" ")
    os.system("clear")

    return new_score


# car scenario
def car(score):
    # describe the scenario
    os.system("clear")
    print("You are attempting to park your car and while doing so, you scratch a nearby car.")
    print("Nobody is in the lot and you can make a run for it.")
    print("Which approach would you take in this scenario?:")
    print(" ")
    print("1) Confucian")
    print("2) Utilitarianism")
    print("3) Deontology")
    print(" ")
    # get decision
    num = input("Type in your choice: ")
    print(" ")
    allowed = ["1","2","3"]
    while num not in allowed:
        print("Nice try....")
        num = input("Type in your choice: ")
    if num == "1":
        print("You leave a note with your information and take responsibility for your actions.")
    elif num == "2":
        print("Leaving would be much cheaper but you would have to live with the guilt of hitting someone’s car so you leave a note. ")
    else:
        print("You decide to be honest and leave a note.")

    print(" ")
    # generate the points
    won = random_num() 
    print("You recieved", won, "points! Another day, another w for the ogs")    
    new_score = points(score, won)
    print("You now have", new_score, "points!!")

    # clear screen 
    print(" ")
    print("Press ENTER to continue")
    input(" ")
    os.system("clear")

    return new_score




# scholarship scenario
def scholarship(score):
    # describe the scenario
    os.system("clear")
    print("You discover that your friend is struggling financially and cannot afford tuition.")
    print("You are in a much more financially stable position")
    print("but you have the opportunity to apply for a prestigious scholarship that would secure your own academic future but, in doing so, you prevent your friend from applying.")
    print("Which approach would you take in this scenario?:")
    print(" ")
    print("1) Confucian")
    print("2) Utilitarianism")
    print("3) Deontology")
    print(" ")
    # get decision
    num = input("Type in your choice: ")
    print(" ")
    allowed = ["1","2","3"]
    while num not in allowed:
        print("Nice try....")
        num = input("Type in your choice: ")
    if num == "1":
        print("You respect your friend so you tell them to also apply. ")
    elif num == "2":
        print("Happiness for all so you tell your friend to apply.")
    else:
        print("You decide that applying for the scholarship aligns with your moral duty to pursue your education")
        print("so you fill out the application while also telling your friend")

    print(" ")

    # generate the points
    won = random_num() 
    print("You recieved", won, "points! Noice!!")    
    new_score = points(score, won)
    print("You now have", new_score, "points!!")

    # clear screen 
    print(" ")
    print("Press ENTER to continue")
    input(" ")
    os.system("clear")

    return new_score





# exam scenario
def exam(score):
    # describe the scenario
    os.system("clear")
    print("You are walking behind your RUSHED math professor when you notice that they have dropped a sheet of paper.")
    print("You pick it up and notice that it contains the answers to the next exam.")
    print("Which approach would you take in this scenario?:")
    print(" ")
    print("1) Confucian")
    print("2) Utilitarianism")
    print("3) Deontology")
    print(" ")
    # get decision
    num = input("Type in your choice: ")
    print(" ")
    allowed = ["1","2","3"]
    while num not in allowed:
        print("Nice try....")
        num = input("Type in your choice: ")
    if num == "1":
        print("You respect your relationship with your professor and respect their authority so you returned the paper.")
    elif num == "2":
        print("Focused on the greater good, you return the sheet of paper to your professor to maintain fairness among your classmates. ")
    else:
        print("You decide to be honest so you return the sheet of paper to your professor.")

    print(" ")

    # generate the points
    won = random_num() 
    print("You recieved", won, "points! Noice!!")    
    new_score = points(score, won)
    print("You now have", new_score, "points!!")

    # clear screen 
    print(" ")
    print("Press ENTER to continue")
    input(" ")
    os.system("clear")

    return new_score



# absent scenario
def absent(score):
    # describe the scenario
    os.system("clear")
    print("You really don’t want to go to class but your professor takes attendance so you have to come up with an excuse as to why you were absent.")
    print("You settle with the idea that your childhood, pet goldfish passed away so you have to attend its funeral (you never had a goldfish)")
    print("The next day your professor asks you how it went....")
    print("Which approach would you take in this scenario?:")
    print(" ")
    print("1) Confucian")
    print("2) Utilitarianism")
    print("3) Deontology")
    print(" ")
    # get decision
    num = input("Type in your choice: ")
    print(" ")
    allowed = ["1","2","3"]
    while num not in allowed:
        print("Nice try....")
        num = input("Type in your choice: ")
    if num == "1":
        print("You respect your relationship with your professor so you decide to be honest and tell them the truth, hoping for forgiveness. ")
    elif num == "2":
        print("The pros of your “dead goldfish” outweigh the cons so you decide to stick with the lie.")
        print("game is game")
    else:
        print("You decide to be honest and tell your professor the truth about your imaginary fishie.")

    print(" ")

    # generate the points
    won = random_num() 
    print("You recieved", won, "points! Noice!!")    
    new_score = points(score, won)
    print("You now have", new_score, "points!!")

    # clear screen 
    print(" ")
    print("Press ENTER to continue")
    input(" ")
    os.system("clear")

    return new_score





# create the final screen 
def final(score):
    os.system("clear")
    print("You won with", score, "points!!!!")
    print(" ")
    print("The points, however, were randomly generated because no answer is wrong...")
    print(" ")
    print("Ultimately, no matter what you decide to do, someone will always judge you so do whatever you think is right and you will also win in life!!")
    print("There isn't a valid reason to be judged unless you pour your milk before your cereal.... :)")
    print(" ")
    print("Thank you for playing!!")

    # clear screen 
    print(" ")
    print("Press ENTER to exit")
    input(" ")
    os.system("clear")




def main():
    # Create a list of your story functions
    stories = [football, car, scholarship, exam, absent]

    # Shuffle the order of stories using random.shuffle
    random.shuffle(stories)

    # Loop through the shuffled list and play each story
    pts = 0
    for story in stories:
        pts = story(pts)
    return pts




if __name__ == "__main__":
    intro()
    pts = main()
    final(pts)