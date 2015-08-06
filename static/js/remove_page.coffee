$ ->
  $('body').on 'click', '.glyphicon-remove', ->
    id = $(this).parent().attr('id_page')
    $(this).parent('button').remove()
    $.ajax
      url: "/remove_page/"
      type: "GET"
      data: {'page_id': id}
      success:(data) ->
        if not $('button').is('.page-select')
          location.reload()
        $('.page-select:first').addClass('curr_page')
        load_page()
      error: ->
        alert 'in remove page'

load_page = ->
  id = $('.curr_page').attr("id_page")
  $.ajax
    url:"/editor/"+$('h2').attr("id_project")+'/'
    type:"POST"
    data:
      'id_return_page':id
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    async:false
    success:(data)->
      $('.for-padding').append(data.page)
