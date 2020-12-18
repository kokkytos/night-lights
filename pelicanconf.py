#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Λεωνίδας Λιάκος'
SITENAME = 'Μοντέλα αστικής εξάπλωσης και παρακολούθηση με τηλεπισκόπηση'
SITEURL = 'https://kokkytos.github.io/night-lights'

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Εργαστήριο Χωρικής Ανάλυσης, Γεωγραφικών Πληροφοριακών Συστημάτων και Θεματικής Χαρτογραφίας', 'http://gislab.gr'),
         ('NASA Black Marble Product', 'https://blackmarble.gsfc.nasa.gov/'),
         ('DMSP-OLS Nighttime Lights', 'https://ngdc.noaa.gov/eog/dmsp/downloadV4composites.html'),
         ('VIIRS Day/Night Band Nighttime Lights', 'https://eogdata.mines.edu/download_dnb_composites.html'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/kokkytos'),
          ('Linkedin', 'https://www.linkedin.com/'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Leonidas_Liakos'),
          ('ORCID', 'https://orcid.org/0000-0003-1961-6940')
)

DEFAULT_PAGINATION = 10

THEME = "/home/leonidas/pelican-themes/bootstrap2"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
