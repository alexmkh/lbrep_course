"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from listings.api import views as listing_api_views
from users.api import views as user_api_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path(
            "api/listings/",
            listing_api_views.ListingList.as_view(),
            name="listing-list",
        ),
        path(
            "api/listings/create/",
            listing_api_views.ListingViewSet.as_view({"get": "list", "post": "create"}),
            name="listing-create",
        ),
        path(
            "api/listings/<int:pk>/",
            listing_api_views.ListingDetail.as_view(),
            name="listing-create",
        ),
        path(
            "api/listings/<int:pk>/delete/",
            listing_api_views.ListingDelete.as_view(),
            name="listing-create",
        ),
        path(
            "api/profiles/",
            user_api_views.ProfileList.as_view(),
            name="profile-list",
        ),
        path(
            "api/profiles/<int:seller>/",
            user_api_views.ProfileDetail.as_view(),
            name="profile-detail",
        ),
        path(
            "api/profiles/<int:seller>/update/",
            user_api_views.ProfileUpdate.as_view(),
            name="profile-detail",
        ),
        path("api-auth-djoser/", include("djoser.urls")),
        path("api-auth-djoser/", include("djoser.urls.authtoken")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
