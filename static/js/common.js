/**
 * Created by ms on 2016/9/25.
 */

//登录验证
$('#login_button').click(
function () {
    var email = $('#login_email').val();
    var password = $('#login_password').val();
    if(email ==""||password==""){
        $('#login_error').text("账号密码不能为空")
    }
    else {
        $.ajax({
            url: "/login_check/",
            data:{username:email,password:password},
            datatype: 'json',
            success: function (data) {
                if (data.info == "None") {
                    $('#login_error').text("账号密码错误")
                }
                else{
                    window.location.reload()
                }
            },
            error: function () {
                $('#login_error').text("登录失败，请重试")
            }
        }
        );
    }

}
);


//用户注册
$('#reg_button').click(
function () {
    var reg = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$/;
    var email = $('#reg_email').val();
    var password = $('#reg_password').val();
    if(email==""||password==""){
        $('#reg_error').text("账号密码不能为空")
    }
    else if(!reg.test(email)){
        $('#reg_error').text("邮箱格式不正确")
    }
    else if(password.length < 8){
        $('#reg_error').text("密码最小长度8位")
    }
    else {
        $.ajax({
            url: "/register/",
            data:{username:email},
            datatype: 'json',
            success: function (data) {
                if (data.info == 'exist') {
                    $('#reg_error').text("账号已存在")
                }
                else if(data.info == 'ok'){
                    window.location.reload()
                }
            },
            error: function () {
                $('#reg_error').text("注册失败，请重试")
            }
        }
        );
    }

}
);

//找回密码
$('#forget_button').click(
function () {
    var reg = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$/;
    var email = $('#forget_passwd').val();
    if(email==""){
        $('#forget_error').text("请填写邮箱账号")
    }
    else if(!reg.test(email)){
        $('#forget_error').text("邮箱格式不正确")
    }
    else {
        alert("正在提交");
        $.ajax({
            url: "/forgot_password/",
            data:{username:email},
            datatype: 'json',
            success: function (data) {
                if (data.info == 'non-existent') {
                    $('#forget_error').text("账号未注册")
                }
                else if(data.info == 'ok'){
                    alert("找回密码申请成功，请登录邮箱进行验证")
                    window.location.reload()
                }
            },
            error: function () {
                $('#forget_error').text("找回密码失败，请重试")
            }
        }
        );
    }

}
);

//职业课程搜索
 $('#search').bind('input propertychange',function () {
var com_input = $("#search").val();
if(com_input!=''){
    $.ajax(
        {
            url: '/careercourse/',
            async: true,
            dataType: 'json',
            data:{com_input:com_input},
            success: function (data) {
                    $('#course_list1').empty();
                    $.each(data, function (index, content) {
                    var img = $('<img src=' +content.img +'>');
                    var a = $('<a href="" style="background-color:#A8C310;">'+ '<img src=' + content.img +'>' +" " +content.info + '</a>');
                    $("#course_list1").append(a);

                        $('#course_list1').children("a").click(
                    function () {
                        $('#search').val($(this).text());
                        $('#keyword-group').hide()
                         });
                    });
                    $('#keyword-group').show();

                }
        }
        )
    }
else{
    $('#course_list1').empty();
    $('#keyword-group').hide();
    }
});

//小课程搜索
$('#search').bind('input propertychange',function () {
var com_input = $("#search").val();
if(com_input!=''){
    $.ajax(
        {
            url: '/small_course/',
            async: true,
            dataType: 'json',
            data:{com_input:com_input},
            success: function (data) {
                    $('#course_list2').empty();
                    $.each(data, function (index, content) {
                    var a = $('<a href="" style="background-color:#A8C310;">' + content.info + '</a>');
                    $("#course_list2").append(a);

                        $('#course_list2').children("a").click(
                    function () {
                        $('#search').val($(this).text());
                        $('#keyword-group').hide()
                         });
                    });
                    $('#keyword-group').show();

                    }
            }
        )
    }
else{
    $('#course_list2').empty();
    $('#keyword-group').hide();
    }
});

// 找回密码修改
$('#change_pass_button').click(
function () {
    var password = $('#new_password').val();
    var password_again = $('#new_password_again').val();
    var user_email = $('#user_info').val();
    if( password==""||password_again==""){
        $('#pass_error').text("输入密码和确认密码不能为空")
    }
    else if(password!=password_again){
        $('#pass_error').text("输入密码和确认密码不同，请重新输入")
    }
    else if(password.length<8||password_again.length<8){
        $('#pass_error').text("密码最小长度不能小于8")
    }
    else {
        $.ajax({
            type:"POST",
            url: "/change_find_pass/",
            data:{username:user_email,password:password},
            datatype: 'json',
            success: function(){
                alert("密码修改成功，请重新登录");
                window.location.replace("/")
            },
            error: function () {
                $('#pass_error').text("修改密码失败，请重试")
                }
            }
        );
    }
}
);
