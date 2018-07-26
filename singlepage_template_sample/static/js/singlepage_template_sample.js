$(function() {
    $('html,body').animate({ scrollTop: 0 }, '1');
    $('#intro .image_back').css({ opacity: 1 });
    $('#intro .image_back').css('transform', 'translate3d(-50%, -314px, 0px)' + 'scale(1.19674)');
});

$(function() {
  var scrolltop = $('#scrolltop');
  $('#scrolltop').on('click', function() {
    $('html, body').animate({
      scrollTop: 0
    }, 500);
    return false;
  });
});

$(function() {
  var scrolltop = $('a.scroll');
  $('a.scroll').on('click', function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1000);
    return false;
  });
});

$(function(){
  $('#iphone_topic .topic .topic_main .iphone_img').each(function(){
    $win = $(window),
    $winH = $win.height(),
    $this = $(this),
    main = $this.offset().top,
    iphone = 0,
    scroll = $win.scrollTop();
  $win.on('load scroll', function() {
      scroll = $win.scrollTop();
      if (scroll < 397.2) {
        iphone = -332 ;
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 397.2 && scroll < 404.4) {
        iphone = - (332 * 2);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 404.4 && scroll < 411.6 ) {
        iphone = - (332 * 3);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 411.6 && scroll < 418.8) {
        iphone = - (332 * 4);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 418.8 && scroll < 426) {
        iphone = - (332 * 5);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 426 && scroll < 433.2) {
        iphone = - (332 * 6);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 433.2 && scroll < 440.4) {
        iphone = - (332 * 7);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 440.4 && scroll < 447.6) {
        iphone = - (332 * 8);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 447.6 && scroll < 454.8) {
        iphone = - (332 * 9);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 454.8 && scroll < 462) {
        iphone = - (332 * 10);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 462 && scroll < 469.2) {
        iphone = - (332 * 11);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 469.2 && scroll < 476.4) {
        iphone = - (332 * 12);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 476.4 && scroll < 483.6) {
        iphone = - (332 * 13);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 483.6 && scroll < 490.8) {
        iphone = - (332 * 14);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 490.8 && scroll < 498) {
        iphone = - (332 * 15);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 498 && scroll < 505.2) {
        iphone = - (332 * 16);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 505.2 && scroll < 512.4) {
        iphone = - (332 * 17);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 512.4 && scroll < 519.6) {
        iphone = - (332 * 18);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 519.6 && scroll < 526.8) {
        iphone = - (332 * 19);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 526.8 && scroll < 534) {
        iphone = - (332 * 20);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 534 && scroll < 541) {
        iphone = - (332 * 21);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 541 && scroll < 553) {
        iphone = - (332 * 22);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 553 && scroll < 565) {
        iphone = - (332 * 23);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 565 && scroll < 575) {
        iphone = - (332 * 24);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 575 && scroll < 585) {
        iphone = - (332 * 25);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 585 && scroll < 590) {
        iphone = - (332 * 26);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 590 && scroll < 595) {
        iphone = - (332 * 27);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 595 && scroll < 600) {
        iphone = - (332 * 28);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll >= 600 ) {
        iphone = - (332 * 29);
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' '+ iphone +'px ');
      } else if (scroll < 390) {
        $('#iphone_topic .topic .topic_main .iphone_img').css('background-position', ' 0px '+' 0px');
      }
    });
  });
});

