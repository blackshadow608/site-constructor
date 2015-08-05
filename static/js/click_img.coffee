#$ ->
#  $('body').on 'click','img',->
#    imageHTML=this.outerHTML
#    imgObj = $.parseHTML(imageHTML)
#    console.log(imgObj)
##    imgObj.removeAttr('width')
##    imgObj.removeProp('height')
#    content =
#      state0:
#        html: imgObj,
#    $.prompt(content)