window.onload = ->
  if $('.page-select').length
    $('.page-select:first').addClass('curr_page')
    load_page()


$ ->
  $('.page-select').click ->
    $('.page-select').removeClass('curr_page')
    $('.content').children().remove()
    $(this).addClass('curr_page')
    load_page()

load_page = ->
  id = $('.curr_page').attr("id_page")
  $.ajax
      url:"/view_mode/"+148+'/'
      type:"POST"
      data:
        'id_return_page':id
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
      async:false
      success:(data)->
        $('.content').append(data.page)
        $.each $('.markdown-field'), (index, val) ->
          text=val.innerHTML;
          text=markdown.toHTML(text)
          $(val).replaceWith(text)
        $.each $('.glyphicon'), (index, val) ->
          $.ajax
            url:"/like/"
            type:"GET"
            data:
              'id_rating_get_likes':$(val).parent().parent().attr('id_rating')
            success: (data) ->
              $(val).parent().children('text').text(data.response)
        fotoramaGal()
fotoramaGal = ->
  $.each $('.sortable-img'), (index, val) ->
    src_arr=[]
    $.each $(this).children(), (num,valli) ->
      src_arr.push($(valli).attr('src'))
    $(val).replaceWith('<div class="fotorama" style="margin-left:25%" data-allowfullscreen="true"  data-nav="thumbs"  data-width="75%"  data-ratio="16/9">'+
      fotorama_img(src_arr)+ '<div>')
    $('.fotorama').fotorama()

fotorama_img =(arr) ->
  content = for item in arr
    '<img src="'+item+'">'