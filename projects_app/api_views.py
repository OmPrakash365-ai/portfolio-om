from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer


# GET ALL PROJECTS
@api_view(['GET'])
def project_list_api(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# GET SINGLE PROJECT
@api_view(['GET'])
def project_detail_api(request, slug):
    project = Project.objects.get(slug=slug)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


# CREATE PROJECT (AUTH REQUIRED)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_create_api(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)