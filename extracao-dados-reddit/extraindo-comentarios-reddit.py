import praw
from praw import MoreComments
import pandas as pd


with open('senha reddit.txt', 'r') as f:
    minha_senha = f.read()

with open('reddit client id.txt', 'r') as g:
    client_key = g.read()

with open('reddit client secret.txt', 'r') as h:
    client_secret = h.read()

headers = {'User-Agent':'windows:script for automation:v0.1 (by u/RevolutionaryLab7729'}

reddit_instance = praw.Reddit(client_id= client_key,
                              client_secret = client_secret,
                              password = minha_senha,
                              user_agent = headers,
                              username = "RevolutionaryLab7729")


sub_instance = reddit_instance.subreddit("AskHistorians")


df = pd.DataFrame()
titles= []
ids = []
urls = []
num_comments = []


for post in sub_instance.new(limit=5):
    titles.append(post.title)
    ids.append(post.id)
    urls.append(post.url)
    num_comments.append(post.num_comments)


df['Títulos'] = titles
df['IDs'] = ids
df['URLs'] = urls
df['Número de comentários'] = num_comments

# -------------------------------------------------------------

# Extraindo comentários.


askscience_instance = reddit_instance.subreddit('AskHistorians')

hot = askscience_instance.hot(limit=5)

all_comments = []

for submission in hot:

    if submission.stickied or (submission.num_comments < 2):
        continue

    submission.comment_sort = "best"
    submission.comment_limit = '2'
    comments = submission.comments
    
    for comment in comments:
        
        if isinstance(comment, MoreComments) or comment.body == '[removed]' or comment.stickied:
            continue

        all_comments.append(comment.body)
        all_comments.append(comment.author)


# Podemos extrair todos os comentários secundários (os que respondem ao comentário top level) usando um loop secundário.
replies =[]

for submission in hot:

    if submission.stickied or (submission.num_comments < 2):
        continue
        
    submission.comments.replace_more(limit=None)
    for top_level_comment in submission.comments:

        for second_level_comment in top_level_comment.replies:
            replies.append(second_level_comment.body)
