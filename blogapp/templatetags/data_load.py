from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from blogapp import models
register = template.Library()

@register.filter(name='contactreg')
def mycontact(request):
    cnt  = models.Contact.objects.filter(Status = True).order_by("-id")
    return cnt

@register.filter(name='footer')
def myfooter(request):
    foot  = models.company_footer_link.objects.filter(Status = True).order_by("-id")
    return foot

@register.filter(name='logoreg')
def logoicon(request):
    logo  = models.Logo.objects.filter(Status = True).order_by("-id")
    return logo

@register.filter(name='pop')
def populer(request):
    p_post  = models.Properte.objects.filter(Status = True).order_by("-view")
    return p_post

@register.filter(name='popb')
def populerblog(request):
    p_blog  = models.blog.objects.filter(Status = True).order_by("-view")
    return p_blog
    
@register.filter(name='cat')
def category(request):
    category    = models.Category.objects.filter(Status=True).all()
    return category

@register.filter(name='scat')
def subcat(request):
    subcategory = models.subcategory.objects.filter(Status=True).all()
    return subcategory


@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep

