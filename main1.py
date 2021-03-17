import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game('서버 상태 관찰')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("봇이 온라인으로 변경되었습니다")

@client.event
async def on_message(message):
    if message.content.startswith("!on"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.purge(limit=int(1))
                await message.channel.send("@everyone")
                embed = discord.Embed(title="[ New World Server ON ]", description="🌍 New World 서버가 열였습니다. 어서 접속해 보세요!", color=0x62c1cc)
                embed.add_field(name="[ Direct Address ]", value="준비중", inline=False)
                embed.add_field(name="[ New World RP Server ]", value="🌐 24시간 ON 상태 입니다. 항상 열심히 노력하는 New World Server 가 되도록하겠습니다.", inline=False)
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
                await message.delete()
        except:
            pass

    if message.content.startswith("!r"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.purge(limit=int(1))
                await message.channel.send("@everyone")
                embed = discord.Embed(title="[ New World Server REBOOT ]", description="🚧 New World 서버가 현재 리붓중입니다", color=0xFFE400)
                embed.add_field(name="[ Direct Address ]", value="준비중", inline=False)
                embed.add_field(name="[ New World RP Server ]", value="🌐 24시간 ON 상태 입니다. 항상 열심히 노력하는 New World Server 가 되도록하겠습니다.", inline=False)
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
                await message.delete()
        except:
            pass
    if message.content.startswith("!off"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.purge(limit=int(1))
                await message.channel.send("@everyone")
                embed = discord.Embed(title="[ New World Server OFF ]", description="🛑 현재 서버 문제 및 패치로 서버가 닫혔습니다. 오픈되면 들어와주세요", color=0xff0000)
                embed.add_field(name="[ Direct Address ]", value="준비중", inline=False)
                embed.add_field(name="[ New World RP Server ]", value="🌐 24시간 ON 상태 입니다. 항상 열심히 노력하는 New World Server 가 되도록하겠습니다.", inline=False)
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
                await message.delete()
        except:
            pass

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
