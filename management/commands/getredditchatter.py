from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot

class Command(BaseCommand):
	help = 'kicks off the Reddit bot and saved matches to our Chatter database'

	def handle(self, *args, **options):
		new_entry = RedditBot(subreddit="eternalguru", matchkey="sandstorm titan")
		new_entry.save()
