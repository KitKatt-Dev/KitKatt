import discord
from discord import user
from discord.ext import commands
import discord.ui
import asyncio
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="/",
                   intents=discord.Intents.all(),
                   case_insensitive=True)


#Greets New User  Message
@bot.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
      f'Hi {member.name}, welcome to Astros Amazing Ventures!')


# in output says "Ready"
@bot.event
async def on_ready():
  print("Ready")


# commands


@bot.command()
async def ping(ctx):
  await ctx.reply("Pong")
  await ctx.message.delete()


@bot.command()
async def say(ctx, *, message):
  embed = discord.Embed(title="",
                        description=message,
                        color=discord.Color.green())
  embed.set_footer(text=f"Sent by: {ctx.author.name}")
  await ctx.message.delete()
  await ctx.send(embed=embed)


@bot.command()
async def purge(ctx, amt):
  await ctx.channel.purge(limit=int(amt) + 1)
  msg = await ctx.send(f"Purged {amt} messages. Used by @{ctx.author.name}")
  await asyncio.sleep(1)
  await msg.delete()


@bot.command()
async def source(ctx):
  await ctx.reply(
      "# KitKatt Source Code ## \n https://github.com/KitKatt-Dev/KitKatt")
  await ctx.message.delete()


@bot.command()
async def commands(ctx, ):
  await ctx.reply(
      "# KitKatt Commands ## \n /say - You can maake it say what you want, but beware staff can see who did it.  \n /purge - (Staff Only) Deletes messages up to 2 weeks prior to use.  \n /source - Gives the link to the source code. \n /ping - KitKatt says Pong! "
  )
  await ctx.message.delete()


keep_alive()
bot.run(
  'YOUR TOKEN HERE')
