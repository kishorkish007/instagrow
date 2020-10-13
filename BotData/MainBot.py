#Impoting Modules
from instabot import Bot
import time
import sys
import random
from tqdm import tqdm
import os

#Importing Mi Functions
from FunctionData.somefun import clear
from MokupData.mokupfun import *

#Men@c
bot = Bot(
    max_likes_per_day=50,
    max_follows_per_day=50,
    max_unfollows_per_day=50,
    min_likes_to_like=10,
    max_likes_to_like=10000000,
    like_delay=25,
    follow_delay=20,
    unfollow_delay=20
    )
#hashtag list to tag in a media
hashtagList = [
            '#hdr #hdriphoneographer #hdrspotters #hdrstyles_gf #hdri #hdroftheday #hdriphonegraphy #hdrepublic #hdr_lovers #awesome_hdr #instagood #hdrphotography #photooftheday #hdrimage #hdr_gallery #hdr_love #hdrfreak #hdrama #hdrart #hdrphoto #hdrfusion #hdrmania #hdrstyles #ihdr #str8hdr #hdr_edits',
            '#nyc #workout #vscocam #happy #handmade #healthy #sweet #instafollow #sun #lol #lifestyle #photooftheday #nofilter #girls #f4f #smile #photo #swag #flowers',
            '#love #couple #cute #adorable #kiss #kisses #hugs #romance #forever #girlfriend #boyfriend #gf #bf #bff #together #photooftheday #happy #me #girl #boy #beautiful #instagood #instalove #loveher #lovehim #pretty #fun #smile #xoxo',
            '#nyc #money #cash #green #dough #bills #crisp #benjamin #benjamins #franklin #franklins #bank #payday #hundreds #twentys #fives #ones #100s #20s #greens #photooftheday #instarich #instagood #capital #stacks #stack #bread #paid',
            '#nyc #followme #follow #followforfollow #followback #followers #follow4follow #followher #follower #followhim #followall #followbackteam #followbackalways #follows #followgram #followalways #tagblender #followmefollowyou #following #followstagram #follownow #ifollowback #followus #followmeback',
            '#like4like #liking #likeall #likeforlike #likes4likes #love #instagood #tagblender #tagblender #likesforlikes #ilikeback #liketeam #liker #ilike #likealways #likebackteam #ilikeyou #ilikeit #likeme #tflers #likes #likesback #photooftheday'
]

