from django.http import HttpResponse
from django.shortcuts import render
import string
#-----------------------------------------------------
def removepunch(request):
    punch=request.GET.get('punch','off')
    djtext=request.GET.get('text')
    list_punch=string.punctuation
    if punch=='on':
        for i in djtext:
            if i  not in list_punch:
                analyzetext+=i
        
        dictionary={"purpose":'remove punch','analyze':analyzetext} 
        if analyzetext==djtext:
            return HttpResponse('NO punctionation sin the given string')
        return render(request,'analyze.html',dictionary)
    else:
        return HttpResponse('error')

def uppercase(request):
    up=request.GET.get('uppercase','off')
    djtext=request.GET.get('text')
    analyzetext=''
    if up=='on':
        analyzetext=djtext.upper()
        dictionary={"purpose":'Uppercase conversion','analyze':analyzetext}
        return render(request,'analyze.html',dictionary)
    else:
        HttpResponse('error')


#-------------------------------------------------------------------------------
# Create your views here.
def text(request):
    return render(request,'uttext.html')
def analyze(request):
    punch=request.GET.get('punch','off')
    up=request.GET.get('uppercase','off')
    nw=request.GET.get('newline','off')
    extraspace=request.GET.get('extra','off')
    counter=request.GET.get('counter','off')

    djtext=request.GET.get('text')
    list_punch=string.punctuation

    analyzetext=''

    if punch=='on':
        for i in djtext:
            if i  not in list_punch:
                analyzetext+=i
       
        dictionary={"purpose":'remove punch','analyze':analyzetext} 
        if analyzetext==djtext:
            return HttpResponse('NO punctionation sin the given string')
        djtext=analyzetext
        #return render(request,'analyze.html',dictionary)
    if up=='on':
        analyzetext=djtext.upper()
        dictionary={"purpose":'Uppercase conversion','analyze':analyzetext}
        #return render(request,'analyze.html',dictionary)
        djtext=analyzetext
    
    if extraspace=='on':
        analyzetext=djtext.strip()
        dictionary={"purpose":'Extra space','analyze':analyzetext}
        #return render(request,'analyze.html',dictionary)
        djtext=analyzetext
    if counter=='on':
        analyzetext=0
        for i in djtext:
            analyzetext+=1
        dictionary={"purpose":'counter','analyze':analyzetext}
        #return render(request,'analyze.html',dictionary)
        
    if(punch!='on' and up!='on'and extraspace!='on' and counter!='on'):
        return HttpResponse("error")
        
    return render(request,'analyze.html',dictionary)
    
    


