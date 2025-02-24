from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('tasks/', include('tasks.urls')),
    # path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)