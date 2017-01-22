from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot, Chatter, EternalCard
import rbot_core as rbot

class Command(BaseCommand):
	help = 'kicks off the Reddit bot and saved matches to our Chatter database'

	def handle(self, *args, **options):
		#new_entry = RedditBot(subreddit="eternalguru", matchkey="sandstorm titan")
		#new_entry.save()
		#stage 'observed' list
		observed = []
		for observation in RedditBot.objects.all():
			observed.append(observation.matchkey)

		for card in EternalCard.objects.all():
			rbot.setupBot(card, observed)
