from django.shortcuts import render_to_response
from django.template import RequestContext
from karrlab import settings
import datetime
import os

###################
### pages
###################
def index(request):
    return render_template('index.html', request, data = {'section': ''})

def research(request):
    return render_template('research.html', request, data = {'section': 'research'})

def resources(request):
    return render_template('resources.html', request, data = {'section': 'resources'})
    
def graphics(request):
    return render_template('graphics.html', request, data = {'section': 'resources'})

def resourcesGradFellowships(request):
    return render_template('resourcesGradFellowships.html', request, data = {'section': 'resources'})

def publications(request):
    return render_template('publications.html', request, data = {'section': 'publications'})
    
def news(request):
    return render_template('news.html', request, data = {'section': 'news'})

def press(request):
    return render_template('press.html', request, data = {'section': 'press'})

def funding(request):
    return render_template('funding.html', request, data = {'section': 'funding'})

def people(request):
    return render_template('people.html', request, data = {'section': 'people'})

def alumni(request):
    return render_template('alumni.html', request, data = {'section': 'people'})

def peopleKarrCv(request):
    return render_template('peopleKarrCv.html', request, data = {'section': 'people'})

def peopleKarrPhotos(request):
    return render_template('peopleKarrPhotos.html', request, data = {'section': 'people'})

def join(request):
    return render_template('join.html', request, data = {'section': 'join'})
    
def join20170316PostdoctoralFellow(request):
    return render_template('join/2017-03-16-Postdoctoral-Fellow.html', request, data = {'section': 'join'})
    
def join20170316SoftwareEngineer(request):
    return render_template('join/2017-03-16-Software-Engineer.html', request, data = {'section': 'join'})
    
def join20170316StudentResearchAssistant(request):
    return render_template('join/2017-03-16-Student-Research-Assistant.html', request, data = {'section': 'join'})

def join20160622PostdoctoralFellowBacteria(request):
    return render_template('join/2016-06-22-Postdoctoral-Fellow-Bacteria.html', request, data = {'section': 'join'})

def join20160622PostdoctoralFellowHuman(request):
    return render_template('join/2016-06-22-Postdoctoral-Fellow-Human.html', request, data = {'section': 'join'})

def join20160622PostdoctoralFellowMethods(request):
    return render_template('join/2016-06-22-Postdoctoral-Fellow-Methods.html', request, data = {'section': 'join'})

def join20160622PostdoctoralFellowGenomics(request):
    return render_template('join/2016-06-22-Postdoctoral-Fellow-Genomics.html', request, data = {'section': 'join'})

def join20150317ScientistBacteria(request):
    return render_template('join/2015-03-17-Scientist-Bacteria.html', request, data = {'section': 'join'})

def join20150317ScientistHuman(request):
    return render_template('join/2015-03-17-Scientist-Human.html', request, data = {'section': 'join'})

def join20150317Engineer(request):
    return render_template('join/2015-03-17-Engineer.html', request, data = {'section': 'join'})

def contact(request):
    return render_template('contact.html', request, data = {'section': 'contact'})

def calendar(request):
    return render_template('calendar.html', request, data = {'section': 'calendar'})

###################
### sitemap
###################
def sitemap(request):
    return render_template('sitemap.xml', request, data = {'ROOT_URL': settings.ROOT_URL}, mimetype='application/xml')

def robots(request):
    return render_template('robots.txt', request, data = {'ROOT_DOMAIN': settings.ROOT_DOMAIN, 'ROOT_URL': settings.ROOT_URL}, mimetype='plain/text')

###################
### helper functions
###################
def render_template(templateFile, request, data = {}, mimetype = 'text/html'):
    #add data
    data['request'] = request
    data['last_updated_date'] = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(settings.TEMPLATE_DIRS[0], templateFile)))

    #render
    return render_to_response(templateFile, data, context_instance = RequestContext(request), mimetype = mimetype)
