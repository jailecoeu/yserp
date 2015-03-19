$(function(){
    $('#state2_save').click(function(){  
        var params = {
            'no':$('#no').val(),
            'issue_time':$('#step2_issue_time').val(),
            'issue_money':$('#step2_issue_money').val() + '-' + $('#step2_issue_money_currency option:selected').val(),
            'agency':$('#step2_agency option:selected').val(),
            'warning_time':$('#step2_warning_time').val(),
            'issue_plan_money':$('#step2_issue_plan_money').val() + '-' + $('#step2_issue_plan_money_currency').val(),
            'issue_file_no':$('#step2_issue_file_no').val(),
            'agency_money':$('#step2_agency_money').val() + '-' + $('#step2_agency_money_currency option:selected').val(),
            'insurance_money':$('#step2_insurance_money').val() + '-' + $('#step2_insurance_money_currency').val(),
            'total_money':$('#step2_total_money').val() + '-' + $('#step2_total_money_currency option:selected').val(),
            'ensure_money':$('#step2_ensure_money').val() + '-' + $('#step2_ensure_money_currency option:selected').val(),
            'ensure_rate':$('#step2_ensure_rate').val(),
            'ensure_percent':$('#step2_ensure_percent').val()
        }
        Erp.ajax.createCarOrder(params,function(){
            window.location.href = '/car/list/';
        });
    })	
})