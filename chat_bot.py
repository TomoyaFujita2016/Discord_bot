import discord
from bs4 import BeautifulSoup
import urllib.request as req
import requests
import threading
from datetime import datetime
import time
import asyncio
import random

from discord.ext.commands import Bot
from discord.ext import commands
 
client2 = commands.Bot(command_prefix="_")

BOT_TOKEN = "NDMwNzIzMjcyNjM2NjI5MDAy.DaUX3w.l1PCuvFJsVqGrjUZtzk_gu21lMo" 
BITCOIN = [["び", "ビ"], ["っ","ッ"], ["と","ト" ], ["こ","コ"], ["い" ,"イ" ], ["ん","ン" ,"ｎ", "n" ]]
USERS = ["りりぃん"]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if client.user == message.author:
        return

    if message.content.startswith("ふえぇ"):
        await client.send_message(message.channel, "ふえぇ///")

    if not len(message.content) < len(BITCOIN):
        if await checkBit(message.content[:len(BITCOIN)]):
            await bitcoin(message)

    if message.content.startswith("りりぃん"):
        await client.send_message(message.channel, USERS[0] + " はね、とっても変態なロリコンさんなんだよ！")
    
async def include_message(message, words):
    for word in words:
        if word in message.content:
            return True
    return False

async def bitcoin(message):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    yen = await getYen()
    value = float(str(value).replace(",", "")) * yen
    await client.send_message(message.channel, "えーとねービットコインの値段は" + str(value) + "円だよぉー(´・ω・｀)")

async def checkBit(string):
    for i, bit in enumerate(BITCOIN):
        if not string[i] in bit:
            return False
    return True

async def getYen():
    url="https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
    res = req.urlopen(url) 
    soup = BeautifulSoup(res, "html.parser");
    d1 = soup.select_one(".stoksPrice").string #(1)
    return float(d1)

async def timeSignal():
    await client.wait_until_ready()
    byOnce = True
    channel = discord.Object(id="366552420068753419")
    message = await hello_word()
    while not client.is_closed:
        m_time = await getTime()
        if m_time == "07" and byOnce:
            await client.send_message(channel, message)
            byOnce = False
        
        if m_time == "08":
            byOnce = True
        await asyncio.sleep(20)
            
async def hello_word():
    messages = ["おはよぉーーーー！(ﾟ∀ﾟ)",
            "(｡･･)ﾉぉはょぅ♪",
            "おはよー！！！！！起きて！！！！！！！！朝だよ！！！！！！すごい朝！！！！外が明るい！！！！！カンカンカンカンカンカンカ",
            "【布団】っω-)おはよう・・",
            ":notes:gooood morning!:notes:",
            "おは翔ございます(｀･3･´)",
            "ｵｯﾊヽ(･ω･｡)ﾉｵﾊヽ(･ω･)ﾉｵﾊヽ(｡･ω･)ﾉｻﾝｻﾝｰ♪",
            "v(＞◇＜)vｵﾊﾖﾝｺﾞｼﾞｬｲﾏｽﾞ",
            "おはよう！今日もいい一日を☆"]
    message = messages[random.randint(0, len(messages)-1)]
    return message 

async def getTime():
    return datetime.now().strftime('%M')
    
if __name__=="__main__":
    
    client.loop.create_task(timeSignal())
    client.run(BOT_TOKEN)
