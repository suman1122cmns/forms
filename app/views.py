from urllib import request
from django.shortcuts import render

# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        #print(request.POST)
        #TN=request.POST['topic']
        TN=request.POST.get('topic')
        print(TN)
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        return HttpResponse('Topic data is inserted Successfully')
    return render(request,'insert_topic.html')