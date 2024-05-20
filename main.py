import tweepy
import random
import requests
import os

#definição das chaves
api_key = os.environ['TWITTER_API_KEY']
api_secret = os.environ['TWITTER_API_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

def get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret) -> tweepy.API:
    """Get twitter conn 1.1"""

    auth = tweepy.OAuth1UserHandler(api_key, api_secret)
    auth.set_access_token(
        access_token,
        access_token_secret,
    )
    return tweepy.API(auth)

def get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret) -> tweepy.Client:
    """Get twitter conn 2.0"""

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client

client_v1 = get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret)
client_v2 = get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret)

# Diretório onde suas imagens estão localizadas
diretorio_imagens = 'imagensvava'

# Lista de arquivos de imagem no diretório
arquivos_imagem = os.listdir(diretorio_imagens)

# Escolhendo uma imagem aleatória
imagem_escolhida = random.choice(arquivos_imagem)

# Caminho completo para a imagem escolhida
caminho_imagem = os.path.join(diretorio_imagens, imagem_escolhida)

print(caminho_imagem)
# Usando a api para pegar a imagem
imagem = client_v1.media_upload(filename=caminho_imagem)

# Pegando o id da imagem
imagem_id = imagem.media_id

client_v2.create_tweet(text="Olha bispo que legal @rflb29", media_ids=[imagem_id])
