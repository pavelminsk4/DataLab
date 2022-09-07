from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project.models import Workspace
from django.views.generic import DetailView
from django.urls import reverse_lazy

@login_required
def detail(request, pk):
  workspace = Workspace.objects.get(id=pk)
  context = {'workspace':workspace}
  return render(request, 'workspace/detail.html', context)
