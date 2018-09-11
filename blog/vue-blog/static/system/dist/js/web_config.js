(function($, WebConfig){
    var app_box = $("#app-box");
    var web_skins = [
        "app-skin-black-header",
        "app-skin-black-aside",
        "app-skin-dark-header",
        "app-skin-dark-aside",
        "app-skin-blue-header",
        "app-skin-white-header",
        "app-skin-purple-header",
        "app-skin-purple",
        "app-skin-green-header",
        "app-skin-green",
        "app-skin-red-header",
        "app-skin-red",
        "app-skin-yellow-header",
        "app-skin-yellow"
    ];
    
    var default_config = {
        appHeaderFixed : true,
        appAsideFixed : true,
        container : true,
        appAsideFolded : false,
        appMusicPanel : true,
        web_skin : 'app-skin-dark-header',
        web_skin_num : 2,
    };
    var rest_config = {
        appHeaderFixed : true,
        appAsideFixed : true,
        container : true,
        appAsideFolded : false,
        appMusicPanel : true,
        web_skin : 'app-skin-dark-header',
        web_skin_num : 2,
    };
    
    /**
     * 切换皮肤
     */
    function change_skin(ele, cls, skin){
        $.cookie('web_skin', skin, { expires: 7, path: '/' });
        $.cookie('web_skin_num', ele.index(), { expires: 7, path: '/' });
        $("#web_skin .lists").removeClass(cls);
        if(ele){
            ele.addClass(cls);
        }
        for(var i= 0; i<web_skins.length; i++){
            app_box.removeClass(web_skins[i]);
        }
        app_box.addClass(skin);
        return false;
    }
    
    /**
     * 切换开关
     */
    function change_switch(ele, cls, val){
        ele.bootstrapSwitch('destroy');
        if(val === true){
            app_box.addClass(cls);
        }else{
            app_box.removeClass(cls);
        }
        if( cls == 'app-header-fixed' ){
            $.cookie('appHeaderFixed', val, { expires: 7, path: '/' });
        }else if( cls == 'app-aside-fixed' ){
            $.cookie('appAsideFixed', val, { expires: 7, path: '/' });
        }else if( cls == 'container' ){
            $.cookie('container', val, { expires: 7, path: '/' });
        }else if( cls == 'app-aside-folded' ){
            $.cookie('appAsideFolded', val, { expires: 7, path: '/' });
        }
        ele.bootstrapSwitch({
            state: val,
            size:'mini',
            onText: '开',
            offText: '关',
            onColor: 'info',
            offColor: 'danger',
            onSwitchChange: function(event, state){
                if( cls == 'app-header-fixed' ){
                    $.cookie('appHeaderFixed', state, { expires: 7, path: '/' });
                }else if( cls == 'app-aside-fixed' ){
                    $.cookie('appAsideFixed', state, { expires: 7, path: '/' });
                }else if( cls == 'container' ){
                    $.cookie('container', state, { expires: 7, path: '/' });
                }else if( cls == 'app-aside-folded' ){
                    $.cookie('appAsideFolded', state, { expires: 7, path: '/' });
                }
                if(state){
                    app_box.addClass(cls)
                }else{
                    app_box.removeClass(cls)
                }
            }
        });
    }
    
    /**
     * 音乐切换开关
     */
    function change_switch_music(ele, cls, val){
        ele.bootstrapSwitch('destroy');
        if(val === true){
            $("#jplayer-fixed").show();
        }else{
            $("#jplayer-fixed").hide();
        }
        $.cookie('appMusicPanel', val, { expires: 7, path: '/' });
        ele.bootstrapSwitch({
            state: val,
            size:'mini',
            onText: '开',
            offText: '关',
            onColor: 'info',
            offColor: 'danger',
            onSwitchChange: function(event, state){
                $.cookie('appMusicPanel', state, { expires: 7, path: '/' });
                if(state){
                    $("#jplayer-fixed").show();
                }else{
                    $("#jplayer-fixed").hide();
                }
            }
        });
    }
    
    function str_to_boolean(str){   //undefined
        if(str !== undefined){
            if( str === 'true' ){
                return true;
            }else if( str === 'false' ){
                return false;
            }else{
                return false;
            }
        }else{
            return false;
        }
    }
    
    function create(config){
        change_switch($("input[name='appheaderfixed']"), $("input[name='appheaderfixed']").data("val"), config.appHeaderFixed);
        change_switch($("input[name='appasidefixed']"), $("input[name='appasidefixed']").data("val"), config.appAsideFixed);
        change_switch($("input[name='appcontainer']"), $("input[name='appcontainer']").data("val"), config.container);
        change_switch($("input[name='appasidefolded']"), $("input[name='appasidefolded']").data("val"), config.appAsideFolded);
        change_switch_music($("input[name='appmusicpanel']"), $("input[name='appmusicpanel']").data("val"), config.appMusicPanel);
        change_skin($("#web_skin .lists").eq(config.web_skin_num), 'active', config.web_skin);
    }
    
    function WebConfigInit(){
        $('body').off('click', '.settings-handle');
        $('body').on("click", '.settings-handle', function(event){
            $("#settings").toggleClass("open");
            $(this).find('.fa').toggleClass("fa-spin");
        });
        
        $('body').off('click', '#web_skin .lists');
        $('body').on("click", '#web_skin .lists', function(event){
            change_skin($(this), 'active', $(this).data("skin"));
        });
        
        $('body').off('click', '#rest_web');
        $('body').on("click", '#rest_web', function(event){
            create(rest_config);
        });
        if( $.cookie('appHeaderFixed') ){
            default_config.appHeaderFixed = str_to_boolean($.cookie('appHeaderFixed'));
        }
        if( $.cookie('appAsideFixed') ){
            default_config.appAsideFixed = str_to_boolean($.cookie('appAsideFixed'));
        }
        if( $.cookie('container') ){
            default_config.container = str_to_boolean($.cookie('container'));
        }
        if( $.cookie('appAsideFolded') ){
            default_config.appAsideFolded = str_to_boolean($.cookie('appAsideFolded'));
        }
        if( $.cookie('appMusicPanel') ){
            default_config.appMusicPanel = str_to_boolean($.cookie('appMusicPanel'));
        }
        if( $.cookie('web_skin') ){
            default_config.web_skin = $.cookie('web_skin');
        }
        if( $.cookie('web_skin_num') ){
            default_config.web_skin_num = $.cookie('web_skin_num');
        }
        
        create(default_config);
    }
    
    WebConfigInit();
})(jQuery, $.WebConfig);