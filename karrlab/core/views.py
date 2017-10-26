""" Core views
:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-10-26
:Copyright: 2017, Karr Lab
:License: MIT
"""

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from karrlab.site import settings
import os

###################
### pages
###################
def index(request):
    return render_template(request, 'index.html', context={'section': ''})

def research(request):
    return render_template(request, 'research.html', context={'section': 'research'})

def resources(request):
    return render_template(request, 'resources.html', context={'section': 'resources'})

def graphics(request):
    return render_template(request, 'graphics.html', context={'section': 'resources'})

def resourcesGradFellowships(request):
    return render_template(request, 'resourcesGradFellowships.html', context={'section': 'resources'})

def publications(request):
    return render_template(request, 'publications.html', context={'section': 'publications'})

def video(request):
    return render_template(request, 'video.html', context={'section': 'video'})

def news(request):
    return render_template(request, 'news.html', context={'section': 'news'})

def press(request):
    return render_template(request, 'press.html', context={'section': 'press'})

def funding(request):
    return render_template(request, 'funding.html', context={'section': 'funding'})

def people(request):
    return render_template(request, 'people.html', context={'section': 'people'})

def alumni(request):
    return render_template(request, 'alumni.html', context={'section': 'people'})

def peopleKarrCv(request):
    return render_template(request, 'peopleKarrCv.html', context={'section': 'people'})

def peopleKarrPhotos(request):
    return render_template(request, 'peopleKarrPhotos.html', context={'section': 'people'})

def join(request):
    return render_template(request, 'join.html', context={'section': 'join'})

def join20171002Scientist(request):
    return render_template(request, 'join/2017-10-02-Scientist.html', context={'section': 'join'})

def join20171002Engineer(request):
    return render_template(request, 'join/2017-10-02-Engineer.html', context={'section': 'join'})

def join20171002Undergrad(request):
    return render_template(request, 'join/2017-10-02-Undergrad.html', context={'section': 'join'})

def join20170812Scientist(request):
    return render_template(request, 'join/2017-08-12-Scientist.html', context={'section': 'join'})

def join20170316PostdoctoralFellow(request):
    return render_template(request, 'join/2017-03-16-Postdoctoral-Fellow.html', context={'section': 'join'})

def join20170316SoftwareEngineer(request):
    return render_template(request, 'join/2017-03-16-Software-Engineer.html', context={'section': 'join'})

def join20170316StudentResearchAssistant(request):
    return render_template(request, 'join/2017-03-16-Student-Research-Assistant.html', context={'section': 'join'})

def join20160622PostdoctoralFellowBacteria(request):
    return render_template(request, 'join/2016-06-22-Postdoctoral-Fellow-Bacteria.html', context={'section': 'join'})

def join20160622PostdoctoralFellowHuman(request):
    return render_template(request, 'join/2016-06-22-Postdoctoral-Fellow-Human.html', context={'section': 'join'})

def join20160622PostdoctoralFellowMethods(request):
    return render_template(request, 'join/2016-06-22-Postdoctoral-Fellow-Methods.html', context={'section': 'join'})

def join20160622PostdoctoralFellowGenomics(request):
    return render_template(request, 'join/2016-06-22-Postdoctoral-Fellow-Genomics.html', context={'section': 'join'})

def join20150317ScientistBacteria(request):
    return render_template(request, 'join/2015-03-17-Scientist-Bacteria.html', context={'section': 'join'})

def join20150317ScientistHuman(request):
    return render_template(request, 'join/2015-03-17-Scientist-Human.html', context={'section': 'join'})

def join20150317Engineer(request):
    return render_template(request, 'join/2015-03-17-Engineer.html', context={'section': 'join'})

def contact(request):
    return render_template(request, 'contact.html', context={'section': 'contact'})

def calendar(request):
    return render_template(request, 'calendar.html', context={'section': 'calendar'})

def survey(request):
    return redirect('https://goo.gl/forms/xH59G9gkPFRORXUa2')

###################
### sitemap
###################
def sitemap(request):
    return render_template(request, 'sitemap.xml', context={'ROOT_URL': settings.ROOT_URL}, content_type='application/xml')

def robots(request):
    return render_template(request, 'robots.txt', context={'ROOT_DOMAIN': settings.ROOT_DOMAIN, 'ROOT_URL': settings.ROOT_URL}, content_type='plain/text')

###################
### helper functions
###################
def render_template(request, template, context=None, content_type='text/html'):
    ''' Returns rendered template

    Args:
        request (:obj:`django.http.request.HttpRequest`): HTTP request
        template (:obj:`str`): path to template to render_template
        context (:obj:`dict`, optional): dictionary of data needed to render template
        content_type (:obj:`str`, optional): mime type

    Returns:
        :obj:`django.http.HttpResponse`: HTTP response
    '''

    if context is None:
        context = {}

    #add data
    context['request'] = request
    context['last_updated_date'] = datetime.fromtimestamp(os.path.getmtime(os.path.join(settings.TEMPLATES[0]['DIRS'][0], template)))

    #render
    return render(request, template, context=context, content_type=content_type)
