(function(a){"use strict";function b(b){var c=null;if(document.cookie&&document.cookie!==''){var d=document.cookie.split(';');for(var e=0;e<d.length;e++){var f=a.trim(d[e]);if(f.substring(0,b.length+1)===(b+'=')){c=decodeURIComponent(f.substring(b.length+1));break;}}}return c;}var c=b('csrftoken');function d(a){return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(a));}a.ajaxSetup({beforeSend:function(a,b){if(!d(b.type)&&!this.crossDomain)a.setRequestHeader("X-CSRFToken",c);}});})(jQuery);(function(a){if(typeof define==="function"&&define.amd)define(["../widgets/datepicker"],a);else a(jQuery.datepicker);}(function(a){a.regional["zh-TW"]={closeText:"關閉",prevText:"&#x3C;上個月",nextText:"下個月&#x3E;",currentText:"今天",monthNames:["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"],monthNamesShort:["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"],dayNames:["星期日","星期一","星期二","星期三","星期四","星期五","星期六"],dayNamesShort:["週日","週一","週二","週三","週四","週五","週六"],dayNamesMin:["日","一","二","三","四","五","六"],weekHeader:"週",dateFormat:"yy/mm/dd",firstDay:1,isRTL:false,showMonthAfterYear:true,yearSuffix:"年"};a.setDefaults(a.regional["zh-TW"]);return a.regional["zh-TW"];}));$(function(){$('.LangDropdown ul.dropdown-menu a').click(function(a){console.log($(this).data('lang'));var b=$(this);$('#language-select').val(b.data('lang')).parents('form').submit();console.log($('#language-select').val());});});