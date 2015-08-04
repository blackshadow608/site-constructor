// Generated by CoffeeScript 1.9.3
(function() {
  var currentPage, request, setAllPages, setHorizontalMenu, setVerticalMenu;

  $(function() {
    return $('input.view_menu[type=radio]').click(function() {
      var id;
      id = $('h2').attr("id_project");
      if ($(this).hasClass('horizontal')) {
        setHorizontalMenu(id);
        return request(id, 'True');
      } else {
        setVerticalMenu(id);
        return request(id, 'False');
      }
    });
  });

  request = function(id, is_horizontal) {
    return $.ajax({
      url: "/menu/",
      type: "GET",
      data: {
        'proj_id': id,
        'is_horizontal': is_horizontal
      },
      success: function(data) {},
      error: function() {
        return alert('gyjudvasf');
      }
    });
  };

  currentPage = "-1";

  setHorizontalMenu = function(id) {
    var local_curr_page;
    local_curr_page = currentPage;
    currentPage = $('.curr_page').attr('id_page');
    $('.page_group_vertical').remove();
    $('.work_space').prepend('<div id="page_group" class="btn-group page_group_horizontal" role="group"></div>');
    if (local_curr_page.toString() === "-1") {
      local_curr_page = currentPage;
    }
    return setAllPages(id, '.page_group_horizontal', local_curr_page);
  };

  setVerticalMenu = function(id) {
    var local_curr_page;
    local_curr_page = currentPage;
    currentPage = $('.curr_page').attr('id_page');
    $('.page_group_horizontal').remove();
    $('.work_space').append('<div id="page_group" class="col-md-2 btn-group-vertical page_group_vertical" role="group"> </div>');
    return setAllPages(id, '.page_group_vertical', local_curr_page);
  };

  setAllPages = function(id, oriented, local_page) {
    return $.ajax({
      url: "/get_all_pages/",
      type: "GET",
      data: {
        'proj_id': id
      },
      success: function(data) {
        var i, len, page, ref, results;
        ref = data.pages;
        results = [];
        for (i = 0, len = ref.length; i < len; i++) {
          page = ref[i];
          $(oriented).append('<button class="btn btn-primary page-select" id_page=""></button>');
          if (page.pageID.toString() === local_page.toString()) {
            $('[id_page = ""]').addClass('curr_page');
          }
          $('[id_page = ""]').append(page.pageName);
          results.push($('[id_page = ""]').attr('id_page', page.pageID));
        }
        return results;
      },
      error: function() {
        return alert('in change_menu');
      }
    });
  };

}).call(this);

//# sourceMappingURL=change_menu.js.map