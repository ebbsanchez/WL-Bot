

import discord
from discord.ext import commands
from discord.utils import get
# Replace 'YOUR_TOKEN_HERE' with your Discord bot token
TOKEN = ""


intents = discord.Intents.all()
intents.members = True
intents.messages = True # Enable the Privileged Message Content Intent

client = commands.Bot(command_prefix='!', intents=intents)




@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	for guild in client.guilds:
		print(f'{len(guild.members)} Users in {guild.name}:')
		# for member in guild.members:
			# print(f'{member.name}#{member.discriminator} (ID: {member.id})')

@client.command()
async def add_wl_standard(ctx):
    print('add_wl_standard command triggered')
    ids = [ # there are ids that need to add WL-Standard
	    '321075064110055425',
	    '983854086883532900',
	    '297825533914382337',
	]

    guild_id = 936963303492706314 # ID of the guild/server where you want to add the role
    guild = client.get_guild(guild_id)
    if guild:
        role_name = 'WL-Standard' # the name of the role you want to add
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            for id in ids:
                member = guild.get_member(int(id))
                if member:
                    await member.add_roles(role)
                    print(f'Added role {role.name} to user {member.name} in server {guild.name}')
                else:
                    print(f'User {id} is not a member of the server')
        else:
            print(f'Role {role_name} not found in server {guild.name}')
    else:
        print(f'Guild {guild_id} not found')

client.run(TOKEN)
