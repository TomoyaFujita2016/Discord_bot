import discord
import asyncio
import itertools
import random

TOKEN = "TOKEN"
client = discord.Client()
BY_MAMORU = True

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global BY_MAMORU
    if message.content.startswith('!team'):
        try:
            num = int(message.content[5:].strip())
        except:
            return
        All = [x for x in range(1, num+1)]
        teams = [[], []]
        team_num = int(num/2)
        first_idx = random.randint(0, 1)
        second_idx = 1 - first_idx

        for _ in range(team_num):
            rand = random.randint(0, len(All)-1)
            teams[first_idx].append(All[rand])
            All.pop(rand)
        teams[second_idx].extend(All)

        teams[first_idx] = [str(x) for x in sorted(teams[first_idx])]
        teams[second_idx] = [str(x) for x in sorted(teams[second_idx])]

        msg = ":skull: `A-team: " + ", ".join(teams[first_idx]) + " `:skull:\n\n"
        msg += ":smiling_imp: `B-team: " + ", ".join(teams[second_idx]) + " `:smiling_imp:\n"

        await client.send_message(message.channel, msg)

    elif message.content.startswith('!wise'):
        wises = ["Some people feel the rain. Others just get wet.",
        "I like to be a free spirit. Some don’t like that, but that’s the way I am.",
        "The man who has no imagination has no wings.",
        "I don’t dream at night, I dream all day; I dream for a living.",
        "がんばれ",
        "To say Good bye is to die a little.",
        "Don’t walk behind me; I may not lead. Don’t walk in front of me; I may not follow. Just walk beside me and be my friend.",
        "I can accept failure, everyone fails at something. But I can’t accept not trying.",
        "Defeat? I do not recognize the meaning of the word.",
        "いける"]
        wise = wises[random.randint(0,len(wises)-1)]

        msg = "*" + wise + "* >:thinking:"

        await client.send_message(message.channel, msg)

    elif message.content.startswith('がんばれ'):
        msg = "がんばる >:smile:"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('守るな') or message.content.startswith("まもるな"):
        msg = "ラジャ! >:hugging: "
        BY_MAMORU = False
        await client.send_message(message.channel, msg)

    elif message.content.startswith('守れ') or message.content.startswith("まもれ"):
        msg = "ラジャ! >:hugging: "
        BY_MAMORU = True
        await client.send_message(message.channel, msg)


    elif message.content.startswith('しばくぞ'):
        if BY_MAMORU:
            msg = "守る！"
        else:
            msg = "あっ、どうぞ"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('あじふらい'):
        msg = "しばくぞ"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('ゆうかす'):
        msg = ":poop:"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('しょうがねぇなぁ') or message.content.startswith('しょうがねえなあ') or message.content.startswith('しょうがねえなぁ'):
        msg = "わからせてやるかぁ"
        await client.send_message(message.channel, msg)

    elif 'くちゅん' in message.content and not ':hugging:' in message.content:
        msg = ":hugging:< ちゃしゃ"
        await client.send_message(message.channel, msg)
        await asyncio.sleep(1.8)
        msg = "せやなー"
        await client.send_message(message.channel, msg)

    elif 'ちゃしゃ' in message.content:
        msg = ":hugging:< くちゅん"
        await client.send_message(message.channel, msg)
        await asyncio.sleep(1.8)
        msg = "そやろなー"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!roulette'):
        PICK_NUM = 5
        SLEEP_TIME = 0.8
        TIME_RATIO = 1.13
        try:
            num = int(message.content[9:].strip())
        except:
            return
        msg = "ルーレットスタート！"
        tmp = await client.send_message(message.channel, msg)

        big_numbers = list(range(1, num+1))
        while len(big_numbers) < PICK_NUM:
            big_numbers *= 2
        picked_numbers = [x for x in random.sample(big_numbers, PICK_NUM)]
        random.shuffle(picked_numbers)
        for number in picked_numbers:
            await client.edit_message(tmp, number)
            await asyncio.sleep(SLEEP_TIME)
            SLEEP_TIME *= TIME_RATIO
        await client.send_message(message.channel, "しゅーりょー")

    elif message.content.startswith('ハンドガンにしちゃった'):
        msg = "斬りに行く"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('あじふ？'):
        msg = "l(l＾o＾)kｱｼﾞﾌｩ…？"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('あじふ☆'):
        msg = "l(l＾o＾)kｱｼﾞﾌｩ…★"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('あじふ！？'):
        msg = "l(l＾o＾)kｱｼﾞﾌｩ…！？"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('あじふ！'):
        msg = "l(l＾o＾)kｱｼﾞﾌｩ…！"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('あじふ'):
        msg = "l(l＾o＾)kｱｼﾞﾌｩ…"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('エビバディセイ'):
        msg = "でゅあぁぁぁぁぁぁぁぁぁぁ('A`)"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('でゅあ'):
        msg = "俺結構マットの才能あるなぁ＞:thinking:"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('こん'):
        msg = "はああああああああああああああああい　ぼぉくだよぉ"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('おきて') and False:
        tyasya = "<@264992109361233921> "
        msg = tyasya*30 + "起きて"
        await client.send_message(message.channel, msg)
        await asyncio.sleep(0.7)
        await client.send_message(message.channel, msg)
        await asyncio.sleep(0.7)
        await client.send_message(message.channel, msg)

    # rare case
    rand = random.randint(0, 150)
    if rand == 0:
        msgs = ["わからせてやるかぁ", "ほげえ", "ふえぇぇ", "ほええぇえ", 'The :monkey: said, "{}"'.format(message.content)]
        msg = msgs[random.randint(0, len(msgs)-1)]
        await client.send_message(message.channel, msg)



client.run(TOKEN)
