from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('new_candidate/',views.createCandidate,name='new_candidate'),
    path('<str:pk>/accept',views.AcceptProfile,name='accept_profile'),
    path('<str:pk>/accepted',views.RAcceptProfile,name='raccept_profile'),
    path('<str:pk>/reject',views.RejectProfile,name='reject_profile'),
    path('viewprofile/<str:pk>',views.ViewProfile,name='view_profile'),
    path('updateprofile/<str:pk>',views.UpdateCandidate,name='update_candidate'),
    path('deleteprofile/<str:pk>',views.DeleteCandidate,name='delete_candidate'),
    path('rejectedprofile/',views.RejectedProfile,name='rejected_profile'),
    path('reviewdelete/',views.ReviewDelete,name='review_delete'),
    path('createproject/<str:pk>/',views.CreateProject,name='create-project'),
    path('updateproject/<str:pk>/',views.UpdateProject,name='update-project'), 
    path('deleteproject/<str:pk>/',views.DeleteProject,name='delete-project'), 
    path('createskill/<str:pk>/',views.CreateSkill,name='create-skill'),
    path('updateskill/<str:pk>/',views.UpdateSkill,name='update-skill'), 
    path('deleteskill/<str:pk>/',views.DeleteSkill,name='delete-skill'), 
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
