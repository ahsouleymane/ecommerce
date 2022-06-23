from django.shortcuts import render

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)