from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import product.views
import account.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product.views.home, name = 'home'),
    path('accounts/', include('account.urls')),
]
