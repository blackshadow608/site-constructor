// Generated by CoffeeScript 1.9.3
(function() {
  var currentPage, request, setAllPages, setHorizontalMenu, setVerticalMenu, setVerticalPages;

  $(function() {
    return $('input.view_menu[type=radio]').click(function() {
      var id;
      id = $('h2').attr("id_project");
      if ($(this).hasClass('horizontal')) {
        if (!$('div').is('.page_group_horizontal')) {
          setHorizontalMenu(id);
          return request(id, 'True');
        }
      } else {
        if (!$('div').is('.page_group_vertical')) {
          setVerticalMenu(id);
          return request(id, 'False');
        }
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

  currentPage = "";

  setHorizontalMenu = function(id) {
    currentPage = $('.curr_page').attr('id_page');
    $('.page_group_vertical').remove();
    $('.work_space').prepend('<div class="col-md-12 btn-group page_group_horizontal" role="group" ></div>');
    return setAllPages(id, '.page_group_horizontal', currentPage);
  };

  setVerticalMenu = function(id) {
    currentPage = $('.curr_page').attr('id_page');
    $('.page_group_horizontal').remove();
    $('.work_space').append('<div class="col-md-2  page_group_vertical" style="overflow: hidden"><table class="table table-menu" ></table></div>');
    return setVerticalPages(id, '.table-menu', currentPage);
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
          $(oriented).append('<span class="btn  page-select" id_page=""><span class="btn btn-xs glyphicon glyphicon-remove navbar-right"></span></span>');
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

  setVerticalPages = function(id, oriented, local_page) {
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
          $(oriented).append('<tr><td  style="cursor: pointer;" class="page-select" id_page=""> <div class="col-md-2" style="word-wrap: break-word" ></div><span class="btn btn-xs glyphicon glyphicon-remove"></span> </td> </tr>');
          if (page.pageID.toString() === local_page.toString()) {
            $('[id_page = ""]').addClass('curr_page');
          }
          $('[id_page = ""]').children('div').prepend(page.pageName);
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
