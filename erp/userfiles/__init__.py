#coding:utf8

from userfiles.managers import Userfiles
from userfiles.settings import USER_FILE_SAVE_RULE

registry = []

class AlreadyRegistered(Exception):
    """
    An attempt was made to register a model more than once.
    """
    pass


def register(model, ufiles_attr, user_field):
    ''' 
    Sets the given model class up for working with ufiles.
    manage func:
        file(user_id, default)
        file_url(user_id, default)
        fiels(user_id, order_by)
        
    eg:
        try:
            userfiles.register(Account, ufiles_attr=('avatar',), user_field='user')
        except userfiles.AlreadyRegistered:
            pass
            
    attribute:
    - account.avatar.url          (avatar url)
    '''
    
    if model in registry:
        raise AlreadyRegistered("The model '%s' has already been "
            "registered." % model._meta.object_name)
    
    # add attr
    for attr in ufiles_attr:
        
        if not USER_FILE_SAVE_RULE.has_key(attr):
            raise AttributeError(u'''不支持 %s 类型''' % attr)
        
        if hasattr(model, attr):
            raise AttributeError("'%s' already has an attribute '%s'. You must "
                "provide a custom tag_descriptor_attr to register." % (
                    model._meta.object_name,
                    attr,
                )
            )
        
        setattr(model, attr, Userfiles(ftype=USER_FILE_SAVE_RULE[attr]['type'], user_field=user_field))
        
    
    # Finally register in registry
    registry.append(model)
    
    