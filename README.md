py-magento-api
==============

Python library for Magento's SOAP API

	http://www.magentocommerce.com/api/soap/introduction.html

- Author: Benton Snyder
- Website: http://www.bensnyde.me
- Created: 5/19/13
- Revised: 3/10/15


Usage
=====
```
magento = Magento('http://magento.example.com/api/v2_soap?wsdl=1', 'apiuser1', 'strongapikey')
print magento.catalogProduct_list()
```
