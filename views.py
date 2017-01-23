from django.shortcuts import render, get_object_or_404

from .models import Chatter, EternalCard
# Create your views here.

def index(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	context = {'latest_chatter_list': latest_chatter_list,}
	return render(request, 'card/index.html', context)

def detail(request, card_name):
	card = get_object_or_404(EternalCard, name__iexact=card_name.replace('_',' '))
	return render(request, 'card/detail.html', {'card': card})

def chatter_detail(request, chatter_id):
	chatter = get_object_or_404(Chatter, pk=chatter_id)
	return render(request, 'chatter/detail.html', {'chatter': chatter})

def chatter(request):
	latest_chatter_list = Chatter.objects.order_by('-pub_date')[:5]
	context = {'latest_chatter_list': latest_chatter_list,}
	return render(request, 'chatter/index.html', context)
