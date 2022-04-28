from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator


class Index(View):
	def post(self , request):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity <= 1:
						cart.pop(product)
					else:
						cart[product] = quantity-1
				else:
					cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		request.session['cart'] = cart
		print('cart' , request.session['cart'])
		return redirect('homepage')


	def get(self , request):
		return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
	search = request.GET.get('search')
	categories = Category.get_all_categories()
	if search is None:
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		products = None
		
		categoryID = request.GET.get('category')
		if categoryID:
			products = Product.get_all_products_by_categoryId(categoryID).order_by('-id')
		else:
			products = Product.get_all_products().order_by('-id')

		paginator = Paginator(products, 9)
		page = request.GET.get('page')
		products_pagination = paginator.get_page(page)
		nums = 'a' * products_pagination.paginator.num_pages

		data = {}
		data['products'] = products_pagination
		data['nums'] = nums
		data['categories'] = categories

		print('you are : ', request.session.get('email'))
		return render(request, 'index.html', data)
	else:
		products = Product.objects.filter(
			Q(name__contains=search)
		)
		data = {}
		data['products'] = products
		data['categories'] = categories
		data['search'] = search

		return render(request, 'index.html', data)
		