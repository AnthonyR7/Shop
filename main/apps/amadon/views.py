from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if request.session.get('total') == None:
		request.session['total'] = 0

    if request.session.get('how_many') == None:
        request.session['how_many'] = 0

    if request.session.get('sentence_about') == None:
        request.session['sentence_about'] = []

    return render(request, "amadon/index.html")
def process(request):
    if request.method == 'POST':
        if request.POST['product'] == '1012':
            t_shirt_purchase = 19.99
            request.session['total'] += t_shirt_purchase
            request.session['sentence_about'].append("We charged your credit card for " + str(t_shirt_purchase))
            if request.POST['quantity']:
                request.session['how_many'] += int(request.POST['quantity'])

        elif request.POST['product'] == '1056':
            sweater_purchase = 29.99
            request.session['total'] += sweater_purchase
            request.session['sentence_about'].append("We charged your credit card for " + str(sweater_purchase))
            if request.POST['quantity']:
                request.session['how_many'] += int(request.POST['quantity'])

        elif request.POST['product'] == '1098':
            dojo_cup = 4.99
            request.session['total'] += dojo_cup
            request.session['sentence_about'].append("We charged your credit card for " + str(dojo_cup))
            if request.POST['quantity']:
                request.session['how_many'] += int(request.POST['quantity'])

        elif request.POST['product'] == '1047':
            algorithm_book = 49.99
            request.session['total'] += algorithm_book
            request.session['sentence_about'].append("We charged your credit card for " + str(algorithm_book))
            if request.POST['quantity']:
                request.session['how_many'] += int(request.POST['quantity'])
    return redirect("/final_sale")

def final_sale(request):
    context = {
        'total': request.session['total'],
        'sentence': request.session['sentence_about'],
        'amount_in_quantity': request.session['how_many']
    }
    return render(request, 'amadon/total.html', context)
def goback(request):
    del request.session['sentence_about']
    return redirect("/")
