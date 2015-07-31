# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gs.group.list.email.text.viewlet import EmailMessageViewlet
from zope.cachedescriptors.property import Lazy


class GroupFooter(EmailMessageViewlet):

    @Lazy
    def groupFooter(self):
        return self.context.groupInfo.get_property('footer', '')

    @Lazy
    def showGroupFooter(self):
        return bool(self.groupFooter)
