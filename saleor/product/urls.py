from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<slug>[a-z0-9-]+?)-(?P<product_id>[0-9]+)/$',
        views.product_details, name='details'),
    url(r'^category/(?P<path>[a-z0-9-_/]+?)-(?P<category_id>[0-9]+)/$',
        views.category_index, name='category'),
    url(r'(?P<slug>[a-z0-9-]+?)-(?P<product_id>[0-9]+)/add/$',
        views.product_add_to_cart, name="add-to-cart"),
    url(r'^(?P<product_id>[0-9]+)/fromcollections/$',
        views.products_from_collections, name="from-collections"),
]
