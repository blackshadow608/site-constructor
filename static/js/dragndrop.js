$(".draggable-video").draggable({
    helper: "clone", connectToSortable: "#droppable",
    start: function (event, ui) {
        var clone = $(ui.helper);
        clone.addClass("xyi");
    },
    stop: function (event, ui) {
        if ($('#droppable').children().is($(ui.helper))){
            var statesdemo = {
                state0: {
                    title: 'Video block',
                    html: '<label>Youtube link <input class="form-control" type="text" name="link" value=""></label><br />',
                    buttons: {OK: 1, Cancel: false},

                    submit: function (e, v, m, f) {
                        var url = (f.link);
                        if (url) {
                            var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
                            var match = url.match(regExp);
                            if (match && match[2].length == 11) {
                                url = match[2];
                                $(ui.helper).empty();
                                $(ui.helper).addClass('embed-responsive embed-responsive-16by9');
                                $(ui.helper).append('<iframe class="embed-responsive-item" width="50%" height="300px" ' +
                                    ' src="https://www.youtube.com/embed/' + url + '" frameborder="0" allowfullscreen></iframe>');
                                $(ui.helper).removeClass('btn-default');
                                $(ui.helper).css('height', 'auto');
                                $(ui.helper).css('width', '100%');
                                stop()
                            } else {
                                $(ui.helper).remove();
                            }
                        } else {
                            $(ui.helper).remove();
                        }
                    },
                    close: function (e, v, m, f) {
                        $(ui.helper).remove()
                    }
                }
            };
            $.prompt(statesdemo);
        }
    }
});

$(".draggable-text").draggable({
    helper: "clone", connectToSortable: "#droppable",
    start: function (event, ui) {
        var clone = $(ui.helper);
        clone.addClass("xyi");
    },
    stop: function (event, ui) {
        $(ui.helper).empty();
        $(ui.helper).removeClass('btn-default');
        $(ui.helper).removeClass('btn');
        $(ui.helper).css('height', 'auto');
        $(ui.helper).css('width', '100%');
        $(ui.helper).append('<textarea style="resize:vertical; width:95%" class="form-control markdown-field"></textarea>');
        stop();
    }
});

$(".draggable-raiting").draggable({
    helper: "clone", connectToSortable: "#droppable",
    start: function (event, ui) {
        var clone = $(ui.helper);
        clone.addClass("xyi");
    },
    stop: function (event, ui) {
        $(ui.helper).empty();
        $(ui.helper).removeClass('btn-default');
        $(ui.helper).removeClass('btn');
        $(ui.helper).css('height', '45px');
        $(ui.helper).css('width', '100%');
        $(ui.helper).append('    <div class="navbar-right" style="font-size: 17px;"><span class="btn glyphicon glyphicon-thumbs-up"style="font-size: 20px;">'+
            '</span><text>0</text></div>');
        if($('#droppable').children().is($(ui.helper)))
        {
            $.ajax({
                url: "/rating/",
                type:"GET",
                data:{"id_project_create_rating":$('h2').attr("id_project")},
                success:function(data){
                    if(data.response=='success'){
                        $(ui.helper).attr('id_rating', data.id_rating)
                        stop()
                    }
                }

            });

        }

    }
});

$(".draggable-gallery").draggable({
    helper: "clone", connectToSortable: "#droppable",
    start: function (event, ui) {
        var clone = $(ui.helper);
        clone.addClass("xyi");
    },
    stop: function (event, ui) {
        $(ui.helper).empty();
        $(ui.helper).removeClass('btn-default');
        $(ui.helper).removeClass('btn');
        $(ui.helper).addClass('container');
        //$(ui.helper).css('min-height', '200px');
        $(ui.helper).css('height', 'auto');
        $(ui.helper).css('padding-bottom', '20px');
        $(ui.helper).css('width', '100%');
        $(ui.helper).append('<div class="col-md-12 btn-group sortable-img well well-sm" min-height="200"></div>');

        $('.sortable-img').sortable({
            connectWith:'.draggable-img',
            over: function () {
                removeIntent = false
            },
            out: function () {
                removeIntent = true;
            }

        });
        stop()

    }
});

$(".draggable-img").draggable({
    helper: "clone", connectToSortable: ".sortable-img",
    start: function (event, ui) {
        var clone = $(ui.helper);
        $(ui.helper).addClass('TEST');

    },
    drag:function(){alert();},
    stop: function (event, ui) {
        $(ui.helper).addClass('TEST');
        stop()
    }
});

$(".sortable-img").sortable({
        over: function () {
            removeIntent = false
        },
        out: function () {
            removeIntent = true
        }

    }
);
$("#droppable").sortable({

    over: function () {
        removeIntent = false
    },
    out: function () {
        removeIntent = true
    },
    beforeStop: function (event, ui) {
        if (removeIntent == true) {
            if(ui.item.hasClass("draggable-raiting")){
                $.ajax({
                    url: "/rating/",
                    type:"GET",
                    data:{"id_delete_rating":ui.item.attr('id_rating')},
                    success:function(data){
                    }

                })
            }
            ui.item.remove()
        }
    }
});

function stop (){

            var conten="";
            $.each($('.for-padding').children(), function (index, val) {
                conten += val.outerHTML;
            });
            var id_curr_page = $('.curr_page').attr("id_page");
            $.ajax({
                url: "/editor/" + $('h2').attr("id_project") + '/',
                type: "POST",
                data: {
                    'id_page': id_curr_page,
                    'content': conten,
                    'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
                },
                success: function () {
                },
                error: function () {
                    return alert('gyjudvasf');
                }
            });
    }