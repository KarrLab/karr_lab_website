""" HTML GUI URL patterns
:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-10-25
:Copyright: 2017, Karr Lab
:License: MIT
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',                                  views.index,                       name='index'),

    url(r'^research/*$',                        views.research,                    name='research'),

    url(r'^resources/*$',                       views.resources,                   name='resources'),
    url(r'^resources/graphics/*$',              views.graphics,                    name='graphics'),
    url(r'^resources/grad-fellowships/*$',      views.resourcesGradFellowships,    name='resourcesGradFellowships'),

    url(r'^publications/*$',                    views.publications,                name='publications'),
    url(r'^video/*$',                           views.video,                       name='video'),

    url(r'^news/*$',                            views.news,                        name='news'),
    url(r'^press/*$',                           views.press,                       name='press'),

    url(r'^funding/*$',                         views.funding,                     name='funding'),

    url(r'^people/*$',                          views.people,                      name='people'),
    url(r'^alumni/*$',                          views.alumni,                      name='alumni'),
    url(r'^people/karr/cv/*$',                  views.peopleKarrCv,                name='peopleKarrCv'),
    url(r'^people/karr/photos/*$',              views.peopleKarrPhotos,            name='peopleKarrPhotos'),

    url(r'^join/*$',                            views.join,                         name='join'),
    url(r'^join/2018-07-26-Scientist/*$', views.join20180726Scientist, name='join20180726Scientist'),
	url(r'^join/2018-07-26-Engineer/*$', views.join20180726Engineer, name='join20180726Engineer'),
	url(r'^join/2018-07-26-Undergrad/*$', views.join20180726Undergrad, name='join20180726Undergrad'),	
    
	#url(r'^join/2018-02-04-Student-Summer-Research-Assistant/*$', views.join20180204StudentSummerResearchAssistant, name='join20180204StudentSummerResearchAssistant'),
    #url(r'^join/2017-10-02-Scientist/*$', views.join20171002Scientist, name='join20171002Scientist'),
	#url(r'^join/2017-10-02-Engineer/*$', views.join20171002Engineer, name='join20171002Engineer'),
	#url(r'^join/2017-10-02-Undergrad/*$', views.join20171002Undergrad, name='join20171002Undergrad'),	
    #url(r'^join/2017-03-16-Postdoctoral-Fellow/*$', views.join20170316PostdoctoralFellow, name='join20170316PostdoctoralFellow'),
    #url(r'^join/2017-03-16-Software-Engineer/*$', views.join20170316SoftwareEngineer, name='join20170316SoftwareEngineer'),
    #url(r'^join/2017-03-16-Student-Research-Assistant/*$', views.join20170316StudentResearchAssistant, name='join20170316StudentResearchAssistant'),    
    #url(r'^join/2016-06-22-Postdoctoral-Fellow-Bacteria/*$', views.join20160622PostdoctoralFellowBacteria, name='join20160622PostdoctoralFellowBacteria'),
    #url(r'^join/2016-06-22-Postdoctoral-Fellow-Human/*$', views.join20160622PostdoctoralFellowHuman, name='join20160622PostdoctoralFellowHuman'),
    #url(r'^join/2016-06-22-Postdoctoral-Fellow-Methods/*$', views.join20160622PostdoctoralFellowMethods, name='join20160622PostdoctoralFellowMethods'),
    #url(r'^join/2016-06-22-Postdoctoral-Fellow-Genomics/*$', views.join20160622PostdoctoralFellowGenomics, name='join20160622PostdoctoralFellowGenomics'),
    #url(r'^join/2015-03-17-Scientist-Bacteria/*$', views.join20150317ScientistBacteria, name='join20150317ScientistBacteria'),
    #url(r'^join/2015-03-17-Scientist-Human/*$', views.join20150317ScientistHuman, name='join20150317ScientistHuman'),
    #url(r'^join/2015-03-17-Engineer/*$', views.join20150317Engineer, name='join20150317Engineer'),

    url(r'^contact/*$',                         views.contact,                     name='contact'),

    url(r'^calendar/*$',                        views.calendar,                    name='calendar'),
    
    url(r'^survey/*$',                          views.survey,                      name='survey'),

    url(r'^sitemap.xml$',                       views.sitemap,                     name='sitemap'),
    url(r'^robots.txt$',                        views.robots,                      name='robots'),
]