from django.views.static import serve
from django.conf import settings


from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as restUrls
from projects import urls as projectsUrls
from rest_framework import routers
from projects.views import ProjectViewSet, PaginatedListView
from accounts.views import ProfileViewSet, UserViewSet, GetMyProfile


from projects.views import RewardViewSet, DetailProjectView, PreviewDetailProjectView, UserProjects, ObservationsViewSet, UpdatesViewSet, UserUpdates, follow_project, FollowedProjects, CategoryList, MobileProjectViewSet

from payments.views import ExecutePay, DonacionViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'rewards', RewardViewSet)
router.register(r'users', UserViewSet)
router.register(r'observations', ObservationsViewSet)
router.register(r'updates', UpdatesViewSet)
router.register(r'donaciones', DonacionViewSet)
router.register(r'mobileprojects', MobileProjectViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(restUrls)),
    url(r'^list/$', PaginatedListView.as_view()),
    url(r'^list/(?P<pk>\d+)/$', 
    	DetailProjectView.as_view()),
    url(r'^profile/$',
    	GetMyProfile.as_view()),
    url(r'^preview/(?P<pk>\d+)/$', 
        PreviewDetailProjectView.as_view()),

    url(r'^userprojects/(?P<pk>\d+)/$', UserProjects.as_view()),
    url(r'^userupdates/$', UserUpdates.as_view()),
    url(r'^followedprojects/$', FollowedProjects.as_view()),
    url(r'^pay/$', ExecutePay.as_view() ),
    url(r'^follow/$', follow_project),
    url(r'^categorias/$', CategoryList.as_view()),


    

    url(r'^', include(router.urls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),
]
