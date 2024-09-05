from django.shortcuts import render, redirect
from .models import Task, FamilyMember, WorkDone
from.forms import TaskForm, FamilyMemberForm, WorkDoneForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'todo/home.html')

def familymember(request):
    members = FamilyMember.objects.all()
    return render(request, 'todo/family_members.html', {'members': members})

def add_family_member(request):
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_members')
        
    else:
        form = FamilyMemberForm()
    return render(request, 'todo/add_family_member.html', {'form': form})
    
def task(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task.html', {'tasks': tasks})

def add_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        
        else:
            form = TaskForm()
    return render(request, 'todo/add_tasks.html', {'form': TaskForm})
    
def work_done(request):
    work = WorkDone.objects.all()
    return render(request, 'todo/work_done.html', {'work': work})

def add_work_done(request):
    if request.method == 'POST':
        form = WorkDoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_done')
        
        else:
            form = WorkDoneForm()
    return render(request, 'todo/addwork_done.html', {'form': WorkDoneForm})