/**
 * 提示框
 * @param text
 * @param icon
 * @param hideAfter

  myAlert("成功样式！", "success", 2000);
  myAlert("提示样式！", "info", 2000);
  myAlert("警告样式！", "warning", 2000);
  myAlert("错误样式！", "error", 2000);
 */
function myAlert(text, icon, hideAfter) {
    if(icon === undefined){
        icon = "info"
    }

    if(hideAfter === undefined){
        hideAfter = 2000
    }

    $.toast({
        text: text,//消息提示框的内容。
        heading: "提示",//消息提示框的标题。
        icon: icon,//消息提示框的图标样式。
        showHideTransition: 'fade',//消息提示框的动画效果。可取值：plain，fade，slide。
        allowToastClose: true,//是否显示关闭按钮。(true 显示，false 不显示)
        hideAfter: hideAfter,//设置为false则消息提示框不自动关闭.设置为一个数值则在指定的毫秒之后自动关闭消息提框
        stack: 1,//消息栈。同时允许的提示框数量
        position: 'top-center',//消息提示框的位置：bottom-left, bottom-right,bottom-center,top-left,top-right,top-center,mid-center。
        textAlign: 'left',//文本对齐：left, right, center。
        loader: true,//是否显示加载条
        //bgColor: '#FF1356',//背景颜色。
        //textColor: '#eee',//文字颜色。
        loaderBg: '#ffffff',//加载条的背景颜色。

        beforeShow: function(){

        },

        afterShown: function () {

        },

        beforeHide: function () {

        },

        afterHidden: function () {

        }

        /*toast事件
        beforeShow 会在toast即将出现之前触发
        afterShown 会在toast出现后触发
        beforeHide 会在toast藏起来之前触发
        afterHidden 会在toast藏起来后被触发
        */
    });
}