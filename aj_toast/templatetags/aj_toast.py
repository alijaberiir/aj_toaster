from django import template
from aj_toast.models import ToastSettings
register = template.Library()





@register.inclusion_tag("aj_toast/toast.html")
def toast(messages):
	return {"obj" : ToastSettings.objects.first(), "messages" : messages,}





