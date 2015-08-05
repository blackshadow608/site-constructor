$ ->
  $('input.view_menu[type=radio]').click ->
    id= $('h2').attr("id_project")
    if $(this).hasClass('horizontal')
      setHorizontalMenu(id)
      request(id,'True')
    else
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

currentPage = "-1"

setHorizontalMenu = (id)->
  local_curr_page = currentPage
  currentPage = $('.curr_page').attr('id_page')
  $('.page_group_vertical').remove()
  $('.work_space').prepend('<div id="page_group" class="btn-group page_group_horizontal" role="group"></div>')
  if local_curr_page.toString() == "-1"
    local_curr_page = currentPage
  setAllPages(id, '.page_group_horizontal', local_curr_page)

setVerticalMenu = (id)->
  local_curr_page = currentPage
  currentPage = $('.curr_page').attr('id_page')
  $('.page_group_horizontal').remove()
  $('.work_space').append('<div id="page_group" class="col-md-2 btn-group-vertical page_group_vertical" role="group">
        </div>')
  setAllPages(id, '.page_group_vertical', local_curr_page)

setAllPages = (id, oriented, local_page) ->
  $.ajax
    url: "/get_all_pages/"
    type: "GET"
    data:
      'proj_id': id
    success:(data) ->
      for page in data.pages
        $(oriented).append('<button class="btn btn-primary page-select" id_page=""></button>')
        if page.pageID.toString() == local_page.toString()
          $('[id_page = ""]').addClass('curr_page')
        $('[id_page = ""]').append page.pageName
        $('[id_page = ""]').attr('id_page', page.pageID)
    error: ->
      alert 'in change_menu'