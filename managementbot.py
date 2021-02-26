import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '/')

status = ['BETA TESTER| /help']

f = open('rules.txt','r', encoding='utf-')
rules = f.readlines()

@client.event
async def on_ready():
	print("Bot is ready")

@client.command()
async def rule(ctx,*,number):
	await ctx.send(rules[int(number)-1])

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= 'Too much talk like a pro!'):
    await member.send("You have been kick from ASTA THF Server!, Because:"+reason)
    await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= 'Too much talk like a PRO!'):
    await member.send(member.name + "have been banned from ASTA THF Server!, Because:"+reason)
    await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('/')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name +'has been unbanned!')
            return
    
    await ctx.send(member+' was not found')

@client.command(aliases=['rules','test'])
async def hello(ctx):
	await ctx.send('Whatsup Dude!')

client.run('YOUR TOKEN')
