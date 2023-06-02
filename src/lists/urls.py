from django.urls import path

from .views import (
	ListListView,
	ListDetailView,
	ListUpdateView,
	ListDeleteView,
	ListCreateView,
	ListSortView,
    
	TaskToggleDoneView,
    
	ToggleHideFinishedTasksView,
)

urlpatterns = [
	path("<int:pk>/", ListDetailView.as_view(), name="list_detail"),
	path("<int:pk>/edit/", ListUpdateView.as_view(), name="list_edit"),
	path("<int:pk>/delete/", ListDeleteView.as_view(), name="list_delete"),
	path("new/", ListCreateView.as_view(), name="list_new"),
    path("<int:pk>/sort/", ListSortView.as_view(), name="list_sort"),
    
	path("task_toggle_done/<int:task_id>/", TaskToggleDoneView.as_view(), name="task_toggle_done"),
    
	path("frontend-options/toggle-hide-finished-tasks/", ToggleHideFinishedTasksView.as_view(), name="toggle_hide_finished_tasks"),
    
	path("", ListListView.as_view(), name="list_list"),
]