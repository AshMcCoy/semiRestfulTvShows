from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    shows = Show.objects.all()
    context = {
        "shows": shows
    }
    return render(request, 'index.html', context)

def show_form(request):
    return render(request, 'add_show.html')

def create_show(request):
    errors = Show.objects.addShow_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new')
    else:
        if request.method == 'POST':
            newShow= Show.objects.create(
                title= request.POST['title'],
                network= request.POST['network'],
                release_date= request.POST['release_date'],
                desc= request.POST['description'],    
            )
            return redirect(f"/shows/{newShow.id}")
        return redirect('shows/new')

def show_info(request, showId):
    thisShow = Show.objects.get(id= showId)
    context = {
        "thisShow": thisShow
    }
    return render(request, 'show_info.html', context)

def edit_show(request, showId):
    thisShow = Show.objects.get(id = showId)
    context = {
        "thisShow" : thisShow
    }
    return render(request, 'edit.html', context)

def update_show(request, showId):
    errors = Show.objects.editShow_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{showId}/edit")
    else: 
        if request.method == 'POST':
            thisShow= Show.objects.get(id= showId)
            thisShow.title = request.POST['title']
            thisShow.network = request.POST['network']
            thisShow.release_date= request.POST['release_date']
            thisShow.desc= request.POST['description']
            thisShow.save()
        
            return redirect(f"/shows/{thisShow.id}")
        return redirect(f"/shows/{thisShow.id}/edit")

def delete_show(request, showId):
    thisShow = Show.objects.get(id= showId)
    thisShow.delete()

    return redirect('/shows')
    
