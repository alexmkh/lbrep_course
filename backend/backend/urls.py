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

# DRF-YASG Documentation Code Snippet (In Project urls.py)
# drf-yasg imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Location-Based Real Estate Website Backend APIs",
        default_version="v1",
        description="This is the API documentation for Location-Based Real Estate Website project APIs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alexmkh33@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

borough_list = listing_api_views.BoroughViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
borough_detail = listing_api_views.BoroughViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

border_list = listing_api_views.BoroughBorderViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
border_detail = listing_api_views.BoroughBorderViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path(
            "",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
        # Listings URLs
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
            name="listing-delete",
        ),
        path(
            "api/listings/<int:pk>/update/",
            listing_api_views.ListingUpdate.as_view(),
            name="listing-delete",
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
        # User registration and authentication
        path("api-auth-djoser/", include("djoser.urls")),
        path("api-auth-djoser/", include("djoser.urls.authtoken")),
        # Area list
        path("api/areas/", listing_api_views.AreaList.as_view(), name="area-list"),
        # Borough list and create
        path(
            "api/boroughs/",
            listing_api_views.BoroughList.as_view(),
            name="borough-list",
        ),
        path(
            "api/boroughs/<int:id>/",
            listing_api_views.BoroughDetail.as_view(),
            name="borough-detail",
        ),
        path(
            "api/boroughs/create/",
            listing_api_views.BoroughCreate.as_view(),
            name="borough-create",
        ),
        path(
            "api/boroughs/delete_all/",
            listing_api_views.BoroughDeleteAllView.as_view(),
            name="borough-delete-all",
        ),
        # path("boroughs/", borough_list, name="borough-list"),
        # path("boroughs/<int:pk>/", borough_detail, name="borough-detail"),
        path("api/boroughborders/", border_list, name="boroughborder-list"),
        path(
            "api/boroughborders/<int:pk>/", border_detail, name="boroughborder-detail"
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
