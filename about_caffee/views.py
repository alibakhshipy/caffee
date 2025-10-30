from django.shortcuts import render

# Create your views here.
def about_caffee(request):
    return render(request, 'about_caffee.html')
