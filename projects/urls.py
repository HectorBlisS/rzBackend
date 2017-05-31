from django.conf.urls import url, include
from rest_framework import routers
from .views import ProjectViewSet, PaginatedListView

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
	url(r'^perro/', PaginatedListView.as_view()),
	# url(r'^', include(router.urls))
]
# urlpatterns = router.urls