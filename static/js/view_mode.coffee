$ ->
  $('.page-select').click ->
    $('.page-select').removeClass('curr_page')
    $('.content').children().remove()
    $(this).addClass('curr_page')
    id = $('.curr_page').attr("id_page")
    console.log id
    $.ajax
      url:"/view_mode/"+148+'/'
      type:"GET"
      data:{'id_return_page':id}
      async:false
      success:(data)->
        $('.content').append(data.page)
