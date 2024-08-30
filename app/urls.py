from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from . import views


urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('user/'), include('user.urls')),
    path(_('rating/'), include('rating.urls')),
    path(_('competitions/'), include('competition.urls')),
    path(_('schoolbooks/'), include('schoolbook.urls')),
    path(_('article/'), include('article.urls')),
    path('', views.home, name='home')
)

handler404 = views.error_404
handler500 = views.error_500
handler403 = views.error_403
handler400 = views.error_400

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)