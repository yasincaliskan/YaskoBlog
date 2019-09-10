from django.shortcuts import render, HttpResponse

def home_view(request):
    context = {
            'name' : 'yasko'
        }
    return render(request, 'home.html', context)
