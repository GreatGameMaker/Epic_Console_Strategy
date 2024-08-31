from time import sleep
from random import randint, choice
import keyboard
from os import _exit


print("\n\nHello, player!\n\nDo you think our planet is the only one with life? I will answer for you - no. So...\n\nThe action took place on some planet far from Earth, called '6kjkh5fb1d5j' (the name\n\nisn't random), where the confrontation between the two only states on the planet\n\nbegan. GovnoCoders opposed ProgaMasters out of envy of their success. The ruler of\n\nGovnoCoders Silly Monkey didn't like the fact that the inhabitants of his state moved\n\nto ProgaMasters, even though it was good for them. There they could work among the same\n\nprofessionals in their field as themselves. So, after years of enmity, Silly Monkey\n\ndecided to attack ProgaMasters, since he had a numerical superiority of 100 times\n\n(then look at the population in both states). He captured village after village,\n\ncity after city. And so, when all the generals lost faith, they called You.\n\nYes, dear player, You. You are the last hope to save ProgaMasters. So...")
name=input("\n\nEnter Your name, captain\n\n")
soldiers=3
level=1
foes=2
foe_level=2
foe_name="Dunger Master"
left_space=5
mid_space=40
min_space=20
state="c"
reward=200
campaign_count=0
money=0
relationship=5

# 237 symbols max

