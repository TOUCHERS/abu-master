# -*- encoding:utf-8 -*-



# 不要在abupy之外再建立包结构
# noinspection PyUnresolvedReferences
import widget_base


def show_ui():
    with widget_base.show_ui_ct() as go_on:
        if not go_on:
            return
        from abupy import WidgetSearchStockInfo
        widget = WidgetSearchStockInfo()
    return widget()
