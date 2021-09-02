import praw
import os
import telegram
from time import sleep
CID = 'CommonID Reddit APP'
SID = 'SecretID Reddit APP'
BID = 'TelegramBotID'
channel = TelegramChannelID
PORT = int(os.environ.get('PORT', 5000))

reddit = praw.Reddit(user_agent="shush",
                client_id=CID,
                client_secret=SID,
                username='username',
                password='password')
token = BID

bot = telegram.Bot(token=token)

sub = reddit.subreddit("mauerstrassenwetten")
postlist = []
leng=len(postlist)
while True:
    try:
        for submissions in sub.hot(limit=4):
            if submissions.stickied:
                if ('Tägliche Diskussion ' in submissions.title) or ('Pläne ' in submissions.title):
                    submissions.comments.replace_more(limit=None)
                    comment_queue = submissions.comments[:]  # Seed with top-level
                    while comment_queue:
                        comment = comment_queue.pop(0)
                        comment_queue.extend(comment.replies)
                        if comment.author == 'dronix111' and '.com' in comment.body:
                        #if comment.author == 'Xeophon':
                            if comment.body in postlist:
                                pass
                            else:
                                postlist.append(comment.body)
        if len(postlist) > leng:
            diff=len(postlist)-leng
            for j in range(diff):
                bot.sendMessage(channel, text=postlist[leng+j], parse_mode=telegram.ParseMode.HTML)
        leng=len(postlist)
        sleep(300)

    except Exception as e:
        sleep(20)
