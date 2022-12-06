from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.routers import SimpleRouter


app_name = 'api'

router = SimpleRouter()

router.register('tags', views.TagsViewSet, basename='tags')
router.register('ingredients', views.IngredientsViewSet, basename='ingredients')
#router.register(
#    r'titles/(?P<title_id>[\d]+)/reviews',
#    views.IngredientsViewSet,
#    basename='reviews'
#)


#auth_patterns = [
#    path('auth/signup/', UserCreateViewSet.as_view()),
#    path('auth/token/', get_token_view),
# ]

urlpatterns = [
    # path('', include(auth_patterns)),
    path('', include(router.urls)),
]
