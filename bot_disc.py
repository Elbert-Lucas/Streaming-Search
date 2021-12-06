import discord
from streaming import stream_search

"""
Esta classe é um adicional,
serve para criar um bot no discord usando a automação de procura de streaming

!IMPORTANTE! para desfrutar do seu bot, você deve primeiramente cria-lo no site 'developer portal' do discord,
             Nomeie-o como  'bot-stream', ou mude a linha 28 deste arquivo para o nome que você preferiu
"""
#Criando o client e preparando ele:
client = discord.Client()

@client.event
async def on_ready():
    print('Bot Online')

#Verificando as mensagens:
@client.event
async def on_message(message):
    # Inicializando os dados da mensagem
    content = message.content.lower()
    channel = message.channel
    author = message.author

    # 1 caso: se o autor for o bot: nao responda
    # 2 caso: se a mensagem iniciar com '-s': exclua este prefixo e repasse a mensagem para a função stream_search
    if author == 'bot-stream':
        return
    if content[:2] == '-s':
        print(content)
        movie_search = content[2:]
        answer = stream_search(movie_search)
        await channel.send(answer)

#Nesta linha você deve adicionar a key do seu bot
client.run("")