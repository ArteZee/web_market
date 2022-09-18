from django.shortcuts import render, redirect

from products.forms import ProductForm


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.form_model(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            # new_item = form.save()
            # return redirect(new_item.slug)
        return render(request, self.template, {"form": form})


class ObjecttUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        item = self.model.objects.get(slug=slug)
        form = self.form_model(instance=item)
        return render(request, self.template, {"form": form})

    def post(self, request, slug):
        item = self.model.objects.get(slug=slug)
        form = self.form_model(request.POST, instance=item)
        if form.is_valid():
            new_form = form.save()

            return redirect(new_form)
        return render(request, self.template, {"form": form, "item": item})
