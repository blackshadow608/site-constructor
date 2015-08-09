$('body').on 'click','img', ->
  src_img=$(this).attr('src')
  target=$(".img-click")
  target.empty()
  target.append('<img class="draggable-img" src="'+src_img+'"style="width:350px;height:250px" >')
  $(".draggable-img").draggable
    helper: "clone"
    connectToSortable: ".sortable-img"
    stop:(event, ui) ->
      $(ui.helper).removeClass('draggable-img')
