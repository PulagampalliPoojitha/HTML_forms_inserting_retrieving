from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST.get('na')
        ur=request.POST['ur']

        TO=Topic.objects.get(topic_name=tn)
        WO=webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        return HttpResponse('Webpage is Created')


    return render(request,'insert_webpage.html',d)

def insert_AcessRecord(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        na=request.POST['na']
        da=request.POST.get('da')
        ar=request.POST['ar']

        WO=webpage.objects.get(name=na)
        AO=AcessRecord.objects.get_or_create(name=WO,date=da,author=ar)[0]
        AO.save()
        return HttpResponse('Acessrecord is Created')
    return render(request,'insert_AcessRecord.html',d)


def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=webpage.objects.none()

        for i in  MSTS:
            RWOS=RWOS|webpage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpage.html',d1)


    return render(request,'retrieve_webpage.html',d)

def retrieve_AcessRecord(request):
    LWO=webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        LMWO=request.POST.getlist('access')
        print(LMWO)
        MWO=AcessRecord.objects.none()
          
        for i in  LMWO:
            MWO=MWO|AcessRecord.objects.filter(id=i) 
        d1={'MWO':MWO}
        return render(request,'display_AcessRecord.html',d1)

    return render(request,'retrieve_AcessRecord.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    return render(request,'checkbox.html',d)






















