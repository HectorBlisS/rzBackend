from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as restUrls
from projects import urls as projectsUrls
from rest_framework import routers
from projects.views import ProjectViewSet, PaginatedListView
from accounts.views import ProfileViewSet, UserViewSet
from projects.views import RewardViewSet, DetailProjectView



router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'rewards', RewardViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(restUrls)),
    url(r'^list/$', PaginatedListView.as_view()),
    url(r'^list/(?P<pk>\d+)/$', 
    	DetailProjectView.as_view()),
    

    url(r'^', include(router.urls))
]
