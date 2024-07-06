print("ZOMBOCALYPSE WALMART SUPREME! THE VIDEOGAME")
print("")
answer = input("Would you like to play? (Yes/No) ").lower().strip()

if answer == 'yes':
    answer = input("You wake up in a dark and empty Walmart in the middle of the night. Lights are buzzing and there's packages scattered all over the floor. Lights are flickering. You see an AXE and a TWINKIE on the ground in front of you. Which one do you pick up: the AXE or the TWINKIE? ").lower().strip()
    if answer == 'axe':
        answer = input("You pick up the axe. The steel blade glistens in your palms. A thought passes through your mind- 'I wonder if there's any zombies around here!' Luckily for you, there is! A zombie stumbles around the corner. You grip the axe and a choice comes to you. 'Should I chop off his head, or go through the top of his skull?' What's it gonna be? CHOP the head off or go through his SKULL? ").lower().strip()
        if answer == 'chop':
            answer = input("You chop off the head of the unlucky zombie in front of you. He topples like a stack of bricks. A GUN, a KNIFE, and a LIGHTER fall out of the vest he was wearing. Which one do you pick up? ").lower().strip()
            if answer == 'gun':
                print("You pick up the gun. Two zombies come at you. You blast away at both of them and successfully find your way out of the Walmart. Congratulations! You’ve won the game!")
            elif answer == 'knife':
                print("You pick up the knife. Knowing that the way out of the store is back toward the front of the store, you start moving that way. Suddenly two zombies come stumbling at you! You pull the knife out and stab the first one in the eyeball. However, the second zombie chomps into your brains right after. You are now a zombie!!! Sorry, you lost the game, unless you wanted to be a zombie, I guess then in that case you’ve won.")
            elif answer == 'lighter':
                print("You pick up the lighter, and see a can of gasoline on a counter as you head toward the exit in the store, which you carry in your other hand. Suddenly two zombies appear walking around the corner! You pour gasoline on them and kick them both back flat. You light them on fire and watch a hazy smoke-filled blaze of fury as two zombies learn who they shouldn’t mess with. Congratulations! You have won the game.")
        elif answer == 'skull':
            answer = input("You swing the axe over your head and into the skull of the quite surprised zombie. Brains splatter everywhere. You look for an escape from this zombie infested Walmart. Now that the zombie is dead, your escape from the building is now covered. Do you EXIT the building, or do you GOBBLE up all the twinkies in the twinkie isle and then leave the building? ").lower().strip()
            if answer == "exit":
                print("You exit the building feeling great. You have successfully killed your first zombie and are ready to begin your new life in the zombocalpse! Congratulations, you have won the game.")
            elif answer == "gobble":
                print("You decide to gobble up all the twinkies in the twinkie isle. 30 minutes later, you’re feeling bloated, sluggish and hazy. Thirty zombies come around the corner but you’re too over encumbered to move swiftly enough to escape them. You are devoured. Sorry! You have lost the game.")
            else:
                print("That is not an available option. You lose!")
    elif answer == 'twinkie':
        answer = input("You pick up the twinkie. Do you OPEN the twinkie package to eat it or do you put it in your POCKET for later? ").lower().strip()
        if answer == "open":
            answer = input("You open up the twinkie and start stuffing your melon, but just as you’re about to finish it, a zombie tumbles around the corner, with brain-eating-lust in his eyes as he looks at your melon that you were just stuffing a twinkie into! Do you PUNCH him in the face, or RUN away? ").lower().strip()
            if answer == 'punch':
                print("You punch the zombie in the face, however, you punch too low and the zombie gets a bite out of your hand. You know the rules! You’ve watched the Walking Dead. You have been infected with the zombocalypse virus and will soon be a virus. ‘I’m not going out a sorry sot!’ you say! You spend the rest of your day eating every delicious treat you can find in the store, and then fade away into becoming a zombie. We don’t do suicide in this game because that’s too drastic. Sorry! You’ve lost the game.")
            elif answer == 'run':
                print("You run! Good for you! You escape the zombie! You find the front entrance and make it out alive. Congratulations! You have won the game!")
            else:
                print("That is not an available option. You lose!")
        elif answer == "pocket":
            answer = input("You put the twinkie in your pocket for later. You decide to walk down the aisle some more. All of a sudden, a zombie stumbles around the corner with a hungry look on his face! You have no weapons, except for, ‘gasp!’ a twinkie! Do you throw the twinkie at the unsuspecting zombie to STUN him and secure your escape? Or do you EAT it so that your last moments in life can be spent in bliss? ").lower().strip()
            if answer == "stun":
                print("You throw the twinkie at the zombie to stun him! It does nothing. What did you expect it to do? It’s a twinkie! The thing probably weighs 2 ounces, temper your expectations you silly billy. The zombie continues forward and eats your brains. Sorry! You’ve lost the game.")
            elif answer == "eat":
                print("‘I’m not going out of this life hungry!!!!’ you yell out into the void. You open the wrapper, throwing it aside as the zombie stumbles forward. You find the bliss you were looking for. But what’s this? The zombie has just slipped on the wrapper you threw on the ground! He hit his head on the shelf next to you and is down for the count! Congratulations! You have accidentally won the game!!!!!")
        else:
            print("That is not an available option. You lose!")
    else:
        print("That is not an available option. You lose!")
else:
    print("That's too bad!")