from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1-ката оңдолду: "nomespace" эмес, "namespace" болушу керек
    path('cart/', include('cart.urls', namespace='cart')),
    
    # 2-ката түшүндүрмөсү төмөндө: "main.urls" файлын камтуу
    path('', include(('main.urls', 'main'), namespace='main')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
