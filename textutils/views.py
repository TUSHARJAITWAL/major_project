# I have created this file - Harry video #17
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # titlized = request.POST.get('titlized', 'off')
    # fulllower = request.POST.get('fulllower', 'off')
    # charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'data_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'data_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'data_text': analyzed}
        # djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'data_text': analyzed}
   
    # if (titlized == "on"):
    #     analyzed = ""
    #     analyzed = analyzed + djtext.title()
    #     params = {'purpose': 'Removed NewLines', 'data_text': analyzed}

    # if (fulllower == "on"):
    #     analyzed = ""
    #     analyzed = analyzed + djtext.lower()
    #     params = {'purpose': 'Removed NewLines', 'data_text': analyzed}

    # # if (center == "on"):
    # #     analyzed = ""
    # #     analyzed = analyzed + djtext.center()
    # #     params = {'purpose': 'Removed NewLines', 'data_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and fullcaps!="on" and extraspaceremover!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


