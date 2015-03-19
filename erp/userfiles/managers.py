#coding:utf8

from userfiles.models import UFile
   
    
class Userfiles(object):
    
    ftype = 0
    user_field = None
    user_id = None
    order_by = '-create_time'
    
    def __init__(self, ftype, user_field):
        self.ftype = ftype
        self.user_field = user_field
    
    
    def __get__(self, instance, owner):
        self.user_id = getattr(instance, '%s_id' % self.user_field)
        return self
    
    
    @property
    def file(self):
        u'''取文件对象'''
        ufile = UFile.objects.filter(user=self.user_id, ftype=self.ftype)[0:1]
        if ufile:
            return ufile[0]
        return None
    
    
    @property
    def url(self):
        u'''取文件地址'''
        ufile = UFile.objects.only('fpath').filter(user=self.user_id, ftype=self.ftype)[0:1]
        if ufile:
            return ufile[0].file_url
        return None
    
    
    @property
    def files(self):
        u'''取文件列表'''
        return UFile.objects.filter(user=self.user_id, ftype=self.ftype).order_by(self.order_by)

