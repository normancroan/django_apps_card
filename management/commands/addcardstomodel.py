from django.core.management.base import BaseCommand, CommandError
from card.models import RedditBot, Chatter, EternalCard
import json

class Command(BaseCommand):
    help = 'adds cards to model from eternal json'

    def handle(self, *args, **options):
        with open('card/management/commands/eternal-0.91.json') as json_data:
            cards = json.load(json_data)
            for card in cards:
                #print(card.get('attack', '0'))
                aliases = []
                aliases.append(card.get('name'))
                new_entry = EternalCard.objects.get_or_create(
                set=card.get('set',''),
                name=card.get('name',''),
                text=card.get('text',''),
                cost=card.get('cost',0),
                influence=card.get('influence',''),
                colors=card.get('colors',''),
                rarity=card.get('rarity',''),
                attack=card.get('attack',0),
                health=card.get('health',0),
                type=card.get('type',''),
                subtypes=card.get('subtypes',''),
                num=card.get('num',0),
                aliases=card.get(aliases,'')
                )
