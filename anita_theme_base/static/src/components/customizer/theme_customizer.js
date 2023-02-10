/** @odoo-module **/

import { Component, useState, useExternalListener} from "@odoo/owl";

import { registry } from "@web/core/registry";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { useService } from "@web/core/utils/hooks";

export class ThemeCustomizer extends Component {
    setup() {
        super.setup();
        this.actionService = useService("action");
    }

    _on_toggle_click() {
        // url action
        this.actionService.doAction({
            type: "ir.actions.act_url",
            url: "https://apps.odoo.com/apps/themes/15.0/anita_theme_setting/",
            target: "current",
        });
    }
}
  
ThemeCustomizer.template = "anita_theme_base.customizer";

ThemeCustomizer.components = {
    Dropdown: Dropdown,
    DropdownItem: DropdownItem,
};

export const systrayItem = {
    Component: ThemeCustomizer,
};
registry.category("systray").add("anita_theme_base.customizer", systrayItem, { sequence: 1 });
