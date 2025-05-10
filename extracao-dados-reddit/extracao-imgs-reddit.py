# Salvando imagens.

import requests
import os
import uuid
import sys


with open('senha reddit.txt', 'r') as f:
    minha_senha = f.read()

with open('reddit client id.txt', 'r') as g:
    client_key = g.read()

with open('reddit client secret.txt', 'r') as h:
    client_secret = h.read()


auth = requests.auth.HTTPBasicAuth(client_key, client_secret)

data = {'grant_type':'password','username':'RevolutionaryLab7729','password':minha_senha}

headers = {'User-Agent':'windows:script for automation:v0.1 (by u/RevolutionaryLab7729'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

if res.status_code == 200:
    token = res.json()['access_token']
    headers['Authorization'] = f"bearer {token}"
else:
    print("Error ", res.status_code)
    exit()

# --------------------------------------------------------------------

# Método de reconhecer postagens com imagens.

teste = requests.get('https://oauth.reddit.com/r/brasil/hot', headers = headers, params = {'limit': '10'})

for post in teste.json()['data']['children']:

    if 'post_hint' in post['data']:
        if post['data']['post_hint'] == 'image':
            print(f'A postagem {post['data']['title']} é uma foto')

'''
Alternativamente, se uma postagem for uma imagem/vídeo/notícia com imagem,
o arquivo terá um atributo preview. Com as imagens, contudo, o atributo enabled será true.
'''

for post in teste.json()['data']['children']:

    if 'preview' in post['data']:
        if post['data']['preview']['enabled'] == 'true':
            print(f'A postagem {post['data']['title']} é uma foto')  

# ----------------------------------------------------------------------------------------------

post_image = requests.get('https://oauth.reddit.com/r/pics/hot', headers = headers, params = {'limit': '1'})

url_list =[]
for post in post_image.json()['data']['children']:
    url_list.append(post['data']['url_overridden_by_dest'])

for url in url_list:

    req = requests.get(url)
    if not req.ok:
        raise Exception("Erro com URL da imagem.")

    dir_name = "ImagensAPI"
    os.makedirs(dir_name, exist_ok = True)

    file_extension = url.split(".")[-1]
    if file_extension.lower() not in ["png", "jpg", "jpeg", "gif"]:
        print("Extensão não disponível")

    unique_id = uuid.uuid4()
    file_path = f"{dir_name}/{unique_id}.{file_extension}"

    with open(file_path, 'wb') as handler:
        handler.write(req.content)
        print(f'Imagem {url} salva em {file_path}')


# --------------------------------------------------------------------

# Salvando imagens de galerias.

post_image = requests.get('https://oauth.reddit.com/r/rarepuppers/hot', headers = headers, params = {'limit': '5'})


for post in post_image.json()['data']['children']:
    if "is_gallery" in post['data'] and post['data']['is_gallery'] == True:
        print(f"A postagem {post['data']['title']} é uma galeria")

        url_list =[]
            
        if not post['data']['stickied']:
            try:
                extensions = []
                for image_id, value in post['data']['media_metadata'].items():
                    extensions.append(value["m"].split("/")[-1])
            
                image_ids = [id for id in post["data"]["media_metadata"]]

                # Adiciona à lista URLs com IDs e extensões seguindo este formato de URL.
                # Ex. 'https://i.redd.it/01vb7df95ree1.jpg'
                for i, extension in enumerate(extensions):
                    url_list.append(f"https://i.redd.it/{image_ids[i]}.{extension}")

            except AttributeError:
                sys.stderr.write("Postagem foi deletada.")

            print(url_list)