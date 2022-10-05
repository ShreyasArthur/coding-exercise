from django.urls import path

from yield_data.views import YieldsView


urlpatterns = [
    path("yield", YieldsView.as_view(), name="yield_data"),
]
