from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'number' :100 }
    return render(request,'templateApp/index.html',context_dict)

def other (request):
    return render(request,'templateApp/other.html')

def relative(request):
    return render(request,'templateApp/rel_url_temp.html')

