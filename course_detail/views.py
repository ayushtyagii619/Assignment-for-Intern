from django.shortcuts import render
from django.conf import settings
import os
import json

def course_detail(request, course_id):
    file_path = os.path.join(settings.BASE_DIR, 'D:\Django\LueinAnalytics Assignment\get_course_detail_API_response.json')
    
    # Load JSON data
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Check if the course_id matches the provided course_id
    course_id = data['course_id']
    filters = data['videos']
    

    '''context = {
        'filters': filters,
        'course_id': course_id  # Pass the course_id to the template if needed
    }'''

    selected_video = filters[0]
    if 'video_id' in request.GET:
        selected_video = next((video for video in filters if video['video_id'] == request.GET['video_id']), filters[0])

    context = {
        'course_id': course_id,
        'filters': filters,
        'selected_video': selected_video
    }
    
    return render(request, 'course_detail.html', context)
