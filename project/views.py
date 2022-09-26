from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from .models import Project
from .forms import ProjectForm

@login_required
def index(request):
  list = Project.objects.filter(creator=request.user)
  context = {'list':list}
  return render(request, 'project/index.html', context)
  
# def create(request):    # move to workspace app
#     form = ProjectForm()
#     return render(request, 'project/create.html')

def delete(request, pk):
  try:
    data = get_object_or_404(Project, id=pk)
  except Exception:
    raise Http404('Post not found')
  
  if request.method == 'POST':
    data.delete()
    return redirect('/projects')
  else:
    return render(request, 'project/delete.html')

class detail(DetailView):
  model = Project
  success_url = reverse_lazy('index')
