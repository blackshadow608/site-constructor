
$('input.view_menu[type=radio]').click ->
  id= $('h2').attr("id_project")
  if $(this).hasClass('horizontal')
      request(id,'True')
  else
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
  $('.work_space').prepend('<div class="col-md-12 btn-group page_group_horizontal" role="group" ></div>')
  setAllPages(id, '.page_group_horizontal', currentPage)

setVerticalMenu = (id)->
  currentPage = $('.curr_page').attr('id_page')
  $('.page_group_horizontal').remove()
  $('.work_space').append('<div class="col-md-2  page_group_vertical" style="overflow: hidden"><table class="table table-menu" ></table></div>')

  setVerticalPages(id, '.table-menu', currentPage)

setAllPages = (id, oriented, local_page) ->
  $.ajax
    url: "/get_all_pages/"
    type: "GET"
    data:
      'proj_id': id
    success:(data) ->
      for page in data.pages
        $(oriented).append('<span class="btn  page-select" id_page=""><span class="btn btn-xs glyphicon glyphicon-remove navbar-right"></span></span>')

        if page.pageID.toString() == local_page.toString()
          $('[id_page = ""]').addClass('curr_page')
        $('[id_page = ""]').append page.pageName
        $('[id_page = ""]').attr('id_page', page.pageID)
    error: ->
      alert 'in change_menu'

setVerticalPages = (id, oriented, local_page) ->
  $.ajax
    url: "/get_all_pages/"
    type: "GET"
    data:
      'proj_id': id
    success:(data) ->
      for page in data.pages
        $(oriented).append('<tr><td  style="cursor: pointer;" class="page-select" id_page="">
<div class="col-md-2" style="word-wrap: break-word" ></div><span class="btn btn-xs glyphicon glyphicon-remove"></span>
                                    </td>
                                </tr>')

        if page.pageID.toString() == local_page.toString()
          $('[id_page = ""]').addClass('curr_page')
        $('[id_page = ""]').children('div').prepend page.pageName
        $('[id_page = ""]').attr('id_page', page.pageID)
    error: ->
      alert 'in change_menu'