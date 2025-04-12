from django.urls import path
from . import views

urlpatterns = [
    path('', views.CashFlowListView.as_view(), name='cashflow_list'),
    path('create/', views.CashFlowCreateView.as_view(), name='cashflow_create'),
    path('<int:pk>/edit/', views.CashFlowUpdateView.as_view(), name='cashflow_edit'),
    path('<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    path('types/', views.TypeListView.as_view(), name='type_list'),
    path('types/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('types/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('types/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('subcategories/', views.SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategories/create/', views.SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategories/<int:pk>/edit/', views.SubCategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategories/<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='subcategory_delete'),
    path('api/categories/', views.get_categories, name='get_categories'),
    path('api/subcategories/', views.get_subcategories, name='get_subcategories'),
]