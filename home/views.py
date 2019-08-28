from django.shortcuts import render, HttpResponse

def home_view(request):
    context = {
            'isim' : 'yasko'
        }
    return render(request, 'home.html', context)
