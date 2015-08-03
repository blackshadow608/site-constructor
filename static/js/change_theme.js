// Generated by CoffeeScript 1.8.0
(function() {
  var request;

  $(function() {
    if ($('.dark').hasClass('is_check')) {
      $('.for-padding').addClass('dark');
    }
    return $('input').click(function() {
      var id, site;
      $('input').removeClass('is_check');
      $(this).addClass('is_check');
      site = $('.for-padding');
      id = $('h2').attr("id_project");
      if ($(this).hasClass('dark')) {
        site.addClass('dark');
        return request(id, 'True');
      } else {
        site.removeClass('dark');
        return request(id, 'False');
      }
    });
  });

  request = function(id, is_dark) {
    return $.ajax({
      url: "/theme/",
      type: "GET",
      data: {
        'proj_id': id,
        'is_dark': is_dark
      },
      success: function(data) {},
      error: function() {
        return alert('gyjudvasf');
      }
    });
  };

}).call(this);

//# sourceMappingURL=change_theme.js.map
