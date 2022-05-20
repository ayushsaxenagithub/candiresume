from django.db.models import Q
from .models import Candidate, Skill, Project




def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skillsname = Skill.objects.filter(name__icontains=search_query)
    skillsdescription = Skill.objects.filter(description__icontains=search_query)
    projecttitle = Project.objects.filter(title__icontains=search_query)
    projectdescription = Project.objects.filter(description__icontains=search_query)


    candidates=Candidate.objects.distinct().filter(
        Q(first_name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(last_name__icontains=search_query) |
        Q(middle_name__icontains=search_query) |
        Q(phone__icontains=search_query) |
        Q(bio__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(skill__in=skillsname)|
        Q(project__in=projecttitle)|
        Q(project__in=projectdescription)|
        Q(skill__in=skillsdescription)
    )

    return candidates, search_query
