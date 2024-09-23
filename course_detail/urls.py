from django.urls import path,include
from .views import course_detail
urlpatterns = [
    
    path('<int:course_id>/',course_detail,name='course-detail'),
]