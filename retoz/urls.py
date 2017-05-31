from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as restUrls
from projects import urls as projectsUrls
from rest_framework import routers
from projects.views import ProjectViewSet, PaginatedListView


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(restUrls)),
    url(r'^perro/', PaginatedListView.as_view()),
    
    url(r'^', include(router.urls))
]
