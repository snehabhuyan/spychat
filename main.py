from spy_details import spy, Spy, ChatMsg, friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

STATUS_MESSAGES = ['available']
SPECIAL_MSG=['SOS','DANGER','URGENT','EMERGENCY']
print colored ("Hello! let's get started", 'red', 'on_grey')
question="do you want to continue as" + spy.salutation + " " + spy.name + "(Y/N)?"
existing=raw_input(question)

def count_words(word):
    word.split()
    length=len(word.split())
    return length

def remove_friend(pos):
    del friends[pos]
    print 'Spy deleted'

def add_status():
    current_status_message = None
    if current_status_message!= None:
        print colored ('your current status message is %s \n' %(current_status_message), 'red','on blue')
    else :
        print 'you don\'t have any status message currently \n'
    default = raw_input(" do you want to select from the older status (y/n)")

    if default.upper() == "N":
        new_status_message= raw_input("what status message do you want to set?")

        if len(new_status_message)>0 :
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message= new_status_message

    elif default.upper()== 'Y':
        item_position= 1
        for message in STATUS_MESSAGES:
            print '%d.%s'%(item_position,message)
            item_position=item_position + 1
        message_selection =int(raw_input("\nChoose from the above messages"))

        if len(STATUS_MESSAGES)>=message_selection:
            updated_status_message=STATUS_MESSAGES[message_selection -1]
    else:
        print 'The option you choose is not valid! Press either y or n.'
    if updated_status_message:
        print 'your updated status message is:%s' %(updated_status_message)
    else:
        print 'your current don\'t have a status update'
    return updated_status_message

def add_friend():
    new_friend=Spy('', '', 0, 0.0)

    new_friend.name= raw_input("please add your friends name: ")
    new_friend.salutation= raw_input("mr. or ms.?: ")

    new_friend.name= new_friend.salutation+" "+new_friend.name

    new_friend.age= raw_input("age?")
    new_friend.age=int(new_friend.age)

    new_friend.rating =raw_input("spy rating?")
    new_friend.rating=float(new_friend.rating)

    if len(new_friend.name)> 0 and new_friend.age > 12 and new_friend.rating >= spy.rating :
      friends.append(new_friend)
    else:
      print 'sorry! Invalid entry. we can\'t add spy with the details you provided'

    return len(friends)

def select_a_friend():
    item_number=0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name,friend.age, friend.rating)
        item_number+=1

    friend_choice= raw_input("choose from your friends")
    friend_choice_position =int(friend_choice)-1
    return friend_choice_position

def send_message():
    friend_choice= select_a_friend()
    print friend_choice

    original_image=raw_input("what is the name of the image?")
    output_path= "secret.jpg"
    text =raw_input("what is the message")
    Steganography.encode(original_image,output_path,text)
    new_chat= ChatMsg(text,True)
    friends[friend_choice].chats.append(new_chat)
    print "your secret message image is ready!"

def read_message():
    sender= select_a_friend()
    output_path= raw_input("what is the name of the file")
    secret_text= Steganography.decode(output_path)

    if secret_text.upper() in SPECIAL_MSG:
        print colored("SPY ALERT! SPECIAL MESSAGE HAS BEEN GENERATED" + secret_text, 'blue', 'on_grey')

    number = count_words(secret_text)

    if number >15:
        remove_friend(sender)
    else:
        print secret_text
        new_chat= ChatMsg(secret_text, False)

        friends[sender].chats.append(new_chat)

        print "your secret message is saved" + secret_text

def read_history():
    read_chat= select_a_friend()
    print'\n'
    for chat in friends[read_chat].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s'% (chat.time.strftime("%d %B %Y"), 'you said:', chat.message)
        else:
            print '[%s] %s said: %s'%(chat.time.strftime("%d %B %Y"), friends[read_chat].name, chat.message)

def start(spy):
    spy.name =spy.salutation+" "+spy.name

    if spy.age>12 and spy.age<50 :
        print "authentication complete. welcome" +spy.name+ "age:" \
              + str(spy.age)+" and rating of: "+str(spy.rating)+ "proud to have you "
        show_mainmenu= True

        while show_mainmenu:
            mainmenu_choices= "what do you want to do? \n 1.Add a status update \n 2.Add a friend \n 3.Select a friend \n 4.send a secret message \n 5. read a secret message \n 6. Read chats from sender \n 7.remove friend \n 8.close application \n"
            mainmenu_choices=raw_input(mainmenu_choices)

            if len( mainmenu_choices) >0:
                mainmenu_choices= int(mainmenu_choices)
                if mainmenu_choices == 1:
                    spy.current_status_messages= add_status()
                elif mainmenu_choices == 2:
                    number_of_friends = add_friend()
                    print "you have %d friends in your account" %(number_of_friends)
                elif mainmenu_choices ==3:
                    select_a_friend()
                elif mainmenu_choices ==4:
                    send_message()
                elif mainmenu_choices ==5:
                    read_message()
                elif mainmenu_choices ==6:
                    read_history()
                elif menu_choice ==7:
                    number=select_a_friend()
                    remove_friend(number)
                else:
                    show_mainmenu= False
    else:
        print "sorry you are of ineligible age to spy"

if existing.upper() == 'Y':
    start(spy)
else:

    spy= Spy('', '', 0, 0.0)
    spy.name= raw_input("welcome, please tell your spy name")

    if len(spy.name) > 0:
        spy.salutation= raw_input("how do you want to be reffered as: ?")

        spy.age= raw_input("what is your age")
        spy.age= int(spy.age)

        spy.rating = raw_input("what is your spy rating? ")
        spy.rating= int(spy.rating)

        start(spy)
    else:
        print "please enter valid spy name"








            




