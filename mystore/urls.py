from django.urls import path
from .views import index, cart, item, user,customer,payment,manage,types,product, addressAPI,warehouse,bank,shipper

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
    path('cart', cart.getCart, name = 'cart'),
    path('add-to-cart', cart.addToCart, name='add-to-cart'),
    path('cart/delete/<item_id>', cart.deleteItem, name='cart/delete'),
    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('customer/notification', customer.notification, name='notification'),
    path('customer/notification/remove/<int:noti_id>', customer.removeNotification, name='customer-remove-notification'),
    path('customer/info', customer.info, name='info'),
    path('customer/order', customer.order, name='customer-order'),
    path('item/<item_id>', item.showItemDetail, name='item-detail'),
    path('item-type/<type_id>', item.item_type, name='item-type'),
    path('search', item.searchItem, name='search-item'),
    path('checkout', payment.checkout, name='checkout'),
    path('handle-checkout', payment.handleCheckout, name='handle-checkout'),
    path('checkout/delivery-address/show-edit', payment.editDeliveryAddress, name='delivery-address/show-edit'),
    path('checkout/delivery-address/handle-edit', payment.handleDeliveryAddress, name='delivery-address/handle-edit'),
    path('type/category', types.getTypeByCategory, name='type-by-category'),    
    path('bank', bank.getBanks, name='bank'),
    path('customer/delivery-address', customer.deliveryAddress, name='customer-address'),
    # customer
    path('order/view/<int:order_id>', customer.viewOrderDetail, name='order/view'),
    path('item/<item_id>/comment', item.showItemComment, name='item/comment'),
    path('item_review', item.handleComment, name='item-review'),
    # manager
    path('manager/orders', manage.saler, name = 'saler'),
    path('registation', user.register, name = 'register'),
    path('manager/product', product.product, name = 'product'),
    path('product/<int:product_id>', product.showProductDetail, name = 'product-detail'),
    path('product/active', product.active, name = 'product-active'),
    path('product/new-product', manage.newProduct, name = 'new-product'),
    path('product/new-product-detail/type/<int:type_id>', manage.newProductDetail, name='new-product-detail'),
    path('product/import-product', manage.importProduct, name='import-product'),
    path('manager/warehouse', warehouse.warehouse, name='warehouse'),
    path('product/search-product', product.active, name = 'search-product'),
    path('order/confirm-order/<int:order_id>', manage.confirmOrder, name='confirm-order'),
    path('order/cancel-order/<int:order_id>', manage.cancelOrder, name='cancel-order'),
    path('order/send-warehouse/<int:order_id>', manage.sendWarehouse, name='send-warehouse'),
    path('warehouse/export-product/<int:order_id>', warehouse.exportProduct, name='export-product'),
    path('manager/shipping', shipper.shipper, name='shipper'),
    path('shipper/shipping/<int:order_id>', shipper.shipping, name='shipping'),
    path('shipper/finished/<int:order_id>', shipper.finished, name='finished'),
    path('saler/view-order/<int:order_id>', manage.viewOrder, name = 'view-order'),
    path('product/put-item', product.getUnSoldProduct, name = 'put-item'),
    path('product/put-item-detail/<int:product_id>', product.putItemDetail, name="put-item-detail"),
    path('product/handle-put-item/<int:product_id>', product.handlePutItem, name="handle-put-item"),
    path('manager/show-feedback', manage.showFeedback, name='show-feedback'),
    path('manager/approve-feedback/<int:feedback_id>', manage.approveFeedback, name='approve-feedback'),
    path('manager/remove-feedback/<int:feedback_id>', manage.removeFeedback, name='remove-feedback'),
    path('manager/response-comment/<int:comment_id>', manage.showResponseComment, name='response-comment'),
    path('manager/handle-comment-feedback/<int:comment_id>', manage.responseComment, name='handle-response-comment'),
    # address api
    path('city', addressAPI.getCities, name='city'),
    path('city/<int:city_id>/district', addressAPI.getDistrictsInCity, name='district-in-city'),
    path('district/<int:city_id>/<int:district_id>/ward', addressAPI.getWardsInDistrict, name='ward-in-district'),
]
