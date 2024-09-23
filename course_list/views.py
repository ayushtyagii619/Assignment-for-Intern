from django.shortcuts import render
import json
import os
from django.conf import settings
from django.http import JsonResponse

def course_list(request):
    file_path  = os.path.join(settings.BASE_DIR,'D:\Django\LueinAnalytics Assignment\get_all_courses_API_response.json')
    with open(file_path,'r') as f:
        data  = json.load(f)
        courses = data['courses']
    filters = data['facets']  # Use filters for facets (course language, subject, etc.)

    # Return JSON response for API testing
    context = {
        'courses': courses,
        'filters': filters
    }
    
    return render(request, 'course_list.html', context)
# Create your views here.
