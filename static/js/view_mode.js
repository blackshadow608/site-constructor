// Generated by CoffeeScript 1.9.3
(function() {
  $(function() {
    return $('.page-select').click(function() {
      var id;
      $('.page-select').removeClass('curr_page');
      $('.content').children().remove();
      $(this).addClass('curr_page');
      id = $('.curr_page').attr("id_page");
      console.log(id);
      return $.ajax({
        url: "/view_mode/" + 148 + '/',
        type: "GET",
        data: {
          'id_return_page': id
        },
        async: false,
        success: function(data) {
          return $('.content').append(data.page);
        }
      });
    });
  });

}).call(this);

//# sourceMappingURL=view_mode.js.map
