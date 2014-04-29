#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Myles McNamara, Matthias Krok, Eric Martel
# @Date:   2014-04-28 01:16:04
# @Last Modified by:   Myles McNamara
# @Last Modified time: 2014-04-28 19:00:25
# @Author URL: http://smyl.es
# @Plugin URL: https://github.com/tripflex/sublime-wp-developer-resources
# @License: GPL 3+

# available commands
#   wordpress_developer_resources_open_selection
#   wordpress_developer_resources_search_selection
#   wordpress_developer_resources_search_from_input

import sublime
import sublime_plugin
import subprocess
import webbrowser

def OpenInBrowser(url):
    webbrowser.open_new_tab(url)

def SearchWPDeveloper(text):
    url = 'http://developer.wordpress.org/?s=' + text.replace(' ','%20')
    OpenInBrowser(url)

def SearchWPCodex(text):
    url = 'http://wordpress.org/search/' + text.replace(' ','%20')
    OpenInBrowser(url)

def OpenWPCodexFunctionReference(text):
    url = 'http://codex.wordpress.org/Function_Reference/' + text.replace(' ','%20')
    OpenInBrowser(url)

def OpenWPDeveloperFunctionReference(text):
    url = 'http://developer.wordpress.org/reference/functions/' + text.replace(' ','%20')
    OpenInBrowser(url)

class WordpressDeveloperResourcesFunctionReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenWPDeveloperFunctionReference(text)

class WordpressDeveloperResourcesSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            SearchWPDeveloper(text)

class WordpressDeveloperResourcesSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search WordPress Codex for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchWPDeveloper(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass