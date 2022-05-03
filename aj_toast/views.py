
from .models import ToastSettings
from .forms import ToastForm
from django.contrib import messages
from django.shortcuts import redirect,render
from .decorators import admin_required
from django.contrib.auth.decorators import login_required

@login_required
@admin_required(login_url='/dashboard')
def ToastConfig(request):
	object_list = ToastSettings.objects.first()
	form = ToastForm(request.POST or None, instance = object_list)
 
	if request.method == 'POST':
		if request.user.is_authenticated:
			if request.user.is_superuser:
				if form.is_valid():
					form.save()
					messages.success(request, 'Settings Save')
					messages.info(request, 'This is a test message from a info format.')
					messages.error(request, 'This is a test message from a error format.')
					messages.warning(request, 'This is a test message from a warning format.')
					messages.success(request, 'This is a test message from a success format.')
					return redirect('toast')
				else:
					messages.error(request, 'Sorry Settings  dont save .')
					form = ToastSettings()
			else:
				messages.error(request, 'only Admin Access')
				return redirect('dashboard:index')
		messages.error(request, 'You Must First Login')
		return redirect('/login/?next=/aj_toast/')
	return render(request, 'aj_toast/toast_config.html', {'object_list': object_list, 'form': form,})



