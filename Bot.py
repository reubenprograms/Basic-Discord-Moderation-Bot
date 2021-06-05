import discord
from discord.ext import commands

bot = discord.Bot(command_prefix=".") #defining the bots prefix, in which case it is "."
admins = [1, 2, 3, 4, 5] #defining the admins id's on the bot, except i'm not going to be using this so i set it to "1 2 3 4 5"

@bot.event #an event
def on_ready(): #on_ready is an event for when the bot is ready to be used
  print("The bot is online and ready to be used") #when the bot is ready it will print the text

@bot.command() #a command
async def ban(ctx, member : int = None, reason : str = None): #ban is going to be a command on the bot, it is defining the member as an integer because it's going to be used as a discord id to ban, the reason is a string as it is a string of characters
  if ctx.author.id not in admins: #if the user's id is not in the variable admins which i defined earlier
    await ctx.send("You need to be an admin to run this command") #then send this

  else: #if the user is in the admins
    if member is None: #if the author didn't enter a member to ban
      await ctx.send("Please enter the id of the member you would like to ban") #then send this

    elif reason is None: #if the author didn't enter a reason for the ban
      await ctx.send("Please enter a reason for the ban") #then send this

    else: #if none of those are true
      await ctx.guild.ban(member, reason=reason) #banning the memmber
      await ctx.send("User was banned.") #once the member is banned send this

@bot.command() #a command
async def kick(ctx, member : int = None, reason : str = None): #kick is going to be a command on the bot, it is defining the member as an integer because it's going to be used as a discord id to kick, the reason is a string as it is a string of characters
  if ctx.author.id not in admins: #if the user's id is not in the variable admins which i defined earlier
    await ctx.send("You need to be an admin to run this command") #then send this

  else: #if the user is in the admins
    if member is None: #if the author didn't enter a member to kick
      await ctx.send("Please enter the id of the member you would like to kick") #then send this

    elif reason is None: #if the author didn't enter a reason for the kick
      await ctx.send("Please enter a reason for the kick") #then send this

    else: #if none of those are true
      await ctx.guild.kick(member, reason=reason) #kicking the memmber
      await ctx.send("User was kicked.") #once the member is kicked send this

bot.run('tokenhere') #running your bots token
