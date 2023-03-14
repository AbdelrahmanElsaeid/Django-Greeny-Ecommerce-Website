from .models import Company



def get_company(request):
    data = Company.objects.last()
    return {'company': data}