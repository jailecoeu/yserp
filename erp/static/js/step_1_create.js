/*新建项目*/
$(function(){
    $('#car_order_create').click(function(){
        var params = {
            'no':$('#no').val(),
            'supplier_no':$('#car_supplier_no').val(),
            'supplier':$('#car_supplier').val(),
            'customer':$('#car_customer').val(),
            'order_no':$('#car_order_no').val(),
            'seat_num':$('#car_seat_num').val(),
            'key_num':$('#car_key_num').val(),
            'car_type':$('#car_version').val(),
            'car_type_remark':$('#car_color').val(),
            'car_conf_detail':$('#car_conf_detail').val(),
            'made_time':$('#car_made_time').val(),
            'vin':$('#car_vin').val(),
            'engine_no':$('#car_engine_no').val(),
            'tire_size':$('#car_tire_size').val(),
            'price':$('#car_price').val(),
            'currency':$('#car_currency').val(),
            'rate':$('#car_currency_rate').val(),
            'overseas_deposit':$('#car_overseas_deposit').val() + '-' + $('#overseas_deposit_currency').val() ,
            'china_deposit':$('#car_china_deposit').val() + '-' + $('#china_deposit_currency').val(),
            'contract_money':$('#car_contract_money').val() + '-' + $('#contract_money_currency').val()
        }
        Erp.ajax.createCarOrder(params,function(){
            window.location.href = '/car/list/';
        });
    })

    function init_brand_select(){
        var option_html = '<option value="">品牌</option>';
        var data_list = Erp.ajax.getCarBrand();
        $.each(data_list,function(i,item){
            option_html +='<option value="' + item.name +  '">' + item.name + '</option>';
        })

        $('#car_brand').html(option_html);
    }

    function init_series_select(brand){
        var option_html = '<option value="">系列</option>';
        if(brand){
            var data_list = Erp.ajax.getCarSeries(brand);
            $.each(data_list,function(i,item){
                option_html +='<option value="' + item.name +  '">' + item.name + '</option>';
            })
        }
        $('#car_series').html(option_html);
    }

    function init_series_no_select(brand,series){
        var option_html = '<option value="">车型</option>';
        if(brand && series){
            var data_list = Erp.ajax.getCarSeriesNo(brand,series);
            $.each(data_list,function(i,item){
                option_html +='<option value="' + item.name +  '">' + item.name + '</option>';
            })
        }
        $('#car_series_no').html(option_html);
    }

    function init_years_select(brand,series,series_no){
        var option_html = '<option value="">年款</option>';
        if(brand && series){
            var data_list = Erp.ajax.getCarYears(brand,series,series_no);
            $.each(data_list,function(i,item){
                option_html +='<option value="' + item.name +  '">' + item.name + '</option>';
            })
        }
        $('#car_years').html(option_html);
    }

    function init_conf_select(brand,series,series_no,years){
        var option_html = '<option value="">配置</option>';
        if(brand && series && series_no && years){
            var data_list = Erp.ajax.getCarConf(brand,series,series_no,years);
            $.each(data_list,function(i,item){
                option_html +='<option value="' + item.name +  '">' + item.name + '</option>';
            })
        }
        $('#car_conf').html(option_html);
    }

    function init_version_select(brand,series,series_no,years,conf){
        var option_html = '<option value="0">版本</option>';
        if(brand && series && series_no && conf){
            var data_list = Erp.ajax.getCarVersion(brand,series,series_no,years,conf);
            $.each(data_list,function(i,item){
                option_html +='<option value="' + item.id +  '">' + item.name + '</option>';
            })
        }
        $('#car_version').html(option_html);
    }


    $('#car_brand').change(function(){
        init_series_select($('#car_brand').val());
        init_series_no_select($('#car_brand').val(),$('#car_series').val());
        init_years_select();
        init_conf_select();
        init_version_select();
    })

    $('#car_series').change(function(){
        init_series_no_select($('#car_brand').val(),$('#car_series').val());
        init_years_select();
        init_conf_select();
        init_version_select();
    })

    $('#car_series_no').change(function(){
        init_years_select($('#car_brand').val(),$('#car_series').val(),
            $('#car_series_no').val());
        init_conf_select();
        init_version_select();
    })

    $('#car_years').change(function(){
        init_conf_select($('#car_brand').val(),$('#car_series').val(),
            $('#car_series_no').val(),$('#car_years').val());
        init_version_select();
    })

    $('#car_conf').change(function(){
        init_version_select($('#car_brand').val(),$('#car_series').val(),
            $('#car_series_no').val(),$('#car_years').val(),$('#car_conf').val())
    })
})