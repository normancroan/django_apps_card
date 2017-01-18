from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot, Chatter, EternalCard
import praw

class Command(BaseCommand):
	help = 'kicks off the Reddit bot and saved matches to our Chatter database'

	def handle(self, *args, **options):
		#new_entry = RedditBot(subreddit="eternalguru", matchkey="sandstorm titan")
		#new_entry.save()
		
		# Create the Reddit instance
		reddit = praw.Reddit('bot1')
		subreddit = reddit.subreddit('eternalcardgame')
		#stage 'observed' list
		observed = []
		for observation in RedditBot.objects.all():
			observed.append(observation.matchkey)
		#stage phrase list
		phraseList = []
		for card in EternalCard.objects.all():
			for alias in card.aliases:
				phraseList.append(alias)
				self.stdout.write('added alias: ',alias)
