$(function(){

      var pageTop1 = $("#page-top1");
      pageTop1.click(function () {
        $('body, html').animate({ scrollTop: 0 }, 500);
        return false;
      });
      $(window).scroll(function () {

        if($(this).scrollTop() >= 200) {
          pageTop1.css( "bottom", "30px" );
        } else {
          pageTop1.css( "bottom", "-85px" );
        }
      });
    });
//
// $(function(){
//   var test = "http://localhost:8080/oki/{%row[0]%}";
//   $('#link').live("click", function(event){
//
//       $.ajax({
//         url: test,
//        });
//
//         event.preventDefault();
//    });
//
//   });

// $(function(){
//   $('#link').on('click', function(e){
//     $('#link img').attr('src', 'static/img/fab_out.png');
//     e.preventDefault();
//   });
//   $('#link').off('click', function(e){
//     $('#link img[src="static/img/fab_out.png"]').attr('src', 'static/img/logo-pic.png');
//     e.preventDefault();
//   });
// });
