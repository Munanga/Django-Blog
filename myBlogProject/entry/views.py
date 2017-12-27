from django.shortcuts import render
from entry.models import Entries
from entry import forms

# Create your views here.

def home(request):
    stories = Entries.objects.order_by('name')
    con = {'var_stories':stories}
    return render(request,'home/stories.html',con)

def entry(request):
    entryForm = forms.EntryForm()
    con = {'var_entry':entryForm}

    if request.method == "POST":
        entryForm = forms.EntryForm(request.POST)

        if entryForm.is_valid():
            entryForm.save()

    return render(request,'entry/entry.html',con)

