from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CashFlow, Status, Type, Category, SubCategory
from .forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse

def get_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category')
    if not category_id or not category_id.isdigit():
        return JsonResponse([], safe=False)
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'dds/cashflow_list.html'
    context_object_name = 'cashflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        type_ = self.request.GET.get('type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')

        if status:
            queryset = queryset.filter(status__name=status)
        if type_:
            queryset = queryset.filter(type__name=type_)
        if category:
            queryset = queryset.filter(category__name=category)
        if subcategory:
            queryset = queryset.filter(subcategory__name=subcategory)
        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'dds/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно создана!")
        return super().form_valid(form)

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'dds/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно обновлена!")
        return super().form_valid(form)

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'dds/cashflow_confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Запись успешно удалена!")
        return super().delete(request, *args, **kwargs)

class StatusListView(ListView):
    model = Status
    template_name = 'dds/status_list.html'

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'dds/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно создан!")
        return super().form_valid(form)

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'dds/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно обновлён!")
        return super().form_valid(form)

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'dds/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Статус успешно удалён!")
        return super().delete(request, *args, **kwargs)
    
class TypeListView(ListView):
    model = Type
    template_name = 'dds/type_list.html'

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'dds/type_form.html'
    success_url = reverse_lazy('type_list')

    def form_valid(self, form):
        messages.success(self.request, "Тип успешно создан!")
        return super().form_valid(form)

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'dds/type_form.html'
    success_url = reverse_lazy('type_list')

    def form_valid(self, form):
        messages.success(self.request, "Тип успешно обновлён!")
        return super().form_valid(form)

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'dds/type_confirm_delete.html'
    success_url = reverse_lazy('type_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Тип успешно удалён!")
        return super().delete(request, *args, **kwargs)

class CategoryListView(ListView):
    model = Category
    template_name = 'dds/category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dds/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, "Категория успешно создана!")
        return super().form_valid(form)

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dds/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, "Категория успешно обновлена!")
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'dds/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Категория успешно удалена!")
        return super().delete(request, *args, **kwargs)

class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'dds/subcategory_list.html'

class SubCategoryCreateView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dds/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, "Подкатегория успешно создана!")
        return super().form_valid(form)

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dds/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')

    def form_valid(self, form):
        messages.success(self.request, "Подкатегория успешно обновлена!")
        return super().form_valid(form)

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'dds/subcategory_confirm_delete.html'
    success_url = reverse_lazy('subcategory_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Подкатегория успешно удалена!")
        return super().delete(request, *args, **kwargs)