export function snakeToPascal(string) {
  return string
    .split('_')
    .map((substr) => substr.charAt(0).toUpperCase() + substr.slice(1))
    .join('')
}

export function splitToSeparateWords(string) {
  return string.replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase()
}

export const isAllEmptyFields = (obj) => {
  for (let key in obj) {
    if (obj[key]) {
      if (typeof obj[key] !== 'object') return false
      if (!isAllEmptyFields(obj[key])) return false
    }
  }
  return true
}
