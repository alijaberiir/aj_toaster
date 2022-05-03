from django.db import models

# Create your models here.
class ToastSettings(models.Model):
	STATUS_CHOICES = (
		('toast-top-right', 'Top Right'),
		('toast-top-left', 'Top Left'),
		('toast-top-center', 'Top Center'),
		('toast-top-full-width', 'Top Full Width'),
		('toast-bottom-right', 'Bottom Right'),
		('toast-bottom-left','Bottom Left'),
		('toast-bottom-full-width', 'Bottom Full Width'),
		('toast-bottom-center', 'Bottom Center'),
	)
	STATUS_EASING=(
		('swing','swing'),
		('linear','linear'),
	)
	STATUS_SHOW=(
		('show','show'),
		('fadeIn','fadeIn'),
		('slideDown','slideDown'),
	)
	STATUS_HIDE=(
		('hide','hide'),
		('fadeOut','fadeOut'),
		('slideUp','slideUp'),
	)
	Close_Button = models.BooleanField(default='false',blank=True)
	Add_behavior_click  = models.BooleanField(default='false',blank=True)
	Progress_Bar  = models.BooleanField(default='false',blank=True)
	Prevent_Duplicates  = models.BooleanField(default='false',blank=True)
	Newest_on_top  = models.BooleanField(default='false',blank=True)

	Position = models.CharField(max_length=50, choices=STATUS_CHOICES, default='toast-top-right')

	showEasing = models.CharField(max_length=50, choices=STATUS_EASING, default='swing')
	hideEasing = models.CharField(max_length=50, choices=STATUS_EASING, default='linear')
	showMethod = models.CharField(max_length=50, choices=STATUS_SHOW, default='fadeIn')
	hideMethod = models.CharField(max_length=50, choices=STATUS_HIDE, default='fadeOut')
	
	
	showDuratio = models.PositiveBigIntegerField(default=300)
	hideDuration = models.PositiveBigIntegerField(default=1000)
	timeOut = models.PositiveBigIntegerField(default=5000)
	extendedTimeOut = models.PositiveBigIntegerField(default=1000)
	
	
 
	def __str__(self):
		return 'Aj Toast Config'