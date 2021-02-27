import discord
from discord.ext import commands, tasks

from random import choice

clients = commands.bot(command_prefix="ur command")

status = ["github.com/JustD09"]
queue = []

@client.event
async def on_ready():
    change_status_start()
    print("Bot Is Online")

@client.event
async def on_member_join():
    channel = discord.utils.get(member.guild.channels, name="general")

@client.command(aliases="S")
async def serverstats(ctx):
    embed=discord.Embed(title=f"Stats Server {ctx.guild.name}")
    embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name="Messages sent:", value=messagecounts[ctx.guild.id], inline=False)
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.guild.id not in messagecount.keys():
        messagecounts[message.guild.id] = 0
    messagecounts[message.guild.id] += 1

@client.command(aliases=["M"])
@commands.has_permissions(muted_members = True)
async def muted(ctx,member : discord.Member,*,reason= "Toxic at chat"):
    await member.send("jaga tu mulut ye ngentod!, Because:"+reason)
    await member.muted(reason=reason)

@client.command(aliases=["K"])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "Breaking The Rules and got kick from server"):
    await member.send("Telah di kick dari server karena melanggar rules!")
    await member.kick(reason=reason)

@client.command(aliases=["B"])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason=  "Breaking The Rules and got bans from server"):
    await member.send("Telah di banned dari server karena melanggar rules!"+reason)
    await member.ban(reason=reason)

@client.command(aliases=["G"])
@commands.has_permissions(giverole_members = True)
async def giverole(ctx,member : discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Hey {ctx.author.name}, {user.name} giving the roles! called: {role.name}")

bot.run("YOUR TOKEN")
                