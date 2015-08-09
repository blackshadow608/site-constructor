$('body').on 'click', '.glyphicon-remove', ->
  id = $(this).parent().attr('id_page')
  #    alert(id)
  $(this).parent().remove()
  $('.for-padding').empty()
  load_page(id)
  $.each $('.for-padding').children('.draggable-raiting'), (index, val) ->
    $.ajax
      url: "/rating/"
      type:"GET"
      data:{"id_delete_rating":$(val).attr('id_rating')}
  $('.for-padding').empty()
  load_page($('.curr_page').attr("id_page"))
  current_page=$(".curr_page")
  $.ajax
    url: "/remove_page/"
    type: "POST"
    data:
      'page_id': id
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    success:(data) ->
      current_page.addClass('curr_page')
      if not $('.page-select').is('.curr_page')
        $('.page-select:first').addClass('curr_page')
      id = $('.curr_page').attr("id_page")
      load_page(id)
      if not $('.btn').is('.page-select')
        location.reload()
    error: ->
      alert 'in remove page'

load_page =(id) ->
  $.ajax
    url:"/editor/"+$('h2').attr("id_project")+'/'
    type:"POST"
    data:
      'id_return_page':id
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    async:false
    success:(data)->
      $('.for-padding').append(data.page)
