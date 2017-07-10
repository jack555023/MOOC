$(function() {
	// $('.dateinput').datepicker($.datepicker.regional[""]);
	/* Set the correct language option to the hidden form and submit. */
	$('.LangDropdown ul.dropdown-menu a').click(function(e) {
		console.log($(this).data('lang'));
		var $this = $(this);
		$('#language-select')
			.val($this.data('lang'))
			.parents('form').submit();
		console.log($('#language-select').val());
		// if($('#language-select').val() == 'zh-hant')
		// 	$('.dateinput').datepicker($.datepicker.regional["zh-TW"]);
		// if($('#language-select').val() == 'en')
		// 	$('.dateinput').datepicker($.datepicker.regional[""]);
	});
    
});
