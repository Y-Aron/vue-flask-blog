webpackJsonp([3],{stFo:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=s("bGai"),c={components:{Checkbox:o.b,VTd:o.h,Container:o.c,List:o.e},data:function(){return{lang:this.$t("comment"),guestbook:!1,checked:!1,tgCheck:!1}},watch:{checkbox:function(t){var e=t.length;e===this.list.length&&(this.tgCheck=!0),0===e&&(this.tgCheck=!1)},$route:"fetchList"},computed:{title:function(){return this.guestbook?this.$t("comment.guestbookIndex"):this.$t("comment.index")},list:function(){return this.$store.state.table.list},checkbox:{get:function(){return this.$store.state.table.checkbox},set:function(t){this.$store.commit("table/SET_CHECKBOX",t)}}},methods:{changeState:function(t){var e=t.status?1:-1,s={id:t.id,status:e};this.$store.dispatch("comment/refState",s)},fetchList:function(){this.guestbook=this.$route.meta.guestbook;var t="";t=this.guestbook?"/api/comment/guestBook/index":"/api/comment/archive/index",this.$store.commit("table/SET_URL",t),this.$store.dispatch("table/fetchList")}},mounted:function(){this.fetchList()}},a={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("container",{attrs:{title:t.title}},[s("list",{attrs:{"show-del":!0}},[s("thead",{attrs:{slot:"thead"},slot:"thead"},[s("tr",[s("th",{attrs:{width:"35"}},[s("checkbox",{attrs:{checked:t.tgCheck},model:{value:t.checked,callback:function(e){t.checked=e},expression:"checked"}})],1),t._v(" "),s("th",[t._v(t._s(t.lang.id))]),t._v(" "),t.guestbook?t._e():s("th",[t._v(t._s(t.lang.arc_title))]),t._v(" "),s("th",[t._v(t._s(t.lang.username))]),t._v(" "),s("th",[t._v(t._s(t.lang.reply_target))]),t._v(" "),s("th",[t._v(t._s(t.lang.email))]),t._v(" "),t.guestbook?t._e():s("th",[t._v(t._s(t.lang.create_time))]),t._v(" "),t.guestbook?s("th",[t._v(t._s(t.lang.message_time))]):t._e(),t._v(" "),s("th",[t._v(t._s(t.lang.status))]),t._v(" "),s("th",{attrs:{width:"125"}},[t._v(t._s(t.$t("operation.name")))])])]),t._v(" "),s("tbody",{attrs:{slot:"tbody"},slot:"tbody"},t._l(t.list,function(e){return s("tr",[s("td",[s("checkbox",{attrs:{checked:t.checked,value:e.id},model:{value:t.checkbox,callback:function(e){t.checkbox=e},expression:"checkbox"}})],1),t._v(" "),s("td",[t._v(t._s(e.id))]),t._v(" "),t.guestbook?t._e():s("td",[t._v(t._s(e.title))]),t._v(" "),s("td",[t._v(t._s(e.username))]),t._v(" "),s("td",[t._v(t._s(e.reply_target))]),t._v(" "),s("td",[t._v(t._s(e.email))]),t._v(" "),s("td",[t._v(t._s(e.create_time))]),t._v(" "),s("td",[s("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},on:{change:function(s){t.changeState(e)}},model:{value:e.status,callback:function(s){t.$set(e,"status",s)},expression:"vol.status"}})],1),t._v(" "),s("v-td",{attrs:{type:"opt","edit-route":"comment_edit",guestbook:t.guestbook,value:e.id}})],1)}))])],1)},staticRenderFns:[]},i=s("VU/8")(c,a,!1,null,null,null);e.default=i.exports}});
//# sourceMappingURL=3.2ed177cdf0988919c73a.js.map