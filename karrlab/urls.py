from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('karrlab.views',
    url(r'^$',                                  'index',                       name='index'),

    url(r'^research/*$',                        'research',                    name='research'),

    url(r'^resources/*$',                       'resources',                   name='resources'),
    url(r'^resources/graphics/*$',              'graphics',                    name='graphics'),
    url(r'^resources/grad-fellowships/*$',      'resourcesGradFellowships',    name='resourcesGradFellowships'),

    url(r'^publications/*$',                    'publications',                name='publications'),

    url(r'^press/*$',                           'press',                       name='press'),

    url(r'^funding/*$',                         'funding',                     name='funding'),

    url(r'^people/*$',                          'people',                      name='people'),
    url(r'^alumni/*$',                          'alumni',                      name='alumni'),
    url(r'^people/karr/cv/*$',                  'peopleKarrCv',                name='peopleKarrCv'),
    url(r'^people/karr/photos/*$',              'peopleKarrPhotos',            name='peopleKarrPhotos'),

    url(r'^join/*$',                            'join',                         name='join'),
    url(r'^join/2016-06-22-Postdoctoral-Fellow-Bacteria/*$', 'join20160622PostdoctoralFellowBacteria', name='join20160622PostdoctoralFellowBacteria'),
    url(r'^join/2016-06-22-Postdoctoral-Fellow-Human/*$',    'join20160622PostdoctoralFellowHuman',    name='join20160622PostdoctoralFellowHuman'),
    url(r'^join/2016-06-22-Postdoctoral-Fellow-Methods/*$',  'join20160622PostdoctoralFellowMethods',  name='join20160622PostdoctoralFellowMethods'),
    url(r'^join/2016-06-22-Postdoctoral-Fellow-Genomics/*$', 'join20160622PostdoctoralFellowGenomics', name='join20160622PostdoctoralFellowGenomics'),
    url(r'^join/2015-03-17-Scientist-Bacteria/*$',           'join20150317ScientistBacteria',          name='join20150317ScientistBacteria'),
    url(r'^join/2015-03-17-Scientist-Human/*$',              'join20150317ScientistHuman',             name='join20150317ScientistHuman'),
    url(r'^join/2015-03-17-Engineer/*$',                     'join20150317Engineer',                   name='join20150317Engineer'),

    url(r'^contact/*$',                         'contact',                     name='contact'),

    url(r'^calendar/*$',                        'calendar',                    name='calendar'),

    url(r'^sitemap.xml$',                       'sitemap',                     name='sitemap'),
    url(r'^robots.txt$',                        'robots',                     name='robots'),
)
