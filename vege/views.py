from django.shortcuts import render, redirect
from .models import Receipe

def mainpage(request):
    return render(request, 'base.html')

def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('/receipe/')  # Redirect to avoid duplicate submissions

    queryset = Receipe.objects.all()
    return render(request, 'receipee.html', {'receipes': queryset})


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')

def update_receipe(request, id):  # sourcery skip: extract-method
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')
        

    context = {'receipe':queryset}
    return render(request, 'update_receipe.html', context)
