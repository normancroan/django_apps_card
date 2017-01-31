from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot, Chatter, EternalCard
from . import rbot_core as rbot

class Command(BaseCommand):
	help = 'kicks off the Reddit bot and saved matches to our Chatter database'

	def handle(self, *args, **options):
		#new_entry = RedditBot(subreddit="eternalguru", matchkey="sandstorm titan")
		#new_entry.save()
		#stage 'observed' list
		observed = []
		for observation in RedditBot.objects.all():
			observed.append(observation.matchkey)
			print(observation.matchkey)

		for card in EternalCard.objects.all():
			rbot.setupBot(card, observed, reddit)

		for item in observed:
			#print(item)
			new_entry = RedditBot.objects.get_or_create(subreddit="eternalguru", matchkey=item)
			#new_entry.save()
