from django.shortcuts import render, redirect
from random import randint
from time import strftime

# Create your views here.
def index(request):
	if 'gold' in request.session:
		pass
	else:
		request.session['gold'] = 0
	if 'messages' in request.session:
		pass
	else:
		request.session['messages'] = []
	context = {
		'gold': request.session['gold'],
		'loop_times': range(len(request.session['messages']), -1, -1)
	}
	return render(request, 'ninjaGoldApp/index.html', context)

def processMoney(request):
	if request.POST['building'] == 'cave':
		gold = randint(5, 10)
		string = "You have earned " + str(gold) + " gold from the cave! (" + strftime("%Y-%m-%d %H:%M:%S") + ")"
		request.session['messages'].append(string)
		request.session['gold'] += gold
	if request.POST['building'] == 'farm':
		gold = randint(10, 20)
		string = "You have earned " + str(gold) + " gold from the farm! (" + strftime("%Y-%m-%d %H:%M:%S") + ")"
		request.session['messages'].append(string)
		request.session['gold'] += gold
	if request.POST['building'] == 'house':
		gold = randint(2, 5)
		string = "You have earned " + str(gold) + " gold from the house! (" + strftime("%Y-%m-%d %H:%M:%S") + ")"
		request.session['messages'].append(string)
		request.session['gold'] += gold
	if request.POST['building'] == 'casino':
		gold = randint(-50, 50)
		if gold < 0:
			string = "You have lost " + str(gold) + " gold from the casino! :( :( :( (" + strftime("%Y-%m-%d %H:%M:%S") + ")"
			request.session['messages'].append(string)
		if gold > 0:
			string = "You have earned " + str(gold) + " gold from the casino! (" + strftime("%Y-%m-%d %H:%M:%S") + ")"
			request.session['messages'].append(string)
		request.session['gold'] += gold		
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')



