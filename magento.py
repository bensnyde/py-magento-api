import logging
from suds.xsd.doctor import ImportDoctor, Import
from suds.client import Client

class Magento:
        def __init__(self, url, username, password):
                self._client = Client(url, doctor=ImportDoctor(Import('http://schemas.xmlsoap.org/soap/encoding/')))
                self._session = self._client.service.login(username, password)

        def catalogCategory_currentStore(self, store_view_id):
                params = {"storeView" : store_view_id}
                return self._client.service.call(self._session, "catalog_category.currentStore", params)

        def catalogCategory_tree(self, parent_id=None, store_view=None):
                params = {"storeView" : store_view, "parentId" : parent_id}
                return self._client.service.call(self._session, "catalog_category.tree", params)

        def catalogCategory_level(self, website=None, store_view=None, parent_category=None):
                params = {"storeView": store_view, "Website": website, "parentCategory": parent_category}
                return self._client.service.call(self._session, "catelog_category.level", params)

        def catalogCategory_info(self, category_id, store_view=None, attributes=[]):
                params = {"categoryId": category_id, "storeView": store_view, "attributes": attributes}
                return self._client.service.call(self._session, "catalog_category.info", params)

        def catalogCategory_create(self, parent_id, category_data=[], store_view=None):
                params = {"parentId": parent_id, "categoryData": category_data, "storeView": store_view}
                return self._client.service.call(self._session, "catalog_category.create", params)

        def catalogCategory_update(self, parent_id, category_data=[], store_view=None):
                params = {"parentId": parent_id, "categoryData": category_data, "storeView": store_view}
                return self._client.service.call(self._session, "catalog_category.update", params)

        def catalogCategory_move(self, category_id, parent_id, after_id):
                params = {"parentId": parent_id, "categoryId": category_id, "afterId": after_id}
                return self._client.service.call(self._session, "catalog_category.move", params)

        def catalogCategory_delete(self, category_id):
                params = {"categoryId": category_id}
                return self._client.service.call(self._session, "catalog_category.delete", params)

        def catalogCategory_assignedProducts(self, category_id):
                params = {"category_id": category_id}
                return self._client.service.call(self._session, "catalog_category.assignedProducts", params)

        def catalogCategory_assignProduct(self, category_id, product_id, position=None, product_identifier_type=None):
                params = {"categoryId": category_id, "productId": product_id, "position": position, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_category.assignProduct", params)

        def catalogCategory_updateProduct(self, category_id, product_id, position=None, product_identifier_type=None):
                params = {"categoryId": category_id, "productId": product_id, "position": position, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_category.updateProduct", params)

        def catalogCategory_removeProduct(self, category_id, product_id, product_identifier_type=None):
                params = {"categoryId": category_id, "productId": product_id, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_category.removeProduct", params)

        def catalogCategoryAttribute_currentStore(self, store_view=None):
                params = {"storeView": store_view}
                return self._client.service.call(self._session, "catalog_product_attribute.currentStore", params)

        def catalogCategoryAttribute_list(self):
                return self._client.service.call(self._session, "catalog_product_attribute.list")

        def catalogCategoryAttribute_options(self, attribute_id, store_view):
                params = {"attributeId": attribute_id, "storeView": store_View}
                return self._client.service.call(self._session, "catalog_product_attribute.options", params)

        def catalogProduct_currentStore(self, store_view=None):
                params = {"storeView": store_view}
                return self._client.service.call(self._session, "catalog_product.currentStore", params)

        def catalogProduct_list(self, filters=[], store_view=None):
                params = {"storeView": store_view, "filters": filters}
                return self._client.service.call(self._session, "catalog_product.list", params)

        def catalogProduct_info(self, product_id, store_view=None, attributes=[], product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false

                params = {"product": product_id, "productIdentifierType": product_identifier_type, "attributes": attributes, "storeView": store_view}
                return self._client.service.call(self._session, "catalog_product.info", pararms)

        def catalogProduct_create(self, type, set_id, sku, product_data=[], store_view=None):
                params = {"type": type, "set": set_id, "sku": sku, "productData": product_data, "storeView": store_view}
                return self._client.service.call(self._session, "catalog_product.create", params)

        def catalogProduct_update(self, product_id, product_data=[], store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false

                params = {"productId": product_id, "productData": product_data, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product.update", params)

        def catalogProduct_setSpecialPrice(self, product_id, special_price, from_date, to_date, store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false

                params = {"productId": product_id, "specialPrice": special_price, "fromDate": from_date, "toDate": to_date, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product.setSpecialPrice", params)

        def catalogProduct_getSpecialPrice(self, product_id, store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false

                params = {"productId": product_id, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product.getSpecialPrice", params)

        def catalogProduct_delete(self, product_id, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false

                params = {"productId": product_id, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product.delete", params)

        def catalogProduct_listOfAdditionalAttributes(self, product_type, attribute_set_id):
                params = {"productType": product_type, "attributeSetId": attribute_set_id}
                return self._client.service.call(self._session, "catalog_product.listOfAdditionalAttributes", params)

        def productAttribute_currentStore(self, store_view=None):
                params = {"storeView": store_view}
                return self._client.service.call(self._session, "catalog_product_attribute.currentStore", params)

        def productAttribute_list(self, set_id):
                params = {"setId": set_id}
                return self._client.service.call(self._session, "catalog_product_attribute.list", params)

        def productAttribute_options(self, attribute_id, store_view=None):
                params = {"attributeId": attribute_id, "storeView": store_view}
                return self._client.service.call(self._session, "catalog_product_attribute.options", params)

        def productAttribute_addOption(self, attribute_id, data=[]):
                params = {"attributeId": attribute_id, "data": data}
                return self._client.service.call(self._session, "product_attribute.addOption", params)

        def productAttribute_create(self, data=[]):
                params = {"data": data}
                return self._client.service.call(self._session, "product_attribute.create", params)

        def productAttribute_info(self, attribute_id):
                params = {"attributeId": attribute_id}
                return self._client.service.call(self._session, "product_attribute.info", params)

        def productAttribute_remove(self, attribute_id):
                params = {"attributeId": attribute_id}
                return self._client.service.call(self._session, "product_attribute.remove", params)

        def productAttribute_removeOption(self, attribute_id, option_id):
                params = {"attributeId": attribute_id, "optionId": option_id}
                return self._client.service.call(self._session, "product_attribute.removeOption", params)

        def productAttribute_types(self):
                return self._client.service.call(self._session, "product_attribute.types")

        def productAttribute_update(self, attribute_id, data=[]):
                params = {"attributeId": attribute_id, "data": data}
                return self._client.service.call(self._session, "product_attribute.update", params)

        def productAttributeSet_list(self):
                return self._client.service.call(self._session, "product_attribute_set.list")

        def productAttributeSet_attributeAdd(self, attribute_id, attribute_group_id=None, sort_order=None):
                params = {"attributeId": attribute_id, "attributeGroupId": attribute_group_id, "sortOrder": sort_order}
                return self._client.service.call(self._session, "product_attribute_set.attributeAdd", params)

        def productAttributeSet_attributeRemove(self, attribute_id, attribute_set_id):
                params = {"attributeId": attribute_id, "attributeSetId": attribute_set_id}
                return self._client.service.call(self._session, "product_attribute_set.attributeRemove", params)

        def productAttributeSet_create(self, attribute_set_name, skeleton_set_id):
                params = {"attributeSetName": attribute_set_name, "skeletonSetId": skeleton_set_id}
                return self._client.service.call(self._session, "product_attribute_set.create", params)

        def productAttributeSet_groupAdd(self, attribute_set_id, group_name):
                params = {"attributeSetId": attribute_set_id, "groupName": group_name}
                return self._client.service.call(self._session, "product_attribute_set.groupAdd", params)

        def productAttributeSet_groupRemove(self, attribute_group_id):
                params = {"attributeGroupId": attribute_group_id}
                return self._client.service.call(self._session, "product_attribute_set.groupRemove", params)

        def productAttributeSet_groupRename(self, group_id, group_name):
                params = {"groupId": group_id, "groupName": group_name}
                return self._client.service.call(self._session, "product_attribute_set.groupRename", params)

        def productAttributeSet_remove(self, attribute_set_id, force_products_remove=None):
                params = {"attributeSetId": attribute_set_id, "forceProductsRemove": force_products_remove}
                return self._client.service.call(self._session, "product_attribute_set.remove", params)

        def productCatalogType_list(self):
                return self._client.service.call(self._session, "catalog_product_type.list")

        def catalogProductAttributeMedia_currentStore(self, store_view=None):
                params = {"storeView": store_view}
                return self._client.service.call(self._session, "catalog_product_attribute_media.currentStore", params)

        def catalogProductAttributeMedia_list(self, product_id, store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false

                params = {"productId": product_id, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_media.list", params)

        def catalogProductAttributeMedia_info(self, product_id, file, store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "file": file, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_media.info", params)

        def catalogProductAttributeMedia_types(self, set_id):
                params = {"setId": set_id}
                return self._client.service.call(self._session, "catalog_product_attribute_media.types", params)

        def catalogProductAttributeMedia_create(self, product_id, data=[], store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "data": data, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_media.create", params)

        def catalogProductAttributeMedia_update(self, product_id, file, data=[], store_view=None, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "file": file, "data": data, "storeView": store_view, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_media.update", params)

        def catalogProductAttributeMedia_remove(self, product_id, file, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "file": file, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_media.remove", params)

        def catalogProductAttributeTierPrice_info(self, product_id, product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_tier_price.info", params)

        def catalogProductAttributeTierPrice_update(self, product_id, tier_prices=[], product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "tierPrices": tier_prices, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_attribute_tier_price.update", params)

        def catalogProductLink_list(self, product_id, type="related", product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                # types = cross_sell, up_sell, related, grouped
                params = {"type": type, "productId": product_id, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_link.list", params)

        def catalogProductLink_assign(self, product_id, linked_product_id, data=[], type="related", product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                # types = cross_sell, up_sell, related, grouped
                params = {"type": type, "productId": product_id, "linkedProductId": linked_product_id, "data": data, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_link.assign", params)

        def catalogProductLink_update(self, product_id, linked_product_id, data=[], type="related", product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                # types = cross_sell, up_sell, related, grouped
                params = {"type": type, "productId": product_id, "linkedProductId": linked_product_id, "data": data, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_link.update", params)

        def catalogProductLink_remove(self, product_id, linked_product_id, type="related", product_identifier_type="id"):
                if product_identifier_type <> "id" and product_identifier_type <> "sku":
                        return false
                # types = cross_sell, up_sell, related, grouped
                params = {"productId": product_id, "linkedProductId": linked_product_id, "type": type, "productIdentifierType": product_identifier_type}
                return self._client.service.call(self._session, "catalog_product_link.remove", params)

        def catalogProductLink_types(self):
                return self._client.service.call(self._session, "catalog_product_link.types")

        def catalogProductLink_attributes(self, type="related"):
                # types = cross_sell, up_sell, related, grouped
                params = {"type": type}
                return self._client.service.call(self._session, "catalog_product_link.attributes", params)

        def productDownloadableLink_add(self, product_id, resource=[], resource_type="link", store_view=None, identifier_type="id"):
                if identifier_type <> "id" and identifier_type <> "sku":
                        return false
                if resource_type <> "link" and resource_type <> "sample":
                        return false
                params = {"productId": product_id, "resource": resource, "resourceType": resource_type, "storeView": store_view, "identifierType": identifier_type}
                return self._client.service.call(self._session, "product_downloadable_link.add", params)

        def productDownloadableLink_list(self, product_id, store_view=None, identifier_type="id"):
                if identifier_type <> "id" and identifier_type <> "sku":
                        return false
                params = {"productId": product_id, "storeView": store_view, "identifierType": identifier_type}
                return self._client.service.call(self._session, "product_downloadable_link.list", params)

        def productDownloadableLink_remove(self, link_id, resource_type="link"):
                if resource_type <> "link" and resource_type <> "sample":
                        return false
                params = {"linkId": link_id, "resourceType": resource_type}
                return self._client.service.call(self._session, "product_downloadable_link.remove", params)

        def productTag_add(self, data=[]):
                params = {"data": data}
                return self._client.service.call(self._session, "catalog_product_tag.add", params)

        def productTag_info(self, tag_id, store_id):
                params = {"tagId": tag_id, "storeId": store_id}
                return self._client.service.call(self._session, "catalog_product_tag.info", params)

        def productTag_list(self, product_id, store_id):
                params = {"productId": product_id, "storeId": store_id}
                return self._client.service.call(self._session, "catalog_product_tag.list", params)

        def productTag_update(self, tag_id, data=[], store_view=None):
                params = {"tagId": tag_id, "data": data, "storeView": store_view}
                return self._client.service.call(self._session, "catalog_product_tag.update", params)

        def productTag_remove(self, tag_id):
                params = {"tagId": tag_id}
                return self._client.service.call(self._session, "catalog_product_tag.remove", params)

        def productCustomerOption_add(self, option_id, data=[], store_view=None):
                params = {"optionId": option_id, "data": data, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option.add", params)

        def productCustomOption_update(self, option_id, data=[], store_view=None):
                params = {"optionId": option_id, "data": data, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option.update", params)

        def productCustomOption_types(self):
                return self._client.service.call(self._session, "product_custom_option.types")

        def productCustomOption_list(self, product_id, store_view=None):
                params = {"productId": product_id, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option.list", params)

        def productCustomOption_info(self, option_id, store_view=None):
                params = {"optionId": option_id, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option.info", params)

        def productCustomOption_remove(self, option_id):
                params = {"optionId": option_id}
                return self._client.service.call(self._session, "product_custom_option.remove", params)

        def productCustomOptionValue_add(self, option_id, data=[], store_view=None):
                params = {"optionId": option_id, "data": data, "store": store_view}
                return self.client.service.call(self._session, "product_custom_option_value.add", params)

        def productCustomOptionValue_list(self, option_id, store_view=None):
                params = {"optionId": option_id, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option_value.list", params)

        def productCustomOptionValue_info(self, value_id, store_view=None):
                params = {"valueId": value_id, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option_value.info", params)

        def productCustomOptionValue_update(self, value_id, data=[], store_view=None):
                params = {"valueId": value_id, "data": data, "store": store_view}
                return self._client.service.call(self._session, "product_custom_option_value.update", params)

        def productCustomOptionValue_remove(self, value_id):
                params = {"valueId": value_id}
                return self._client.service.call(self._session, "product_custom_option_value.remove", params)

        def cartCoupon_add(self, quote_id, coupon_code, store_view=None):
                params = {"quoteId": quote_id, "couponCode": coupon_code, "store": store_view}
                return self._client.service.call(self._session, "cart_coupon.add", params)

        def cartCoupon_remove(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart_coupon.remove", params)

        def cartCustomer_set(self, quote_id, customer_data=[], store_view=None):
                params = {"quoteId": quote_id, "customerData": customer_data, "store": store_view}
                return self._client.service.call(self._session, "cart_customer.set", params)

        def cartCustomer_addresses(self, quote_id, customer_address_data=[], store_view=None):
                params = {"quoteId": quote_id, "customerAddressData": customer_address_data, "store": store_view}
                return self._client.service.call(self._session, "cart_customer.addresses", params)

        def cartPayment_method(self, quote_id, payment_data=[], store_view=None):
                params = {"quoteId": quote_id, "paymentData": payment_data, "store": store_view}
                return self._client.service.call(self._session, "cart_payment.method", params)

        def cartPayment_list(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart_payment.list", params)

        def cartProduct_add(self, quote_id, products=[], store_view=None):
                params = {"quoteId": quote_id, "products": products, "storeId": store_view}
                return self._client.service.call(self._session, "cart_product.add", params)

        def cartProduct_update(self, quote_id, products=[], store_view=None):
                params = {"quoteId": quote_id, "products": products, "store": store_view}
                return self._client.service.call(self._session, "cart_product.update", params)

        def cartProduct_remove(self, quote_id, products=[], store_view=None):
                params = {"quoteId": quote_id, "products": products, "store": store_view}
                return self._client.service.call(self._session, "cart_product.remove", params)

        def cartProduct_list(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart_product.list", params)

        def cartProduct_moveToCustomerQuote(self, quote_id, products=[], store_view=None):
                params = {"quoteId": quote_id, "products": products, "store": store}
                return self._client.service.call(self._session, "cart_product.moveToCustomerQuote", params)

        def cartShipping_method(self, quote_id, shipping_method, store_view=None):
                params = {"quoteId": quote_id, "shippingMethod": shipping_method, "store": store_view}
                return self._client.service.call(self._session, "cart_shipping.method", params)

        def cartShipping_list(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart_shipping.list", params)

        def cart_create(self, store_view=None):
                params = {"storeId": store_view}
                return self._client.service.call(self._session, "cart.create", params)

        def cart_order(self, quote_id, store_view=None, agreements=[]):
                params = {"quoteId": quote_id, "store": store_view, "agreements": agreements}
                return self._client.service.call(self._session, "cart.order", params)

        def cart_info(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart.info", params)

        def cart_totals(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart.totals", params)

        def cart_license(self, quote_id, store_view=None):
                params = {"quoteId": quote_id, "store": store_view}
                return self._client.service.call(self._session, "cart.license", params)

        def customer_list(self, filters=[]):
                params = {"filters": filters}
                return self._client.service.call(self._sesssion, "customer.list", params)

        def customer_create(self, customer_data=[]):
                params = {"customerData": customer_data}
                return self._client.service.call(self._session, "customer.create", params)

        def customer_update(self, customer_id, customer_data=[]):
                params = {"customerId": customer_id, "customerData": customer_data}
                return self._client.service.call(self._session, "customer.update", params)

        def customer_delete(self, customer_id):
                params = {"customerId": customer_id}
                return self._client.service.call(self._session, "customer.delete", params)

        def customer_info(self, customer_id, filters=[]):
                params = {"customerId": customer_id, "filters": filters}
                return self._client.service.call(self._session, "customer.info", params)

        def customerGroup_list(self):
                return self._client.service.call(self._session, "customer_group.list")

        def customerAddress_list(self, customer_id):
                params = {"customerId": customer_id}
                return self._client.service.call(self._session, "customer_address.list", params)

        def customerAddress_create(self, customer_id, address_data=[]):
                params = {"customerId": customer_id, "addressData": address_data}
                return self._client.service.call(self._session, "customer_address.create", params)

        def customerAddress_update(self, address_id, address_data=[]):
                params = {"addressId": address_id, "addressData": address_data}
                return self._client.service.call(self._session, "customer_address.update", params)

        def customerAddress_delete(self, address_id):
                params = {"addressId": address_id}
                return self._client.service.call(self._session, "customer_address.delete", params)

        def customerAddress_info(self, address_id):
                params = {"addressId": address_id}
                return self._client.service.call(self._session, "customer_address.info", params)

        def salesOrder_list(self, filters=[]):
                params = {"filters": filters}
                return self._client.service.call(self._session, "sales_order.list", params)

        def salesOrder_info(self, order_increment_id):
                params = {"orderIncrementId": order_increment_id}
                return self._client.service.call(self._session, "sales_order.info", params)

        def salesOrder_addComment(self, order_increment_id, status, comment=None, notify=None):
                params = {"orderIncrementId": order_increment_id, "status": status, "comment": comment, "notify": notify}
                return self._client.service.call(self._session, "sales_order.addComment", params)

        def salesOrder_hold(self, order_increment_id):
                params = {"orderIncrementId": order_increment_id}
                return self._client.service.call(self._session, "sales_order.hold", params)

        def salesOrder_unhold(self, order_increment_id):
                params = {"orderIncrementId": order_increment_id}
                return self._client.service.call(self._session, "sales_order.unhold", params)

        def salesOrder_cancel(self, order_increment_id):
                params = {"orderIncrementId": order_increment_id}
                return self._client.service.call(self._session, "sales_order.cancel", params)

        def salesOrderInvoice_list(self, filters=[]):
                params = {"filters": filters}
                return self._client.service.call(self._session, "sales_order_invoice.list", params)

        def salesOrderInvoice_info(self, invoice_increment_id):
                params = {"invoiceIncrementId": invoice_increment_id}
                return self._client.service.call(self._session, "sales_order_invoice.info", params)

        def salesOrderInvoice_create(self, order_increment_id, items_qty=[], comment=None, email=None, include_comment=None):
                params = {"orderIncrementId": order_increment_id, "itemsQty": items_qty, "comment": comment, "email": email, "includeComment": include_comment}
                return self._client.service.call(self._session, "sales_order_invoice.create", params)

        def salesOrderInvoice_addComment(self, invoice_increment_id, comment=None, email=None, include_commnet=None):
                params = {"invoiceIncrementId": invoice_increment_id, "comment": comment, "email": email, "includeComment": include_comment}
                return self._client.service.call(self._session, "sales_order_invoice.addComment", params)

        def salesOrderInvoice_capture(self, invoice_increment_id):
                params = {"invoiceIncrementId": invoice_increment_id}
                return self._client.service.call(self._session, "sales_order_invoice.capture", params)

        def salesOrderInvoice_cancel(self, invoice_increment_id):
                params = {"invoiceIncrementId": invoice_increment_id}
                return self._client.service.call(self._session, "sales_order_invoice.cancel", params)

        def salesOrderShipment_list(self, filters=[]):
                params = {"filters": filters}
                return self._client.service.call(self._session, "sales_order_shipment.list", params)

        def salesOrderShipment_info(self, shipment_increment_id):
                params = {"shipmentIncrementId": shipment_increment_id}
                return self._client.service.call(self._session, "sales_order_shipment.info", params)

        def salesOrderShipment_create(self, order_increment_id, items_qty=[], comment=None, send_email=None, include_comment=None):
                params = {"orderIncrementId": order_increment_id, "itemsQty": items_qty, "comment": comment, "sendEmail": send_email, "includeComment": include_comment}
                return self._client.service.call(self._session, "sales_order_shipment.create", params)

        def salesOrderShipment_addComment(self, shipment_increment_id, comment=None, email=None, include_in_email=None):
                params = {"shipmentIncrementId": shipment_increment_id, "comment": comment, "email": email, "includeInEmail": include_in_email}
                return self._client.service.call(self._session, "sales_order_shipment.addComment", params)

        def salesOrderShipment_addTrack(self, shipment_increment_id, carrier, title, track_number):
                params = {"shipmentIncrementId": shipment_increment_id, "carrier": carrier, "title": title, "trackNumber": track_number}
                return self._client.service.call(self._session, "sales_order_increment.addTrack". params)

        def salesOrderShipment_removeTrack(self, shipment_increment_id, track_id):
                params = {"shipmentIncrementId": shipment_increment_id, "trackId": track_id}
                return self._client.service.call(self._session, "sales_order_shipment.removeTrack", params)

        def salesOrderShipment_getCarriers(self, order_increment_id):
                params = {"orderIncrementId": order_increment_id}
                return self._client.service.call(self._session, "sales_order_shipment.getCarriers", params)

        def salesOrderCreditmemo_list(self, filters=[]):
                params = {"filters": filters}
                return self._client.service.call(self._session, "order_creditmemo.list", params)

        def salesOrderCreditmemo_info(self, creditmemo_increment_id):
                params = {"creditmemoIncrementId": creditmemo_increment_id}
                return self._client.service.call(self._session, "order_creditmemo.info", params)

        def salesOrderCreditmemo_create(self, order_increment_id, creditmemo_data=[], comment=None, notify_customer=None, include_comment=None, refund_to_store_credit_amount=None):
                params = {"orderIncrementId": order_increment_id, "creditmemoData": creditmemo_data, "comment": comment, "notifyCustomer": notify_customer, "includeComment": include_comment, "refundToStoreCreditAmount": refund_to_store_credit_amount}
                return self._client.service.call(self._session, "order_creditmemo.create", params)

        def salesOrderCreditmemo_addComment(self, creditmemo_increment_id, comment=None, notify_customer=None, include_comment=None):
                params = {"creditmemoIncrementId": creditmemo_increment_id, "comment": comment, "notifyCustomer": notify_customer, "includeComment": include_comment}
                return self._client.service.call(self._session, "order_creditmemo.addComment", params)

        def salesOrderCreditmemo_cancel(self, creditmemo_increment_id):
                params = {"creditmemoIncrementId": creditmemo_increment_id}
                return self._client.service.call(self._session, "order_creditmemo.cancel", params)

        def catalogInventoryStockItem_list(self, product_ids=[]):
                params = {"productIds": product_ids}
                return self._client.service.call(self._session, "cataloginventory_stock_item.list", params)

        def catalogInventoryStockItem_update(self, product_id, data=[]):
                params = {"productId": product_id, "data": data}
                return self._client.service.call(self._session, "cataloginventory_stock_item.update", params)
