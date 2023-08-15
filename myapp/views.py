from django.shortcuts import render,HttpResponseRedirect
from .mangasearch import get_mdetails
from .mangadetails import get_minfo
from .mangaimages import get_chapter_link
from django.http import JsonResponse

# Create your views here.

def showresults(request, para):
    # print(para)
    result=get_mdetails(str(para))
    # print(result)
    response=JsonResponse(result,status=200)
    # data={"result1":result}
    # return render(request, 'index.html', {'mangaresult' : data})
    return response

def showinfo(request, para):
    #print(para)
    result=get_minfo(str(para))
    #print(result)
    response=JsonResponse(result,status=200)
    # data={"result1":result}
    # return render(request, 'index.html', {'mangaresult' : data})
    return response


def showlink(request, para,para2):
    #print(para)
    result=get_chapter_link(str(para),str(para2))
    #print(result)
    response=JsonResponse(result,status=200)
    # data={"result1":result}
    # return render(request, 'index.html', {'mangaresult' : data})
    return response

