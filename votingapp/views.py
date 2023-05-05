from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
arr = ["JavaScript", "React", "Python", "PHP", "Angular", "SQL", "Java"]
langcount = dict()

def index(request):
    print(arr) # debug statement
    mydict = {"arr": arr}
    return render(request, "index.html", context=mydict)


def getquery(request):
    q = request.GET["language"]
    if q in langcount:
        langcount[q] = langcount[q] +1
    else:
        langcount[q] = 1
    mydict={
        "arr":arr,
        "langcount":langcount
    }
    return render(request, "index.html", context=mydict)

def sortdata(request):
    global langcount
    langcount = dict(sorted(langcount.items(), key = lambda x:x[0], reverse = True))
    mydict = {
        "arr": arr,
        "langcount": langcount,

    }
    return render(request, "index.html", context = mydict)