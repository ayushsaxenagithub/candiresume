from cgitb import html
from django.shortcuts import render,redirect
from matplotlib.style import context
from django.db.models import Q
from .models import Candidate, Project,Skill
from django.contrib.auth.decorators import login_required
from .forms import CandidateForm, ProjectForm, SkillForm
from .utils import searchProfiles

# Create your views here.
def home(request):
    candidate, search_query = searchProfiles(request)
    context = {'candidate': candidate,'search_query': search_query}
    return render(request,'candidate/home.html',context)


def ViewProfile(request,pk):
    candidate = Candidate.objects.get(id=pk)
    context = {'candidate': candidate}
    return render(request,'candidate/view_profile.html',context)

@login_required(login_url='login')
def createCandidate(request):
   form = CandidateForm()
   if request.method == 'POST':
      form= CandidateForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('home')
   context = {'form': form}
   return render(request,'candidate/new_candidate.html', context)


@login_required(login_url='login')
def UpdateCandidate(request,pk):
   candidate = Candidate.objects.get(id=pk)
   form = CandidateForm(instance=candidate)
   if request.method == 'POST':
      form = CandidateForm(request.POST,request.FILES, instance=candidate)
      if form.is_valid():
         form.save()
         return redirect('home')
   context = {'form': form}
   return render(request,'candidate/new_candidate.html', context)



@login_required(login_url='login')
def DeleteCandidate(request,pk):
   candidate = Candidate.objects.get(id=pk)
   if request.method == 'POST':
         candidate.delete()
         return redirect('home')     
   context = {'candidate': candidate}
   return render(request, 'candidate/delete_candidate.html', context)

def AcceptProfile(request,pk):
    candidate = Candidate.objects.get(id=pk)
    candidate.status = 2
    candidate.save()
    candi = Candidate.objects.all()
    context = {'candidate': candi,}
    return render(request, 'candidate/home.html',context)

def RAcceptProfile(request,pk):
    candidate = Candidate.objects.get(id=pk)
    candidate.status = 2
    candidate.save()
    candi = Candidate.objects.all()
    context = {'candidate': candi,}
    return render(request, 'candidate/rejected.html',context)

def RejectProfile(request,pk):
    candidate = Candidate.objects.get(id=pk)
    candidate.status = 3
    candidate.save()
    candi = Candidate.objects.all()
    context = {'candidate': candi,}
    return render(request, 'candidate/home.html',context)

def RejectedProfile(request):
    candidate = Candidate.objects.all()
    context = {'candidate': candidate,}
    return render(request,'candidate/rejected.html',context)


def ReviewDelete(request):
    candidate = Candidate.objects.all()
    context = {'candidate': candidate,}
    return render(request,'candidate/review_delete.html',context)

@login_required(login_url='login')
def CreateProject(request,pk):
   candidate =Candidate.objects.get(id=pk)
   project = request.user.profile
   print(project)

   form = ProjectForm()
   if request.method == 'POST':
      form= ProjectForm(request.POST, request.FILES)
      if form.is_valid():
         project=form.save(commit=False)
         project.owner = candidate
         project.save()
         return redirect('view_profile',pk)
   context = {'form': form}
   return render(request,'candidate/create-project.html', context)


@login_required(login_url='login')
def UpdateProject(request,pk):
   proj =Project.objects.get(id=pk)
   of=proj.owner.id
   print('proj=',proj)
   candidate = proj.owner
   print('candidate=',candidate)
   form = ProjectForm(instance=proj)
   if request.method == 'POST':
      form= ProjectForm(request.POST, request.FILES, instance=proj)
      if form.is_valid():
         project=form.save()
         return redirect('view_profile',pk=of)
   context = {'form': form}
   return render(request,'candidate/create-project.html', context)


@login_required(login_url="login")
def DeleteProject(request, pk):
    project =Project.objects.get(id=pk)
    of=project.owner.id
    project.delete()
    return redirect('view_profile',pk=of)

@login_required(login_url='login')
def CreateSkill(request,pk):
   candidate =Candidate.objects.get(id=pk)
   project = request.user.profile
   form = SkillForm()
   if request.method == 'POST':
      form= SkillForm(request.POST, request.FILES)
      if form.is_valid():
         project=form.save(commit=False)
         project.owner = candidate
         project.save()
         return redirect('view_profile',pk)
   context = {'form': form}
   return render(request,'candidate/create-skill.html', context)


@login_required(login_url='login')
def UpdateSkill(request,pk):
   skill =Skill.objects.get(id=pk)
   of=skill.owner.id
   form = SkillForm(instance=skill)
   if request.method == 'POST':
      form= SkillForm(request.POST, request.FILES, instance=skill)
      if form.is_valid():
         skill=form.save()
         return redirect('view_profile',pk=of)
   context = {'form': form}
   return render(request,'candidate/create-skill.html', context)


@login_required(login_url="login")
def DeleteSkill(request, pk):
    skill =Skill.objects.get(id=pk)
    of=skill.owner.id
    skill.delete()
    return redirect('view_profile',pk=of)