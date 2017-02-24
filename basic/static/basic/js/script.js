
$(document).ready(function(){
		    $('select').material_select();
	$('.bookings_form').on('click',function(){
	  	// alert($( this ).find( 'input' ).attr( "value"));
	  	$(this).find('form:first').submit();
			// alert($(this).find('input');
	});
	console.log('asd');
	
	$('.datepicker').pickadate({
	selectMonths: true, // Creates a dropdown to control month
	selectYears: 15, // Creates a dropdown of 15 years to control year
	format: 'yyyy-mm-dd',
	closeOnSelect: true,
	closeOnClear: true,
	});

});


$('.err').on('click', function(){
	alert('asd');
});