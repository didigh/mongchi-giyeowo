from django.contrib import admin
from django.urls import path, include
import diaryapp.views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', diaryapp.views.create, name='create'),
    path('new/', diaryapp.views.new, name = 'new'),
    path('', diaryapp.views.mains, name='mains'),
    path('<int:diary_id>', diaryapp.views.detail, name = 'detail'),
    path('edit/<int:diary_id>', diaryapp.views.edit, name='edit'),
    path('delete/<int:diary_id>', diaryapp.views.delete, name='delete'),
    path('login/', diaryapp.views.login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('map/', diaryapp.views.map, name='map'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
