$ ->
  $('.page-select').click ->
    id_curr_page = $('.curr_page').attr("id_page")

    content = $('.for-padding').children().clone().html()
    console.log(content)
    id_page = $(this).attr("id_page")
    $.ajax
      url: "/editor/"+$('h2').attr("id_page")+'/'
      type: "GET"
      data: {'id_page':id_page,'content': content}
      success:(data) ->
        alert id_curr_page
        alert id_page
      error: ->
        alert 'gyjudvasf'
    $('.page-select').removeClass('curr_page')
    $('.for-padding').children().remove()
    $(this).addClass('curr_page')

  $('#droppable').on('mousemove', ->
    )
