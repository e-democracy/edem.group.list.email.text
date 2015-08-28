# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gs.group.list.email.text.footer import Footer
from zope.cachedescriptors.property import Lazy


class GroupFooter(Footer):

    @Lazy
    def groupFooter(self):
        return self.context.groupInfo.get_property('footer', '')

    @Lazy
    def showGroupFooter(self):
        return bool(self.groupFooter)

    @Lazy
    def groupEmail(self):
        return self.listInfo.get_property('mailto')
