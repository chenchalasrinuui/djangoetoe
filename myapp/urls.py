from django.urls import path
from . import views
urlpatterns = [
    path('get/',views.f1)
    # path('reg-std/', views.regStudent),
    # path('update-std/', views.updateStudent),
    # path('delete-std/', views.delStudent),
    # path('get-std/', views.getStudents),
]