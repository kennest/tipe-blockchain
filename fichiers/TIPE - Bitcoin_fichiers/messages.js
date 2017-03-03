define("widgets/messageList",["jquery","app/core","widgets/baseWidget"],function(a,b,c){"use strict";return a.widget("OC.messageList",c,{options:{},_create:function(){this._super(),this.elements.$toggleAll=a(".js-list-msg-toggleall",this.element),this.elements.$selectedMsg=a(".js-list-msg-selectedtext",this.element),this.elements.$selectAll=a(".js-list-msg-selectalltext",this.element),this._attachEvents()},_attachEvents:function(){var b=this;a(this.element).on("click",".js-list-msg-selectalltext",function(){b.toggleMessages(!0)}).on("change",".js-list-msg-toggleall",function(){b.toggleMessages(a(this).is(":checked"))}).on("change",".js-list-msg-toggle",function(){var c=a(this);b.toggleMessages(c.is(":checked"),c.parents("tr"))})},_updateDisplay:function(){var a=this.getSelectedAmount(),b=a>0;this.element.toggleClass("list-msg--selected",b),this._updateSelectedText(),this._trigger("select",null,{amount:a})},_updateSelectedText:function(){var a=this.getSelectedAmount(),c=this.getItemAmount(),d=1===a?"<strong>1</strong> message sélectionné.":"<strong>"+a+"</strong> messages sélectionnés.";this.elements.$selectedMsg.html(d),this.elements.$selectAll.html(b.string.format(this.elements.$selectAll.html(),c)).toggle(c>a)},toggleMessages:function(b,c){c?c=a(c):(c=a("tbody tr",this.element),b&&this.elements.$toggleAll.prop("checked",!0)),c.toggleClass("list-msg__item--selected",b).find(".js-list-msg-toggle").prop("checked",b),this._updateDisplay()},getSelectedAmount:function(){return a(".js-list-msg-toggle:checked",this.element).length},getItemAmount:function(){return a("tbody tr",this.element).length}}),a.OC.messageList}),define("widgets/threadPost",["jQuery","widgets/baseWidget"],function(a,b){"use strict";return a.widget("OC.threadPost",b,{options:{},_create:function(){this._super(),this._attachEvents(),this.content=this.element.find(".js-post-content").html().trim()},_attachEvents:function(){var a=this;this.element.on("click",".js-action-quote",function(b){b.preventDefault(),a.quote()})},quote:function(){var b=a.extend(this.getData(),{action:"quote"});this._trigger("action",null,b)},getData:function(){var a=this.element,b=a.find(".js-post-author").text().trim(),c=this.content;return{author:b,content:c}}}),a.OC.threadPost}),define("modules/pm-list",["jQuery","app/core","modules/confirm","common/commands","common/pubsub"],function(a,b,c,d,e){"use strict";function f(c,d){var e=1===d?"Supprimer ce message":"Supprimer {0} messages",f=1===d?"Êtes-vous sûr de vouloir supprimer ce message privé&nbsp;?":"Êtes-vous sûr de vouloir supprimer ces {0}&nbsp;messages privés&nbsp;?";c.toggleClass("pm-actions--can-delete",!!d),a(".js-pm-actions-delete-txt").text(b.string.format(e,d)),a(".js-confirm-pm-delete").data("message",b.string.format(f,d))}d.execute("registerAnchor",["/new",function(){a(function(){e.publish("thread.post.action",{action:"new"})})}]),a(function(){var b=a(".js-pm-actions"),d=a(".js-list-msg");d.messageList({select:function(a,c){f(b,c.amount)}}),a(".js-confirm-pm-delete").on("click",function(){c.show({element:this,confirmCallback:function(){d.closest("form").submit()}})})})}),define("modules/postsList",["jQuery","common/pubsub","widgets/threadPost"],function(a,b,c){"use strict";function d(a){var d={action:function(a,c){b.publish("thread.post.action",c)}};a.each(function(a,b){new c(d,b)})}a(function(){d(a(".js-thread-post")),a(".js-threadpost-new").on("click",function(){b.publish("thread.post.action",{action:"new"})}),a(".oc-form .error").length>0&&b.publish("thread.post.action",{action:"post-errors"})})}),define("modules/postWrite",["jQuery","common/pubsub","widgets/tagsSelect","bridge/modules/tinymce"],function(a,b,c,d){"use strict";var e=null,f=function(b,c){var f=!1,g=[];c||(c=a(".js-wysiwyg-content")),c.each(function(b,c){a(c).is(":visible")&&(f=!0)}),c.length&&f&&(c.each(function(c,f){var h=a("textarea",f);d.isElementInited(h)?b():(h.prop("required",!1),e||(e=h),g.push(h))}),d.add(g,null,b))},g=function(){var b=a(".js-user-select"),d=b.parent().find("label"),e='<a>  <img class="thumbnail" src="<%= avatar %>"/>  <span><%- username %></span></a>',f={dataMap:{label:"username",value:"username",icon:"avatar"},itemTemplate:e,change:function(){var b=a(this).tagsSelect("getItems").length;d.text(d.data("i18n")[2>b?0:1])},select:function(a,b){a.stopPropagation()}},g=a(".js-user-select").get(0);g&&new c(f,a(".js-user-select"))},h=function(a){var b="<blockquote><cite>"+a.author+" a écrit:</cite><div>"+a.content+"</div></blockquote>";return b},i=function(b){a("html, body").animate({scrollTop:b.offset().top},250)},j=function(b,c){var g=a(".js-write-thread-form").eq(0);g.is(":visible")||g.addClass("write-thread-form--opened"),f(function(){b&&(d.getInstance(e).setContent(b),(c||a.noop)())}),i(g)};a(function(){f(),g()}),b.subscribe("thread.post.action",function(a,b){var c=b.action;switch(c){case"quote":e&&j(e.val()+h(b),function(){var a,b=d.getInstance(e),c=tinymce.DOM.uniqueId();b.dom.add(b.getBody(),"span",{id:c},'<br data-mce-bogus="1" />'),a=b.dom.select("span#"+c),b.selection.select(a[0]),b.focus()});break;case"post-errors":case"new":j()}})});