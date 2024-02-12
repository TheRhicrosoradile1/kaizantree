 
from django.urls import path ,include
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework import routers
from apis import views 
  
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [ 
    path('items/<int:pk>', views.ItemDetail.as_view()), 
    path('items/list/', views.ItemList.as_view()), 
    path('categories/list/', views.CategoryList.as_view()), 
    path('categories/<int:pk>', views.CategoryDetail.as_view()), 
    path('', include(router.urls)),
    path('items/filter/', views.FilterItems.as_view(), name='item-filter'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 
urlpatterns += router.urls
  
# urlpatterns = format_suffix_patterns(urlpatterns)