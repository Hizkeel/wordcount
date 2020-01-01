#views.py file ....we have created thi file so we can define the funcitons here. in this case we have fedined funcitons like home and about


from django.http import HttpResponse

from django.shortcuts import render # this library is added to direct the page to the html file.

def home(request):
    return render(request, 'home.html') # this will direct to the home.html file we have created in the templates folder. whatever
    # is mentioned in the html file will be shown on the hompage of the server.

def about(request):
    return render(request, 'about.html')


def count(request):
    ft =request.GET["fulltext"]  # the fulltext in inverted commas is from home.html page. whatever we enter in that textbox is requested
    # by the get function and stored in ft
    words= ft.split() # to split the words before counting

    worddictionary ={}
    for word in words:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] =1

    return render(request, 'count.html', {'fulltext': ft, 'count': len(words), 'wordscount': worddictionary.items()})
