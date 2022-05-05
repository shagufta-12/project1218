from .views import RegisterAPI, LoginAPI, ChangePasswordView
from knox import views as knox_views
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='Login'),
    path('api/Logout/', knox_views.LogoutView.as_view(), name='Logout'),
    path('api/Logoutall/', knox_views.LogoutAllView.as_view(), name='Logoutall'),
    path('api/Change-password/', ChangePasswordView.as_view(), name='Change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

   path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

