function setStatus(_checkbox,options){
  const help = _checkbox.next('ins.iCheck-help')
  if (options === 'check') {
    help.addClass('checked')
    return
  }
  if(options === 'uncheck'){
    help.removeClass('checked')
  }
}

require('jquery').fn.iCheck = function (options) {
  // 初始化dom
  const _checkbox = $(this)
  const _box = $('<label class="iCheck-box"></label>')
  const _help = $('<ins class="iCheck-help"></ins>')

  /* checkbox 已美化 */
  if (_checkbox.parent().is('.iCheck-box')) {
    setStatus(_checkbox,options)
    return
  }
  // 添加 label.iCheck-box
  _checkbox.wrap(_box)
  // 添加 ins.iCheck-help
  _checkbox.after(_help)
  // 设置初始状态
  if (options) {
    setStatus(_checkbox,options)
    // return
  }
  const next_help = _checkbox.next('ins.iCheck-help')
  /* 点击切换状态 */
  next_help.on('click',function () {
    if (!next_help.hasClass('checked')){
      next_help.addClass('checked')
    }else{
      next_help.removeClass('checked')
    }
  })
}
