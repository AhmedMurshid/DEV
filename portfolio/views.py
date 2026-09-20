from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render
from .content import PROFILE, PROJECTS, EXPERTISE, EXPERIENCE

def site_context(request):
    return {'profile': PROFILE}

def home(request):
    return render(request, 'home.html', {'projects': PROJECTS, 'expertise': EXPERTISE, 'experience': EXPERIENCE})

def project(request, slug):
    selected = next((p for p in PROJECTS if p['slug'] == slug), None)
    if not selected:
        raise Http404('Project not found')
    return render(request, 'project.html', {'project': selected, 'projects': [p for p in PROJECTS if p != selected]})

def resume(request):
    return FileResponse((settings.BASE_DIR / 'static' / 'Ahmed_Abdullahi_Resume.pdf').open('rb'), as_attachment=True, filename='Ahmed_Abdullahi_Resume.pdf')
