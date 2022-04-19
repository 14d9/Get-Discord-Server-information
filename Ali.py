import requests, webbrowser, time

print("""
      _____    __    ____                       _      ___                    __  _         
     / ___/__ / /_  / __/__ _____  _____ ____  (_)__  / _/__  ______ _  ___ _/ /_(_)__  ___ 
    / (_ / -_) __/ _\ \/ -_) __/ |/ / -_) __/ / / _ \/ _/ _ \/ __/  ' \/ _ `/ __/ / _ \/ _ \ 
    \___/\__/\__/ /___/\__/_/  |___/\__/_/   /_/_//_/_/ \___/_/ /_/_/_/\_,_/\__/_/\___/_//_/                                                                                       
""")
print("""
      [1] Get Discord Server information
      [0] Exit
""")

choice = int(input('Choose number :'))

# Exit
if choice == 0 :
    print('Goodbye see you later <3')
    time.sleep(2)
    exit()
# Get Discord Server information
if choice == 1 :
      discordlink = input("[+] DISCORD SERVER LINK : ")

      url = (f"https://discord.com/api/v9/invites/{discordlink}?with_counts=true&with_expiration=true")
      headers = {
            'accept': 'application/json',
            'accept-language': 'en',
            'user-agent': 'ios:2.65.0:488:14:iPhone13,3',
      }
      req = requests.get(url,headers=headers)
      instagram = 'https://www.instagram.com/q97l/'

      if req.status_code == 200:
            id = req.json()["guild"]["id"]
            avatar = req.json()["guild"]["icon"]
            banner = req.json()["guild"]["banner"]
            splash = req.json()["guild"]["splash"]
            print("")
            print("")
            print(f"[ Server Link : https://discord.gg/{discordlink} ]")

            print("   Server Name : ",req.json()["guild"]["name"])
            print("   Server Description : ",req.json()["guild"]["description"])
            print("   Server ID : ",req.json()["guild"]["id"])
            print("   Server Avatar : ",f"https://cdn.discordapp.com/icons/{id}/{avatar}.webp?size=96")
            print("   Server Banner : ",f"https://cdn.discordapp.com/banners/{id}/{banner}.webp?size=2048")
            print("   Server Invite Background : ",f"https://cdn.discordapp.com/splashes/{id}/{splash}.jpg?size=2048")
            print("   Online Members : ",req.json()["approximate_presence_count"])
            print("   All Members : ",req.json()["approximate_member_count"])
            print("   Server Boosts : ",req.json()["guild"]["premium_subscription_count"])
            print("   Custom Invite Link : ",req.json()["guild"]["vanity_url_code"])
            print("   Server Level : ",req.json()["guild"]["verification_level"])
            print("   nsfw : ",req.json()["guild"]["nsfw"])
            print("   nsfw Level : ",req.json()["guild"]["nsfw_level"])

      elif req.status_code == 404:
            print("ERROR!")

      print("")
      print("")
      print("[+] Thank you for using my tool")
      time.sleep(1)
      webbrowser.open(instagram)
      print("")
      print("[!] After 15 seconds [Get Discord Server information] will be closed automatically")
      time.sleep(15)
