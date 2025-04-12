from django.urls import path
from . import views

urlpatterns = [
    path('', views.CashFlowListView.as_view(), name='cashflow_list'),
    path('create/', views.CashFlowCreateView.as_view(), name='cashflow_create'),
    path('<int:pk>/edit/', views.CashFlowUpdateView.as_view(), name='cashflow_edit'),
    path('<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/subcategories/', views.get_subcategories, name='get_subcategories'),
]