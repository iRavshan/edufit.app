from django.shortcuts import render
from .models import JobCategory, JobSubcategory

def Jobs(request):
    categories = []
    jobs = JobCategory.objects.all()

    for job in jobs:
        subcategories = JobSubcategory.objects.filter(id=job.id)
        categories.append({
            'id': job.id,
            'name': job.name,
            'subcategories': subcategories
        })
    context = {
        "jobs": categories
    }
    return render(request, 'job/jobs.html', context)

