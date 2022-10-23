from django.urls import path
from . import views
urlpatterns = [
    path('reg-std/', views.regStudent),
    path('update-std/', views.updateStudent),
    path('delete-std/', views.delStudent),
    path('get-std/', views.getStudents),
]