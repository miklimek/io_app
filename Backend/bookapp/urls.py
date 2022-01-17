from django.urls import path, include
from rest_framework_nested import routers
from .views import BookViewSet, OpinionViewSet, UserViewSet, GenreViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'opinions', OpinionViewSet)

books_router = routers.NestedSimpleRouter(router, r'books', lookup='book')
books_router.register(r'opinions', OpinionViewSet, basename='book-opinions')

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'opinions', OpinionViewSet, basename='user-opinions')

genres_router = routers.NestedSimpleRouter(router, r'genres', lookup='genre')
genres_router.register(r'books', BookViewSet, basename='genre-book')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
    path('', include(user_router.urls)),
    path('', include(genres_router.urls))
]
