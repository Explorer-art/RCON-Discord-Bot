import disnake
from disnake.ext import commands
import asyncio
from websockets.sync.client import connect

config = {
    "token" : "MTIyMTEyMjI3NjQ1MjMzNTY0Nw.GUOiUt.1bX8At4e1SZs3FybMw0mC5F9DjwpIjcIGCQZSo",
    "prefix" : "$"
}

allowed_ids = [640856584595046421] # ID пользователя/ей которые смогут использовать RCON

ip = "92.63.107.40:9001" # IP и порт сервера (порт веб-сервера)
rcon_password = "nDqNo7WnRd" # RCON пароль

bot = commands.Bot(command_prefix=config["prefix"], intents=disnake.Intents.all())

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

bot.run(config["token"])