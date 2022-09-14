from django.shortcuts import render, redirect

from products.forms import ProductForm


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self,request):
        form =self.form_model()
        return render(request,self.template,{"form":form})

    def post(self,request):

        form =self.form_model(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            # new_item = form.save()
            # return redirect(new_item.slug)
        return render(request,self.template,{"form":form})