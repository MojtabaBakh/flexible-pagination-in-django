from django.shortcuts import render
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from .models import Student



def paginationview(request):
    students=Student.objects.all()

    page=request.GET.get('page' , 1)
    perpage=request.GET.get('per_page' , 3)
    
    if (perpage =='all') :
        paginator=Paginator( students , students.count())
    else :
        paginator=Paginator( students , perpage )
    result = paginator.page(page)
    try :
        result = paginator.page(page)
        
    except PageNotAnInteger :
            
        result = paginator.page(1)
        
    except EmptyPage :
        
        result = paginator.page(paginator.num_pages)
        
    except :
        
        result = paginator.page(1)
        perpage = "3"
        
        
    contex={
        'result' : result ,
        'perpage' : perpage
    }
    
    
    return render(request , 'univercity/index.html' , contex)    



# Create your views here.
