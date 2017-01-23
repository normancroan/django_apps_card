from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot, Chatter, EternalCard
import json

class Command(BaseCommand):
	help = 'adds cards to model from eternal json'

	def handle(self, *args, **options):
        with open('eternal-0.91.json') as json_data:
            cards = json.load(json_data)
            for card in cards:
    			print(card['name'])
    			#new_entry = RedditBot.objects.get_or_create(subreddit="eternalguru", matchkey=item)
    			#new_entry.save()
