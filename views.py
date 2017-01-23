from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Chatter, EternalCard
# Create your views here.

def index(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	context = {'latest_chatter_list': latest_chatter_list,}
	return render(request, 'card/index.html', context)

def detail(request, card_name):
	name = card_name.replace('_',' ')
	card = get_object_or_404(EternalCard, name=card_name)
	return render(request, 'card/detail.html', {'card': card})

def chatter_detail(request, chatter_id):
	chatter = get_object_or_404(Chatter, pk=chatter_id)
	return render(request, 'chatter/detail.html', {'chatter': chatter})

def chatter(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	#output = ', '.join([c.chatter_content for c in latest_chatter_list])
	#return HttpResponse(output)
	template = loader.get_template('chatter/index.html')
	context = {
		'latest_chatter_list': latest_chatter_list,
	}
	return HttpResponse(template.render(context, request))
