from django.shortcuts import render
from django.http import HttpResponse

from .models import Chatter
# Create your views here.

def index(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	output = ', '.join([c.chatter_content for c in latest_chatter_list])
	return HttpResponse(output)

def detail(request, card_id):
	response = "Here you'll find the details for card %s."
	return HttpResponse(response % card_id)

