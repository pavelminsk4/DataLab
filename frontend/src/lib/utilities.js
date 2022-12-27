export function snakeToPascal(string) {
  return string
    .split('_')
    .map((substr) => substr.charAt(0).toUpperCase() + substr.slice(1))
    .join('')
}
