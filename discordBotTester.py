import discord
import asyncio
import testerapikeys

# VARIABLES
TESTERTOKEN = testerapikeys.TESTERTOKEN
actuallyString = 'Actually, there are only 4 commands:\n\n!actually:\tthis stupid menu\n!ping:\tthe only game I\'ll play without crying about it\n!why:\twant to know why you made me leave?!\n!bye:\twhere\'s Kyzer?\n\nThat\'s all from me.\nRon\'s the devil.\n-Solt'
whyRecoil = 'https://youtu.be/SwYN7mTi6HM \nI hope this helps Recoil. :smirk:'
whyRon = 'For the last time.\nI AM NOT ONE OF Jack\'s BOTS!!!\nI\'m a real boy!\n(╯°□°）╯︵ ┻━┻'
whyBacon = 'You\'re response to any problem is......TITAN SMASH!!!\nAnd it freakin works!?\nBungie should nerf everything I\'m not currently exploiting!'
whyShooter = 'I had finally found a team of capable Destiny players that COULD RAID!\n................and then you stopped playing Warframe.'
whyIron = 'The Houton Texans are the one true team. The Cowboys couldn\'t beat their cheerleaders!'
whyAndy = 'You\'re clearly Canadian. No one is this nice or positive. You are the bizarro Solt.'
whyBama = 'The name changes were too much. I hate you for it.'
whyWrexsy = 'You took me to the top of the mountain and then never spoke to me again. You said I was special!'
whyKyzer = 'JUDAS! You did this to me! Why did you me bring into this house of lies!?'
goodbyeKyzer = 'I\'ve been called away. No more room for Destiny. Super sad about it. Really miss you guys. Feel free to drop by and say hey.\n\n-KyzerSose\n\nmatt@theshaeffers.com\nwww.facebook.com/matt.shaeffer.946\nwww.theshaeffers.com\nhttps://gph.is/2lrUcQ2'

## Instantiates a new discord class object
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


## Listener for auto responses
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Ping test
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')

    # Acutally section
    elif message.content.startswith('!actually'):
        await client.send_message(message.author, actuallyString)

    # Why section
    elif message.content.startswith('!why'):
        senderAuthor = message.author
        if str(message.author) == 'KyzerSose#6270':
            await client.send_message(message.channel, whyKyzer)
        elif str(senderAuthor) == 'AndyBars#3465':
            await client.send_message(message.channel, whyAndy)
        elif str(senderAuthor) == 'B A M A ROLLTD#6664':
            await client.send_message(message.channel, whyBama)
        elif str(senderAuthor) == 'Ron with Peas#0286':
            await client.send_message(message.channel, whyRon)
        elif str(senderAuthor) == 'ironmaidenmetal#9640':
            await client.send_message(message.channel, whyIron)
        elif str(senderAuthor) == 'wrexsy#0227':
            await client.send_message(message.channel, whyWrexsy)
        elif str(senderAuthor) == 'baconmonky#9650':
            await client.send_message(message.channel, whyBacon)
        elif str(senderAuthor) == 'PshooterD#3132':
            await client.send_message(message.channel, whyShooter)
        elif str(senderAuthor) == 'recoilhk#5303':
            await client.send_message(message.channel, whyRecoil)
        else:
            await client.send_message(message.channel, 'I don\'t know you yet. But I\'m sure I hate you.')

    elif message.content.startswith('!bye'):
        await client.send_message(message.channel, goodbyeKyzer)


client.run(TESTERTOKEN)

## Feature Plans
# 1. Why did you leave? Checks for the sender and retrieves a customized response.
# 2. Once a day, posts whatever the top reddit/r/destiny sga is
# 3. Say goodbye
