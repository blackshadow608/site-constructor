$ ->
  old_site_name = ""

  $('body').on 'click','#edit_site_name_button', ->
    old_site_name = $('#name_not_edit_span').attr("name_project")
    $('#name_not_edit_span').remove()
    $('#change_site_name_block').append('<span id="name_edit_span">
                          <input id="input_site_name" type="text" size=10 value="">
                          <button class="btn btn-xs" id="change_site_name_button">OK</button> </span>')
    $('#input_site_name').val(old_site_name)

  $('body').on 'click','#change_site_name_button', ->
    set_new_name()

  set_new_name = ()->
    new_site_name = $('#input_site_name').val()
    if not new_site_name
      new_site_name = old_site_name
    id= $('h2').attr("id_project")
    $.ajax
      url: "/change_site_name/"
      type: "GET"
      data:
        'proj_id': id
        'new_site_name': new_site_name
      success:(data) ->
        end_change_name(data.newName)
      error: ->
        alert 'in change site name'

  end_change_name = (site_name)->
    $('#name_edit_span').remove()
    $('#change_site_name_block').append('<span id="name_not_edit_span" name_project = "">
                        <button type="button" class="btn btn-link" id="edit_site_name_button">
                        edit</button>
                    </span>')
    $('#name_not_edit_span').prepend(site_name)
    $('#name_not_edit_span').attr('name_project', site_name)