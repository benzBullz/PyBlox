from roblopy import Users
from roblopy import Friends
from roblopy import Groups
from roblopy import User
from roblopy import Assets
from roblopy import Group
from termcolor import colored
import os
os.system("color")

# Hello if you are reading this :)

logo1=colored("""
┏━━━┳┓╋╋┏┳━━┓┏┓╋╋┏━━━┳━┓┏━┓
┃┏━┓┃┗┓┏┛┃┏┓┃┃┃╋╋┃┏━┓┣┓┗┛┏┛
┃┗━┛┣┓┗┛┏┫┗┛┗┫┃╋╋┃┃╋┃┃┗┓┏┛
┃┏━━┛┗┓┏┛┃┏━┓┃┃╋┏┫┃╋┃┃┏┛┗┓
┃┃╋╋╋╋┃┃╋┃┗━┛┃┗━┛┃┗━┛┣┛┏┓┗┓
┗┛╋╋╋╋┗┛╋┗━━━┻━━━┻━━━┻━┛┗━┛
      Developed By B.P
 (Missing commands: Errors)""", "red")
print(logo1)

print(colored(" O P T I O N S","white"))
print(colored(" 0. Options","white"))
print(colored(" 1. Is online","white"))
print(colored(" 2. First friend","white"))
print(colored(" 3. Is friend","white"))
print(colored(" 4. Latest friend","white"))
print(colored(" 5. Is banned","white"))
print(colored(" 6. Description","white"))
print(colored(" 7. Status","white"))
print(colored(" 8. Date of creation","white"))
print(colored(" 9. Is in group","white"))
print(colored(" 10. Role in group","white"))
print(colored(" 11. Group is primary","white"))
print(colored(" 12. ID from username","white"))
print(colored(" 13. Username from ID","white"))
print(colored(" 14. Rank in group","white"))
print(colored(" 15. Last online","white"))
print(colored(" 16. Can manage asset","white"))
print(colored(" 17. Friends","white"))
print(colored(" 18. Asset Info","white"))
print(colored(" 19. Groups","white"))
print(colored(" 20. Groups (ID)","white"))
print(colored(" 21. Online Status","white"))
print(colored(" 22. Display name","white"))
print(colored(" 23. Group Info","white"))
print(colored(" 24. Has Asset","white"))
print(colored(" 25. Avatar Image Link","white"))
print(colored(" 26. Troubleshooting","magenta"))
print(colored(" 27. Donate","blue"))
print(colored("================================","red"))
try:
    while True:
            ans = input(colored(" Choice $ ","white"))
            if ans == "0":
                print(colored(" O P T I O N S","white"))
                print(colored(" 0. Options","white"))
                print(colored(" 1. Is online","white"))
                print(colored(" 2. First friend","white"))
                print(colored(" 3. Is friend","white"))
                print(colored(" 4. Latest friend","white"))
                print(colored(" 5. Is banned","white"))
                print(colored(" 6. Description","white"))
                print(colored(" 7. Status","white"))
                print(colored(" 8. Date of creation","white"))
                print(colored(" 9. Is in group","white"))
                print(colored(" 10. Role in group","white"))
                print(colored(" 11. Group is primary","white"))
                print(colored(" 12. ID from username","white"))
                print(colored(" 13. Username from ID","white"))
                print(colored(" 14. Rank in group","white"))
                print(colored(" 15. Last online","white"))
                print(colored(" 16. Can manage asset","white"))
                print(colored(" 17. Friends","white"))
                print(colored(" 18. Asset Info","white"))
                print(colored(" 19. Groups","white"))
                print(colored(" 20. Groups (ID)","white"))
                print(colored(" 21. Online Status","white"))
                print(colored(" 22. Display Name","white"))
                print(colored(" 23. Group Info","white"))
                print(colored(" 24. Has Asset","white"))
                print(colored(" 25. Avatar Image Link","white"))

                print(colored(" 26. Troubleshooting","magenta"))
                print(colored(" 27. Donate","blue"))
                print(colored("================================","red"))
            elif ans == "1":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    txt = colored(" Is online:","white")
                    on = Users.is_online(userid)
                    if on == False:
                        on = colored(Users.is_online(userid),"red")
                    elif on == True:
                        on = colored(Users.is_online(userid),"green")
                    print(txt,on)
                except:
                    print(colored(" Error: Invalid user","red"))
            elif ans == "2":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    firstf = Friends.get_first_friend(userid)
                    hshs = colored(firstf["Username"],"green")
                    hshb = colored(firstf["Id"],"green")
                    jjh = colored(" First friend:","white")
                    print(jjh,hshs)
                    print(colored(f" User ID: {hshb}","white"))
                except:
                    print(colored("Error: Invalid user/user has no friends","red"))
            elif ans == "3":
                try:
                    user = input(colored(" User1> ","red"))
                    user2 = input(colored(" User2> ","red"))
                    userid = Users.get_id_from_username(user)
                    userid2 = Users.get_id_from_username(user2)
                    is_friends = Friends.users_are_friends(userid,userid2)
                    if is_friends == True:
                        is_friends = colored(Friends.users_are_friends(userid,userid2),"green")
                    elif is_friends == False:
                        is_friends = colored(Friends.users_are_friends(userid,userid2),"red")
                    blah = colored(" Are friends:","white")
                    print(blah,is_friends)                    
                except:
                    print(colored("Error: Invalid user(s)/user(s) has no friends","red"))
            elif ans == "4":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    x = Friends.get_recent_friend(userid)
                    user = colored(x["Username"],"green")
                    id = colored(x["Id"],"green")
                    print(colored(f" Latest friend: {user}","white"))
                    print(colored(f" User ID: {id}","white"))
                except:
                    print(colored("Error: Invalid user/user has no friends","red"))
            elif ans == "5":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    ahbah=Users.is_banned(userid)
                    if ahbah == True:
                        ahbah=colored(Users.is_banned(userid),"red")
                    elif ahbah == False:
                        ahbah=colored(Users.is_banned(userid),"green")
                    print(colored(f" Is banned: {ahbah}","white"))
                except:
                    print(colored(" Error: Invalid user","red"))
            elif ans == "6":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    ahbah=colored(Users.get_profile_description(userid),"green")
                    print(colored(f" Description: {ahbah}","white"))
                except:
                    print(colored(" Error: Invalid user","red"))
            elif ans == "7":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    ahbah=colored(Users.get_profile_status(userid),"green")
                    print(colored(f" Status: {ahbah}","white"))
                except:
                    print(colored(" Error: Invalid user","red"))
            elif ans == "8":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    i = User(userid)
                    cr = colored(i.created,"green")
                    print(colored(f" Date of creation: {cr}","white"))

                    
                except:
                    print(colored(" Error: Invalid user","red"))
            elif ans == "9":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    groupid = input(colored(" Group ID> ","red"))
                    result=Users.is_in_group(userid,groupid)
                    if result == True:

                        result=colored(Users.is_in_group(userid,groupid),"green")
                    elif result == False:

                        result=colored(Users.is_in_group(userid,groupid),"red")

                    print(colored(f" User in group: {result}","white"))
                except:
                    print(colored("Error: Invalid user/group"))
            elif ans == "10":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    groupid = int(input(colored(" Group ID> ","red")))
                    res = colored(Users.get_role_in_group(userid,groupid),"green")
                    print(colored(f" Role in group: {res}","white"))
                except:
                    print(colored(" Error: Invalid user/group","red"))
            elif ans == "11":
               try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    groupid = int(input(colored(" Group ID> ","red")))
                    res = Users.group_is_primary(userid,groupid)
                    if res == True:
                        res = colored(Users.group_is_primary(userid,groupid),"green")
                    elif res == False:

                        res = colored(Users.group_is_primary(userid,groupid),"red")
                    print(colored(f" Group is primary: {res}","white"))
               except:
                   print(colored(" Error: Invalid user/group","red"))
            elif ans == "12":
                try:
                    user = input(colored(" User> ","red"))
                    outp = colored(Users.get_id_from_username(user),"green")
                    print(colored(f" ID: {outp}","white"))
                except:
                    print(colored(" Invalid user","red"))
            elif ans == "13":
                try:
                    user = input(colored(" ID> ","red"))
                    outp = colored(Users.get_username_from_id(user),"green")
                    print(colored(f" User: {outp}","white"))
                except:
                    print(colored(" Invalid user","red"))
            elif ans == "14":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    groupid = int(input(colored(" Group ID> ","red")))
                    res = colored(Users.get_rank_in_group(userid,groupid),"green")
                    print(colored(f" Rank in group: {res}","white"))
                except:
                    print(colored(" Error: Invalid user/group","red"))
            elif ans == "15":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)

                    gen = Users.get_online_status(userid)
                    lonline = colored(gen["LastOnline"],"green")
                    print(colored(f" Last online: {lonline}","white"))
                except:
                    print(colored("Error: Invalid user","red"))
            elif ans == "16":
                try:
                    user = input(colored(" User> ","red"))
                    userid = Users.get_id_from_username(user)
                    assetid = int(input(colored(" Asset ID> ","red")))
                    outp = Users.can_manage_asset(userid,assetid)
                    if outp == True:
                        outp = colored(Users.can_manage_asset(userid,assetid),"green")
                    elif outp == False:
                        outp = colored(Users.can_manage_asset(userid,assetid),"red")

                    print(colored(f" User can manage asset: {outp}","white"))
                except:
                    print(colored("Error: Invalid user/asset","red"))
            elif ans == "17":
                try:
                   user = input(colored(" User> ","red"))
                   userid = Users.get_id_from_username(user)
                   frnds = colored(Friends.get_friends(userid),"green")
                   warn = input(colored(" Warning: This may return a massive unordered list of friends. Proceed? (Y,n): ","yellow"))
                   if warn == "Y":
                       print(colored(" Friends","white"))
                       print(colored(" -------","white"))
                       print(frnds)
                   elif warn == "n":
                       print(colored(" Error: Prompt cancelled","red"))
                   else:
                       print(colored(" Invalid answer","red"))
                except:
                   print(colored(" Error: Invalid user","red"))
            elif ans == "18":
                try:
                    assetid = int(input(colored(" Asset ID> ","red")))
                    get =Assets.get_asset(assetid)
                    name = colored(get["Name"],"green")
                    ptype = colored(get["ProductType"],"green")
                    pid = colored(get["ProductId"],"green")
                    desc = colored(get["Description"],"green")
                    atypeid = colored(get["AssetTypeId"],"green")
                    cname = colored(get["Creator"]["Name"],"green")
                    cid = colored(get["Creator"]["Id"],"green")
                    ctype = colored(get["Creator"]["CreatorType"],"green")
                    ctargetid = colored(get["Creator"]["CreatorTargetId"],"green")
                    created = colored(get["Created"],"green")
                    lupdated = colored(get["Updated"],"green")
                    tprice = colored(get["PriceInTickets"],"green")

                    rprice = colored(get["PriceInRobux"],"green")
                    iimagea = colored(get["IconImageAssetId"],"green")
                    sales = colored(get["Sales"],"green")
                    isnew = get["IsNew"]
                    onsale = get["IsForSale"]
                    pdomain = get["IsPublicDomain"]
                    limited = get["IsLimited"]
                    limitedu = get["IsLimitedUnique"]
                    rem = colored(get["Remaining"],"green")
                    minm = colored(get["MinimumMembershipLevel"],"green")
                    crtid = colored(get["ContentRatingTypeId"],"green")

                    print(colored(f" Name: {name}","white"))
                    print(colored(f" Product Type: {ptype}","white"))
                    print(colored(f" Product ID: {pid}","white"))
                    print(colored(" Description:","white"))
                    print(colored(" ---------------------","white"))
                    print(desc)
                    print(colored(" ---------------------","white"))
                    print(colored(f" Asset type ID: {atypeid}","white"))
                    print(colored(" Creator {","white"))
                    print(colored(f" Creator: {cname}","white"))
                    print(colored(f" Creator ID: {cid}","white"))
                    print(colored(f" Creator Type: {ctype}","white"))
                    print(colored(f" Creator Target ID: {ctargetid}","white"))
                    print(colored(" }","white"))
                    print(colored(f" Creation date: {created}","white"))
                    print(colored(f" Last updated: {lupdated}","white"))
                    print(colored(f" Original Robux Price: R${rprice}","white"))
                    print(colored(f" Original Tix Price: T${tprice}","white"))
                    if isnew == True:

                        isnew = colored(get["IsNew"],"green")
                    else:

                        isnew = colored(get["IsNew"],"red")

                    if onsale == True:

                        onsale = colored(get["IsForSale"],"green")
                    else:

                        onsale = colored(get["IsForSale"],"red")

                    if pdomain == True:

                        pdomain = colored(get["IsPublicDomain"],"green")
                    else:

                        pdomain = colored(get["IsPublicDomain"],"red")

                    if limited == True:

                        limited = colored(get["IsLimited"],"green")
                    else:

                        limited = colored(get["IsLimited"],"red")

                    if limitedu == True:

                        limitedu = colored(get["IsLimitedUnique"],"green")
                    else:

                        limitedu = colored(get["IsLimitedUnique"],"red")

                    print(colored(f" Is new: {isnew}","white"))
                    print(colored(f" On sale: {onsale}","white"))
                    print(colored(f" Public Domain: {pdomain}","white"))
                    print(colored(f" Limited: {limited}","white"))
                    print(colored(f" LimitedU: {limitedu}","white"))
                    print(colored(f" Remaining: {rem}","white"))
                    print(colored(f" Minimum Membership LvL: {minm}","white"))
                    print(colored(f" Content Rating Type ID: {crtid}","white"))

                    
                except:
                    print(colored(" Error: Invalid user/asset","red"))
            elif ans == "19":
                user = input(colored(" User $ ","red"))
                userid = Users.get_id_from_username(user)
                groups = Groups.get_users_groups(userid)
                x=1
                for group in groups:
                    print(colored(f" [{x}]{group}","green"))
                    x=x+1
            elif ans == "20":
                user = input(colored(" User $ ","red"))
                userid = Users.get_id_from_username(user)
                groups = Groups.get_users_group_ids(userid)
                x=1
                for group in groups:
                    print(colored(f" [{x}]{group}","green"))
                    x=x+1
            elif ans == "21":
                try:
                    user = input(colored(" User $ ","red"))
                    userid = Users.get_id_from_username(user)
                    status = Users.get_online_status(userid)
                    GameId = colored(status["GameId"],"green")
                    IsOnline = status["IsOnline"]
                    if IsOnline == True:
                        IsOnline = colored(status["IsOnline"],"green")
                    else:
                        IsOnline = colored(status["IsOnline"],"red")
                    LastLocation = colored(status["LastLocation"],"green")
                    LastOnline = colored(status["LastOnline"],"green")
                    LocationType = colored(status["LocationType"],"green")
                    PlaceId = colored(status["PlaceId"],"green")
                    VisitorId = colored(status["VisitorId"],"green")
                    PresenceType = colored(status["PresenceType"],"green")
                    UniverseId = colored(status["UniverseId"],"green")
                    print(colored(f" Game ID: {GameId}","white"))
                    print(colored(f" Online: {IsOnline}","white"))
                    print(colored(f" Last Location: {LastLocation}","white"))
                    print(colored(f" Last Online: {LastOnline}","white"))
                    print(colored(f" Location Type: {LocationType}","white"))
                    print(colored(f" Place ID: {PlaceId}","white"))
                    print(colored(f" Visitor ID: {VisitorId}","white"))
                    print(colored(f" Presence Type: {PresenceType}","white"))
                    print(colored(f" Universe ID: {UniverseId}","white"))
                except:
                    print(colored(f" Error: Invalid user","red"))
            elif ans == "22":
                try:
                    user = input(colored(" User $ ","red"))
                    userid = Users.get_id_from_username(user)
                    x = User(userid)
                    y = colored(x.display_name,"green")
                    print(colored(f" Display Name: {y}","white"))
                except:
                    print(colored(f" Error: Invalid user","red"))
            elif ans == "23":
                try:
                    groupid = int(input(colored(" Group ID $ ","red")))
                    instance = Group(groupid)
                    name = colored(instance.name,"green")
                    id = colored(instance.id,"green")
                    owner = instance.owner
                    ownername = colored(f"{owner['Name']}","green")
                    ownerid = colored(f"{owner['Id']}","green")
                    emblem_url = colored(instance.emblem_url,"green")
                    description = colored(instance.description,"green")
                    roles = instance.roles
                    
                    print(colored(f" Group Name: {name}","white"))
                    print(colored(f" Group ID: {id}","white"))
                    print(colored(" Owner {","white"))
                    print(colored(f" Owner Name: {ownername}","white"))
                    print(colored(f" Owner ID: {ownerid}","white"))
                    print(colored(" }","white"))
                    print(colored(" Roles {","white"))
                    for role in roles:
                        name=colored(role["Name"],"yellow")
                        rank=colored(role["Rank"],"yellow")
                        txt = colored("| Rank:","green")
                        print(colored(f" Role Name: {name} {txt} {rank}","white"))
                    print(colored(" }","white"))
                    print(colored(" Description:","white"))
                    print(colored(" ------------------","white"))
                    print(f" {description}")
                    print(colored(" ------------------","white"))
                    print(colored(f" Emblem URL: {emblem_url}","white"))

                except:
                    print(colored(f" Error: Invalid group","red"))
            elif ans == "24":
                try:
                    user = input(colored(" User $ ","red"))
                    userid = Users.get_id_from_username(user)
                    assetid = int(input(colored(" Asset ID $ ","red")))
                    result = Assets.user_has_asset(userid,assetid)
                    if result == True:
                        result = colored(Assets.user_has_asset(userid,assetid),"green")
                    else:
                        result = colored(Assets.user_has_asset(userid,assetid),"red")
                    print(colored(f" User Has Asset: {result}","white"))
                except:
                    print(colored(" Error: Invalid user/asset","red"))

            elif ans == "25":
                try:
                    user = input(colored(" User $ ","red"))
                    userid = Users.get_id_from_username(user)
                    avatarlink = colored(Users.get_avatar_image(userid),"green")
                    print(colored(f" Avatar Img Link: {avatarlink}","white"))
                except:
                    print(colored(" Error: Invalid user","red"))

            elif ans == "26":
                print(colored(" T R O U B L E S H O O T I N G","magenta"))
                print(colored(" 1. Application is slow","red"))
                print(colored(" 1. Fix: Simply use the clear command","yellow"))
                print(colored(" 2. No thread state found","red"))
                print(colored(" 2. Fix: Restart LibTerm/program","yellow"))
                print(colored(" Others: Make an issue in the Github page.","green"))
            elif ans == "27":
                print(colored(" Donate to my BTC","blue"))
                print(colored(" ---------------------","white"))
                print(colored(" bc1qtcuncnuckyt4kh7j \n 6cy0hx0s0suuyxgj6qk0zp","yellow"))
                print(colored(" ---------------------","white"))

except:
    pass
