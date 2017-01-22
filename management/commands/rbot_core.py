#!/usr/bin/python
import praw, re
from card.models import RedditBot, Chatter, EternalCard

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('eternalcardgame')
observed = []

def setupBot(card, observedList):
    print('starting bot for: ',card.name)
    global observed
    observed = observedList
    getSubmissions(subreddit,card)


def getSubmissions(subreddit,card):
    print("getting submissions from: ",subreddit, 'for: ',card.name)
    for submission in subreddit.hot(limit=5):
        submission.comments.replace_more(limit=0)
        parseSubmission(submission,card)

def parseSubmission(submission,card):
    for phrase in card.aliases:
        #print('gathering posts for phrase: ',phrase)
        # If we haven't harvested this post before
        if str('submission' + submission.id + phrase) not in observed:
        # Do a case insensitive search
            if re.search(phrase, submission.title, re.IGNORECASE):
                #print("Bot found match for: ",phrase," at: ",submission.title)
                # Store the current id into our list
                observed.append(str('submission' + submission.id + phrase))
                saveMatch('post',submission.title,phrase,card,submission.created)

    for comment in submission.comments.list():
        parseComment(comment,card)

def parseComment(comment,card):
    for phrase in card.aliases:
        #print('gathering comments for phrase: ',phrase)
        # If we haven't harvested this comment before
        if str('comment' + comment.id + phrase) not in observed:
        # Do a case insensitive search
            if re.search(phrase, comment.body, re.IGNORECASE):
                #print("Bot found match for: ",phrase, comment.body," at: ",comment.id)
                # Store the current id into our list
                observed.append(str('comment' + comment.id + phrase))
                saveMatch('comment',comment.body,phrase,card,comment.created)

def saveMatch(matchType,matchContent,phrase,card,date):
    print('saving... ',matchType,' to card: ',card.name,' with match on alias: ',phrase,'...match is: ',matchContent)
    cardObject = EternalCard.objects.get(name=card.name)
    new_entry = Chatter.objects.get_or_create(eternalcard=cardObject, chatter_type=matchType, chatter_content=matchContent, chatter_source='reddit', pub_date=)
