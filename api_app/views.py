from django.http import HttpResponse

def project_list_api(request):
    return HttpResponse("API working")

def project_detail_api(request, slug):
    return HttpResponse(f"Project detail {slug}")

def project_create_api(request):
    return HttpResponse("Create project")