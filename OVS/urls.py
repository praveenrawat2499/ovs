from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from voting import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('changepass/', views.changepass, name='changepass'),
    path('position/', views.position, name='position'),
    path('result/', views.result, name='result'),
    # path('candidate/detail/<int:id>/', views.candidate_detail, name='detail'),	
    # path('candidate/<int:pos>/', views.candidate, name='candidate'),	
    	
    path('candidate/<int:pk_position>/', views.candidate, name='candidate'),
    path('candidate/detail/<int:pk_candidate>/', views.candidate_detail, name='detail'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

admin.site.site_header = "University Students Association Voting System"
admin.site.index_title = "Welcome to University Students Association Voting System admin panel"
admin.site.site_title = "OVS"
