from django.contrib import admin

# Register your models here.
from.models import LmsPost

class LmsPostAdmin(admin.ModelAdmin):
	list_display=['name','faculty','book','borrowed','duedate','returned']
	list_editable=['returned']
	list_filter=['name','book','faculty']
	search_fields=['name','book']
	ordering =['borrowed']
	list_per_page=5
admin.site.register(LmsPost,LmsPostAdmin)