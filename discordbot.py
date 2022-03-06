import discord
from discord.ext import commands
from discord.activity import Game
from discord.ext import tasks
from discord.utils import find
from discord.utils import get
import math
from datetime import datetime, timezone, timedelta


JST = timezone(timedelta(hours=+9), "JST")
intents = discord.Intents.default()
intents.members = True
prefix = "?"
bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    print('{0.user} login'.format(bot))
    count = len(bot.guilds)
    await bot.change_presence(activity=discord.Game(name=str(count) + "servers"))

#コマンド

#help
@bot.command()
async def help(ctx):
    await ctx.send("Please check **https://halu-33.github.io**")


#挨拶
@bot.command()
async def hello(ctx, arg):
    await ctx.send("hello " + arg)

#四則計算
@bot.command()
async def add(ctx, x:int, y:int):
    answer_add = x + y
    await ctx.send(f"``{x} + {y} = {answer_add}``")

@bot.command()
async def sub(ctx, x:int, y:int):
    answer_sub = x - y
    await ctx.send(f"``{x} - {y} = {answer_sub}``")

@bot.command()
async def mul(ctx, x:int, y:int):
    answer_mul = x * y
    await ctx.send(f"``{x} * {y} = {answer_mul}``")

@bot.command()
async def div(ctx, x:int, y:int):
    answer_div = x / y
    await ctx.send(f"``{x} / {y} = {answer_div}``")

@bot.command()
async def mod(ctx, x:int, y:int):
    answer_mod = x % y
    await ctx.send(f"``{x} (mod {y} ) = {answer_mod}``")

@bot.command()
async def exp(ctx, x:int, y:int):
    answer_exp = x ** y
    await ctx.send(f"``{x} ^ {y} = {answer_exp}``")

#招待リンク
@bot.command()
async def inv(ctx):
    await ctx.send('``Invitation link for this bot`` -> https://discord.com/api/oauth2/authorize?client_id=875102698352025600&permissions=8&scope=bot')

#開発者用URL
@bot.command()
async def api(ctx):
    await ctx.send('``Twitter API`` -> https://developer.twitter.com/en/portal/dashboard\n``Discord API`` -> https://discord.com/developers/applications')

#白猫のルーン周回数計算
@bot.command()
async def gather(ctx, once:int, now:int, total:int):
    #once:1回あたりのルーン数 now:現在のルーン数 total:必要なルーン数
    remain: int = total - now
    laps: int = remain / once
    extra: int = remain % once
    await ctx.send(f"***【白猫】ルーンの必要数と周回数を計算***\n>>> **1回あたり手に入るルーン数 : ``{once}個``\n現在あるルーン数 : ``{now}個``\n必要なルーン数 : ``{total}個``\n残りのルーン数 : ``{remain}個``\n残り周回数 : ``{math.ceil(laps)}周``\n余るルーン数 : ``{math.ceil(extra)}個``**")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
