import disnake
from disnake.ext import commands
import asyncio
from websockets.sync.client import connect
from config import token, prefix, allowed_ids, ip, rcon_password

bot = commands.Bot(command_prefix=prefix, intents=disnake.Intents.all())

@bot.slash_command()
async def rcon(ctx, command):
    if ctx.author.id in allowed_ids:
        websocket = connect("ws://" + ip)
        websocket.send(rcon_password)
        data = websocket.recv()

        websocket.send("/" + command)
        data = websocket.recv()

        embed = disnake.Embed(
            title = "RCON > /" + command,
            description = str(data),
            colour = disnake.Colour.orange())

        print("[LOG] User " + str(ctx.author) + " used RCON command: " + command)
    else:
        embed = disnake.Embed(
            title = "RCON",
            description = "Извините, но у вас недостаточно прав для использования RCON!",
            colour = disnake.Colour.orange())

    await ctx.send(embed=embed)

bot.run(token)
