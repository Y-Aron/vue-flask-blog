webpackJsonp([9],{wua1:function(e,s,t){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var a=t("bGai"),r={components:{Group:a.d,VForm:a.g,Container:a.c},data:function(){return{title:this.$t("user.editTitle"),advanced:!0,lang:this.$t("user"),isEdit:!1,sex_options:[{value:0,text:"男"},{value:1,text:"女"}]}},computed:{user:{set:function(e){this.$store.commit("user/SET_USER",e)},get:function(){return this.$store.state.user.user}}},created:function(){var e=this.$route.query.id;e&&(this.isEdit=!0),this.$store.dispatch("user/fetchUser",e)},methods:{submit:function(){var e=this;this.user.password===this.user.repass?this.$store.dispatch("user/editUser").then(function(s){s&&e.$toast.success({title:"API 请求成功",message:s.error})}):this.$toast.warn({title:"form submit error ~",message:"password is equal of repass !"})}}},u={render:function(){var e=this,s=e.$createElement,t=e._self._c||s;return t("Container",{attrs:{title:e.title}},[t("v-form",{attrs:{advanced:e.isEdit},on:{submit:e.submit}},[t("template",{slot:"base"},[t("group",{attrs:{disabled:e.isEdit,label:e.lang.username,type:"input"},model:{value:e.user.username,callback:function(s){e.$set(e.user,"username",s)},expression:"user.username"}}),e._v(" "),e.isEdit?e._e():t("group",{attrs:{label:e.lang.password,type:"password"},model:{value:e.user.password,callback:function(s){e.$set(e.user,"password",s)},expression:"user.password"}}),e._v(" "),e.isEdit?e._e():t("group",{attrs:{label:e.lang.repass,type:"password"},model:{value:e.user.repass,callback:function(s){e.$set(e.user,"repass",s)},expression:"user.repass"}}),e._v(" "),t("group",{attrs:{label:e.lang.nickname,type:"input"},model:{value:e.user.nickname,callback:function(s){e.$set(e.user,"nickname",s)},expression:"user.nickname"}}),e._v(" "),t("group",{attrs:{label:e.lang.email,type:"input"},model:{value:e.user.email,callback:function(s){e.$set(e.user,"email",s)},expression:"user.email"}}),e._v(" "),t("group",{attrs:{label:e.lang.mobile,type:"input"},model:{value:e.user.mobile,callback:function(s){e.$set(e.user,"mobile",s)},expression:"user.mobile"}}),e._v(" "),t("group",{attrs:{label:e.lang.status,type:"status"},model:{value:e.user.status,callback:function(s){e.$set(e.user,"status",s)},expression:"user.status"}})],1),e._v(" "),t("template",{slot:"advanced"},[t("group",{attrs:{type:"image",label:e.lang.avatar},model:{value:e.user.avatar,callback:function(s){e.$set(e.user,"avatar",s)},expression:"user.avatar"}}),e._v(" "),t("group",{attrs:{type:"select",label:e.lang.sex,options:e.sex_options},model:{value:e.user.sex,callback:function(s){e.$set(e.user,"sex",s)},expression:"user.sex"}}),e._v(" "),t("group",{attrs:{type:"input",label:e.lang.qq},model:{value:e.user.qq,callback:function(s){e.$set(e.user,"qq",s)},expression:"user.qq"}}),e._v(" "),t("group",{attrs:{type:"date",label:e.lang.birthday},model:{value:e.user.birthday,callback:function(s){e.$set(e.user,"birthday",s)},expression:"user.birthday"}}),e._v(" "),t("group",{attrs:{type:"editor",label:e.lang.info},model:{value:e.user.info,callback:function(s){e.$set(e.user,"info",s)},expression:"user.info"}})],1)],2)],1)},staticRenderFns:[]},l=t("VU/8")(r,u,!1,null,null,null);s.default=l.exports}});
//# sourceMappingURL=9.f032ffa3e9e3cca98e9e.js.map