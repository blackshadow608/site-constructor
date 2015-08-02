    $(function() {
        $(".draggable-video").draggable({
            helper: "clone", connectToSortable: "#droppable",
            start: function (event, ui) {
                var clone = $(ui.helper);
                clone.addClass("xyi");
            },
            stop: function (event, ui) {
                var statesdemo = {
                    state0: {
                        title: 'Video block',
                        html:'<label>Youtube link <input class="form-control" type="text" name="link" value=""></label><br />',
                        buttons: {OK: 1, Cancel:false },

                        submit:function(e,v,m,f){
                            var url=(f.link);
                            if(url) {
                                var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
                                var match = url.match(regExp);
                                if (match && match[2].length == 11) {
                                    url = match[2];
                                    $(ui.helper).empty();
                                    $(ui.helper).append('<iframe width="560" height="315"  src="https://www.youtube.com/embed/' + url + '" frameborder="0" allowfullscreen></iframe>');
                                    $(ui.helper).removeClass('btn-primary');
                                    $(ui.helper).css('height', 'auto');
                                    $(ui.helper).css('width', '100%');
                                } else {
                                    $(ui.helper).remove();
                                }
                            }else{
                                $(ui.helper).remove();
                            }
                        },
                        close: function(e,v,m,f){$(ui.helper).remove()}
                    }
                };
                $.prompt( statesdemo);
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
                $(ui.helper).removeClass('btn-primary');
                $(ui.helper).removeClass('btn');
                $(ui.helper).css('height', 'auto');
                $(ui.helper).css('width', '100%');
                $(ui.helper).append('<textarea style="resize:vertical; width:95%" class="form-control markdown-field"></textarea>');
            }
        });
        $("#droppable").sortable({
            over: function () {
                removeIntent = false
            },
            out: function () {
                removeIntent = true
            },
            beforeStop: function (event, ui) {
                if (removeIntent == true) {
                    ui.item.remove()
                }
            }
        });
    });