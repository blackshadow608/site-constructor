$ ->
  $('.page-select').click ->
    id_page = $(this).attr("id_page")
    $('.page-select').removeClass('curr_page')
    $('.for-padding').children().remove()
    $(this).addClass('curr_page')

  $('#droppable').on('mousemove', ->
    )