$(function() {
  $('div.image_back').each(function() {
      $win = $(window),
      $winH = $win.height(),
      $this = $(this),
      header_top = $this.offset().top,
      header_topic = 0,
      header_topic_check = 0,
      scroll = $win.scrollTop();
    $win.on('load scroll', function() {
      scroll = $win.scrollTop() ;
      header_topic = (1 - (header_top - scroll * 1.5) / $winH) * 2;
      header_topic_check = header_topic - 4.68;
      if (scroll >= 390 && scroll < 600) {
        // $('.scrollTopj').text(scroll);
        $('header.iphone_header').css({opacity: header_topic_check});
        $('div.topic').removeClass('topic_sub');
        $('#iphone_topic').removeClass('fixed seen');
        $('div.video').css({opacity: 0});
      } else if (scroll >= 600 && scroll < 650) {
        // $('.scrollTopg').text(scroll);
        $('header.iphone_header').css({opacity: 1});
        $('div.video').css({opacity: 1});
        $('div.topic').addClass('topic_sub');
        $('#iphone_topic').addClass('fixed seen');
        // $('#iphone_topic div.topic_sub').css('position', 'fixed');
      } else if (scroll >= 650 && scroll < 800) {
        $('.scrollTopf').text(scroll);
        // $('#iphone_topic div.topic_sub').css('position', 'relative');
        $('#iphone_topic').removeClass('fixed');
        $('#main_content').removeClass('seen');
      } else if (scroll >= 800 ) {
        // $('.scrollTope').text(scroll);
        $('#main_content').addClass('seen');
      } else if (scroll < 390) {
        // $('.scrollTopq').text(scroll);
        $('header.iphone_header').css({opacity: 0});
        $('div.video').css({opacity: 0});
        $('div.topic').removeClass('topic_sub');
        $('#iphone_topic').removeClass('seen');
      }
    });
  });
});

$(function() {
  $('div.image_back').each(function() {
      $win = $(window),
      $winH = $win.height(),
      $this = $(this),
      test = $this.offset().top,
      image = 0,
      image_change_test = 0,
      image_change = 0,
      img_change = 0,
      header_text = 0,
      header_img = 0,
      header_image = 0,
      header_text_after = 0,
      header_img_after = 0,
      header = 0,
      img = 0,
      scroll = $win.scrollTop();
    $win.on('load scroll', function() {
      scroll = $win.scrollTop() ;
      image = (1 - (test - scroll * 1.2) / $winH) * 2;
      image_sub = (1 - (test - scroll * 1.275) / $winH) * 2;
      header_img = (1 - (test - scroll * 2.5) / $winH) * 0.2;
      header_image = (1 - (test - scroll * 2.3) / $winH) * 2;
      if (scroll == 0 ){
        scroll = $win.scrollTop() ;
        // $('.scrollTopq').text(scroll);
        img_change = 4.05 - image_sub;
        $('ul.menu_after').css({opacity: 0});
        $('div.top_bar').css({opacity: 0});
        $('div.image_back').css({opacity: 1});
        $('div.image_back').css('transform', 'translate3d(-50%, -314px, 0)' + 'scale('+ img_change +')');
      }
      if (image > 1) {
        image_back = image - 3.0;
        img = 4.05 - image_sub;
        header = 4.05 - header_image;
        header_text = header_img;
        image_change = scroll * 2.1;
        image_change_test = image_change - 314;
      }
      if (header > 0.0046242 && scroll > 0) {
        scroll = $win.scrollTop() ;
        image_change = scroll * 2.017;
        image_change_test = image_change - 314;
        // $('.scrollTope').text(test);
        // $('.scrollTopa').text(image);
        // $('.scrollTopc').text(scroll);
        // $('.scrollTopd').text(header);
        $('img.image_back_home').css({opacity: image_back});
        $('img.image_back_check').css({opacity: image_back});
        $('img.image_back_bar').css({opacity: image_back});
        $('div.header_top').css({opacity: header});
        $('div.header_top').css('z-index', '30');
        $('div.inner_text').css({opacity: header});
        $('ul.menu_after').css({opacity: 0});
        $('div.top_bar').css({opacity: 0});
        $('div.image_back').css({opacity: 1});
        $('div.image_back').css('transform', 'translate3d(-50%, '+ image_change_test +'px, 0)' + 'scale('+ img + ')');
      } else if (header <= 0.0046242 && header > -0.7398843930635843 ) {
        scroll = $win.scrollTop() ;
        // $('.scrollTopf').text(header_text);
        // $('.scrollTopc').text(scroll);
        // $('.scrollTopd').text(header);
        image_change = scroll * 2.017;
        image_change_test = image_change - 314;
        image = (1 - (test - scroll * 1.8) / $winH) * 2;
        header_text_after = image - 3.3;
        img_change = img;
        // $('.scrollToph').text(header);
        // $('.scrollTopg').text(header_text_after);
        $('img.image_back_home').css({opacity: image_back});
        $('img.image_back_check').css({opacity: image_back});
        $('img.image_back_bar').css({opacity: image_back});
        $('div.header_top').css({opacity: 0});
        $('div.header_top').css('z-index', '0');
        $('div.inner_text').css({opacity: 0});
        $('ul.menu_after').css({opacity: header_text_after });
        $('ul.menu_after').css('pointer-events', 'auto');
        $('div.top_bar').css({opacity: header_text_after});
        $('div.image_back').css({opacity: 1});
        $('div.image_back').css('transform', 'translate3d(-50%, '+ image_change_test +'px, 0)' + 'scale('+ img +')');
        $('#intro').removeClass('seen');
      } else if ( header <= -0.7398843930635843 ) {
        // $('.scrollTop').text(scroll);
        // $('.scrollTopj').text(header);
        // $('.scrollTopc').text(scroll);
        $('img.image_back_home').css({opacity: 1});
        $('img.image_back_check').css({opacity: 1});
        $('img.image_back_bar').css({opacity: 1});
        $('ul.menu_after').css({opacity: 1});
        $('div.top_bar').css({opacity: 1});
        $('ul.menu_after').css('pointer-events', 'auto');
        $('div.image_back').css('transform', 'translate3d(-50%, 314px, 0)' + 'scale(0.1227)');
        $('div.image_back').css({opacity: 0});
        $('img.image_back_home').css({opacity: 0});
        $('img.image_back_check').css({opacity: 0});
        $('img.image_back_bar').css({opacity: 0});
        $('#intro').addClass('seen');
      }
    });
  });
});

