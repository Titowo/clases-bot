import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', description='Bot para links de zoom')

@bot.command()
async def horario(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/785349529385566211/815749011981336606/WhatsApp_Image_2021-02-25_at_20.54.37.jpeg')

@bot.command()
async def ping(ctx):
   await ctx.send('pong')

@bot.command()
async def diseño(ctx):
   await ctx.send('Link para clases de Diseño y Arquitectura: https://zoom.us/j/92354583934?pwd=b0NpZ2Zka2FPeDVTREVJNU56Y01mQT09')

@bot.command()
async def consejo(ctx):
   await ctx.send('Link para clases de Consejo de Curso: https://zoom.us/j/95607745483?pwd=dDFLYjRLelRxTGZXL1FNcFUzQlFRdz09 ')

@bot.command()
async def cienciasciudadania(ctx):
   await ctx.send('Link para clases de Ciencias para la Ciudadanía: https://zoom.us/j/98594957802?pwd=YUxjUEEyTzI4NmlvQUZ6ZGVYN25iQT09')

@bot.command()
async def quimica(ctx):
   await ctx.send('Link para clases de Quimica: https://zoom.us/j/97696436575?pwd=M05DSEtHclpRclhuWER0Y1FDNWNaZz09')

@bot.command()
async def fisica(ctx):
   await ctx.send('Link para clases de Fisica: https://zoom.us/j/91911040013?pwd=YWVMT0tyVlo2WkQ3OGZYS3FrVitUdz09')

@bot.command()
async def edciudadana(ctx):
   await ctx.send('Link para clases de Educacion Ciudadana: https://zoom.us/j/92842701052?pwd=eHhiYzRSNUhaRUJJMzh3VDZRc2l5Zz09')

@bot.command()
async def orientacion(ctx):
   await ctx.send('Link para clases de Orientacion: https://zoom.us/j/99259769490?pwd=ZGtYTkpaWHFlR2NrRzNMTDJPYUVlUT09')

@bot.command()
async def edfisica(ctx):
   await ctx.send('Link para clases de Educacion Fisica: https://zoom.us/j/96916847715?pwd=NS9Dc3ZlQ3dKZTBFOEhkeUc2TTB6UT09')

@bot.command()
async def filosofia(ctx):
   await ctx.send('Link para clases de Filosofia: https://zoom.us/j/97606050534?pwd=OTBRSGFLbnExaWpBUmluUXVQWlFsZz09 ')

@bot.command()
async def lenguaje(ctx):
   await ctx.send('Link para clases de Lenguaje: https://zoom.us/j/92822213801?pwd=TUdxUXJlZ2FieXkrTVhaVXJHNlg4QT09')

@bot.command()
async def argumentacion(ctx):
   await ctx.send('Link para clases de Argumentacion en Democracia: https://zoom.us/j/93396283165?pwd=ZzZ2dXVYN2F1OG5jYVhwRGRoQUxJUT09')

@bot.command()
async def clases(ctx):
   await ctx.send('Usa este nombre para el comando de clases: diseño, argumentacion, lenguaje, filosofia, edfisica, orientacion, edciudadana, fisica, quimica, cienciasciudadania, consejo.  ')


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Ramsta', url='https://www.twitch.tv/ramstaaa'))
    print('My bot is Ready')

bot.run('ODEwOTk1ODE0MzUyNDIwOTA1.YCrwtQ.yQ7pTbbL12UV0jkx1jvpN-3NsgU')
