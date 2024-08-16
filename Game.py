from time import sleep
from random import randint
import keyboard

name=input("Your name, captain\n")
soldiers=15
level=1
foes=10
foe_level=1
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

        if foes>=1000:
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
        print(f"Press:\n<a> to attack {foe_name}'s army\n<r> to run away and lose this battle. Enemy has chance kill your running army\n<t> to try make {foe_name}'s army surrender. You'll give all of remain soldiers\n<h> to heal everyone and relive 20-30% of your army\n<s> to fire artillery at the enemy. You may kill from 10 to 5% of enemies per 1 artillery")
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

        if state=='d':
            lost=min(randint(int((foes*foe_level)/(8*level)),int(foes*foe_level/4*level)),soldiers)
            soldiers-=lost
            if action=='a':
                print('Attack!')
                foes_lost=min(randint(int((soldiers*level)/(8*foe_level)),int(soldiers*level/4*foe_level)),foes)
                foes-=foes_lost
                soldiers_attack+=soldiers
            if action=='r':
                print('Run!')
                if randint(0,5)!=0:
                    killed_running_soldiers=randint(1,soldiers)
                    print('Enemy killed', killed_running_soldiers ,'soldiers')
                    soldiers-=killed_running_soldiers
                else: print("You've run away with all your remain soldiers")
            if action=='t':
                print('Surrender!')
                if soldiers//10<foes: print("They don't want to surrender")
                else:
                    soldiers+=foes
                    foes=0
                    print("Congratulations! You've made them surrender!")
        if state=='a' or state=='q' or state=='c':
            if action=='a':
                print('Attack!')
                foes_lost=min(randint(int((soldiers*level)/(8*foe_level)),int(soldiers*level/4*foe_level)),foes)
                foes-=foes_lost
                soldiers_attack+=soldiers
            if action=='r':
                print('Run!')
                if randint(0,5)!=0:
                    killed_running_soldiers=randint(1,soldiers)
                    print('Enemy killed', killed_running_soldiers ,'soldiers')
                    soldiers-=killed_running_soldiers
                else: print("You've run away with all your remain soldiers")
            if action=='t':
                print('Surrender!')
                if soldiers//10<foes: print("They don't want to surrender")
                else:
                    soldiers+=foes
                    foes=0
                    print("Congratulations! You've made them surrender!")
            lost=min(randint(int((foes*foe_level)/(8*level)),int(foes*foe_level/4*level)),soldiers)
            soldiers-=lost
    view()
    if not foes:
        if state=='q': money_change=reward-(soldiers_attack//20)
        elif state=='c':
            money_change=reward-(soldiers_attack//20)
            campaign_count+=1
        else: money_change=randint((foes_all*foe_level)-(soldiers_attack//20),foes_all*foe_level*2-(soldiers_attack//20))
        relationship+=0.1
        print("You win!\nReward:",money_change,"money","\nRelationship:",relationship,"(+0.1)\nPress <space> to continue")
        money+=money_change
    else:
        money_change=soldiers_attack//20
        print(f"{foe_name} win!\nYou lost: {money_change} money\nPress <space> to continue")
        if action=='r': relationship-=1
        else: relationship-=0.2
        money-=money_change
    sleep(0.5)
    keyboard.wait("space")
    home(soldiers, level, money, campaign_count,relationship)





def home(soldiers, level, money, campaign_count,relationship):
    place=["ProgaMasters's capital 'CleanCode'",
           "CleanCode inn 'Progers hope'",
           "Town 'CodeBridge'",
           "Village 'CodeMakerovo'",
           "Village 'DreamProgavo'",
           "City 'Perfectoria'",
           "RoadBlock",
           "Town 'Googling' (Enemy's)",
           "Village 'Indusovo' (Enemy's)",
           "Town 'YouTubeCodeCatchers' (Enemy's)",
           "Village 'ChatGPTCoderovo'"
           "City 'MudCoders' (Enemy's)",
           "GovnoCoders's capital 'HuynjaNoSoydjet' (Enemy's)"]
    campaign_reward=[200,
                     300,
                     1000,
                     700,
                     800,
                     2500,
                     10000,
                     1700,
                     1200,
                     2750,
                     1500,
                     15000,
                     100000]
    campaign_foe_name=["Dunger Master",
                       "Drunken Bastard",
                       "Code Destroyer",
                       "Mud Master",
                       "Silly CodeCatcher"
                       "AntiPerfect",
                       "Security",
                       "Bezdar'",
                       "Vijebistiy Small Eblan",
                       "Kind Toxic",
                       "Brainless Critic",
                       "1000Print() Master",
                       "Silly Monkey"]
    campaign_foes=[0,
                   15,
                   55,
                   60,
                   70,
                   170,
                   20,
                   250,
                   150,
                   300,
                   160,
                   900,
                   7500]
    campaign_levels=[0,
                     1,
                     2,
                     1,
                     2,
                     3,
                     7,
                     3,
                     2,
                     4,
                     2,
                     6,
                     8]
    if not soldiers and money<=0:
        print("\n\nYou haven't got any soldiers and money. You are BAD Captain\nBye!")
        return
    
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
        while True:
            try:
                buy=int(input(f"Here you can Buy soldiers your level\nEnrer the count of the soldiers you wanna buy\n1 soldier cost {level*50/relationship} ( level * 50 / relationship ) money\nYou can buy max {money//(level*50/relationship)} soldiers\n"))
                while money<buy*(level*50/relationship):
                    buy=int(input("you haven't enough money. Try again\n"))
                break
            except: print("Incorrect enter! Try again.")
        money-=buy*(level*50/relationship)
        soldiers+=buy
        home(soldiers, level, money, campaign_count,relationship)

    elif action=='u' and soldiers:
        print(f"Level up\n\nHere you can Level Up your Soldiers\nDo you wanna spend {soldiers*level*100/relationship} ( soldiers * level * 100 / relationship ) money (now you have {money} money)?\n<y> - Yes\n<n> - No")
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
            if money<soldiers*level*100/relationship: print("you haven't got enough money")
            else:
                money-=soldiers*level*100/relationship
                level+=1
        home(soldiers, level, money, campaign_count,relationship)
    
    elif action=='s':
        print('Sell\n\n')
        while True:
            try:
                sell=int(input(f"Here you can Sell Soldiers\nEnrer the count of the soldiers you wanna sell\n1 soldier cost {0.5*level*relationship} (0.5 * level * relationship)\n"))
                while sell>soldiers:
                    sell=int(input("You haven't got enough soldiers. Try again\n"))
                break
            except: print("Incorrect enter! Try again.")
        money+=sell*0.5*level*relationship
        soldiers-=sell
        home(soldiers, level, money, campaign_count,relationship)
    
    elif action=='q':
        print("Quests\n\nYou have very many Quests. You can choose:\n<t> - tiny (2-8 enemies 1-2 lvl, reward: 15-50 money)\n<s> - small (5-20 enemies 1-2 lvl, reward: 40-100 money)\n<n> - normal (20-65 enemies 1-3 lvl, reward: 150-400 money)\n<b> - big (50-250 enemies 2-4 lvl, reward: 400-800 money)\n<l> - LARGE (200-1000 enemies 2-5 lvl, reward: 1000-4000 money)\n<q> - Quit to Home")
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
                foes=randint(2,8)
                foe_level=randint(1,2)
                reward=randint(15,50)
            elif action=='s':
                foes=randint(5,20)
                foe_level=randint(1,2)
                reward=randint(40,100)
            elif action=='n':
                foes=randint(20,65)
                foe_level=randint(1,3)
                reward=randint(150,400)
            elif action=='b':
                foes=randint(50,250)
                foe_level=randint(2,4)
                reward=randint(400,800)
            else:
                foes=randint(200,1000)
                foe_level=randint(2,5)
                reward=randint(1000,4000)
            state='q'

    elif action=='c':
        print(f"Campaign\n\nThis is Campaign mode, where you will pass the game plot.\nHere You, Our Captain and Hope of ProgaMasters, will fight with your enemy - GovnoCoders.\nSo Epic :)\n\nYou can:\n<n> - reject and go home\n<y> - accept and fight\n<i> - info about place where you are and next place. Here You also can see info about enemy and reward complete reward")
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
            print(f"\nInfo\n\n{20*' '}Now (You are here){' '*60}Next place\n\nPlace:{' '*14,place[campaign_count-1],' '*(60-len(str(place[campaign_count-1]))),place[campaign_count]}\n\nEnemy's Name:{' '*7,campaign_foe_name[campaign_count-1],' '*(60-len(str(campaign_foe_name[campaign_count-1]))),campaign_foe_name[campaign_count]}\n\nEnemy Count:{' '*8,campaign_foes[campaign_count-1],' '*(60-len(str(campaign_foes[campaign_count-1]))),campaign_foes[campaign_count]}\n\nReward:{' '*13,campaign_reward[campaign_count-1],' '*(60-len(str(campaign_reward[campaign_count-1]))),campaign_reward[campaign_count]}\n\nEnemy level:{' '*8,campaign_levels[campaign_count-1],' '*(60-len(str(campaign_levels[campaign_count-1]))),campaign_levels[campaign_count]}\n\nWanna fight?\n<y> - Yes\n<n> - No")
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
        print(f"Grab\n\nDo you really wanna grab {place}?\nYour reputation will reduce for 3-5 points")
        keys=['y','n']
        broken=False
        while True:
            for key in keys:
                if not keyboard.is_pressed(key): pass
                else: 
                    broken=True
                    action=key
            if broken: break
        if action=='y': pass
        else: home(soldiers, level, money, campaign_count,relationship)
            

    war(soldiers,level,foes,foe_level,foe_name,state,reward,money,relationship,campaign_count)













war(soldiers,level,foes,foe_level,foe_name,state,reward,money,relationship,campaign_count)


