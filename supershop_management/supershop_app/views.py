from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import (UserRegistrationForm, UserLoginForm,
                    CategoryForm, CategoryEditForm, ProductForm,
                    ProductEditForm)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum, Count
from django.db.utils import IntegrityError
from . import models
from django.http import JsonResponse
from fpdf import FPDF
import qrcode
import json
import os
from django.conf import settings
from django.http import FileResponse, Http404


# class HomePage(LoginRequiredMixin, View):
#     template_name = "supershop_app/index.html"
#
#     def get(self, request):
#         # paraphrase_class = ParaphraseTool()
#         return render(request, self.template_name, context={'get': 1})
#
#     def post(self, request):
#         return render(request, self.template_name)

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home_page.html',
                  {
                      'is_logged_in': request.user.is_authenticated,
                      'home': 'active'
                  })


@login_required(login_url='/supershop_admin/')
def admin_home(request):
    return render(request, 'admin_home.html',
                  {
                      'is_logged_in': request.user.is_authenticated,
                      "admin": 1,
                      "admin_home": "active"
                  })


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserRegistrationForm()
            return render(request, 'all_forms.html', {'form': form,
                                                      "btn_name": "SignUp",
                                                      "title": "Sign Up",
                                                      "signup": "active"})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, "all_forms.html", context={"form": form,
                                                              "btn_name": "Login",
                                                              "title": "Login",
                                                              "login": "active"})


def logout_view(request):
    logout(request)
    return redirect('login')


def admin_logout_view(request):
    logout(request)
    return redirect('supershop_admin')