$(function() {
  $('a.left').on("click", function(){
    // $('.scrollTopd').text('as');
    if ($('div.theme').eq(2).hasClass('theme_previous_in') ) {
      // $('.scrollTopb').text('test');
      $('div.theme').eq(2).removeClass('theme_previous_in').addClass('theme_previous_out');
      $('div.theme').eq(1).addClass('theme_previous_in');
      $('div.theme').eq(0).removeClass('theme_previous_out');
    } else if ($('div.theme').eq(2).hasClass('theme_previous_out') ) {
      // $('.scrollTopc').text('test');
      $('div.theme').eq(2).removeClass('theme_previous_out');
      $('div.theme').eq(1).removeClass('theme_previous_in').addClass('theme_previous_out');
      $('div.theme').eq(0).addClass('theme_previous_in');
    } else if ( $('div.theme').eq(2).hasClass('theme') ) {
      // $('.scrollTopa').text('test');
      $('div.theme').eq(2).addClass('theme_previous_in');
      $('div.theme').eq(1).removeClass('theme_previous_out');
      $('div.theme').eq(0).removeClass('theme_previous_in').addClass('theme_previous_out');
    }
 });

 $('a.right').on("click", function(){
   if ($('div.theme').eq(0).hasClass('theme_previous_in')) {
     // $('.scrollTopb').text('test');
     // $('div.theme').eq(2).addClass('theme_previous_out');
     $('div.theme').eq(1).removeClass('theme_previous_out').addClass('theme_previous_in');
     $('div.theme').eq(0).removeClass('theme_previous_in').addClass('theme_previous_out');
   } else if ( $('div.theme').eq(0).hasClass('theme_previous_out') ){
     // $('.scrollTopc').text('test');
     $('div.theme').eq(2).addClass('theme_previous_in');
     $('div.theme').eq(1).removeClass('theme_previous_in').addClass('theme_previous_out');
     $('div.theme').eq(0).removeClass('theme_previous_out');
   } else if ( $('div.theme').eq(0).hasClass('theme') ) {
     // $('.scrollTopa').text('test');
     $('div.theme').eq(0).addClass('theme_previous_in');
     $('div.theme').eq(1).removeClass('theme_previous_out');
     $('div.theme').eq(2).addClass('theme_previous_out');
   }

 });
});

