from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView

from products.models import ProductModel, CategoryModel


def home_page(request):
    return render(request, 'index.html', {})


# icontains = Pr
# contains = Product2
# def shop_page(request):
#     # products = ProductModel.objects.all().filter(user__icontains = 'buy')
#     # products = ProductModel.objects.all().order_by('-created_at')
#     products = ProductModel.objects.all()
#     return render(request, 'shop.html', {'products': products})

# class ShopPage(TemplateView):
#     template_name = 'shop.html'


# def get_queryset(self):
#         qs = ProductModel.objects.order_by('-pk')
#
#         q = self.request.GET.get('q')
#         category = self.request.GET.get('category')
#         brand = self.request.GET.get('brand')
#         tag = self.request.GET.get('tag')
#         sort = self.request.GET.get('sort')
#         price = self.request.GET.get('price')
#
#         if q:
#             qs = qs.filter(title__icontains=q)
#
#         if category:
#             qs = qs.filter(category_id=category)
#
#         if brand:
#             qs = qs.filter(brand_id=brand)
#
#         if tag:
#             qs = qs.filter(tags__id=tag)
#
#         if price:
#             price_from, price_to = price.split(';')
#             qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)
#
#         if sort:
#             if sort == 'price':
#                 qs = qs.order_by('real_price')
#             elif sort == '-price':
#                 qs = qs.order_by('-real_price')
#
#         return qs

class ShopPage(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        return context
@login_required
def add_to_favorite(request, product_id):
    print(request)
    product = get_object_or_404(ProductModel, pk=product_id)
    user = request.user

    print(user)
    print(user.favorite_products.all())
    if product in user.favorite_products.all():
        user.favorite_products.remove(product)
    else:
        user.favorite_products.add(product)

    return redirect('shop')


class ShopPageDetail(DetailView):
    template_name = 'shop-details.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'




class RegisterView(TemplateView):
    template_name = 'signup.html'


class LoginView(TemplateView):
    template_name = 'login.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

# def test(request):
#     products = ProductModel.objects.all()
#     return render(request, 'index.html', {'products': products})