def supershop_admin(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    if request.GET.get('next', None):
                        return redirect(request.GET.get('next'))
                    return redirect("admin_home")
                else:
                    messages.error(request, "You are not a superuser")
                    return redirect("supershop_admin")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    elif request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            if request.GET.get('next', None):
                return redirect(request.GET.get('next'))
            return redirect('admin_home')
        else:
            form = UserLoginForm()
            return render(request, "all_forms.html", context={"form": form,
                                                              "btn_name": "Login",
                                                              "title": "Admin Login",
                                                              "admin_login": "active"})


@login_required(login_url='/supershop_admin/')
def admin_category(request):
    if request.method == 'GET':
        return render(request, "admin_category.html",
                      context={'is_logged_in': request.user.is_authenticated,
                               "title": "Category",
                               "admin": 1,
                               "admin_category": "active"
                               })


@login_required(login_url='/supershop_admin/')
def admin_product(request):
    if request.method == 'GET':
        return render(request, "admin_product.html",
                      context={'is_logged_in': request.user.is_authenticated,
                               "title": "Product",
                               "admin": 1,
                               "admin_product": "active"
                               })


@login_required(login_url='/supershop_admin/')
def admin_category_operation(request, ops):
    if request.method == "POST":
        if ops == 'add':
            form = CategoryForm(request.POST)
            if form.is_valid():
                messages.success(request, "Succesfully added.")
                form.save()
            else:
                messages.error(request, "Something Went Wrong.")
            return redirect("/supershop_admin/category/add/")
        elif 'edit' in ops:
            cat_id = ops.split('__')[-1]
            cat = models.ProductCategory.objects.filter(pk=cat_id).first()
            form = CategoryForm(request.POST, instance=cat)
            if form.is_valid():
                form.save()
                messages.success(request, "Succesfully Updated.")
            else:
                messages.error(request, "Something Went Wrong.")
            return redirect("/supershop_admin/category/view/")
        elif 'delete' in ops:
            cat_id = ops.split('__')[-1]
            # return JsonResponse(cat_id, safe=False)
            cat = models.ProductCategory.objects.filter(pk=cat_id).delete()
            return JsonResponse(1, safe=False)

    elif request.method == 'GET':
        if ops == 'add':
            form = CategoryForm()
            return render(request, "all_forms.html",
                          context={'is_logged_in': request.user.is_authenticated,
                                   "form": form,
                                   "title": "Add Category",
                                   "admin": 1,
                                   'logout': request.user.is_authenticated,
                                   "btn_name": "ADD Category",
                                   "admin_category": "active"})
        elif ops == 'view':
            categories = models.ProductCategory.objects.all()
            return render(request, 'view_categories.html',
                          context={
                              'is_logged_in': request.user.is_authenticated,
                              "categories": categories,
                              "title": "View Category",
                              "admin": 1,
                              'logout': request.user.is_authenticated,
                              "admin_category": "active"
                          })
        elif 'edit' in ops:
            cat_id = ops.split('__')[-1]
            cat = models.ProductCategory.objects.filter(pk=cat_id).first()
            form = CategoryEditForm(initial={"category_name": cat.category_name,
                                             "category_code": cat.category_code})
            return render(request, "all_forms.html",
                          context={'is_logged_in': request.user.is_authenticated,
                                   "form": form,
                                   "title": "Edit Category",
                                   "admin": 1,
                                   'logout': request.user.is_authenticated,
                                   "btn_name": "Edit Category",
                                   "admin_category": "active"})
        else:
            return redirect("admin_category")


@login_required(login_url='/supershop_admin/')
def admin_product_operation(request, ops):
    if request.method == "POST":
        if ops == 'add':
            form = ProductForm(request.POST)
            if form.is_valid():
                messages.success(request, "Succesfully added.")
                form.save()
            else:
                messages.error(request, "Something Went Wrong.")
            return redirect("/supershop_admin/product/add/")
        elif 'edit' in ops:
            cat_id = ops.split('__')[-1]
            cat = models.Product.objects.filter(pk=cat_id).first()
            form = ProductEditForm(request.POST, instance=cat)
            if form.is_valid():
                form.save()
                messages.success(request, "Succesfully Updated.")
            else:
                messages.error(request, "Something Went Wrong.")
            return redirect("/supershop_admin/category/view/")
        elif 'delete' in ops:
            prod_id = ops.split('__')[-1]
            # return JsonResponse(cat_id, safe=False)
            cat = models.Product.objects.filter(pk=prod_id).delete()
            return JsonResponse(1, safe=False)

    elif request.method == 'GET':
        if ops == 'add':
            form = ProductForm()
            return render(request, "all_forms.html",
                          context={"is_logged_in": request.user.is_authenticated,
                                   "form": form,
                                   "title": "Add Product",
                                   "admin": 1,
                                   'logout': request.user.is_authenticated,
                                   "btn_name": "ADD Product",
                                   "admin_product": "active"})
        elif ops == 'view':
            all_products = models.Product.objects.all()
            return render(request, 'view_products.html',
                          context={
                              'is_logged_in': request.user.is_authenticated,
                              "products": all_products,
                              "title": "View Products",
                              "admin": 1,
                              'logout': request.user.is_authenticated,
                              "admin_product": "active"
                          })
        elif 'edit' in ops:
            prod_id = ops.split('__')[-1]
            prod = models.Product.objects.filter(pk=prod_id).first()
            form = ProductEditForm(initial={"product_code": prod.product_code,
                                            "product_name": prod.product_name,
                                            "product_category": prod.product_category,
                                            "product_unit_price": prod.product_unit_price,
                                            "current_stock": prod.current_stock
                                            })
            return render(request, "all_forms.html",
                          context={'is_logged_in': request.user.is_authenticated,
                                   "form": form,
                                   "title": "Edit Category",
                                   "admin": 1,
                                   'logout': request.user.is_authenticated,
                                   "btn_name": "Edit Category",
                                   "admin_product": "active"})
        else:
            return redirect("admin_product")


# Order and main site
@login_required(login_url='/login/')
def products(request):
    if request.method == 'GET':
        all_products = models.Product.objects.filter(current_stock__gt=0)
        return render(request, "products.html",
                      context={"is_logged_in": request.user.is_authenticated,
                               "products": all_products,
                               "title": "Products",
                               "left_utils": [
                                   {
                                       "name": "Cart",
                                       "url": "/cart/",
                                       # "is_active": "active",
                                       "id": "cart-id"
                                   }]
                               # "right_utils": ["Cart"]
                               })


def update_cart(request):
    if request.method == 'POST':
        # return JsonResponse(1, safe=False)
        prev_order = models.Order.objects.filter(purchase_by=request.user, order_placed=False).first()
        prod = models.Product.objects.filter(pk=request.POST['prod_id'], current_stock__gt=0).first()
        op = int(request.POST['op'])
        if prod is None:
            return JsonResponse(0, safe=False)
        if prev_order is not None:
            try:
                cart = prev_order.purchased_products.filter(
                    added_products__pk=prod.pk).update(product_count=F('product_count') + op)
            except IntegrityError:
                return JsonResponse(0, safe=False)
            if cart == 0:
                cart = models.Cart.objects.create(added_products=prod)
                prev_order.purchased_products.add(cart)
            return JsonResponse(1, safe=False)
        else:
            cart = models.Cart.objects.create(added_products=prod)
            order = models.Order.objects.create(purchase_by=request.user)
            order.purchased_products.add(cart)
            return JsonResponse(1, safe=False)
    else:
        prev_order = models.Order.objects.filter(purchase_by=request.user, order_placed=False).first()
        if prev_order is None:
            return JsonResponse(0, safe=False)
        return JsonResponse(prev_order.purchased_products.aggregate(Sum('product_count'))['product_count__sum'],
                            safe=False)


@login_required(login_url='/login/')
def cart_view(request):
    cart_product = models.Order.objects.filter(purchase_by=request.user, order_placed=False).first()
    total_orders = models.Order.objects.filter(purchase_by=request.user, order_placed=False).first()
    if total_orders is None:
        total_orders = 0
    else:
        total_orders = total_orders.purchased_products.aggregate(Sum('product_count'))['product_count__sum']
    cart_count = cart_product.purchased_products.filter(product_count__gt=0) if cart_product is not None else None
    context = {
        "cart_products": cart_count,
        "order_id": cart_product.pk if cart_product is not None else None,
        "total_orders": total_orders,
        "is_logged_in": request.user.is_authenticated,
        "title": "Cart",
        "left_utils": [
            {
                "name": "Products",
                "url": "/products/",
                "id": "cart-id"
            }]
    }

    return render(request, "cart_template.html", context=context)


def remove_item_from_cart(request):
    if request.method == 'POST':
        rmv_id = request.POST['rmv_id']
        prev_order = models.Order.objects.filter(purchase_by=request.user, order_placed=False).first()
        if prev_order is not None:
            try:
                _ = prev_order.purchased_products.filter(added_products__pk=rmv_id).delete()
                return JsonResponse(1, safe=False)
            except:
                return JsonResponse(0, safe=False)
    else:
        return JsonResponse(0, safe=False)


def generate_pdf(name, img_data, qr_path, invoice_path, file_name, order):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=28)
    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 6
    th = pdf.font_size
    pdf.ln(4 * th)
    pdf.set_font('Arial', 'B', 15.0)

    pdf.cell(200, 10, txt=f"Invoice of {name}",
             ln=1, align='C')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(img_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if not os.path.exists(qr_path):
        os.mkdir(qr_path)
    img_name = file_name + str('.png')
    img_path = os.path.join(qr_path, img_name)
    img.save(img_path)
    pdf.image(img_path)

    for d in ['SL No.', 'Item', 'Unit Price', 'QTY', 'Total']:
        pdf.cell(col_width, 1 * th, str(d), border=1)
    pdf.ln(th)
    sl = 1

    purchased = order.purchased_products.all()
    for row in purchased:
        pdf.cell(col_width, 1 * th, str(sl), border=1)
        # for datum in row:
        pdf.cell(col_width, 1 * th, str(row.added_products.product_name), border=1)
        pdf.cell(col_width, 1 * th, str(row.added_products.product_unit_price), border=1)
        pdf.cell(col_width, 1 * th, str(row.product_count), border=1)
        pdf.cell(col_width, 1 * th, str((row.product_count * row.added_products.product_unit_price)), border=1)

        sl += 1
        pdf.ln(th)
    pdf.cell(col_width * 4, 1 * th, "Total", border=1)
    pdf.cell(col_width, 1 * th, str(order.total_amount), border=1)
    pdf.ln(th)
    pdf.cell(col_width * 4, 1 * th, "VAT + SD", border=1)
    pdf.cell(col_width, 1 * th, str(order.vat_price), border=1)
    pdf.ln(th)

    pdf.cell(col_width * 4, 1 * th, "Total Payable", border=1)
    pdf.cell(col_width, 1 * th, str(order.total_amount + order.vat_price), border=1)
    pdf.ln(th)

    if not os.path.exists(invoice_path):
        os.mkdir(invoice_path)

    pdf_name = file_name + str('.pdf')
    actual_invoice_path = os.path.join(invoice_path, pdf_name)
    _ = pdf.output(actual_invoice_path, 'F')

    return actual_invoice_path


def finalize_order_and_make_invoice(request):
    if request.method == 'POST':
        amt_without_vat_and_sd = float(request.POST["amtWithoutVatAndSD"])
        vat = float(request.POST["vat"])
        order_id = int(request.POST['orderId'])

        order = models.Order.objects.filter(pk=order_id).first()
        order.vat_price = vat
        order.total_amount = amt_without_vat_and_sd
        order.save()

        name = request.user.username
        img_data = f'Username: {request.user.username}\n' \
                   f'Full Name: {request.user.full_name}\n' \
                   f'Email: {request.user.email}\n' \
                   f'Phone no. : {request.user.phone}\n' \
                   f'Invoice: {str(order.order_id)}'
        invoice = generate_pdf(
            name=name,
            img_data=img_data,
            qr_path='qr_images',
            invoice_path='invoices',
            file_name=str(order.order_id),
            order=order
        )
        _ = models.Order.objects.filter(
            purchase_by=request.user, order_placed=False, pk=order_id
        ).update(total_amount=amt_without_vat_and_sd, vat_price=vat,
                 order_placed=True, invoice_path=invoice)

        return JsonResponse(json.dumps(1, default=str), safe=False)


@login_required(login_url='/login/')
def order_success(request):
    order = models.Order.objects.filter(purchase_by=request.user, order_placed=True).last()
    context = {"is_logged_in": request.user.is_authenticated,
               "title": "Success",
               "invoice_path": order.invoice_path
               }
    return render(request, 'order_success.html', context=context)


def invoice_view(request, invoice_id):
    f = open(os.path.join(settings.BASE_DIR, 'invoices', invoice_id), 'rb')
    try:
        return FileResponse(f, content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