#Program For Unfollow Everyone
def ig_teamhunter():
    KMFHEADER()
    TEAMHUNTER()
    userdata = input("\u001b[32m[+]\u001b[0m Enter Target Team username:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    n = 70 #number of repeats
    while n >= 0:
        n -= 1
        bot.follow(userdata)
        time.sleep(220)
        bot.unfollow(userdata)
        time.sleep(20)
    #repeat()

#Program For Unfollow Everyone
def ig_masslooker():
    KMFHEADER()
    MASSLOOKER()
    if len(sys.argv) >= 2:
        bot.logger.info(
            """
                Going to get '%s' likers and watch their stories
                (and stories of their likers too).
            """
            % (sys.argv[1])
        )
        user_to_get_likers_of = bot.convert_to_user_id(sys.argv[1])
    else:
        bot.logger.info(
        """
        Going to get your likers and watch their stories and stories
        of their likers too.(by default we use you as a starting point).
        """
        )
        user_to_get_likers_of = bot.get_user_id_from_username("ariana")

        current_user_id = user_to_get_likers_of
    while True:
        try:
            # GET USER FEED
            if not bot.api.get_user_feed(current_user_id):
                print("Can't get feed of user_id=%s" % current_user_id)

            # GET MEDIA LIKERS
            user_media = random.choice(bot.api.last_json["items"])
            if not bot.api.get_media_likers(media_id=user_media["pk"]):
                bot.logger.info(
                    "Can't get media likers of media_id='%s' by user_id='%s'"
                    % (user_media["id"], current_user_id)
                )

            likers = bot.api.last_json["users"]
            liker_ids = [
                str(u["pk"])
                for u in likers
                if not u["is_private"] and "latest_reel_media" in u
            ][:20]

            # WATCH USERS STORIES
            if bot.watch_users_reels(liker_ids):
                bot.logger.info("Total stories viewed: %d" % bot.total["stories_viewed"])

            # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
            current_user_id = random.choice(liker_ids)

            if random.random() < 2:
                current_user_id = user_to_get_likers_of
                bot.logger.info(
                    "Sleeping and returning back to original user_id=%s" % current_user_id
                )
                time.sleep(100 * random.random() + 60)
        except Exception as e:
            # If something went wrong - sleep long and start again
            bot.logger.info(e)
            current_user_id = user_to_get_likers_of
            time.sleep(240 * random.random() + 60)


#Program For ReHashtag
def ig_rehashtag():
    KMFHEADER()
    REHASHTAG()
    postlink = input("\u001b[32m[+]\u001b[0m Enter Media link:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        media_link = postlink
        media_id = bot.get_media_id_from_link(media_link)
        comments = bot.get_media_comments(media_id)
        commented_users = [] 
        for comment in tqdm(comments):
            replied = False
            parent_comment_id = comment["pk"] 
            user_id = comment["user"]["pk"]
            comment_type = comment["type"]
            commenter = comment["user"]["username"]
            text = comment["text"]

            #process
            bot.logger.info("Go to Delete Hashtags")    
            bot.delete_comment(media_id,parent_comment_id)
            #commented_users.append(user_id)
            time.sleep(10)
            bot.logger.info("Go to insert Hashtags")
            bot.comment(media_id,comment_text=random.choice(hashtagList))
            time.sleep(60)               
    repeat() 

#Infinity Feed Liker
wait = 5 * 60  # in seconds
def ig_feedliker():
    KMFHEADER()
    FEEDLIKER()
    while True:
        bot.like_timeline()
        time.sleep(wait)

#Inshackle Followers
waitaft = 8 * 60  # in seconds
def ig_inshackle():
    KMFHEADER()
    INSHACKLE()
    while True:
        bot.follow("selenagomez")
        bot.follow("neymarjr")
        bot.follow("ariana")
        bot.follow("beyonce")
        bot.follow("cristiano")
        bot.follow("kendalljenner")
        bot.follow("therock")
        bot.follow("kyliejenner")
        bot.follow("leomessi")
        bot.follow("madonna")
        bot.follow("ladygaga")
        bot.follow("dualipa")
        bot.follow("instagram")
        bot.follow("lelepons")
        time.sleep(waitaft)  
        bot.unfollow("selenagomez")
        bot.unfollow("neymarjr")
        bot.unfollow("ariana")
        bot.unfollow("beyonce")
        bot.unfollow("cristiano")
        bot.unfollow("kendalljenner")
        bot.unfollow("therock")
        bot.unfollow("kyliejenner")
        bot.unfollow("leomessi")
        bot.unfollow("madonna")
        bot.unfollow("ladygaga")
        bot.unfollow("dualipa")
        bot.unfollow("instagram")
        bot.unfollow("lelepons")
        time.sleep(120)



#Program For Unfollow Non-Followers
def ig_nonfollowers():
    time.sleep(1)
    KMFHEADER()
    NONFOLLOWERS()
    bot.unfollow_non_followers()

#Profile-Scraper
def ig_ProfileScraper():
    KMFHEADER()
    PROFILE_SCRAPER()
    userID = input("\u001b[32m[+]\u001b[0m Enter Username:-")
    user_id = bot.get_user_id_from_username(userID)
    user_info = bot.get_user_info(user_id)
    CHECKING = (user_info['is_private'])
    print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    FULLNAME = print("\u001b[32m[+]\u001b[0m Name:-",user_info['full_name'])
    MEDIA_COUNT = print("\u001b[32m[+]\u001b[0m Media Count:-",user_info['media_count'])
    FOLLOWERS = print("\u001b[32m[+]\u001b[0m Followers:-",user_info['follower_count'])
    FOLLOWING = print("\u001b[32m[+]\u001b[0m Following:-",user_info['following_count'])
    BIO = print("\u001b[32m[+]\u001b[0m Bio:-",user_info['biography'])
    WEBSITE = print("\u001b[32m[+]\u001b[0m Website:-",user_info['external_url'])
    if CHECKING == True:
        hi = "hello"
    if CHECKING == False:
        PHONENUMBER = print("\u001b[32m[+]\u001b[0m Phone:-","+",user_info['public_phone_country_code'],user_info['public_phone_number'])
        EMAIL =  print("\u001b[32m[+]\u001b[0m Email:-",user_info['public_email'])
    print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    print('\u001b[32m[1]\u001b[0m Check Another Profile')         
    print('\u001b[32m[2]\u001b[0m Main-Menu')
    print("\u001b[33;1m-------------------------------------------------------\u001b[0m")

#---------------------------------------------------------------------------------------------------------------

#Login Process
def Login():
    time.sleep(1)
    KMFHEADER()
    BOTLOGIN()
    USERNAME = input("\u001b[32m[+]\u001b[0m Enter username:-")
    PASSWORD = input("\u001b[32m[+]\u001b[0m Enter password:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    bot.login(username=USERNAME,password=PASSWORD)
    clear()

#After Login Displaying Options
def Option():
    KMFHEADER()
    OPTIONLIST()
    usrInp = input("\u001b[32m[+]\u001b[0m Enter Input:-")
    #If statment for option selection
    if usrInp == "1":
        clear()
        ig_teamhunter()
        
    if usrInp == "2":
        clear()
        ig_masslooker()

    if usrInp == "3":
        clear()
        ig_rehashtag()

    if usrInp == "4":
        clear()
        ig_feedliker()

    if usrInp == "5":
        clear()
        ig_inshackle() 

    if usrInp == "6":
        clear()
        ig_nonfollowers() 

    if usrInp == "7":
        def ProfileScraper():
            clear()
            ig_ProfileScraper()
            SCRA_Inpur = input("\u001b[32m[+]\u001b[0m Enter Input:-")
            if SCRA_Inpur == "1":
                clear()
                ProfileScraper()
            if SCRA_Inpur == "2":
                clear()
                Option()
        ProfileScraper()

    if usrInp == "8":
        clear()
        KMFHEADER()
        INSTRUCTIONS()
        DONATE()
        BackInp = input("\u001b[32m[+]\u001b[0m Enter Key to Main Menu ")
        if BackInp == "":
            clear()
            Option()
        else:
            clear()
            Option()
    if usrInp == "9":
        clear()
        bot.logout()

    else:
        clear()
        bot.logout()
        clear()
        exit()

def MainBot():
    clear()
    Login()
    Option()