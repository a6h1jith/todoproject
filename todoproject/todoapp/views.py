from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import todoupdate
from todoapp.models import Task
from django.views.generic import ListView,DetailView,UpdateView,DeleteView


class ListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class DetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class UpdateView(UpdateView):
    model = Task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})

class DeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url=reverse_lazy('classlist')


#Create your views here.
def home(request):
    task1= Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
def delete(request, taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=todoupdate(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})