import discord
import db
from services import userservice

# https://medium.com/@moomooptas/how-to-make-a-simple-discord-bot-in-python-40ed991468b4
# https://discordpy.readthedocs.io/en/latest/api.html#client
client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready")
    db.get_connection()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Making bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!join"):
        username = str(message.author)
        formattedUsername = username.split("#")[0]
        if userservice.get_user(formattedUsername) == formattedUsername:
            await message.channel.send("User already exists ")
        else:
            userservice.create_user(formattedUsername)
            await message.channel.send("Thanks for joining " + formattedUsername)
    if message.content.startswith("!whoami"):
        username = str(message.author)
        formattedUsername = username.split("#")[0]
        player = userservice.get_user(formattedUsername)
        await message.channel.send("You are " + player)
    if message.content.startswith("!players"):
        players = userservice.get_players()
        await message.channel.send("List of players: " + str(players))
    if message.content.startswith("!leave"):
        username = str(message.author)
        formattedUsername = username.split("#")[0]
        player = userservice.remove_player(formattedUsername)
        await message.channel.send("Removed player: " + player)
    if message.content.startswith("!stop"):
        await client.close()
    if message.content.startswith("!begin"):
        count = userservice.countdown()
        while count >= 0:
            await message.channel.send("Game starting in " + str(count))
client.run('NTY1Mzc3NTgxNjYzMzg3NjY5.XK1jhg.SRwo6In-VdJPzoVZxjn8vEJQXuE')