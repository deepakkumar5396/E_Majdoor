from django.contrib import admin
from django.urls import path
#from job.views import *
from job.views import*
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
   #path('admin/', admin.site.urls),
   # path('',include('emajdoor.urls')),
   path('',index,name='index'),
   path('admin_login',admin_login,name='admin_login'),
   path('user_login',user_login,name='user_login'),
   path('recruiter_login',recruiter_login,name='recruiter_login'),
   path('user_signup',user_signup,name='user_signup'),
   path('user_home', user_home, name='user_home'),
   path('Logout', Logout, name='Logout'),
   path('view_users',view_users,name='view_users'),
   path('recruiter_signup',recruiter_signup,name='recruiter_signup'),
   path('recruiter_home', recruiter_home, name='recruiter_home'),
   path('recruiter_pending',recruiter_pending,name='recruiter_pending'),
   path('admin_home', admin_home, name='admin_home'),
   path('delete_user/<int:pid>',delete_user , name='delete_user'),
   path('change_status/<int:pid>',change_status , name='change_status'),
   path('recruiter_accepted',recruiter_accepted, name='recruiter_accepted'),
   path('recruiter_rejected',recruiter_rejected, name='recruiter_rejected'),
   path('recruiter_all',recruiter_all, name='recruiter_all'),
   path('delete_recruiter/<int:pid>',delete_recruiter , name='delete_recruiter'),
   path('change_passwordadmin',change_passwordadmin , name='change_passwordadmin'),
   path('change_passworduser',change_passworduser, name='change_passworduser'),
   path('change_passwordrecruiter',change_passwordrecruiter, name='change_passwordrecruiter'),
   path('add_job',add_job, name='add_job'),
   path('job_list',job_list, name='job_list'),
   path('edit_jobdetail/<int:pid>',edit_jobdetail, name='edit_jobdetail'),
   path('change_companylogo/<int:pid>',change_companylogo, name='change_companylogo'),
   path('latest_job',latest_job, name='latest_job'),
   path('latest_userjob',latest_userjob, name='latest_userjob'),
   path('apply_job', apply_job, name='apply_job'),
   #migrent worker link
   path('migrentuser_signup',migrentuser_signup,name='migrentuser_signup'),
   path('migrentuser_login',migrentuser_login,name='migrentuser_login'),


]