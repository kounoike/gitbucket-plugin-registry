#!/usr/bin/env python
# coding: utf-8

import json
import os

plugins_dir = "registry/plugins"

for ver in os.listdir(plugins_dir):
    available_plugins = []
    for plugin in os.listdir(os.path.join(plugins_dir, ver)):
        with open(os.path.join(plugins_dir, ver, plugin)) as f:
            plugin_data = json.load(f)
        available_plugins.append(plugin_data)
    with open("release/{}.json".format(ver), "w") as f:
        json.dump(available_plugins, f)