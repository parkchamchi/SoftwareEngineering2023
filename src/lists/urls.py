from django.urls import path

from .views import (
	ListListView,
	ListDetailView,
	ListUpdateView,
	ListDeleteView,
	ListCreateView,
	ListSortView,
	
	TaskUpdateView,
	TaskDeleteView,
	TaskToggleDoneView,
	
	ToggleHideFinishedTasksView,
)

urlpatterns = [
	path("<int:pk>/", ListDetailView.as_view(), name="list_detail"),
	path("<int:pk>/edit/", ListUpdateView.as_view(), name="list_edit"),
	path("<int:pk>/delete/", ListDeleteView.as_view(), name="list_delete"),
	path("new/", ListCreateView.as_view(), name="list_new"),
	path("<int:pk>/sort/", ListSortView.as_view(), name="list_sort"),
	
	path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit"),
	path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
	path("task/<int:task_id>/toggle_done/", TaskToggleDoneView.as_view(), name="task_toggle_done"),
	
	path("frontend-options/toggle-hide-finished-tasks/", ToggleHideFinishedTasksView.as_view(), name="toggle_hide_finished_tasks"),
	
	path("", ListListView.as_view(), name="list_list"),
]