window.onload = ->
  if $('.page-select').length
    $('.page-select:first').addClass('curr_page')
    load_page()

$ ->
  $('.page-select').click ->
    $('.page-select').removeClass('curr_page')
    $('.content').children().remove()
    $(this).addClass('curr_page')
    console.log $('.page-select').length
    load_page()

load_page = ->
  id = $('.curr_page').attr("id_page")
  $.ajax
      url:"/view_mode/"+148+'/'
      type:"GET"
      data:{'id_return_page':id}
      async:false
      success:(data)->
        $('.content').append(data.page)

