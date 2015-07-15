# -*- coding: UTF-8 -*-
from django.http import HttpResponse

from landsite import settings

class RedirectMiddleware(object):

    def process_request(self, request):
        if 'HTTP_USER_AGENT' in request.META:
            for user_agent_regex in settings.Redirect_USER_AGENTS:
                if user_agent_regex.search(request.META['HTTP_USER_AGENT']):
                    return HttpResponse(
                        '<body style="margin-left:25%;margin-right:25%;marigin-top:80px;text-align: center; ">\
                        <div >\
                        <h2>我们支持所有的现代浏览器.如果您遇到问题，请更新您的浏览器</h2>\
                        <ul style="list-style-type: none;">\
                        <li style="background-image: url(); background-repeat: no-repeat;background-position: left;padding-left: 12px;">\
                        <a href="http://windows.microsoft.com/zh-cn/internet-explorer/download-ie"><img border="0" src="/static/home/img/ie.png" style="height:120px;margin-left:-70px;"></a>\
                        </li>\
                        <li style="background-image: url(); background-repeat: no-repeat;background-position: left;padding-left: 12px;">\
                        <a href="http://www.google.cn/intl/zh-CN/chrome/browser/"><img border="0" src="/static/home/img/chrome.png" style="margin-left:-30px;"></a>\
                        </li>\
                        <li style="background-image: url(); background-repeat: no-repeat;background-position: left;padding-left: 12px;">\
                        <a href="http://www.firefox.com.cn/"><img border="0" src="/static/home/img/fire-fox.png" style="margin-left:-90px;"></a>\
                        </li>\
                        <li style="background-image: url(); background-repeat: no-repeat;background-position: left;padding-left: 12px;">\
                        <a href="http://browser.qq.com/"><img border="0" src="/static/home/img/qq.png" style="margin-left:10px;"></a>\
                        </li>\
                        </div>\
                        </body>\
                        ', 
                        content_type='text/html; charset=utf-8')