from django.urls import path

from .views import (
	ListListView,
	ListDetailView,
	ListUpdateView,
	ListDeleteView,
	ListCreateView,
)

urlpatterns = [
	path("<int:pk>/", ListDetailView.as_view(), name="list_detail"),
	path("<int:pk>/edit/", ListUpdateView.as_view(), name="list_edit"),
	path("<int:pk>/delete/", ListDeleteView.as_view(), name="list_delete"),
	path("new/", ListCreateView.as_view(), name="list_new"),
	path("", ListListView.as_view(), name="list_list"),
]