// $(function(){
//  $('a.right').on("click", function(){
//    if ($('div.theme').eq(1).hasClass('theme_previous_in')) {
//
//      $('div.theme').eq(2).addClass('theme_previous_in');
//      $('div.theme').eq(1).removeClass('theme_previous_in').addClass('theme_previous_out');
//      $('div.theme').eq(0).removeClass('theme_previous_out');
//    }
//  });
// });

$(function(){
  $('#sound').each(function(){
    $win = $(window),
    $height = $('#sound'),
    $heightH = $height.height(),
    $this = $('#sound'),
    height_off = $this.offset().top;
  $win.on('load scroll', function(){
    test_1 = $win.scrollTop();
    test_2 = $win.height();
    scroll = test_1 + test_2;
    if ($('#sound').offset().top < scroll -350 ) {
      $('#sound').addClass('seen');
    } else {
      $('#sound').removeClass('seen');
    }
   });
  });
});

$(function(){
  $('a.soundtrack.sound_1').on('click', function(){
    $('#audio').attr("src", "https://secure-c.vimeocdn.com/p/cameo/soundtrack1.mp3");
    if ( $('#audio_player')[0].paused == false ) {
      $('#audio_player')[0].pause();
      $('#sound .content .group_content.test .soundtrack.sound_1 .overlay img.audio_playing').css('display', 'none');
      $('a .overlay div.info').css('color', 'white');
      $('#sound .content .group_content.test .soundtrack.sound_1').removeClass('playing');
    } else {
      $('#audio_player')[0].load();
      $('#audio_player')[0].play();
      $('#sound .content .group_content.test .soundtrack.sound_1').addClass('playing');
      $('#sound .content .group_content.test .soundtrack.sound_1 .overlay img.audio_playing').css('display', 'block');
      $('a .overlay div.info').css('color', 'black')
    }
  });
  $('a.soundtrack.sound_2').on('click', function(){
    $('#audio').attr("src", "https://secure-c.vimeocdn.com/p/cameo/soundtrack2.mp3");
    if ( $('#audio_player')[0].paused == false ) {
      $('#audio_player')[0].pause();
      $('#sound .content .group_content.test .soundtrack.sound_2 .overlay img.audio_playing').css('display', 'none');
      $('a .overlay div.info').css('color', 'white');
      $('#sound .content .group_content.test .soundtrack.sound_2').removeClass('playing');
    } else {
      $('#audio_player')[0].load();
      $('#audio_player')[0].play();
      $('#sound .content .group_content.test .soundtrack.sound_2').addClass('playing');
      $('#sound .content .group_content.test .soundtrack.sound_2 .overlay img.audio_playing').css('display', 'block');
      $('a .overlay div.info').css('color', 'black')
    }
  });
  $('a.soundtrack.sound_3').on('click', function(){
    $('#audio').attr("src", "https://secure-c.vimeocdn.com/p/cameo/soundtrack3.m4a");
    if ( $('#audio_player')[0].paused == false ) {
      $('#audio_player')[0].pause();
      $('#sound .content .group_content.test .soundtrack.sound_3 .overlay img.audio_playing').css('display', 'none');
      $('a .overlay div.info').css('color', 'white');
      $('#sound .content .group_content.test .soundtrack.sound_3').removeClass('playing');
    } else {
      $('#audio_player')[0].load();
      $('#audio_player')[0].play();
      $('#sound .content .group_content.test .soundtrack.sound_3').addClass('playing');
      $('#sound .content .group_content.test .soundtrack.sound_3 .overlay img.audio_playing').css('display', 'block');
      $('a .overlay div.info').css('color', 'black')
    }
  });
  $('a.soundtrack.sound_4').on('click', function(){
    $('#audio').attr("src", "https://secure-c.vimeocdn.com/p/cameo/soundtrack4.mp3");
    if ( $('#audio_player')[0].paused == false ) {
      $('#audio_player')[0].pause();
      $('#sound .content .group_content.test .soundtrack.sound_4 .overlay img.audio_playing').css('display', 'none');
      $('a .overlay div.info').css('color', 'white');
      $('#sound .content .group_content.test .soundtrack.sound_4').removeClass('playing');
    } else {
      $('#audio_player')[0].load();
      $('#audio_player')[0].play();
      $('#sound .content .group_content.test .soundtrack.sound_4').addClass('playing');
      $('#sound .content .group_content.test .soundtrack.sound_4 .overlay img.audio_playing').css('display', 'block');
      $('a .overlay div.info').css('color', 'black')
    }
  });
});

