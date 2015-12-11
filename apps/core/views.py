from django.shortcuts import render
from django.views import generic

from . import models as core_models
# Create your views here.

class BasePage(generic.TemplateView):
	template_name = "core/default_page.html"

	def get_context_data(self, *args, **kwargs):
		context = super(BasePage, self).get_context_data(**kwargs)
		menus = core_models.Menu.objects.all()
		for menu in menus:
			menu.submenus = core_models.SubMenu.objects.filter(menu=menu)
			for submenu in menu.submenus:
				if self.request.resolver_match.url_name == submenu.url:
					submenu.current_item = True
		context['menus'] = menus
		return context


class Page1(BasePage):
	template_name = "core/page1.html"


class Page2(BasePage):
	template_name = "core/page2.html"
