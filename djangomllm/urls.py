from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views  # Ensure you have this line if you are using a custom view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('set_language/', views.set_language, name='set_language'),  # Custom language set view
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    prefix_default_language=False,
)
