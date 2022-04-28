#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.conf import LazySettings
from django.utils.translation import ugettext_lazy as _

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default


# Items by page on paginator views
ITEMS_BY_PAGE = 10

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

API_SUFFIX = "_api"
style = "base_django/flexbox"

# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

CONFIGURING_APPLICATION = _("Configuring application {}")
CREATING_PERMISSION_WITH_NAME = _("Creating Permission with name {}")
CREATING_GROUP_WITH_NAME = _("Creating Group with name {}")

CLIENTE_PREFIX = "CLIENTE"

CLIENTE_VERBOSE_NAME = _("Cliente")
CLIENTE_VERBOSE_NAME_PLURAL = _("Cliente")

CLIENTE_LIST_URL_NAME = CLIENTE_PREFIX + LIST_SUFFIX
CLIENTE_CREATE_URL_NAME = CLIENTE_PREFIX + CREATE_SUFFIX
CLIENTE_DETAIL_URL_NAME = CLIENTE_PREFIX + DETAIL_SUFFIX
CLIENTE_UPDATE_URL_NAME = CLIENTE_PREFIX + UPDATE_SUFFIX
CLIENTE_DELETE_URL_NAME = CLIENTE_PREFIX + DELETE_SUFFIX
CLIENTE_LIST_JSON_URL_NAME = CLIENTE_PREFIX + '_list_json'

VENDEDOR_PREFIX = "VENDEDOR"

VENDEDOR_VERBOSE_NAME = _("Vendedor")
VENDEDOR_VERBOSE_NAME_PLURAL = _("Vendedor")

VENDEDOR_LIST_URL_NAME = VENDEDOR_PREFIX + LIST_SUFFIX
VENDEDOR_CREATE_URL_NAME = VENDEDOR_PREFIX + CREATE_SUFFIX
VENDEDOR_DETAIL_URL_NAME = VENDEDOR_PREFIX + DETAIL_SUFFIX
VENDEDOR_UPDATE_URL_NAME = VENDEDOR_PREFIX + UPDATE_SUFFIX
VENDEDOR_DELETE_URL_NAME = VENDEDOR_PREFIX + DELETE_SUFFIX
VENDEDOR_LIST_JSON_URL_NAME = VENDEDOR_PREFIX + '_list_json'

FORMAPAGAMENTO_PREFIX = "FORMAPAGAMENTO"

FORMAPAGAMENTO_VERBOSE_NAME = _("FormaPagamento")
FORMAPAGAMENTO_VERBOSE_NAME_PLURAL = _("FormaPagamento")

FORMAPAGAMENTO_LIST_URL_NAME = FORMAPAGAMENTO_PREFIX + LIST_SUFFIX
FORMAPAGAMENTO_CREATE_URL_NAME = FORMAPAGAMENTO_PREFIX + CREATE_SUFFIX
FORMAPAGAMENTO_DETAIL_URL_NAME = FORMAPAGAMENTO_PREFIX + DETAIL_SUFFIX
FORMAPAGAMENTO_UPDATE_URL_NAME = FORMAPAGAMENTO_PREFIX + UPDATE_SUFFIX
FORMAPAGAMENTO_DELETE_URL_NAME = FORMAPAGAMENTO_PREFIX + DELETE_SUFFIX
FORMAPAGAMENTO_LIST_JSON_URL_NAME = FORMAPAGAMENTO_PREFIX + '_list_json'

STATUSPEDIDO_PREFIX = "STATUSPEDIDO"

STATUSPEDIDO_VERBOSE_NAME = _("StatusPedido")
STATUSPEDIDO_VERBOSE_NAME_PLURAL = _("StatusPedido")

STATUSPEDIDO_LIST_URL_NAME = STATUSPEDIDO_PREFIX + LIST_SUFFIX
STATUSPEDIDO_CREATE_URL_NAME = STATUSPEDIDO_PREFIX + CREATE_SUFFIX
STATUSPEDIDO_DETAIL_URL_NAME = STATUSPEDIDO_PREFIX + DETAIL_SUFFIX
STATUSPEDIDO_UPDATE_URL_NAME = STATUSPEDIDO_PREFIX + UPDATE_SUFFIX
STATUSPEDIDO_DELETE_URL_NAME = STATUSPEDIDO_PREFIX + DELETE_SUFFIX
STATUSPEDIDO_LIST_JSON_URL_NAME = STATUSPEDIDO_PREFIX + '_list_json'

PEDIDO_PREFIX = "PEDIDO"

PEDIDO_VERBOSE_NAME = _("Pedido")
PEDIDO_VERBOSE_NAME_PLURAL = _("Pedido")

