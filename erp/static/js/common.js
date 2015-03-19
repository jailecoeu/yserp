/**
 * User: Yanjie.Chang
 * Date: 14-12-25
 */
var Erp = Erp || {};

Erp.code = {
     SUCC : '10000', //成功
     EXIST_ERR : '10006', // 未登录,
     ERR : '10001',  //未知错误
     NOT_LOGIN : '11004' // 未登录,

};

Erp.common = {

    //获取当前域名，带http:
    getHost: function(){
        return  window.location.protocol + '//' + window.location.host ;
    },

    /*通用分页回调函数*/
    paginationCallback:function(page_index, pagination_container){
        var new_page_index = page_index+1;
        window.location.href = Erp.utils.changeURLArg(window.location.href,'page',new_page_index);
        return false;
    },

    /*通用分页初始化函数*/
    initPagination:function(pagination_dom,total_count,page_size,current_page){

        $(pagination_dom).pagination(total_count, {
            items_per_page:page_size,
            current_page:current_page-1,
            callback: Erp.common.paginationCallback
        });
    }
 };

Erp.ajax = {
    /*
    登录
     */
    login: function(params,okCallback,errCallback){
        okCallback = okCallback || function(){};
        errCallback = errCallback || function(){};
        $.post('/account/login/', params, function(rsp_data) {
            if(Erp.code.SUCC === rsp_data.code) {
                okCallback();
            } else {
                errCallback();
            }
        });
    },

    /*
    fileupload 文件上传
     */
    fileUpload:function(btnDom,formData,okCallback,errCallback,startCallback){
        var startCallback = startCallback || function(){},
            okCallback = okCallback || function(){},
            errCallback = errCallback || function(){};

        $('' + btnDom).fileupload({
            url: "/userfiles/upload/",
            formData: formData||{},
            dataType: 'json',
            start:function(){
                startCallback();
            },
            done: function (e, data) {
                var rsp_data = eval(data);
                if(rsp_data.result.code == Erp.code.SUCC){
                    okCallback(rsp_data.result.data)
                }else{
                    Erp.common.alert(rsp_data.result.msg);
                    errCallback()
                }
            },
            progressall: function (e, data) {
            }
        })
    },

    createCarOrder:function(params,okCallback){
        $.ajax({
            url:'/car/api/order/create/',
            method:'POST',
            async:false,
            data: params,
            success:function(rsp_data){
                if(Erp.code.SUCC == rsp_data.code){
                    okCallback(rsp_data)
                } else{
                    alert(rsp_data.msg);
                }
            },
            error:function(){
                alert('error');
            }
        })
    },

    /*车型相关接口*/
    //获取 品牌
    getCarBrand:function(okCallback){
        var brand_list = [];
        $.ajax({
            url:'/system/api/car/brand/',
            async:false,
            success:function(rsp_data){
                if (Erp.code.SUCC == rsp_data.code){
//                    okCallback()
                    brand_list = rsp_data.data.brand;
                }
            }
        })
        return brand_list
    },

    getCarSeries:function(brand,okCallback){
        var series_list = [];
        $.ajax({
            url:'/system/api/car/series/',
            async:false,
            data:{'brand':brand},
            success:function(rsp_data){
                if (Erp.code.SUCC == rsp_data.code){
//                    okCallback()
                    series_list = rsp_data.data.series;
                }
            }
        })
        return series_list
    },

    getCarSeriesNo:function(brand,series,okCallback){
        var series_no_list = [];
        $.ajax({
            url:'/system/api/car/series_no/',
            async:false,
            data:{'brand':brand,'series':series},
            success:function(rsp_data){
                if (Erp.code.SUCC == rsp_data.code){
//                    okCallback()
                    series_no_list = rsp_data.data.series_no;
                }
            }
        })
        return series_no_list
    },

    getCarYears:function(brand,series,series_no){
        var years_list = [];
        $.ajax({
            url:'/system/api/car/years/',
            async:false,
            data:{'brand':brand,'series':series,'series_no':series_no},
            success:function(rsp_data){
                if (Erp.code.SUCC == rsp_data.code){
//                    okCallback()
                    years_list = rsp_data.data.years;
                }
            }
        })
        return years_list;
    },

     getCarConf:function(brand,series,series_no,years,okCallback){
         var conf_list = [];
         $.ajax({
             url:'/system/api/car/conf/',
             async:false,
             data:{'brand':brand,'series':series,'series_no':series_no,'years':years},
             success:function(rsp_data){
                 if (Erp.code.SUCC == rsp_data.code){
//                    okCallback()
                     conf_list = rsp_data.data.conf;
                 }
             }
         })
         return conf_list;
    },

    getCarVersion:function(brand,series,series_no,years,conf,okCallback){
        var version_list = [];
        $.ajax({
            url:'/system/api/car/version/',
            async:false,
            data:{'brand':brand,'series':series,'series_no':series_no,'years':years,'conf':conf},
            success:function(rsp_data){
                if (Erp.code.SUCC == rsp_data.code){
//                    okCallback()
                    version_list = rsp_data.data.version;
                }
            }
        })
        return version_list;
    },

    /*ajax 测试*/
    ajaxTest: function(params,method,async){
        var async = async || true,
            method = method || 'GET';
        $.ajax({
            url:params.url,
            method:method,
            async:async,
            data: params.data,
            success:function(rsp_data){
//                console.log(rsp_data);
            },
            error:function(){
                alert('error');
            }
        })
    }
}

