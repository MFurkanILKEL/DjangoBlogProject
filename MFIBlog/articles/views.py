from django.shortcuts import render , HttpResponse , redirect , get_object_or_404 , reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Network , SoC , Forensic , karisik


def index(request):
    networkArticles = Network.objects.all()[:3]
    SoCArticles = SoC.objects.all()[:3]
    forensicArticles = Forensic.objects.all()[:3]
    karisikArticles = karisik.objects.all()[:3]
    return render(request , "index.html" , {"networkArticles" : networkArticles , "SoCArticles" : SoCArticles ,
     "forensicArticles" : forensicArticles , "karisikArticles" : karisikArticles})



def networkArticles(request):
    keyword = request.GET.get("keyword")
    articles = Network.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(articles, 8)
    try:
        networkArticles = paginator.page(page)
    except PageNotAnInteger:
        networkArticles = paginator.page(1)
    except EmptyPage:
        networkArticles = paginator.page(paginator.num_pages)

    if keyword:
        networkArticles = Network.objects.filter(title__contains = keyword)
    
    return render(request , "networkArticles.html" , {"networkArticles" : networkArticles})



def SoCArticles(request):
    keyword = request.GET.get("keyword")
    articles = SoC.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(articles, 8)
    try:
        SoCArticles = paginator.page(page)
    except PageNotAnInteger:
        SoCArticles = paginator.page(1)
    except EmptyPage:
        SoCArticles = paginator.page(paginator.num_pages)


    if keyword:
        SoCArticles = SoC.objects.filter(title__contains = keyword)

    return render(request , "SoCArticles.html" , {"SoCArticles" : SoCArticles})




def forensicArticles(request):
    keyword = request.GET.get("keyword")
    articles = Forensic.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(articles, 8)
    try:
        forensicArticles = paginator.page(page)
    except PageNotAnInteger:
        forensicArticles = paginator.page(1)
    except EmptyPage:
        forensicArticles = paginator.page(paginator.num_pages)


    if keyword:
        forensicArticles = Forensic.objects.filter(title__contains = keyword)

    return render(request , "forensicArticles.html" , {"forensicArticles" : forensicArticles})



def karisikArticles(request):

    articles = karisik.objects.all()
    keyword = request.GET.get("keyword")

    page = request.GET.get('page')
    paginator = Paginator(articles, 8)
    try:
        karisikArticles = paginator.page(page)
    except PageNotAnInteger:
        karisikArticles = paginator.page(1)
    except EmptyPage:
        karisikArticles = paginator.page(paginator.num_pages)

    if keyword:
        karisikArticles = karisik.objects.filter(title__contains = keyword)

    return render(request , "karisikArticles.html" , {"karisikArticles" : karisikArticles})




def networkDetail(request , id):
    detail = get_object_or_404(Network , id = id)
    networkArticles = Network.objects.all()[:2]
    SoCArticles = SoC.objects.all()[:2]
    forensicArticles = Forensic.objects.all()[:2]
    karisikArticles = karisik.objects.all()[:2]
    return render(request , "detail.html" , {"detail" : detail , "networkArticles" : networkArticles , "SoCArticles" : SoCArticles ,
     "forensicArticles" : forensicArticles , "karisikArticles" : karisikArticles})

def SoCDetail(request , id):
    detail = get_object_or_404(SoC , id = id)
    networkArticles = Network.objects.all()[:2]
    SoCArticles = SoC.objects.all()[:2]
    forensicArticles = Forensic.objects.all()[:2]
    karisikArticles = karisik.objects.all()[:2]
    return render(request , "detail.html" , {"detail" : detail , "networkArticles" : networkArticles , "SoCArticles" : SoCArticles ,
     "forensicArticles" : forensicArticles , "karisikArticles" : karisikArticles})

def forensicDetail(request , id):
    detail = get_object_or_404(Forensic , id = id)
    networkArticles = Network.objects.all()[:2]
    SoCArticles = SoC.objects.all()[:2]
    forensicArticles = Forensic.objects.all()[:2]
    karisikArticles = karisik.objects.all()[:2]
    return render(request , "detail.html" , {"detail" : detail , "networkArticles" : networkArticles , "SoCArticles" : SoCArticles ,
     "forensicArticles" : forensicArticles , "karisikArticles" : karisikArticles})

def karisikDetail(request , id):
    detail = get_object_or_404(karisik , id = id)
    networkArticles = Network.objects.all()[:2]
    SoCArticles = SoC.objects.all()[:2]
    forensicArticles = Forensic.objects.all()[:2]
    karisikArticles = karisik.objects.all()[:2]
    return render(request , "detail.html" , {"detail" : detail , "networkArticles" : networkArticles , "SoCArticles" : SoCArticles ,
     "forensicArticles" : forensicArticles , "karisikArticles" : karisikArticles})

     