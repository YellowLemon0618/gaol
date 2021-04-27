import asyncio
import discord
import discord.utils
import random
import time
import math
import datetime
import string
from skingrabber import skingrabber
sg = skingrabber()

from discord import Member
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix=';;;', intents=intents)
client.remove_command("help")
now = datetime.datetime.now()

token = "Nzk3MzM5MjM5NDg5NzMyNjQ4.X_lCCA.GHshSJ7F7UzH_U7AJdfXqcm5Uz8"

dob_money = 0

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    async def presense_change_def(games):
        await client.wait_until_ready()
        while not client.is_closed():
            for g in games:
                await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
                await asyncio.sleep(10)
    await presense_change_def(["Partnered with ByteBrew", "https://bytebrew.io/?disccid=hkdev#Pre_Register_Section"])
    dob_money = 1000
    #"\';;;����\'�� �Է��غ�����", "�׽�Ʈ���� ������", "Powered by Lemon", 

def isjoined(au, message):
    aid = '{0.author.id}'.format(message)
    m = open("C:/Users/Kyu Wan KIM/Desktop/Visual Studio/projects/Python/HK Money System/money.txt", "r")
    li = 0
    idn = 0
    line = ""
    while True:
        line = m.readline()
        if not line: break
        else:
            li = li + 1
            line = line.split(':')
            if line[0] == aid: break
            else: idn = idn + 1
    m.close()
    if idn == li:
        return False
    else:
        return str(line[1])

def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

@client.command()
async def help(ctx):
    color = random.randint(0, 0xfffffe)
    hem=discord.Embed(title="������ �ʿ� �ϽŰ���?", description="", color=color)
    hem.set_footer(icon_url = ctx.author.avatar_url, text = "{}".format(ctx.author) + " ? " + str(now.month) + "�� " + str(now.day) + "�� | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    await ctx.send(embed=hem)

@client.command()
async def ����(ctx):
    await help(ctx)

@client.command()
async def ping(ctx):
    color = random.randint(0, 0xfffffe)
    embed=discord.Embed(title="pong!", description=f'{round(round(client.latency, 4)*1000)}ms', color=color)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = "{}".format(ctx.author) + " ? " + str(now.month) + "�� " + str(now.day) + "�� | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759299677274505219/828843117502267412/ping-pong.jpg")
    await ctx.send(embed=embed)

@client.command()
async def ��(ctx):
    await ping(ctx)

@client.command()
async def join(ctx):
    join = isjoined('{message.author}', ctx)
    if join is False:
        await ctx.send("���Խ� ���� ������ �����Ͻô°ɷ� ���ֵ˴ϴ�. \n�����ϽŴٸ� 15�� ���� '����' ��� �Է��� �ּ���.")
        def check(m):
            return m.author == ctx.author and m.content=="����"

        msg = await client.wait_for(event='message', timeout=15.0, check=check)
 
        if msg is None:
            await ctx.send("���Կ� �����߽��ϴ�. \n �ٽýõ� : \';;;����\'")
            return
        else:
            await ctx.send("���Կ� �����߽��ϴ�.")
            f = open("C:/Users/Kyu Wan KIM/Desktop/Visual Studio/projects/Python/HK Money System/money.txt", "a")
            f.write('{0.author.id}'.format(ctx) + ":100\n")
            f.close()
    else:
        await ctx.send("�̹� ���ԵǾ� �ֽ��ϴ�!")

@client.command()
async def ����(ctx):
    await join(ctx)

@client.command()
async def money(ctx):
    color = random.randint(0, 0xfffffe)
    join = isjoined('{ctx.author}', ctx)
    if join is False:
        await ctx.send("���� \';;;����\'�� �Է��� �ּ���!")
    else:
        await ctx.send(embed=discord.Embed(title=":moneybag: �� :moneybag:" ,description=f"\n ���� {ctx.author.name}���� �ܰ�� " + join + "���Դϴ�!", color=color))

@client.command()
async def ��(ctx):
    await money(ctx)

@client.command()
async def send(ctx, arg1=None):
    try:
        join = isjoined('{message.author}', ctx)
        if join is False:
            await ctx.send("���� \';;;����\'�� �Է��� �ּ���!")
        else:
            m = int(join)
            if arg1 == None:
                await ctx.send(embed=discord.Embed(title="�󸶳� �Ͻǰǰ���??", description="\n\t\';;;����\' �� �Է��� ������!", color=0xFF0000))
            else:
                if arg1.isdigit():
                    rm = int(join)
                    pm = int(arg1)
                    chpm = rm - 100
                    if pm <= chpm:
                        if pm == 0:
                            await ctx.send(embed=discord.Embed(title="�ƴ� 0�� ���ϴ°� �� �ҿ��� �־��;;", description="\n\t0 �̻��� ���� �Է��� �ּ���!", color=0xFF0000))
                        else:
                            await ctx.send("~~ACCESS SUCCESSED~~ \n\nrm : " + str(rm) + "\tpm : " + str(pm) + "\tchpm : " + str(chpm))
                    else:
                        await ctx.send(embed=discord.Embed(title="�۱��� �ݾ��� �ʹ� Ŀ��!", description="\n\t\';;;����\' �� �Է��� ������!", color=0xFF0000))
                else:
                    await ctx.send(embed=discord.Embed(title="�۱��� �ݾ��� ���ڿ��� �ؿ�!", color=0xFF0000))
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning: " + error)

@client.command()
async def �۱�(ctx, arg1=None):
    await send(ctx, arg1)

@client.command()
async def ����(ctx, arg1=None):
    try:
        join = isjoined('{ctx.author}', ctx)
        if join is False:
            await ctx.send("���� \';;;����\'�� �Է��� �ּ���!")
        else:
            global dob_money
            if arg1 == None:
                await ctx.send("\';;;���� ����\' �� �Է��� ������!")
            elif arg1 == "help" or arg1 == "����":
                await ctx.send(embed=discord.Embed(title="\';;;����\' ����", description="\n ;;;���� <�׼�>", color=0xFFFFFE))
            elif arg1.isdigit():
                await ctx.send("isDigit")
            else:
                await ctx.send(embed=discord.Embed(title="��? ���󱸿�?", color=0xFF0000))
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning: " + error)

@client.command(name="random")
async def _random(ctx, arg1=None):
    try:
        if arg1 == None:
            await ctx.send("1���� ����� �Ͻǰ��� �����ּ���!")
        elif arg1.isdigit(): #true
            if int(arg1) <= 1:
                await ctx.send("���ڴ� 1�̰ų� 1���� ������ �����!")
            else:
                r = random.randint(1, int(arg1))
                await ctx.send("�ֻ��� �����.... \n\n" + str(r) + "!!")
        else:
            await ctx.send("���� ���ڿ��̳� �Ǽ� ���� �ƴ� �ڿ����̿��� �ؿ�!")
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning: " + error)

@client.command()
async def dice(ctx, arg1=None):
    await _random(ctx, arg1)

@client.command()
async def ����(ctx, arg1=None):
    await _random(ctx, arg1)

@client.command()
async def �ֻ���(ctx, arg1=None):
    await _random(ctx, arg1)
    
