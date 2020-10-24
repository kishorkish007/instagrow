#Impoting Modules
from instabot import Bot
import time
import sys
import random
from tqdm import tqdm
import os
from FunctionData.USER_DATABase import *

#Importing Mi Functions
from FunctionData.somefun import *
from MokupData.mokupfun import *
from BotData.ConfiG import *
#Men@c
bot = Bot(
    max_likes_per_day=400,
    max_follows_per_day=300,
    max_unfollows_per_day=300,
    max_messages_per_day=100,
    max_comments_per_day=150,
    min_likes_to_like=10,
    max_likes_to_like=10000000,
    like_delay=30,
    follow_delay=25,
    unfollow_delay=25,
    message_delay=2
    )
#hashtag list to tag in a media
hashtagList = [
            '#love #instagood #me #cute #tbt #photooftheday #instamood #iphonesia #tweegram #picoftheday #igers #girl #beautiful #instadaily #summer #instagramhub #iphoneonly #follow #igdaily #bestoftheday #happy #picstitch #tagblender #jj#sky #nofilter #fashion #followme #fun #su',
            '#followme #follow #followforfollow #followback #followers #follow4follow #followher #follower #followhim #followall #followbackteam #followbackalways #follows #followgram #followalways #tagblender #followmefollowyou #following #followstagram #follownow #ifollowback #followus #f4f#ifollo#followyou',
            '#like4like #liking #likeall #likeforlike #likes4likes #love#instagood #tagblender #tagblender #likesforlikes #ilikeback #liketeam #liker#ilike #likealways #likebackteam #ilikeyou #ilikeit #likeme #tflers #likes #likesback #photooftheday #likesforlike #iliketurtles #likes4followers #likemebac #ilu #likesreturned #l4l',
            '#followforfollow #picture #italy #art #fashion #pink #blackandwhite #work #f4f #hot #fashionblogger #nyc #makeup #music #luxury #healthy #amazing #funny #happy #Home #inspiration #followme #like4like #fitfam #model #photooftheday #igers #instapic #USA #follow4follow #tattoo #Halloween #swag',
            '#TagsForLikes #blogger #nice #night #autumn #bodybuilding #bestoftheday #red #instagram #likeforlike #beauty #dog #happiness #hair #foodporn #picoftheday #sky #flowers #Repost #instadaily #style #girl #instagood #vsco #goals #black #TBT #lifestyle #outfit #beach #wanderlust #Family #Selfie',
            '#like4like #liking #likeall #likeforlike #likes4likes #love #instagood #tagblender #tagblender #likesforlikes #ilikeback #liketeam #liker #ilike #likealways #likebackteam #ilikeyou #ilikeit #likeme #tflers #likes #likesback #photooftheday'
]

#Program For Unfollow Everyone
def ig_teamhunter():
    KMFHEADER()
    TEAMHUNTER()
    userdata = input("\u001b[32m[+]\u001b[0m Enter Target Team username:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        try:
            bot.follow(userdata)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(120)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            bot.unfollow(userdata)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(30)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

#Program For Unfollow Everyone
def ig_masslooker():
    KMFHEADER()
    MASSLOOKER()
    while True:
        try:
            bot.reset_cache()
            user_to_get_likers_of = bot.get_user_id_from_username(username=random.choice(USERID_FOR_MASSLOOKER))
            current_user_id = user_to_get_likers_of
            try:
                bot.reset_cache()
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
                            ][:30]

                # WATCH USERS STORIES
                if bot.watch_users_reels(liker_ids):
                    bot.logger.info("Total stories viewed: %d" % bot.total["stories_viewed"])

                # CHOOSE RANDOM LIKER TO GRAB HIS LIKERS AND REPEAT
                countdown(60)
            except Exception as e:
                # If something went wrong - sleep long and start again
                bot.logger.info(e)
                current_user_id = user_to_get_likers_of
                time.sleep(240 * random.random() + 60)

        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Program For ReHashtag
