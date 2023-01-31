export const capitalizeFirstLetter = (string) =>
  string?.charAt(0)?.toUpperCase() + string?.slice(1)

export const snakeToPascal = (string) =>
  string
    .split('_')
    .map((substr) => capitalizeFirstLetter(substr))
    .join('')

export const splitToSeparateWords = (string) =>
  string.replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase()

export const isAllEmptyFields = (obj) => {
  for (let key in obj) {
    if (obj[key]) {
      if (typeof obj[key] !== 'object') return false
      if (!isAllEmptyFields(obj[key])) return false
    }
  }
  return true
}

export const defaultDate = (date) =>
  new Date(date).toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric',
  })
