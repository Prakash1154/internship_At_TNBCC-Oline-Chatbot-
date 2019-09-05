function myFunction() 
{

 var x= document.getElementById("Form").value;
 senddata(x)
}
function senddata(value)
{
	$.ajax({ 
 url : '/',
type : 'GET', 
 { "value" : value },success : function(data) { }
});
}