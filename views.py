from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Chatter
# Create your views here.

def index(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	context = {'latest_chatter_list': latest_chatter_list,}
	return render(request, 'card/index.html', context)

def detail(request, card_id):
	response = "Here you'll find the details for card %s."
	return HttpResponse(response % card_id)

def chatter_detail(request, chatter_id):
	response = "Here you'll find the details for chatter %s."
	return HttpResponse(response % chatter_id)

def chatter(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	#output = ', '.join([c.chatter_content for c in latest_chatter_list])
	#return HttpResponse(output)
	template = loader.get_template('chatter/index.html')
	context = {
		'latest_chatter_list': latest_chatter_list,
	}
	return HttpResponse(template.render(context, request))