PEDIDO_LIST_URL_NAME = PEDIDO_PREFIX + LIST_SUFFIX
PEDIDO_CREATE_URL_NAME = PEDIDO_PREFIX + CREATE_SUFFIX
PEDIDO_DETAIL_URL_NAME = PEDIDO_PREFIX + DETAIL_SUFFIX
PEDIDO_UPDATE_URL_NAME = PEDIDO_PREFIX + UPDATE_SUFFIX
PEDIDO_DELETE_URL_NAME = PEDIDO_PREFIX + DELETE_SUFFIX
PEDIDO_LIST_JSON_URL_NAME = PEDIDO_PREFIX + '_list_json'

ITEM_PREFIX = "ITEM"

ITEM_VERBOSE_NAME = _("Item")
ITEM_VERBOSE_NAME_PLURAL = _("Item")

ITEM_LIST_URL_NAME = ITEM_PREFIX + LIST_SUFFIX
ITEM_CREATE_URL_NAME = ITEM_PREFIX + CREATE_SUFFIX
ITEM_DETAIL_URL_NAME = ITEM_PREFIX + DETAIL_SUFFIX
ITEM_UPDATE_URL_NAME = ITEM_PREFIX + UPDATE_SUFFIX
ITEM_DELETE_URL_NAME = ITEM_PREFIX + DELETE_SUFFIX
ITEM_LIST_JSON_URL_NAME = ITEM_PREFIX + '_list_json'

ITEMPEDIDO_PREFIX = "ITEMPEDIDO"

ITEMPEDIDO_VERBOSE_NAME = _("ItemPedido")
ITEMPEDIDO_VERBOSE_NAME_PLURAL = _("ItemPedido")

ITEMPEDIDO_LIST_URL_NAME = ITEMPEDIDO_PREFIX + LIST_SUFFIX
ITEMPEDIDO_CREATE_URL_NAME = ITEMPEDIDO_PREFIX + CREATE_SUFFIX
ITEMPEDIDO_DETAIL_URL_NAME = ITEMPEDIDO_PREFIX + DETAIL_SUFFIX
ITEMPEDIDO_UPDATE_URL_NAME = ITEMPEDIDO_PREFIX + UPDATE_SUFFIX
ITEMPEDIDO_DELETE_URL_NAME = ITEMPEDIDO_PREFIX + DELETE_SUFFIX
ITEMPEDIDO_LIST_JSON_URL_NAME = ITEMPEDIDO_PREFIX + '_list_json'

ORCAMENTO_PREFIX = "ORCAMENTO"

ORCAMENTO_VERBOSE_NAME = _("Orcamento")
ORCAMENTO_VERBOSE_NAME_PLURAL = _("Orcamento")

ORCAMENTO_LIST_URL_NAME = ORCAMENTO_PREFIX + LIST_SUFFIX
ORCAMENTO_CREATE_URL_NAME = ORCAMENTO_PREFIX + CREATE_SUFFIX
ORCAMENTO_DETAIL_URL_NAME = ORCAMENTO_PREFIX + DETAIL_SUFFIX
ORCAMENTO_UPDATE_URL_NAME = ORCAMENTO_PREFIX + UPDATE_SUFFIX
ORCAMENTO_DELETE_URL_NAME = ORCAMENTO_PREFIX + DELETE_SUFFIX
ORCAMENTO_LIST_JSON_URL_NAME = ORCAMENTO_PREFIX + '_list_json'


ITEMORCAMENTO_PREFIX = "ITEMORCAMENTO"

ITEMORCAMENTO_VERBOSE_NAME = _("ItemOrcamento")
ITEMORCAMENTO_VERBOSE_NAME_PLURAL = _("ItemOrcamento")

ITEMORCAMENTO_LIST_URL_NAME = ITEMORCAMENTO_PREFIX + LIST_SUFFIX
ITEMORCAMENTO_CREATE_URL_NAME = ITEMORCAMENTO_PREFIX + CREATE_SUFFIX
ITEMORCAMENTO_DETAIL_URL_NAME = ITEMORCAMENTO_PREFIX + DETAIL_SUFFIX
ITEMORCAMENTO_UPDATE_URL_NAME = ITEMORCAMENTO_PREFIX + UPDATE_SUFFIX
ITEMORCAMENTO_DELETE_URL_NAME = ITEMORCAMENTO_PREFIX + DELETE_SUFFIX
ITEMORCAMENTO_LIST_JSON_URL_NAME = ITEMORCAMENTO_PREFIX + '_list_json'