@client.command()
async def calculate(ctx, arg1=None, arg2=None, arg3=None, arg4=None):
    try:
        if arg1 == None or arg2 == None or arg3 == None:
            if arg2 == '!' or arg2.lower() == 'f':
                if arg1.isdigit(): # true
                    color = random.randint(0, 0xfffffe)
                    await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + str(arg1) + str(arg2) + "\n��� ��� : " + str(math.factorial(int(arg1))), color=color))
                else:
                    await ctx.send("���丮��(factorial)���� ���ڿ�, �Ǽ�, ���� ���� ���� �����!")
            else:
                await ctx.send("������ �Է��� �ּ���!")
        elif is_digit(arg1): # true
            if is_digit(arg3): # true
                color = random.randint(0, 0xfffffe)
                n1 = arg1
                n2 = arg3
                if n1.isdigit():
                    n1 = int(arg1)
                else:
                    n1 = float(arg1)
                if n2.isdigit():
                    n2 = int(arg3)
                else:
                    n2 = float(arg3)
                r = 3
                if arg4 is not None:
                    if arg4.isdigit():
                        r = int(arg4)
                    else:
                        await ctx.send("�Ҽ��� �ڸ����� ���ڿ�, �Ǽ� ���� �� �����!")
                else:
                    r = 3
                if arg2 == '+':
                    result = round((n1 + n2), r)
                    await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + arg2 + " " + arg3 + "\n��� ��� : " + str(result), color=color))
                elif arg2 == '-':
                    result = round((n1 - n2), r)
                    await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + arg2 + " " + arg3 + "\n��� ��� : " + str(result), color=color))
                elif arg2 == '*' or arg2 == 'x' or arg2 == 'X':
                    result = round((n1 * n2), r)
                    await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + "X" + " " + arg3 + "\n��� ��� : " + str(result), color=color))
                elif arg2 == '/':
                    if arg1 == '0' or arg3 == '0':
                        await ctx.send("0�� 0���� 0���� ������ ����0~~ �˰ھ�0?")
                    else:
                        result = round((n1 / n2), r)
                        await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + arg2 + " " + arg3 + "\n��� ��� : " + str(result), color=color))
                elif arg2 == '^':
                    if str(type(n1)) == "<class 'int'>" and str(type(n2)) == "<class 'int'>":
                        if n1 != 0 and n2 != 0:
                            result = round(pow(n1, n2), r)
                            await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + arg2 + " " + arg3 + "\n��� ��� : " + str(result), color=color))
                        else:
                            await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + arg2 + " " + arg3 + "\n��� ��� : 1", color=color))
                    else:
                        await ctx.send("�������� �Ҽ��� ���� �� �� �����!")
                elif arg2.lower() == 't' or arg2.lower() == 'tetr':
                    if str(type(n1)) == "<class 'int'>" and str(type(n2)) == "<class 'int'>":
                        if n1 != 0 and n2 != 0:
                            m = n2
                            temp = 0
                            for i in range(0, n1):
                                temp = m ** n2
                                m = temp
                            await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + "TETR" + " " + arg3 + "\n��� ��� : " + str(temp), color=color))
                        else:
                            await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + " " + "TETR" + " " + arg3 + "\n��� ��� : 1", color=color))
                    else:
                        await ctx.send("��Ʈ���̼�(tetration)���� �Ҽ��� ���� �� �� �����!")
                elif arg2 == '!' or arg2.lower() == 'f':
                    if arg1.isdigit(): # true
                        color = random.randint(0, 0xfffffe)
                        await ctx.send(embed=discord.Embed(title="��� ���", description="��� �� : " + arg1 + arg2 + "\n��� ��� : " + str(math.factorial(int(arg1))), color=color))
                    else:
                        await ctx.send("���丮��(factorial)���� ���ڿ�, �Ǽ�, ���� ���� ���� �����!")  
            else:
                await ctx.send("���� ���ڿ��̳� �Ǽ� ���� �ƴ� �ڿ����̿��� �ؿ�!")       
        else:
            await ctx.send("���� ���ڿ��̳� �Ǽ� ���� �ƴ� �ڿ����̿��� �ؿ�!")
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning: " + error)

@client.command()
async def cal(ctx, arg1=None, arg2=None, arg3=None, arg4=None):
    await calculate(ctx, arg1, arg2, arg3, arg4)

@client.command()
async def ���(ctx, arg1=None, arg2=None, arg3=None, arg4=None):
    await calculate(ctx, arg1, arg2, arg3, arg4)

@client.command()
async def clean(ctx, arg1=None):
    try:
        id = '{0.author.id}'.format(ctx)
        if id == "656059360882982912" or id == "743429399956947067" or id == "822445708467503114" or id == "756828069649580074":
            if arg1 == None:
                await ctx.send("�󸶳� û�������� �˷��ּ���!")
            else:
                if arg1.isdigit():
                    if arg1 != '0':
                        try:
                            limit = int(arg1) + 1
                            await ctx.message.channel.purge(limit=limit)
                            await ctx.send(embed=discord.Embed(title="û�� �Ϸ�", description=f'{ctx.author.mention}' + " �Կ� ���� " + arg1 + "��ŭ�� �޼����� �����Ǿ����ϴ�!", color=0xFFFFFE))
                        except:
                            await ctx.send("���� ���� ������ �����ϴ�!")
                    else:
                        await ctx.send("0���� �޼����� �����Ҽ� �����")
                else:
                    await ctx.send("���� ������ ���ڿ��� �ؿ�(No �Ҽ���, No ���̳ʽ�... ��)")
        else:
            await ctx.send("������ �����ϴ�!\n@����#1491 ���� dm���� �����ϼ���!")
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning: " + error)

@client.command()
async def delete(ctx, arg1=None):
    await clean(ctx, arg1)

@client.command()
async def û��(ctx, arg1=None):
    await clean(ctx, arg1)

@client.command()
async def ����(ctx, arg1=None):
    await clean(ctx, arg1)

