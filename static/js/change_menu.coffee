$ ->
  $('input.view_menu[type=radio]').click ->
    id= $('h2').attr("id_project")
    if $(this).hasClass('horizontal')
      if not $('div').is('.page_group_horizontal')
        setHorizontalMenu(id)
        request(id,'True')
    else
      if not $('div').is('.page_group_vertical')
        setVerticalMenu(id)
        request(id,'False')

request = (id, is_horizontal)->
  $.ajax
    url: "/menu/"
    type: "GET"
    data:
      'proj_id': id
      'is_horizontal': is_horizontal
    success:(data) ->
    error: ->
      alert 'gyjudvasf'

currentPage = ""

setHorizontalMenu = (id)->
  currentPage = $('.curr_page').attr('id_page')
  $('.page_group_vertical').remove()
  $('.work_space').prepend('<div id="page_group" class="btn-group page_group_horizontal" role="group"></div>')
  setAllPages(id, '.page_group_horizontal', currentPage)

setVerticalMenu = (id)->
  currentPage = $('.curr_page').attr('id_page')
  $('.page_group_horizontal').remove()
  $('.work_space').append('<div id="page_group" class="col-md-2 btn-group-vertical page_group_vertical" role="group">
        </div>')
  setAllPages(id, '.page_group_vertical', currentPage)

setAllPages = (id, oriented, local_page) ->
  $.ajax
    url: "/get_all_pages/"
    type: "GET"
    data:
      'proj_id': id
    success:(data) ->
      for page in data.pages
        $(oriented).append('<button class="btn btn-primary page-select" id_page=""><span class="btn btn-xs glyphicon glyphicon-remove navbar-right"></span></button>')
        if page.pageID.toString() == local_page.toString()
          $('[id_page = ""]').addClass('curr_page')
        $('[id_page = ""]').append page.pageName
        $('[id_page = ""]').attr('id_page', page.pageID)
    error: ->
      alert 'in change_menu'