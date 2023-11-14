from django.shortcuts import render

def board(request):
    if request.method == "GET":
        context = {
            "title":"안녕 14강 실습"
        }
        return render(request, 'page/index.html', context=context)