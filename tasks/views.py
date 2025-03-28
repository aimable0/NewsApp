#!/usr/bin/python3

from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="task name:")


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {"tasks": request.session["tasks"]})


# add a new task
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # lets redirect the user to see the list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        else:  # if form is not valid
            return render(request, "tasks/add.html", {"form": form})
    return render(request, "tasks/add.html", {"form": NewTaskForm()})