Erp.utils = {

    //载入模块
    use: function(module, callback){
        var i = 0, head = $('head')[0];
        var module = module.replace(/\s/g, '');
        var iscss = /\.css$/.test(module);
        var node = document.createElement(iscss ? 'link' : 'script');
        var id = module.replace(/\.|\//g, '');
        if(iscss){
            node.type = 'text/css';
            node.rel = 'stylesheet';
        }
        node[iscss ? 'href' : 'src'] = /^http:\/\//.test(module) ? module : Erp.common.getHost() + module;
        node.id = id;
        if(!$('#'+ id)[0]){
            head.appendChild(node);
        }
        if(callback){
            if(document.all){
                $(node).ready(callback);
            } else {
                $(node).load(callback);
            }
        }
    },
    /*
     * 判断是否为数字
     */
    isNum: function(s) {
        if(s != null && s != "") {
            return !isNaN(s);
        }
        return false;
    },

    /*
     * 转换为数字
     */
    intval: function(v) {
        v = parseInt(v);
        return isNaN(v) ? 0 : v;
    },

    /*
     * 合法Email
     */
    isEmail: function(str) {
        return /^([.a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(str);
    },

    /*
     * 合法手机号
     */
    isPhone: function(str) {
        return /^1(3|4|5|7|8)[0-9]\d{9}$/.test(str);
    },

    /*
     * 反序列化参数串
     */
    parseParams: function(str) {
        var params = {},
            e,
            a = /\+/g,
            r = /([^&=]+)=?([^&]*)/g,
            d = function (s) { return decodeURIComponent(s.replace(a, " ")); };

        while (e = r.exec(str))
            params[d(e[1])] = d(e[2]);

        return params;
    },

    /*
     * Timeago 相对时间  2011-05-06 12:30:22  ---> 三分钟之前
     */
    prettyDate: function(time){
        var date = new Date((time || "").replace(/-/g,"/").replace(/[TZ]/g," ")),
            diff = (((new Date()).getTime() - date.getTime()) / 1000),
            day_diff = Math.floor(diff / 86400);

        if ( isNaN(day_diff) || day_diff < 0 || day_diff >= 31 )
            return;

        return day_diff == 0 && (
            diff < 60 && "刚刚" ||
                diff < 120 && "1分钟前" ||
                diff < 3600 && Math.floor( diff / 60 ) + "分钟前" ||
                diff < 7200 && "1个小时前" ||
                diff < 86400 && Math.floor( diff / 3600 ) + "小时前") ||
            day_diff == 1 && "昨天" ||
            day_diff < 7 && day_diff + "天前" ||
            day_diff < 31 && Math.ceil( day_diff / 7 ) + "周前";
    },

    changeURLArg: function changeURLArg(url, arg, arg_val) {
        if(url.indexOf('#')){
            url = url.split('#')[0]
        }
        var pattern = arg + '=([^&]*)';
        var replaceText = arg + '=' + arg_val;
        if (url.match(pattern)) {
            var tmp = '/(' + arg + '=)([^&]*)/gi';
            tmp = url.replace(eval(tmp), replaceText);
            return tmp;
        } else {
            if (url.match('[\?]')) {
                return url + '&' + replaceText;
            } else {
                return url + '?' + replaceText;
            }
        }
        return url + '\n' + arg + '\n' + arg_val;
    },
    
    /*
     * 中文链接编码 
     */
    b64EncodeUrl: function b64EncodeUrl(string) {
    	if (window.BASE64) {
    		return BASE64.encoder(string).replace('+', '-').replace('/', '_').replace('=', '');
    	}
    	return string
    }
};

Erp.init = {};