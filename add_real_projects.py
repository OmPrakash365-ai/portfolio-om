#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from projects_app.models import Project

def add_real_projects():
    """
    Add your REAL projects here!
    Replace the sample data below with your actual projects.
    """

    # Example format - replace with your real projects
    real_projects = [
        {
            "title": "Portfolio Website",
            "description": "A personal portfolio website showcasing projects, education, skills, achievements, and internship experiences. Built with Django framework, featuring project management, contact forms, and a clean responsive design.",
            "tech_stack": "Python, Django, PostgreSQL, HTML, CSS, JavaScript",
            "github_link": "https://github.com/OmPrakash365-ai/portfolio_site",
            "live_demo": "https://your-portfolio.com",
        },
        {
            "title": "Automated Time Table",
            "description": "An intelligent timetable management system that automates scheduling and resource allocation. Helps in organizing classes, exams, and events with conflict detection and optimization features.",
            "tech_stack": "Python, Django, PostgreSQL",
            "github_link": "https://github.com/OmPrakash365-ai/portfolio_site",
            "live_demo": "https://your-timetable.com",
        },
        # Add more projects as needed...
    ]

    print("Adding your real projects...")

    for project_data in real_projects:
        try:
            Project.objects.create(**project_data)
            print(f"✅ Added: {project_data['title']}")
        except Exception as e:
            print(f"❌ Error adding {project_data['title']}: {e}")

    total_projects = Project.objects.count()
    print(f"\n🎉 Successfully added {len(real_projects)} projects!")
    print(f"Total projects in database: {total_projects}")

if __name__ == "__main__":
    add_real_projects()