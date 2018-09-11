$(function(){

    // $('body').off('click', '.aside-toggle');
    // $('body').on("click", '.aside-toggle', function(event){
    //     $('#app-box').toggleClass('app-aside-folded');
    // });

    // $('body').off('click', '.sidebar-menu > li.treeview > a');
    // $('body').on("click", '.sidebar-menu > li.treeview > a', function(event){
    //     var _this = $(this);
    //     var _checkElement = _this.next();
    //     var _parent = _this.parent("li");
    //
    //     if( _parent.hasClass('active') ){
    //         _checkElement.slideUp();
    //         _parent.removeClass("active");
    //     }else{
    //         $('.sidebar-menu li.treeview').removeClass("active");
    //         $('.sidebar-menu li.treeview ul').slideUp();
    //         _parent.addClass("active");
    //         _checkElement.slideDown()
    //     }
    // });

    // _initLoadPlugin()

})

function _initLoadPlugin(){
    $("[data-toggle='tooltip']").tooltip();     //title提示框
}
