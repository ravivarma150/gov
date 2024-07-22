
from django.urls import path
from new import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name="user_login"),
    path('help/',views.help,name='help'),
    path('feedback/',views.feedback,name='feedback'),
    path('schems/',views.schems,name="schemes")

]
