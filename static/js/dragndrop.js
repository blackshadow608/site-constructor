    $(function() {
        $(".draggable").draggable({
            helper: "clone", connectToSortable: "#droppable",
            start: function (event, ui) {
                var clone = $(ui.helper);
                clone.addClass("xyi");
            },
            stop: function (event, ui) {
                $(ui.helper).css('width', '100%');
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