$(function(){
  $('#video_main').each(function(){
    $win = $(window)
    video_height = $('#video_main').offset().top;
    scroll;
  $win.on('load scroll', function(){
    video_1 = $win.scrollTop();
    video_2 = $win.height();
    scroll = video_1 + video_2;
    if ($('#video_main').offset().top < scroll -250) {
      $('.header_video').addClass('seen');
    } else {
      $('.header_video').removeClass('seen');
    }

    if ($('#video_main').offset().top < scroll -400 ) {
      $('.video_item').addClass('seen');
    } else {
      $('.video_item').removeClass('seen');
    }

    if ($('#video_main').offset().top < scroll -770) {
      $('.video_item.under').addClass('seen');
    } else {
      $('.video_item.under').removeClass('seen');
    }

    if ($('#video_main').offset().top < scroll -950) {
      $('.video_content a.more_link').addClass('seen');
    } else {
      $('.video_content a.more_link').removeClass('seen');
    }

   });
  });
});

$(function(){
  $('#creaters').each(function(){
    $win = $(window)
    video_height = $('#creaters').offset().top;
    scroll;
  $win.on('load scroll', function(){
    video_1 = $win.scrollTop();
    video_2 = $win.height();
    scroll = video_1 + video_2;
    $('.scrollTopa').text(scroll);
    $('.scrollTopb').text(video_height);
  if ($('#creaters').offset().top < scroll -400) {
    $('div.row').eq(0).addClass('seen');
  } else {
    $('div.row').eq(0).removeClass('seen');
    $('div.row').eq(2).removeClass('seen');

  }

  if ($('#creaters').offset().top < scroll -450 ) {
    $('div.row').eq(1).addClass('seen');

  } else {
    $('div.row').eq(1).removeClass('seen');
    $('div.row').eq(3).removeClass('seen');

  }

  if ( $('#creaters').offset().top < scroll -590 ) {
    $('.creaters_content .more_link').addClass('seen');
    $('#creaters .inner .creaters_content .row .video_items.last').css('transform', 'translate3d(0, 0, 0)');
    $('#creaters .inner .creaters_content .row.seen .video_items.last').css('transform', 'translate3d(0, 0, 0)');
    $('#creaters .inner .creaters_content .row .video_items.main').css('transform', 'translate3d(0, 0, 0)');

    // $('#creaters .inner .community div.social').addClass('seen');
  } else {
    $('.creaters_content .more_link').removeClass('seen');
    $('#creaters .inner .creaters_content .row .video_items.last').css('transform', 'translate3d(0, 30px, 0)');

    // $('#creaters .inner .community div.social').removeClass('seen');
  }

  if ( $('div').hasClass('social') ) {
   if ($('#creaters').offset().top < scroll -730) {
     $('.scrollTopg').text('test');
     $('div.social').addClass('seen');
   } else {
     $('div.social').removeClass('seen');
     }
   }
  });
 });
});