def ig_rehashtag():
    KMFHEADER()
    REHASHTAG()
    postlink = input("\u001b[32m[+]\u001b[0m Enter Media link:-")
    print ("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        try:
            media_link = postlink
            media_id = bot.get_media_id_from_link(media_link)
            comments = bot.get_media_comments(media_id)
            commented_users = []
            bot.logger.info("Commenting Hashtags to Your Photo")
            bot.comment(media_id, comment_text=random.choice(hashtagList))
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(600)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            for comment in tqdm(comments):
                replied = False
                parent_comment_id = comment["pk"]
                user_id = comment["user"]["pk"]
                comment_type = comment["type"]
                commenter = comment["user"]["username"]
                text = comment["text"]
                #process
                bot.logger.info("Deleting Hashtags From Your Photo")
                bot.delete_comment(media_id,parent_comment_id)
                #commented_users.append(user_id)
                print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
                countdown(60)
                print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Infinity Feed Like
def ig_feedliker():
    KMFHEADER()
    FEEDLIKER()
    while True:
        try:
            bot.like_timeline(amount=10)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(300) #waiting for 3min
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

#Inshackle Followers
def ig_inshackle():
    KMFHEADER()
    INSHACKLE()
    while True:
        try:
            bot.follow_users(user_ids=USERID_FOR_INSHACKLE)
            countdown(counter_time=600)
            bot.unfollow_users(user_ids=USERID_FOR_INSHACKLE)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(120)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Program For Unfollow Non-Followers
def ig_nonfollowers():
    KMFHEADER()
    NONFOLLOWERS()
    while True:
        try:
            bot.unfollow_non_followers(n_to_unfollows=10)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            countdown(240)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()


#Direct Message
def ig_directmessage():
    KMFHEADER()
    DIRECTMESSAGE()
    INUsrp_TEXT = input("\u001b[32m[+]\u001b[0m Enter Message want to Sent:-")
    print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
    while True:
        try:
            USER = bot.get_hashtag_users(hashtag="mallu")
            USER_IDD = random.choice(USER)
            NAME = bot.get_username_from_user_id(USER_IDD)
            FULL_TEXT = ("Hi "+NAME+", "+INUsrp_TEXT)
            bot.send_profile(profile_user_id=bot.user_id,user_ids=USER_IDD,text=FULL_TEXT)
            bot.logger.info("Message Sented to "+ NAME)
            countdown(300)
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

#Profile-Scraper
def ig_ProfileScraper():
    KMFHEADER()
    PROFILE_SCRAPER()
    while True:
        try:
            userID = input("\u001b[32m[+]\u001b[0m Enter Username:-")
            user_id = bot.get_user_id_from_username(userID)
            user_info = bot.get_user_info(user_id)
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            FULLNAME = print("\u001b[32m[+]\u001b[0m Name:-",user_info['full_name'])
            MEDIA_COUNT = print("\u001b[32m[+]\u001b[0m Media Count:-",user_info['media_count'])
            FOLLOWERS = print("\u001b[32m[+]\u001b[0m Followers:-",user_info['follower_count'])
            FOLLOWING = print("\u001b[32m[+]\u001b[0m Following:-",user_info['following_count'])
            BIO = print("\u001b[32m[+]\u001b[0m Bio:-",user_info['biography'])
            WEBSITE = print("\u001b[32m[+]\u001b[0m Website:-",user_info['external_url'])
            PHONENUMBER = print("\u001b[32m[+]\u001b[0m Phone:-","+",user_info['public_phone_country_code'],user_info['public_phone_number'])
            EMAIL =  print("\u001b[32m[+]\u001b[0m Email:-",user_info['public_email'])
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            print('\u001b[32m[1]\u001b[0m Main-Menu')
            print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
            SCRA_Inpur = input("\u001b[32m[+]\u001b[0m Enter Input:-")
            if SCRA_Inpur == "1":
                Option()
            else:
                clear()
                Option()

        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()

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


def MainBot():
    clear()
    Login()
    Option()

def ELSE_BOT():
    Option()

def LogOut():
    exit()
