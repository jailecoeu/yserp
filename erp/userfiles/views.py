#coding:utf-8
import os
import copy
import uuid
import ujson as json
import Image
from datetime import date
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.contrib import auth
from django.db import connection
from django.template.response import TemplateResponse

from common.files.storage import id2sid
from common.decorators import user_decrypto
from paravalidate.decorators import require_param
from account.decorators import login_required
from userfiles import settings
from userfiles.parameters import upload_params,upload_swf_params
from userfiles.models import UFile

@login_required
def upload_test(request):
    ''''''
    return TemplateResponse(request,'v3/userfiles/upload_test.html')


@require_param(upload_swf_params)
@user_decrypto(ajax=True)
def upload_swf(request):
    '''flash上传'''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    uid = request.POST['uid']
    upload_file = request.FILES.get('file')
    upload_type = request.POST.get('type','') or 'default'
    upload_folder = request.POST.get('folder','')
    upload_name = request.POST.get('name','')

    rsp_data = __handel_file(upload_file,upload_type,upload_folder,upload_name,uid)

    return HttpResponse(json.dumps(rsp_data),mimetype='application/json')


@login_required
@require_param(upload_params)
def upload(request):
    '''
    文件上传接口
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    uid = request.session[auth.SESSION_KEY]
    upload_file = request.FILES.get('file')
    upload_type = request.POST.get('type','') or 'default'
    upload_folder = request.POST.get('folder','')
    upload_name = request.POST.get('name','')

    rsp_data = __handel_file(upload_file,upload_type,upload_folder,upload_name,uid)

    response = HttpResponse(json.dumps(rsp_data))

    if 'application/json' in request.META['HTTP_ACCEPT']:
        response = HttpResponse(json.dumps(rsp_data),mimetype='application/json')

    return response


def __handel_file(upload_file,upload_type,upload_folder,upload_name,uid):
    '''
    文件上传处理
    '''
    rsp_data = copy.copy(settings.ERROR['SUCC'])

    try:
        # 保存临时文件
        file_name = 'userfiles_%s' % str(uuid.uuid1())
        tmp_file_path = '/tmp/%s' % file_name
        tmp_file = open(tmp_file_path,'wb')
        tmp_file.write(upload_file.read())
        upload_file.close()
        tmp_file.close()

        rsp_data = __check_file(upload_file,tmp_file_path,upload_type)
        if rsp_data['code'] == '10000':
            rsp_data = __save_file(upload_file,tmp_file_path,upload_type,uid,upload_folder,upload_name)
    except:
        rsp_data = copy.copy(settings.ERROR['ERROR'])
    finally:
        # 移除临时文件
        os.remove(tmp_file_path)

    return rsp_data


def __check_file(upload_file,tmp_file_path,upload_type='default'):
    '''
    检测文件是否符合规则
    '''
    error = copy.copy(settings.ERROR['SUCC'])
    file_name = upload_file.name
    file_ext = file_name.split('.')[-1].upper()
    rule = settings.USER_FILE_SAVE_RULE.get(upload_type,None)

    #获取检测规则
    if not rule:
        return copy.copy(settings.ERROR['UPLOAD_RULE_ERROR'])

    #检测文件格式
    if rule['ext'] and (file_ext not in rule['ext']):
        return copy.copy(settings.ERROR['FILE_EXT_ERROR'])

    #检测文件大小
    file_size = upload_file.size
    if rule['file_size_max'] and file_size > rule['file_size_max']:
        return copy.copy(settings.ERROR['FILE_MAX_SIZE_ERROR'])


    #检测图片尺寸, 此处判断的是最小尺寸，规则中 0 代表不检测
    if rule.get('xsize',''):
        im = Image.open(tmp_file_path)
        xsize,ysize = im.size
        if (rule['xsize'] and  xsize < rule['xsize']) or (rule['ysize'] and  xsize < rule['ysize']):
            return copy.copy(settings.ERROR['FILE_XYSIZE_ERROR'])
        error['img_size'] = {'xsize':xsize,'ysize':ysize}

    #检测已上传文件总数
    if rule.get('unique', False):
        pass
    elif rule.get('total_count',0):
        ftype = int(rule['type'])
        db_count = UFile.objects.filter(state=0,ftype=ftype).count()
        if db_count >= rule['total_count']:
            return copy.copy(settings.ERROR['FILE_TOTAL_COUNT_ERROR'])

    #检测已上传文件存储总大小
    if rule.get('total_size',0):
        ftype = int(rule['type'])
        sql_query = '''SELECT SUM(msize) FROM userfiles_ufile WHERE ftype=%(ftype)s and state=0'''
        cursor = connection.cursor()
        cursor.execute(sql_query,{'ftype':ftype})
        db_total_size = cursor.fetchone()[0]
        cursor.close()
        if db_total_size >= rule['total_size']:
            return copy.copy(settings.ERROR['FILE_TOTAL_SIZE_ERROR'])

    return error


def __save_file(upload_file,tmp_file_path,upload_type,uid=0,upload_folder='',upload_name='',upload_desc=''):
    '''
    保存文件
    @return:
    '''
    error = copy.copy(settings.ERROR['SUCC'])
    file_name = upload_file.name
    file_ext = file_name.split('.')[-1].upper()
    rule = settings.USER_FILE_SAVE_RULE.get(upload_type,None)
    if not rule:
        return copy.copy(settings.ERROR['FILE_SAVE_ERROR'])

    #路径及文件名
    folder = rule.get('folder','') or upload_folder or date.today().strftime('%Y%m%d')
    save_name = rule.get('file_name','') or upload_name or (str(uuid.uuid1()).replace('-','') + '.' + file_ext)

    #保存路径
    save_file_path = (os.path.join(id2sid(uid),folder,save_name)).lower()
    custom_path = default_storage.path(save_file_path)

    #保存文件
    if not os.path.exists(os.path.dirname(custom_path)):
        os.makedirs(os.path.dirname(custom_path))
    tmp_file = open(tmp_file_path)
    default_storage.save(custom_path,tmp_file.read())
    tmp_file.close()

    #如果是图片获取图片尺寸信息
    xsize,ysize = 0,0
    if file_ext in ['JPG','JPEG','PNG','BMP']:
        im = Image.open(tmp_file_path)
        xsize,ysize = im.size

    #保存文件信息
    desc = upload_desc or file_name
    file_info = {
        'origin_name':file_name,
        'origin_size':upload_file.size,
        'origin_xsize':xsize,
        'origin_ysize':ysize,
        'save_path':save_file_path,
        'save_url':default_storage.url(save_file_path)
    }

    if rule.get('save_db',True):
        if rule.get('unique', False):
            
            try:
                obj = UFile.objects.get(user_id=uid,ftype=rule['type'])
                default_storage.delete(obj.fpath)#删除老图片
                obj.fpath = save_file_path
                obj.desc = desc
                obj.xsize = xsize
                obj.ysize = ysize
                obj.msize = upload_file.size
                obj.save()
            except UFile.DoesNotExist:
                obj = UFile.objects.create(user_id=uid,fpath=save_file_path,desc=desc,ftype=rule['type'],
                                        xsize=xsize,ysize=ysize,msize=upload_file.size)
        else:
            obj = UFile.objects.create(user_id=uid,fpath=save_file_path,desc=desc,ftype=rule['type'],
                                        xsize=xsize,ysize=ysize,msize=upload_file.size)
        file_info['obj_id'] = obj.id
        file_info['obj_desc'] = obj.desc

    error['data'] = file_info

    return error


def get_ueditor_settings(request):
    return HttpResponse(json.dumps(settings.UEditorUploadSettings,ensure_ascii=False), content_type="application/javascript")

def ueditor_controller(request):
    '''百度编辑器'''
    action=request.GET.get('action','')
    response_dict={
        'config':get_ueditor_settings,
        'uploadimage':ueditor_upload,
    }
    action = action or 'config'
    return response_dict[action](request)


def ueditor_upload(request):
    '''文件上传'''
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    uid = request.session.get(auth.SESSION_KEY,0)
    return_info = {
        'state':'ERROR'
    }
    if uid:
        upload_file = request.FILES.get('upfile')
        upload_type = 'ueditor_image'
        upload_folder = request.POST.get('folder','')
        upload_name = ''

        rsp_data = __handel_file(upload_file,upload_type,upload_folder,upload_name,uid)

        if rsp_data['code'] == '10000':
            file_info = rsp_data['data']
            return_info = {
                'url': file_info['save_url'] ,                # 保存后的文件名称
                'original': file_info['origin_name'],                  #原始文件名
                'type': upload_file.name.split('.')[-1],
                'state': 'SUCCESS',                         #上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
                'size': file_info['origin_size']
            }
        else:
            return_info = {
                'state':'ERROR'
            }

    return HttpResponse(json.dumps(return_info),content_type="application/javascript")