$(function(){
 var slick = $('.slide').slick({
  // アクセシビリティ。左右ボタンで画像の切り替えをできるかどうか
  accessibility: true,
  // 自動再生。trueで自動再生される。
  autoplay: false,
  // 自動再生で切り替えをする時間
  autoplaySpeed: 3000,
  // 自動再生や左右の矢印でスライドするスピード
  speed: 400,
  // 自動再生時にスライドのエリアにマウスオンで一時停止するかどうか
  pauseOnHover: true,
  // 自動再生時にドットにマウスオンで一時停止するかどうか
  pauseOnDotsHover: true,
  // 切り替えのアニメーション。ease,linear,ease-in,ease-out,ease-in-out
  cssEase: 'ease',
  // 画像下のドット（ページ送り）を表示
  dots: false,
  // ドットのclass名をつける
  dotsClass: 'dot-class',
  // ドラッグができるかどうか
  draggable: true,
  // 切り替え時のフェードイン設定。trueでon
  fade: false,
  // 左右の次へ、前へボタンを表示するかどうか
  arrows: false,
  // 無限スクロールにするかどうか。最後の画像の次は最初の画像が表示される。
  infinite: true,
  // 最初のスライダーの位置
  initialSlide: 0,
  // 画像の遅延表示。‘ondemand’or'progressive'
  lazyLoad: 'ondemand',
  // スライドのエリアにマウスオーバーしている間、自動再生を止めるかどうか。
  pauseOnHover: true,
  // スライドのエリアに画像がいくつ表示されるかを指定
  slidesToShow: 2,
  // 一度にスライドする数
  slidesToScroll: 1,
  // タッチスワイプに対応するかどうか
  swipe: false,
  // 縦方向へのスライド
  vertical: false,

 });

 $("a.navigation.right").click(function(e){
   e.preventDefault();
   // slideIndex = $(this).index();
   $('div.slide').slick();
   $('div.row').eq(0).removeClass('seen');
   $('div.row').eq(1).removeClass('seen');
   $('div.row').eq(2).addClass('seen');
   $('div.row').eq(3).addClass('seen');
   $('a.navigation.right').addClass('disabled');
   $('a.navigation.left').removeClass('disabled');
   $('.contents .sliders .slide').eq(1).css('visibility', 'visible');
   $('.contents .sliders .slide').eq(0).css('visibility', 'hidden');
   $('.contents .sliders .slide').eq(0).animate({'left' : '-100%' } , 700);
   $('.contents .sliders .slide').eq(1).animate({'left' : 0 }, 700);
   $('#creaters .inner .creaters_content .row .video_items').css('transform', 'translate3d(0, 0, 0)');
   $('#creaters .inner .creaters_content .row.seen .video_items').css('transform', 'translate3d(0, 0, 0)');
   if ($('.contents .sliders .slide.next_in').eq(0).hasClass('next_in')) {
     $('.contents .sliders .slide').eq(0).removeClass('next_in');
     $('.contents .sliders .slide').eq(0).addClass('next_out');
     $('.contents .sliders .slide').eq(1).removeClass('next_out');
     $('.contents .sliders .slide').eq(1).addClass('next_in');
   }
 });
 $("a.navigation.left").click(function(e){
   e.preventDefault();
   // slideIndex = $(this).index();
   $('div.slide').slick();
   $('div.row').eq(0).addClass('seen');
   $('div.row').eq(1).addClass('seen');
   $('div.row').eq(2).removeClass('seen');
   $('div.row').eq(3).removeClass('seen');
   $('a.navigation.left').addClass('disabled');
   $('a.navigation.right').removeClass('disabled');
   $('.contents .sliders .slide').eq(1).css('visibility', 'hidden');
   $('.contents .sliders .slide').eq(0).css('visibility', 'visible');
   $('.contents .sliders .slide').eq(1).animate({'left' : '100%' }, 700);
   $('.contents .sliders .slide').eq(0).animate({'left' : 0 }, 700);
      $('#creaters .inner .creaters_content .row .video_items').css('transform', 'translate3d(0, 0, 0)');
   if ($('.contents .sliders ul.slide').eq(0).hasClass('next_out')) {
     $('.contents .sliders ul.slide').eq(0).removeClass('next_out');
     $('.contents .sliders ul.slide').eq(0).addClass('next_in');
     $('.contents .sliders .slide').eq(1).removeClass('next_in');
     $('.contents .sliders .slide').eq(1).addClass('next_out');
   }
 });
});

$(function(){
  $('div.input_overlay').click(function(){
    $('div.phone_number.invalid').addClass('active');
  });
  $('div.flag-dropdown').on('click',function(){
    if ( $('ul.country-list').hasClass('hide') ){
      $('ul.country-list').removeClass('hide');
    } else {
      $('ul.country-list').addClass('hide');
    }
  });
});

$(function(){
  $('#phone').on('input', function(){
    var val = $(this).val().replace(/[！-～]/g , function(tmpStr){

      return String,fromCharCode(tmpStr.charCodeAt(0) - 0xFEE0);

    }
   );
   $(this).val(val.replace(/[^0-9]/g, ''));

  });
});
