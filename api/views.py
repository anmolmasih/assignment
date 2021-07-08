from django.shortcuts import render
from stackapi import StackAPI
# Create your views here.
def questions(request):
    if "GET" == request.method:
        return render(request, '../templates/index.html', {})
    else:
        que =str(request.POST.get("question"))
        #print("print question")
        #print(que)
        title_search_string=str(que)
        SITE = StackAPI('stackoverflow')
        #SITE.max_pages=1
        comments = SITE.fetch('search/advanced', title=title_search_string)
        #print(comments['items'])
        #print(type(comments))
        return render(request,'index.html',{"result":comments['items']})
    return render(request, '../templates/index.html', {"message":"Please upload right file format or download template"})