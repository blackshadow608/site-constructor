$ ->
  $('.page-select').click ->
    id_curr_page = $('.curr_page').attr("id_page")
    content = ""
    $.each $('.for-padding').children(), (index, val) ->
      content += val.outerHTML
    id_page = $(this).attr("id_page")
    $.ajax
      url: "/editor/"+$('h2').attr("id_project")+'/'
      type: "GET"
      data: {'id_page':id_page,'content': content}
      success:(data) ->
      error: ->
        alert 'gyjudvasf'
    $('.page-select').removeClass('curr_page')
    $('.for-padding').children().remove()
    $(this).addClass('curr_page')

  $('#droppable').on('mousemove', ->
    )
