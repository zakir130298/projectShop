from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ShopOnline import settings
from products.views import home_page, ShopPage, ShopPageDetail, RegisterView, LoginView, ProfileView, add_to_favorite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('shop', ShopPage.as_view(), name='shop'),
    path('signup', RegisterView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('shop/<int:pk>', ShopPageDetail.as_view(), name='shop-detail'),
    path('add_to_favorite/<int:product_id>/', add_to_favorite, name='add_to_favorite'),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
