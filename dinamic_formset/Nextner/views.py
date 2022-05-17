from django.forms import formset_factory
from django.http import HttpResponseNotFound
from django.views.generic import View, ListView
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class AddManyItem(View):
    def get(self, request):
        ProductsFormSet = formset_factory(AddPostForm)
        formset = ProductsFormSet()
        return render(request, "nextner/new_order.html", {"formset": formset})

    def post(self, request):
        # Делаем копии request, потому что request неизменяемый
        query_dict = request.POST.copy()
        files_dict = request.FILES.copy()

        x = request.POST.getlist("form-TOTAL_FORMS")
        query_dict.setlist("form-INITIAL_FORMS", x)

        lenght = int(x[0])
        # Заполняем недостающие, одинаковые для всех форм, атрибуты.
        # В соответствии с количеством 'form-TOTAL_FORMS'
        for n in range(1, lenght):
            query_dict.update({"form-" + str(n) + "-title": query_dict["form-0-title"]})

            query_dict.update(
                {"form-" + str(n) + "-product_type": query_dict["form-0-product_type"]}
            )

            query_dict.update(
                {
                    "form-"
                    + str(n)
                    + "-delivery_date": query_dict["form-0-delivery_date"]
                }
            )

            query_dict.update(
                {
                    "initial-form-"
                    + str(n)
                    + "-delivery_date": query_dict["initial-form-0-delivery_date"]
                }
            )

            files_dict.update(
                {
                    "form-"
                    + str(n)
                    + "-file_attachment": files_dict["form-0-file_attachment"]
                }
            )

        ProductsFormSet = formset_factory(AddPostForm)

        formset = ProductsFormSet(query_dict, files_dict)

        if formset.is_valid():
            for form in formset:
                form.save()

        return redirect("orders_list")


class OrdersList(ListView):
    template_name = "nextner/orders_list.html"
    context_object_name = "orders"
    model = Products


class AddType(View):
    def get(self, request):
        type_form = AddTypeForm()
        return render(request, "nextner/new_type.html", {"type_form": type_form})

    def post(self, request):
        type_form = AddTypeForm(request.POST)
        if type_form.is_valid:
            type_form.save()
        return redirect("types_list")


class TypesList(ListView):
    template_name = "nextner/type_list.html"
    context_object_name = "types"
    model = Types
    

class AddAddress(View):
    def get(self, request):
        address_form = AddAddressForm()
        return render(request, "nextner/new_address.html", {"address_form": address_form})

    def post(self, request):
        address_form = AddAddressForm(request.POST)
        if address_form.is_valid:
            address_form.save()
        return redirect("address_list")


class AddressesList(ListView):
    template_name = "nextner/address_list.html"
    context_object_name = "addresses"
    model = Addreses