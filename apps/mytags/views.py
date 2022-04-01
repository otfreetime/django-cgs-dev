from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    html = """
            <script>
                document.write('<h1>Hello world!</h1>');
            </script>
           """
    context = {'hello':html}
    return render(request,'mytags/index.html',context)

# def index(request):
#     return HttpResponse('Hellow World!')