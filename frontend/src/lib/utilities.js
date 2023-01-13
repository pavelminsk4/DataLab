export function snakeToPascal(string) {
  return string
    .split('_')
    .map((substr) => substr.charAt(0).toUpperCase() + substr.slice(1))
    .join('')
}

export function splitToSeparateWords(string) {
  return string.replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase()
}
