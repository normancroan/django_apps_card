from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot, Chatter, EternalCard
import json

class Command(BaseCommand):
    help = 'adds cards to model from eternal json'

    def handle(self, *args, **options):
        with open('card/management/commands/eternal-0.91.json') as json_data:
            cards = json.load(json_data)
            for card in cards:
                print(card.get('attack', '0'))
                #new_entry = EternalCard.objects.get_or_create(
                #set=card['set'],
                #name=card['name'],
                #text=card['text'],
                #cost=card['cost'],
                #influence=card['influence'],
                #colors=card['colors'],
                #rarity=card['rarity'],
                #attack=card['attack'],
                #health=card['health'],
                #type=card['type'],
                #subtypes=card['subtypes'],
                #num=card['num'],
                #aliases=card['name']
                #)
