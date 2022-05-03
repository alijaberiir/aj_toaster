# Aj Toastr
**toastr** is a Javascript library for non-blocking notifications. jQuery is required. The goal is to create a simple core library that can be customized and extended.


## Quick Start

### 3 Easy Steps

1. Copy to aj_toast in your django project near other apps

2. install app in your settings.py
    ```
    INSTALLED_APPS = [
        ...
	'aj_toast',
    ]
    ```

3. add url in urls.

	```
    path('aj_toast/', include('aj_toast.urls'), name='aj_toast'),
	
	```
4. run the following in a virtual environment:

    ```
    python manage.py migrate
    ```
5. add in template html page you like use massages by toaster.

    ```
    {% load aj_toast %}

    {% toast messages %}

    ```

###  Options

http://127.0.0.1:8000/aj_toast

