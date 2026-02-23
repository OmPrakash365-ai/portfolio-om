from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


# 📄 Project List
def project_list(request):
    query = request.GET.get('q')
    tech = request.GET.get('tech')

    projects = Project.objects.all().order_by('-created_date')

    if query:
        projects = projects.filter(title__icontains=query)

    if tech:
        projects = projects.filter(tech_stack__icontains=tech)

    return render(request, 'projects/project_list.html', {'projects': projects})



# 🔍 Project Detail
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})


# ➕ Create Project (Admin only)
def project_create(request):

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)   # FIX IMAGE

        if form.is_valid():
            form.save()
            return redirect('dashboard')   # or project_list

    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {'form': form})


   
def project_update(request, slug):

    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)  # 🔥 FIX IMAGE

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {'form': form})





def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        project.delete()
        return redirect('dashboard')

    return render(request, 'projects/project_confirm_delete.html', {'project': project})
