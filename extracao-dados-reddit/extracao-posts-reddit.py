import requests

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

# ---------------------------

top_worldnews = requests.get('https://oauth.reddit.com/r/worldnews/hot', headers=headers, params = {'limit':'2'})

post_list = []

for post in top_worldnews.json()['data']['children']:

    if not post['data']['stickied']:
    
        post_list.append({'subreddit': post['data']['subreddit'],
                          'title': post['data']['title'],
                          'selftext': post['data']['selftext'],
                          'ups': post['data']['ups'],
                          'url': post['data']['url'],
                          'kind': post['kind'],
                          'id': post['data']['id']})

# ---------------------------------------

# Salva uma postagem que ancora filtro de antes/depois.
anchor = {'kind':'t3', 'id':'1e5ekeg'}

anchor_kind = anchor.get('kind')
anchor_id = anchor.get('id')
anchor_fullname = anchor_kind + "__" + anchor_id

filtro_worldnews = requests.get('https://oauth.reddit.com/r/worldnews/new', headers = headers, params = {'limit': '2', 'after': anchor_fullname})

post_list_2 = []

for post in filtro_worldnews.json()['data']['children']:

    if not post['data']['stickied']:
    
        post_list_2.append({'subreddit': post['data']['subreddit'],
                          'title': post['data']['title'],
                          'selftext': post['data']['selftext'],
                          'ups': post['data']['ups'],
                          'url': post['data']['url'],
                          'kind': post['kind'],
                          'id': post['data']['id'],
                          'flair': post['data']['link_flair_text']})


# ------------------------------

# Filtrando por categoria (flair).

flairs = 'flair:"Education" OR flair:"Technology"'
limite = '3'
parametros = {'limit':limite, 'q':flairs}

res_com_parametros = requests.get('https://oauth.reddit.com/r/YouShouldKnow/search', headers = headers, params = parametros)


res_com_parametrosURL = requests.get('https://oauth.reddit.com/r/askscience/search?q=flair%3A%27Biology%27+OR+flair%3A%27Engineering%27', headers=headers, params = {'limit':'4'})

# Obs. O encoding ASC-II transforma %3A em : (dois pontos) e %27 em ' (aspas simples).
# Assim, q=flair%3A%27flair_nome%27 se torna q=flair:'flair_nome'.
