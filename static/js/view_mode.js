// Generated by CoffeeScript 1.9.3
(function() {
  var fotoramaGal, fotorama_img, load_page;

  window.onload = function() {
    if ($('.page-select').length) {
      $('.page-select:first').addClass('curr_page');
      return load_page();
    }
  };

  $(function() {
    return $('.page-select').click(function() {
      $('.page-select').removeClass('curr_page');
      $('.content').children().remove();
      $(this).addClass('curr_page');
      return load_page();
    });
  });

  load_page = function() {
    var id;
    id = $('.curr_page').attr("id_page");
    return $.ajax({
      url: "/view_mode/" + 148 + '/',
      type: "POST",
      data: {
        'id_return_page': id,
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
      },
      async: false,
      success: function(data) {
        $('.content').append(data.page);
        $.each($('.markdown-field'), function(index, val) {
          var text;
          text = val.innerHTML;
          text = markdown.toHTML(text);
          return $(val).replaceWith(text);
        });
        $.each($('.glyphicon'), function(index, val) {
          return $.ajax({
            url: "/like/",
            type: "GET",
            data: {
              'id_rating_get_likes': $(val).parent().parent().attr('id_rating')
            },
            success: function(data) {
              return $(val).parent().children('text').text(data.response);
            }
          });
        });
        return fotoramaGal();
      }
    });
  };

  fotoramaGal = function() {
    return $.each($('.sortable-img'), function(index, val) {
      var src_arr;
      src_arr = [];
      $.each($(this).children(), function(num, valli) {
        return src_arr.push($(valli).attr('src'));
      });
      $(val).replaceWith('<div class="fotorama" data-allowfullscreen="true"  data-width="700"  data-ratio="16/9">' + fotorama_img(src_arr) + '<div>');
      return $('.fotorama').fotorama();
    });
  };

  fotorama_img = function(arr) {
    var content, item;
    return content = (function() {
      var i, len, results;
      results = [];
      for (i = 0, len = arr.length; i < len; i++) {
        item = arr[i];
        results.push('<img src="' + item + '">');
      }
      return results;
    })();
  };

}).call(this);

//# sourceMappingURL=view_mode.js.map
