"""URLs Configuration for task_manager app."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),
    # path('', RedirectView.as_view(url='tasks/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)