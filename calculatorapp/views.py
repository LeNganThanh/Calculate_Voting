from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def submit(request):

    q = request.GET["query"]
    try:
        ans = eval(q) #eval is used for matching values
        mydict = {
            "q":q,
            "ans": ans,
            "error":False,
            "result": True
        }
        return render(request, "index.html", context = mydict)
    except:
        #mydict["error"] = True 
        mydict = {
            "error": True,
            "result": False
        }
        return render(request, "index.html", context = mydict)
   #jsondict = {
    #    "q":q
    #}
    #return JsonResponse(jsondict) # HttpResponse(q) """