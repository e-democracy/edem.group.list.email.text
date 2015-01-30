# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gs.group.list.email.text.viewlet import EmailMessageViewlet
from zope.cachedescriptors.property import Lazy
from zope.component import createObject


class Signature(EmailMessageViewlet):

    @Lazy
    def postingUser(self):
        # EmailMessageViewlet does not have the proper acquisition path for
        # self.loggedInUser. Thus, this method exists.
        return createObject('groupserver.UserFromId', self.context.messages,
                            self.context.post['user_id'])

    @Lazy
    def postingUserAbsoluteUrl(self):
        r = '{siteUrl}{userUrl}'
        retval = r.format(siteUrl=self.context.groupInfo.siteInfo.url,
                          userUrl=self.postingUser.url)
        return retval
