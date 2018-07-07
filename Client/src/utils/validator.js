function checkId (value) {
  var pattern = /^1\d{7}$/
  return pattern.test(value)
}

export function validateUsername (rule, value, callback) {
  if (!checkId(value)) {
    callback(new Error('学号/工号为8位数字！'))
  } else {
    callback()
  }
}

export function validatePassword (rule, value, callback) {
  if (value.length < 6) {
    callback(new Error('密码长度至少为六位！'))
  } else {
    callback()
  }
}


