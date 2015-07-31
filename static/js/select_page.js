// Generated by CoffeeScript 1.9.3
(function() {
  $(function() {
    $('.page-select').click(function() {
      var content, id_curr_page, id_page;
      id_curr_page = $('.curr_page').attr("id_page");
      content = "";
      $.each($('.for-padding').children(), function(index, val) {
        return content += val.outerHTML;
      });
      id_page = $(this).attr("id_page");
      $.ajax({
        url: "/editor/" + $('h2').attr("id_project") + '/',
        type: "GET",
        data: {
          'id_page': id_page,
          'content': content
        },
        success: function(data) {},
        error: function() {
          return alert('gyjudvasf');
        }
      });
      $('.page-select').removeClass('curr_page');
      $('.for-padding').children().remove();
      return $(this).addClass('curr_page');
    });
    return $('#droppable').on('mousemove', function() {});
  });

}).call(this);

//# sourceMappingURL=select_page.js.map