@client.command()
async def search(ctx, searchtype=None, *, searchargs=None):
    try:
        if searchtype == None or searchargs == None:
            await ctx.send("������, ��𿡼� �˻����� �Է��� �ּ���")
        else:
            search = searchargs.split()
            searchmessage = ""
            for i in range(0, len(search)):
                searchmessage = searchmessage + search[i]
                searchmessage = searchmessage + "+"
            searchmessage = searchmessage[:-1]
            if searchtype == "naver":
                await ctx.send("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + searchmessage)
            elif searchtype == "���̹�":
                await ctx.send("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + searchmessage)
            elif searchtype == "daum":
                await ctx.send("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=" + searchmessage)
            elif searchtype == "����":
                await ctx.send("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=" + searchmessage)
            elif searchtype == "zum":
                await ctx.send("https://search.zum.com/search.zum?method=uni&option=accu&rd=1&qm=f_typing.top&query=" + searchmessage)
            elif searchtype == "google":
                await ctx.send("https://www.google.com/search?q=" + searchmessage)
            elif searchtype == "����":
                await ctx.send("https://www.google.com/search?q=" + searchmessage)
            else:
                await ctx.send("�׷�... ����Ʈ�� ���µ���?")
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning:" + error)
    return None

@client.command()
async def profile(ctx, user: discord.Member = None):
    try:
        if user == None:
            user = ctx.author
        
        pf = discord.Embed(title=f'{user.name}' + "`s information", description="This message is about information of " + f'{user.mention}' + ".\n\n\n")
        pf.set_thumbnail(url=f'{user.avatar_url}')
        pf.add_field(name="User Name", value=f'{user.name}', inline=True)
        pf.add_field(name="Tag (Discriminator)", value="#" + f'{user.discriminator}', inline=True)
        pf.add_field(name="ID", value=f'{user.id}', inline=True)
        if str(user.status) == "online":
            pf.add_field(name="Status", value="<:online:832592999312916500>\nOnline", inline=False)
        elif str(user.status) == "idle":
            pf.add_field(name="Status", value="<:idle:832602456474517542>\nIdle", inline=False)
        elif str(user.status) == "dnd":
            pf.add_field(name="Status", value="<:dnd:832593085333635112>\nDo Not Disturb", inline=False)
        elif str(user.status) == "offline":
            pf.add_field(name="Status", value="<:offline:832593131760648223>\nOffline", inline=False)
        elif str(user.status) == "streaming":
            pf.add_field(name="Status", value="<:streaming:832593671253786654>\nStreaming Now!", inline=False)

        if user.activities == ():
            pf.add_field(name="Game playing", value="N/A", inline=False)
            pf.add_field(name="Custom Status", value="N/A", inline=False)
        elif len(user.activities) == 2:
            pf.add_field(name="Game playing", value=f'{user.activities[1].name}'+" �ϴ���", inline=False)
            pf.add_field(name="Custom Status", value=f'{user.activity}', inline=False)
        elif len(user.activities) == 1:
            if str(user.activities[0].type) == "ActivityType.playing":
                pf.add_field(name="Game playing", value=f'{user.activities[0].name}'+" �ϴ���", inline=False)
                pf.add_field(name="Custom Status", value="N/A", inline=False)
            elif str(user.activities[0].type) == "ActivityType.custom":
                pf.add_field(name="Game playing", value="N/A", inline=False)
                pf.add_field(name="Custom Status", value=f'{user.activity}', inline=False)

        cre = str(user.created_at)
        cre_split = cre.split('.')
        cre = cre_split[0]
        pf.add_field(name="Created At", value=str(cre), inline=True)
        joi = str(user.joined_at)
        joi_split = joi.split('.')
        joi = joi_split[0]
        pf.add_field(name="Joined At", value=str(joi), inline=True)

        pf.add_field(name="Bot", value=str(user.bot), inline=False)
        pf.set_footer(icon_url = f'{ctx.author.avatar_url}', text = f'{ctx.author}' + " ? " + str(now.month) + "�� " + str(now.day) + "�� " + str(now.hour) + "�� " + str(now.minute) + "��")
        color = random.randint(0, 0xfffffe)
        pf.color = color

        await ctx.send(embed=pf)
        return None
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning:" + str(error))
        return None

@client.command()
async def pf(ctx, user: discord.Member = None):
    await profile(ctx, user)

@client.command()
async def ������(ctx, user: discord.Member = None):
    await profile(ctx, user)

@client.command()
async def serverinfo(ctx):
    try:
        guild = ctx.guild
        info = discord.Embed(title="Guild " + guild.name + "'s information", description="This message is about information of guild " + f'{guild.name}' + ".\n\n\n")

        info.set_thumbnail(url=guild.icon_url)
        info.add_field(name="Name", value=guild.name, inline=False)
        info.add_field(name="Description", value=guild.description, inline=False)
        info.add_field(name="Id", value=guild.id, inline=False)
        info.add_field(name="verification_level", value=guild.verification_level, inline=False)
        info.add_field(name="Owner", value=guild.owner.mention, inline=True)
        info.add_field(name="Member Count", value=guild.member_count, inline=True)
    
        cre = str(guild.created_at)
        cre_split = cre.split('.')
        cre = cre_split[0]
        info.add_field(name="Created At", value=cre, inline=True)
        info.add_field(name="Region", value=guild.region, inline=True)
        info.add_field(name="Role Count", value=str(len(ctx.guild.roles)), inline=True)

        statuses = [
            len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),
        ]
        info.add_field(name="Statuses", value="<:online:832592999312916500> " + str(statuses[0]) + "\n" + "<:idle:832602456474517542> " + str(statuses[1]) + "\n" + "<:dnd:832593085333635112> " + str(statuses[2]) + "\n" + "<:offline:832593131760648223> " + str(statuses[3]), inline=False)

        info.set_footer(icon_url = f'{ctx.author.avatar_url}', text = f'{ctx.author}' + " ? " + str(now.month) + "�� " + str(now.day) + "�� " + str(now.hour) + "�� " + str(now.minute) + "��")
        info.color = random.randint(0, 0xfffffe)
        await ctx.send(embed=info)
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning:" + str(error))

@client.command()
async def server(ctx):
    await serverinfo(ctx)

@client.command()
async def ��������(ctx):
    await serverinfo(ctx)

@client.command()
async def ����(ctx):
    await serverinfo(ctx)

@client.command()
async def skin(ctx, user=None):
    try:
        if user is None:
            await ctx.send("��? ������?")
        else:
            response = sg.get_uuid(user=user)
            if response is None:
                await ctx.send("�׷� ������ ���µ�....\n:thinking:")
                return None
            color = random.randint(0, 0xfffffe)
            embed = discord.Embed(title=user + "`s Minecraft Skin", color=color)
            embed.add_field(name="uuid", value=response)
            embed.set_image(url="https://visage.surgeplay.com/full/304/" + response)
            await ctx.send(embed=embed)
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning:" + error)

@client.command()
async def ��Ų(ctx, user=None):
    await skin(ctx, user)

@client.command()
async def mute(ctx, arg1=None):
    try:
        guild = ctx.guild
        await ctx.send(guild)
        member = guild.get_member(client.get_user(int(arg1)).id)

        try:
            if ctx.guild.id == 753864878338342943:
                await member.add_roles(ctx.guild.get_role(828102999062609991), atomic=True)
            elif ctx.guild.id == 684020305286397964:
                await member.add_roles(ctx.guild.get_role(811236838496927794), atomic=True)
            elif ctx.guild.id == 759299677274505216:
                await member.add_roles(ctx.guild.get_role(828218592424230952), atomic=True)
        except:
            await ctx.send("������ �߰��� ������ �����ϴ�!\n�����ڿ��� ������ ���� ����(Permission)�� ������ �ּ���!")
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning:" + str(error))
    return None

@client.command()
async def base(ctx, b=None, n=None):
    try:
        if b.isdigit():
            if n.isdigit():
                if int(b) <= 1:
                    await ctx.send("0, 1������ ����� ;;")
                    return None
                embed=discord.Embed(title=str(n) + " -> " + str(b) + "���� ��ȯ ���", description="```" + convert(int(n), int(b)) + "```")
                embed.set_footer(icon_url = f'{ctx.author.avatar_url}', text = f'{ctx.author}' + " ? " + str(now.month) + "�� " + str(now.day) + "�� " + str(now.hour) + "�� " + str(now.minute) + "��")
                embed.color = random.randint(0, 0xfffffe)
                await ctx.send(embed=embed)
            else:
                await ctx.send("��ȯ�� ��, ��ȯ�� ������ ��� ���ڿ��� �ؿ�!")
        else:
            await ctx.send("��ȯ�� ��, ��ȯ�� ������ ��� ���ڿ��� �ؿ�!")
    except Exception as error:
        await ctx.send(":warning: ����! ������!")
        await ctx.send(":warning:" + str(error))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.channel.send("�׷� ������ �����!")

    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send("�׷� ��ɾ�� �����ϴ�!")
        await ctx.channel.send("**';;;����'** �� �Է��� ������!")

client.run(token)