def war(soldiers,level,foes,foe_level,foe_name,state,reward,money,relationship, campaign_count):
    
    lost=0
    foes_lost=0
    all=soldiers
    foes_all=foes
    action=''
    soldiers_attack=0
    is_first=True
    
    def view():
        view_soldiers=soldiers
        view_foes=foes
        soldiers_mask="*"
        foes_mask="*"
        print(f"Name:{10*' '}{name}{' '*(110-len(name))}{foe_name}\nSoldiers:{6*' '}{soldiers}{' '*(110-len(str(soldiers)))}{foes}\nLevel:{9*' '}{level}{' '*(110-len(str(level)))}{foe_level}\nLast lost:{' '*5}{lost}{' '*(110-len(str(lost)))}{foes_lost}\nLost:{10*' '}{all-soldiers}{' '*(110-len(str(all-soldiers)))}{foes_all-foes}\n\n")
        

        if soldiers>9990:
            view_soldiers=(soldiers//100)+int(bool(soldiers%100))
            soldiers_mask="&"
        elif soldiers>=1000:
            view_soldiers=(soldiers//10)+int(bool(soldiers%10))
            soldiers_mask="#"
        else:
            view_soldiers=soldiers
            soldiers_mask="*"

        if view_soldiers<=100:
            for i in range(9,1,-1):
                if view_soldiers%i==0:
                    rows=i
                    break
                if view_soldiers==1:
                    rows=1
                    break
                if i==2:
                    rows=5
        elif view_soldiers<=250:
            for i in range(15,5,-1):
                if view_soldiers%i==0:
                    rows=i
                    break
                if i==6:
                    rows=10
        elif view_soldiers<=500:
            for i in range(20,9,-1):
                if view_soldiers%i==0:
                    rows=i
                    break
                if i==10:
                    rows=15
        elif view_soldiers<1000:
            for i in range(30,14,-1):
                if view_soldiers%i==0:
                    rows=i
                    break
                if i==15:
                    rows=25

        if foes>9990:
            view_foes=(foes//100)+int(bool(foes%100))
            foes_mask="&"
        elif foes>=1000:
            view_foes=foes//10
            foes_mask="#"
        else:
            view_foes=foes
            foes_mask="*"


        if view_foes<=100:
            for i in range(9,1,-1):
                if view_foes%i==0:
                    foes_rows=i
                    break
                if view_foes==1:
                    foes_rows=1
                    break
                if i==2:
                    foes_rows=5
        
        elif view_foes<=250:
            for i in range(15,5,-1):
                if view_foes%i==0:
                    foes_rows=i
                    break
                if i==6:
                    foes_rows=10
        
        elif view_foes<=500:
            for i in range(20,9,-1):
                if view_foes%i==0:
                    foes_rows=i
                    break
                if i==10:
                    foes_rows=15
        elif view_foes<1000:
            for i in range(30,14,-1):
                if view_foes%i==0:
                    foes_rows=i
                    break
                if i==15:
                    foes_rows=25

            
        while view_soldiers!=0 or view_foes!=0:
            if view_soldiers>=view_soldiers//rows and view_foes>=view_foes//foes_rows: print(left_space*' ',soldiers_mask*(view_soldiers//rows),(120-mid_space-left_space-view_soldiers//rows)*' ',foes_mask*(view_foes//foes_rows))
            elif view_soldiers>=view_soldiers//rows and view_foes<view_foes//foes_rows: print(left_space*' ',soldiers_mask*(view_soldiers//rows),(120-mid_space-left_space-view_soldiers//rows)*' ',foes_mask*(view_foes%foes_rows))
            elif view_soldiers<view_soldiers//rows and view_foes>=view_foes//foes_rows: print(left_space*' ',soldiers_mask*(view_soldiers%rows),(120-mid_space-left_space-view_soldiers//rows)*' ',foes_mask*(view_foes//foes_rows))
            elif view_soldiers<view_soldiers//rows and view_foes<view_foes//foes_rows: print(left_space*' ',soldiers_mask*(view_soldiers%rows),(120-mid_space-left_space-view_soldiers//rows)*' ',foes_mask*(view_foes%foes_rows))
            view_soldiers-=view_soldiers//rows
            view_foes-=view_foes//foes_rows
            if rows>1: rows-=1
            if foes_rows>1: foes_rows-=1

    while soldiers>0 and foes>0 and action!='r':        
        view()
        print(f"Press:\n<a> to attack {foe_name}'s army\n<r> to run away and lose this battle. Enemy has chance kill your running army\n<t> to try make {foe_name}'s army surrender. You'll give all of remain soldiers.")
        keys=['a','r','t']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        sleep(0.5)
    
        lost=0
        foes_lost=0

        
        if action=='a':
            print('\nAttack!\n')
            foes_lost=min(randint(int((soldiers*level)/(8*foe_level)),int(soldiers*level/(4*foe_level))),foes)
            soldiers_attack+=soldiers
            if soldiers<4 and foes<4 and (soldiers>foes or foe_level<=level): foes-=1
            elif soldiers<4 and foes<4 and (foes>soldiers or foe_level>level): soldiers-=1
        if action=='r':
            print('\nRun!\n')
            if randint(0,5)!=0:
                killed_running_soldiers=randint(1,soldiers)
                print('Enemy killed', killed_running_soldiers ,'soldiers')
                soldiers-=killed_running_soldiers
            else: print("You've run away with all your remain soldiers")
        if action=='t' and not is_first:
            print('\nSurrender, Enemy!\n')
            if soldiers//10<foes: print("They don't want to surrender")
            else:
                soldiers+=foes
                foes=0
                print("\nCongratulations! You've made them surrender!\n")
        elif action=='t': print("\nEnemy don't want to surrender at first step\n")
        is_first=False
        lost=min(randint(int((foes*foe_level)/(8*level)),int(foes*foe_level/(4*level))),soldiers)
        if action!='r':
            foes-=foes_lost
            soldiers-=lost
    view()
    if not foes:
        if state=='q':
            money_change=reward-(soldiers_attack//20)
            print(f"You win!\nReward: {money_change} money ({reward} - {soldiers_attack//20})\nPress <space> to continue")
        elif state=='c':
            money_change=reward-(soldiers_attack//20)
            campaign_count+=1
            relationship+=0.25
            print(f"You win!\nReward: {money_change} money ({reward} - {soldiers_attack//20})\nRelationship: {round(relationship,2)} (+0.25)\nPress <space> to continue")
        else:
            money_change=randint((foes_all*foe_level)-(soldiers_attack//20),foes_all*foe_level*2-(soldiers_attack//20))
            relationship+=0.1
            print(f"You win!\nReward: {money_change} money ({reward} - {soldiers_attack//20})\nRelationship: {round(relationship,2)} (+0.1)\nPress <space> to continue")
        relationship=round(relationship,2)
        
        money+=money_change
    else:
        money_change=soldiers_attack//20
        if action=='r':
            relationship-=0.5
            print(f"{foe_name} win!\nYou lost: {money_change} money\n Relationship: {relationship} (-0.5)\nPress <space> to continue")
        else:
            relationship-=0.2
            print(f"{foe_name} win!\nYou lost: {money_change} money\n Relationship: {relationship} (-0.2)\nPress <space> to continue")
        money-=money_change
    sleep(0.5)
    keyboard.wait("space")
    home(soldiers, level, money, campaign_count,relationship)





def home(soldiers, level, money, campaign_count,relationship):

    money=round(money,2)

    place=["ProgaMasters's capital 'CleanCode'",
           "CleanCode inn 'Progers hope'",
           "Town 'CodeBridge'",
           "Village 'Clean_Makerovo'",
           "Village 'Dream_Progavo'",
           "City 'Perfectoria'",
           "RoadBlock",
           "Town 'Everything_Googling' (Enemy's)",
           "Village 'Indusovo' (Enemy's)",
           "Town 'YouTube_Code_Tupo_Catchers' (Enemy's)",
           "Village 'ChatGPT_Coderovo'"
           "City 'Mud_Coders' (Enemy's)",
           "Town 'Depression-Friendless-Life'",
           "Town 'Forum_Bezdarey'",
           "Village 'Bezdum'e'",
           "City 'Web_Compiler_Progers'",
           "GovnoCoders's capital 'Rabotaet - ne - Trogay' (Enemy's)"]
    campaign_reward=[200,
                     300,
                     1000,
                     700,
                     800,
                     2500,
                     10000,
                     4000,
                     2500,
                     5000,
                     3500,
                     15000,
                     6500,
                     8000,
                     4500,
                     20000,
                     65000]
    campaign_foe_name=["Dunger Master",
                       "Drunken Bastard",
                       "Code Destroyer",
                       "Mud Master",
                       "Silly CodeCatcher"
                       "AntiPerfect",
                       "Security",
                       "Bezdar'",
                       "Boy - Tutor-Master",
                       "Kind Toxic",
                       "Brainless Critic",
                       "1000Print() Master",
                       "Ignorshchik",
                       "Bad-Tutorials Maker",
                       "Balabol",
                       "Fast - Speaking Coder",
                       "Silly Monkey"]
    campaign_foes=[0,
                   35,
                   150,
                   240,
                   300,
                   1500,
                   500,
                   6000,
                   950,
                   8500,
                   1000,
                   19000,
                   10000,
                   14000,
                   3400,
                   25000,
                   55000]
    campaign_levels=[0,
                     1,
                     2,
                     1,
                     2,
                     3,
                     15,
                     3,
                     2,
                     4,
                     2,
                     6,
                     5,
                     5,
                     3,
                     7,
                     9]
    quest_foe_names=["Robin Hood",
                     "Tomy 'Sharp knife'",
                     "Blind archer",
                     "Unknown",
                     "Player_"+"".join([str((randint(0,9))) for i in range(4)]),
                     "Billy Herrington"]
    grab_foes=[350,
               30,
               50,
               80,
               190,
               400, # 1.100
               40,
               4000,
               650,
               5000,
               850,
               15000,
               7000,
               8450,
               1200,
               22850,
               45000] # 110.000
    grab_reward=[14800,
                 450,
                 1500,
                 2900,
                 3100,
                 8600,
                 1320,
                 18400,
                 4350,
                 23000,
                 5030,
                 65000,
                 28000,
                 36000,
                 7000,
                 125000,
                 465000]
    
    
    if campaign_count==len(place):
        print(f"\n\nCongratulations!\n\nYou complete this game!\n\nWanna continue?\n<y> - Yes\n<n> - No")
        keys=['y','n']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        sleep(0.5)
        if action=='n':
            print("\n\nRemember: It's not the one who doesn't know who is bad, but the one who doesn't want to know")
            exit()
                    
    if not soldiers and money<=int(level*50//relationship):
        print("\n\nYou haven't got any soldiers and money. You are BAD Captain\nBye!")
        exit()
    
    if not soldiers:
        print("Oh! You haven't got any soldiers. Your level decrease to 1") 
        level=1

    if relationship<2: rel="Very Bad"
    elif relationship<4: rel="Bad"
    elif relationship<7: rel="Normal"
    elif relationship<9: rel="Good"
    else: rel="Very Good"
    print(f"\n\nName: {name}          Soldiers: {soldiers}          Level: {level}          Money: {money}          Relationship:  {rel} ({relationship})")
    print("\n\nThere is your home. Here you can:\n\n<b> - Buy soldiers\n<u> - Level Up soldiers\n<s> - Sell soldiers\n<q> - take a Quest\n<c> - Go Campaign\n<g> - Grab villages, towns and cities\n<p> - Play a poker (yeah boy!)\n\n")
        
    keys=['b','u','s','q','c','g','p']
    broken=False
    while True:
        for key in keys:
            if not keyboard.is_pressed(key): pass
            else: 
                broken=True
                action=key
        if broken: break
    sleep(0.5)
    
    if action=='b':
        print("Buy\n\n")
        formula=int(level*50//relationship)
        if money<formula:
            print(f"You can't buy any soldiers\nThe one soldier cost {int(level*50//relationship)} money")
            home(soldiers, level, money, campaign_count,relationship)
        while True:
            try:
                buy=int(input(f"Here you can Buy soldiers your level\nEnrer the count of the soldiers you wanna buy\n1 soldier cost {formula} money ( level * 50 / relationship )\nYou can buy max {int(money/formula)} soldiers\n"))
                while money<buy*(formula):
                    buy=int(input("you haven't enough money. Try again\n"))
                break
            except: print("Incorrect enter! Try again.")
        money-=buy*(formula)
        soldiers+=buy
        home(soldiers, level, money, campaign_count,relationship)

    elif action=='u' and soldiers:
        formula=int(soldiers*level*level*50/relationship)
        print(f"Level up\n\nHere you can Level Up your Soldiers\nDo you wanna spend {formula} ( soldiers * level * level * 50 / relationship ) money (now you have {money} money)?\n<y> - Yes\n<n> - No")
        keys=['y','n']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        sleep(0.5)
        if action=='y':
            if money<formula: print("you haven't got enough money")
            else:
                money-=formula
                level+=1
        home(soldiers, level, money, campaign_count,relationship)
    
    elif action=='s':
        print('Sell\n\n')
        formula=round(level*relationship*2,2)
        while True:
            try:
                sell=int(input(f"Here you can Sell Soldiers\nEnrer the count of the soldiers you wanna sell\n1 soldier cost {formula} ( level * relationship * 2 )\n"))
                while sell>soldiers:
                    sell=int(input("You haven't got enough soldiers. Try again\n"))
                break
            except: print("Incorrect enter! Try again.")
        money+=sell*formula
        soldiers-=sell
        home(soldiers, level, money, campaign_count,relationship)
    
    elif action=='q':
        print("Quests\n\nYou have very many Quests. You can choose:\n<t> - tiny (2-10 enemies 1-2 lvl, reward: 15-35 money)\n<s> - small (8-25 enemies 1-2 lvl, reward: 30-80 money)\n<n> - normal (20-65 enemies 1-3 lvl, reward: 150-350 money)\n<b> - big (50-250 enemies 2-4 lvl, reward: 800-2500 money)\n<l> - LARGE (200-1000 enemies 2-5 lvl, reward: 5000-12000 money)\n<q> - Quit to Home")
        keys=['t','s','n','b','l','q']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        sleep(0.5)
        if action=='q': home(soldiers, level, money, campaign_count,relationship)
        else:
            if action=='t':
                foes=randint(2,10)
                foe_level=randint(1,2)
                reward=randint(15,35)
            elif action=='s':
                foes=randint(8,25)
                foe_level=randint(1,2)
                reward=randint(30,80)
            elif action=='n':
                foes=randint(20,65)
                foe_level=randint(1,3)
                reward=randint(150,350)
            elif action=='b':
                foes=randint(50,250)
                foe_level=randint(2,4)
                reward=randint(800,2500)
            else:
                foes=randint(200,1000)
                foe_level=randint(2,5)
                reward=randint(5000,12000)
            foe_name=choice(quest_foe_names)
            state='q'

    elif action=='c':
        print(f"Campaign\n\nThis is Campaign mode, where you will pass the game plot.\nHere You, Our Captain and Hope of ProgaMasters, will fight with your enemy - GovnoCoders.\nSo Epic :)\n\nYou can:\n<n> - reject and go home\n<y> - accept and fight\n<i> - info about place where you are and next place. Here You also can see info about enemy and complete reward")
        keys=['y','n','i']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        if action=='y':
            state='c'
            foe_level=campaign_levels[campaign_count]
            foes=campaign_foes[campaign_count]
            foe_name=campaign_foe_name[campaign_count]
            reward=campaign_reward[campaign_count]
        elif action=='i':
            print(f"\nInfo\n\n{20*' '}Now (You are here){' '*62}Next place\n\nPlace:{' '*14}{place[campaign_count-1]}{' '*(80-len(str(place[campaign_count-1])))}{place[campaign_count]}\n\nEnemy's Name:{' '*7}{campaign_foe_name[campaign_count-1]}{' '*(80-len(str(campaign_foe_name[campaign_count-1])))}{campaign_foe_name[campaign_count]}\n\nEnemy Count:{' '*8}{campaign_foes[campaign_count-1]}{' '*(80-len(str(campaign_foes[campaign_count-1])))}{campaign_foes[campaign_count]}\n\nEnemy level:{' '*8}{campaign_levels[campaign_count-1]}{' '*(80-len(str(campaign_levels[campaign_count-1])))}{campaign_levels[campaign_count]}\n\nReward:{' '*13}{campaign_reward[campaign_count-1]}{' '*(80-len(str(campaign_reward[campaign_count-1])))}{campaign_reward[campaign_count]}\n\nWanna fight?\n<y> - Yes\n<n> - No")
            keys=['y','n']
            broken=False
            while True:
                for key in keys:
                    if not keyboard.is_pressed(key): pass
                    else: 
                        broken=True
                        action=key
                if broken: break
            if action=='y':
                state='c'
                foe_level=campaign_levels[campaign_count]
                foes=campaign_foes[campaign_count]
                foe_name=campaign_foe_name[campaign_count]
                reward=campaign_reward[campaign_count]
            else: home(soldiers, level, money, campaign_count,relationship)
        else: home(soldiers, level, money, campaign_count,relationship)
    
    elif action=='g':
        print(f"Grab\n\nDo you really wanna grab {place[campaign_count-1]}?\nYour reputation will reduce for 2 - 3 points\n\nYou can:\n<n> - reject and go home\n<y> - accept and fight\n<i> - info about place where you are. Here You also can see info about enemy and complete reward")
        keys=['y','n','i']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        if action=='y': 
            foe_level=1
            foe_name="Sitizen"
            foes=grab_foes[campaign_count-1]
            reward=grab_reward[campaign_count-1]
            relationship-=randint(2,3)
        elif action=='i':
            print(f"\nInfo\n\nPlace:{' '*14}{place[campaign_count-1]}\n\nEnemy's Name:{' '*7}Sitizen\n\nEnemy Count:{' '*8}{grab_foes[campaign_count-1]}\n\nEnemy level:{' '*8}1\n\nReward:{' '*13}{grab_reward[campaign_count-1]}\n\nWanna fight?\n<y> - Yes\n<n> - No")
            keys=['y','n']
            broken=False
            while True:
                for key in keys:
                    if not keyboard.is_pressed(key): pass
                    else: 
                        broken=True
                        action=key
                if broken: break
            if action=='y':
                state='q'
                foe_level=1
                foe_name="Sitizen"
                foes=grab_foes[campaign_count-1]
                reward=grab_reward[campaign_count-1]
                relationship-=randint(2,3)
            else: home(soldiers, level, money, campaign_count,relationship)
        else: home(soldiers, level, money, campaign_count,relationship)
    
    elif action=='p':
        print("Play a poker\n\nHere you can win and lose your money without fights and bloodshed.\nPress:\n<y> - play\n<n> - go away\n<i> - info about game")
        keys=['y','n','i']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        if action=='n': home(soldiers, level, money, campaign_count,relationship)
        elif action=='i': print(f"\n\nInfo\n\nCombination{49*' '}Multiple\n\nRoyal Flush{49*' '}500.000\n\nStraight Flush{46*' '}75.000\n\nFour of a kind{46*' '}1.500\n\nFull House{50*' '}250\n\nFlush{55*' '}100\n\nStraight{52*' '}30\n\nThree of a kind{45*' '}8\n\nTwo pairs{51*' '}4\n\nPair{56*' '}1.5")
        poker(soldiers, level, money, campaign_count,relationship, last=25)



    war(soldiers,level,foes,foe_level,foe_name,state,reward,money,relationship,campaign_count)

def poker(soldiers, level, money, campaign_count,relationship, last):
    
    card_suits=["♠","♣","♥","♦"]
    card_names=[*[str(i) for i in range(2,11)],'Jack','Queen','King','Ace']

    print("\nWanna play?\n<y> - yes\n<n> - no")
    keys=['y','n']
    broken=False
    while True:
        for key in keys:
            if not keyboard.is_pressed(key): pass
            else: 
                broken=True
                action=key
        if broken: break
    if action=='n': home(soldiers, level, money, campaign_count,relationship)
                
    elif(action=='y' and money>=25):
        print("\n\nPlay!")
        while True: 
            try: 
                bet=int(input(f"\nMake a bet (You have {money} money)\n<-1> - the last bet\n<-2> - all in\n\n"))
                if bet==-1: bet=last
                elif bet==-2: bet=money
                while bet<25 or bet>money:
                    bet=int(input("25 money <= bet <= money.\nUnderstand?\n"))
                    if bet==-1: bet=last
                    elif bet==-2: bet=money
                break
            except: print("\nIncorrect Enter! Try again.\n")
        print('Bet is done')
        money-=bet
        last=bet
        poker_set=[]

        for i in range(5):

            card=choice(card_suits)+choice(card_names)
            while card in poker_set: card=choice(card_suits)+choice(card_names)
            poker_set.append(card)
            print("\n\n",*poker_set,"\n\n",sep='   ')
            sleep(0.5)                                

        print("\n\nPress <space> to watch result")
        keyboard.wait("space")

        for i in range(4):
                            
            if (card_suits[i]+"10" in poker_set) and (card_suits[i]+"Jack" in poker_set) and (card_suits[i]+"Queen" in poker_set) and (card_suits[i]+"King" in poker_set) and (card_suits[i]+"Ace" in poker_set):
                print(f"Royal Flush!\nYour win: {bet*500000}\nBet * 500.000")
                money+=(bet*500000)
                poker(soldiers, level, money, campaign_count,relationship, last)
                            
            for (j) in range(9):
                if ((card_suits[i]+card_names[j] in poker_set) and (card_suits[i]+card_names[j+1] in poker_set) and (card_suits[i]+card_names[j+2] in poker_set) and (card_suits[i]+card_names[j+3] in poker_set) and (card_suits[i]+card_names[j+4] in poker_set)):
                    print(f"Straight Flush!\nYour win: {bet*75000}\nBet * 75.000")
                    money+=(bet*75000)
                    poker(soldiers, level, money, campaign_count,relationship, last)

            if ((card_suits[i]+"Ace" in poker_set) and (card_suits[i]+"2" in poker_set) and (card_suits[i]+"3" in poker_set) and (card_suits[i]+"4" in poker_set) and (card_suits[i]+"5" in poker_set)):
                print(f"Straight Flush!\nYour win: {bet*75000}\nBet * 75.000")
                money+=(bet*75000)
                poker(soldiers, level, money, campaign_count,relationship, last)

        suitless_poker_set=[i[1:] for i in poker_set]
        for i in card_names:
                            
            if suitless_poker_set.count(i)==4:
                print(f"Four of a kind!\nYour win: {bet*1500}\nBet * 1.500")
                money+=(bet*1500)
                poker(soldiers, level, money, campaign_count,relationship, last)

            elif suitless_poker_set.count(i)==3:
                for j in card_names:
                    if suitless_poker_set.count(j)==2 and i!=j:
                        print(f"Full House!\nYour win: {bet*250}\nBet * 250")
                        money+=(bet*250)
                        poker(soldiers, level, money, campaign_count,relationship, last)
                        
        nameless_poker_set=[i[1] for i in poker_set]
        for i in nameless_poker_set:
            if nameless_poker_set.count(i)==5:
                print(f"Flush!\nYour win: {bet*100}\nBet * 100")
                money+=(bet*100)
                poker(soldiers, level, money, campaign_count,relationship, last)
                        
        for (i) in range(10):
            if (card_names[i] in suitless_poker_set and card_names[i+1] in suitless_poker_set and card_names[i+2] in suitless_poker_set and card_names[i+3] in suitless_poker_set and card_names[i+4] in suitless_poker_set):
                print(f"Straight!\nYour win: {bet*30}\nBet * 30")
                money+=(bet*30)
                poker(soldiers, level, money, campaign_count,relationship, last)

        if ("Ace" in suitless_poker_set and "2" in suitless_poker_set and "3" in suitless_poker_set and "4" in suitless_poker_set and "5" in suitless_poker_set):
            print(f"Straight!\nYour win: {bet*30}\nBet * 30")
            money+=(bet*30)
            poker(soldiers, level, money, campaign_count,relationship, last)

        for i in card_names:
            if suitless_poker_set.count(i)==3:
                print(f"Three of a kind!\nYour win: {bet*8}\nBet * 8")
                money+=(bet*8)
                poker(soldiers, level, money, campaign_count,relationship, last)


        for i in card_names:
            if suitless_poker_set.count(i)==2:
                for j in card_names:
                    if suitless_poker_set.count(j)==2 and i!=j:
                        print(f"Two pairs!\nYour win: {bet*4}\nBet * 4")
                        money+=(bet*4)
                        poker(soldiers, level, money, campaign_count,relationship, last)
                
                print(f"Pair!\nYour win: {bet*1.5}\nBet * 1.5")
                money+=(bet*1.5)
                poker(soldiers, level, money, campaign_count,relationship, last)



        else: print("You Lose!")
        poker(soldiers, level, money, campaign_count,relationship, last)

    else:
        print("You haven't got a money for minimum bet (25)")
        home(soldiers, level, money, campaign_count,relationship)



war(soldiers,level,foes,foe_level,foe_name,state,reward,money,relationship,campaign_count)















