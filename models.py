#!/usr/bin/env python

from pyquery import PyQuery as pq
import glob

class Post:
    title    = ''
    url      = ''
    date     = ''
    content  = ''
    imageurl = ''
    extracss = ''
    extrajs  = ''
    
    def spit_dict(self):
        return {
            'title':self.title,
            'url':self.url,
            'date':self.date,
            'content':self.content,
            'imageurl':self.imageurl,
            'extracss':self.extracss,
            'extrajs':self.extrajs
        }

post_files = []
posts = []

with open('./blogxml/slugs.txt', 'r') as slugs_txt:
    st = slugs_txt.read().split('\n')
    for n in st:
        post_files.append(n.split('|'))

for n in post_files:
    
    with open('./blogxml/' + n[0], 'rb') as f:
        d = pq(f.read())
        g = Post()
        
        g.url      =  n[1]
        g.title    =  d.find('title').html()
        g.date     =  n[2]
        g.content  =  d.find('content').html()
        g.imageurl =  d.find('imageurl').html()
        g.extracss =  d.find('extracss').html()
        g.extrajs  =  d.find('extrajs').html()
        
        if g.extrajs == None:
            g.extrajs = ''
        
        if n[2] == '':
            index = False
        else:
            index = True
        
        posts.append({'data':g, 'index':index })
        
