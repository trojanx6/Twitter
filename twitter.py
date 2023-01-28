import os
requmen = ["pip install requests ", "pip install bs4", "pip install colorama"]
for i in requmen:
    os.system(i)



from bs4 import BeautifulSoup as btu
import requests as req
from colorama import Fore, Style



print(Fore.WHITE+ Style.BRIGHT +"""
#########                                    
    #    #    # # ##### ##### ###### #####  
    #    #    # #   #     #   #      #    # 
    #    #    # #   #     #   #####  #    # 
    #    # ## # #   #     #   #      #####  
    #    ##  ## #   #     #   #      #   #  
    #    #    # #   #     #   ###### #    # 
                                            
Twwitter Osnit Tool
coder:Trojanx6
"""+Fore.WHITE)


username = input(Fore.GREEN+ Style.BRIGHT +"user name twiter: ")


class Main:
    def __init__(self):
        self.url =f"https://nitter.net/{username}/"
    def KaziKurek(self):
        istek = req.get(self.url)
        html = istek.text
        soup = btu(html, "html.parser")
        user = soup.find("a", {"class":"profile-card-fullname"}).text
        tweets_num = soup.find("span",{"class":"profile-stat-num"}).text
        following = soup.find("li",{"class":"following"}).find("span",{"class":"profile-stat-num"}).text
        followers = soup.find("li",{"class":"followers"}).find("span",{"class":"profile-stat-num"}).text
        likes = soup.find("li",{"class":"likes"}).find("span",{"class":"profile-stat-num"}).text
        img = soup.find("div",{"class":"profile-card"}).find("div",{"class":"profile-card-info"}).find("a", {"class":"profile-card-avatar"}).get("href")
        imglink = "https://nitter.net"+img#
        print(Fore.GREEN+ Style.BRIGHT + "User:"+Fore.WHITE+user)
        print(Fore.GREEN+ Style.BRIGHT + "following:"+Fore.WHITE+following)
        print(Fore.GREEN + Style.BRIGHT + "follwers:"+Fore.WHITE+followers)
        print(Fore.GREEN + Style.BRIGHT + "likes:"+Fore.WHITE+likes)
        print(Fore.GREEN+ Style.BRIGHT + 'Tweets Num:'+Fore.WHITE+tweets_num)
        print(Fore.GREEN+ Style.BRIGHT + 'Prodfile Img:'+Fore.WHITE+imglink)
        
if __name__=="__main__":
    app = Main()
    app.KaziKurek()