import discord
import random
from discord.ext import commands

# Configurações do bot
TOKEN = 'Token do Bot'
PREFIX = '.'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


async def on_ready():
    print(f'{bot.user} está conectado!')


@bot.command()
async def r(ctx, quant: int = 1, lados: str = 'd10'):
    await ctx.send('Qual a dificuldade do teste?  ')

    def check_dados(message):

        return message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit()

    def rolagem_d10():
        for i in range(quant):
            resultado = random.randint(1, 10)
            resultados.append(resultado)
            if resultado >= number:
                sucessos.append(resultado)
            elif resultado == 1:
                falhas.append(resultado)

    def checar_rolagem_d10():
        existe_sucesso = False
        for numero in resultados:
            if numero >= number:
                existe_sucesso = True
                break
        if existe_sucesso and len(falhas) == 0:
            quantidade_sucessos = len(sucessos)
            return quantidade_sucessos
        elif existe_sucesso and len(falhas) > 0:
            for i in falhas:
                sucessos.remove(max(sucessos))
            if len(sucessos) > 0:
                quantidade_sucessos = len(sucessos)
            else:
                quantidade_sucessos = 0
            return quantidade_sucessos
        elif existe_sucesso is False and len(falhas) == 0:
            quantidade_sucessos = 'falha'
            return quantidade_sucessos
        elif existe_sucesso is False and len(falhas) > 0:
            quantidade_sucessos = 'falha critica'
            return quantidade_sucessos

    def rolagem_d20():
        for i in range(quant):
            resultado = random.randint(1, 20)
            resultados.append(resultado)
            if resultado >= number:
                sucessos.append(resultado)

    def checar_rolagem_d20():
        quantidade_sucessos = len(sucessos)
        return quantidade_sucessos

    try:
        response = await bot.wait_for('message', check=check_dados, timeout=30.0)
        number = int(response.content)
        resultados = []
        sucessos = []
        falhas = []
        if lados == 'd10':
            rolagem_d10()
            resultado_jogada = checar_rolagem_d10()
        elif lados == 'd20':
            rolagem_d20()
            resultado_jogada = checar_rolagem_d20()

        await ctx.send(f'Os resultados de {ctx.author.nick} são: {resultados}')

        if resultado_jogada == 'falha' or resultado_jogada == 0:
            await ctx.send(f'{ctx.author.nick} falhou no teste!')
        elif resultado_jogada == 'falha critica':
            await ctx.send(f'{ctx.author.nick} sofreu uma falha crítica!')
        else:
            await ctx.send(f'{ctx.author.nick} obteve {resultado_jogada} sucesso(s)')

    except TimeoutError:
        await ctx.send("Tempo esgotado. Tente novamente mais tarde.")
    except ValueError:
        await ctx.send("Isso não parece ser um número inteiro válido. Tente novamente.")


@bot.command()
async def d(ctx, quant: int = 1, lados: str = 'd10', modif: int = 0):

    def rolagem_d4():
        for i in range(quant):
            resultado = random.randint(1, 4)
            resultados.append(resultado)

    def rolagem_d6():
        for i in range(quant):
            resultado = random.randint(1, 6)
            resultados.append(resultado)

    def rolagem_d8():
        for i in range(quant):
            resultado = random.randint(1, 8)
            resultados.append(resultado)

    def rolagem_d12():
        for i in range(quant):
            resultado = random.randint(1, 12)
            resultados.append(resultado)

    def rolagem_dano():
        soma = 0
        for numero in resultados:
            soma += numero
        return soma + modif

    try:
        resultados = []

        if lados == 'd4':
            rolagem_d4()
            quantidade_dano = rolagem_dano()
        elif lados == 'd6':
            rolagem_d6()
            quantidade_dano = rolagem_dano()
        elif lados == 'd8':
            rolagem_d8()
            quantidade_dano = rolagem_dano()
        elif lados == 'd12':
            rolagem_d12()
            quantidade_dano = rolagem_dano()

        await ctx.send(f'Os resultados de {ctx.author.nick} são: {resultados}')
        await ctx.send(f'{ctx.author.nick} causou {quantidade_dano} de dano!')

    except TimeoutError:
        await ctx.send("Tempo esgotado. Tente novamente mais tarde.")
    except ValueError:
        await ctx.send("Isso não parece ser um número inteiro válido. Tente novamente.")


bot.run(TOKEN)
