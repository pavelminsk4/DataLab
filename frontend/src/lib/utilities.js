import moment from 'moment'
import {widgetsConfig} from '@lib/configs/widgetsConfigs'
import {PREDEFINED_COLORS, SORTED_SENTIMENT} from '@lib/constants'

export const capitalizeFirstLetter = (string) =>
  string?.charAt(0)?.toUpperCase() + string?.slice(1)

export const lowerFirstLetter = (string) =>
  string?.charAt(0)?.toLowerCase() + string?.slice(1)

export const stringToPascalCase = (str) =>
  (' ' + str).toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => {
    return chr.toUpperCase()
  })

export const snakeCaseToSentenseCase = (snakeCase) =>
  snakeCase
    .replace(/^[-_]*(.)/, (_, word) => word.toUpperCase())
    .replace(/[-_]+(.)/g, (_, word) => ' ' + word.toUpperCase())

export const splitToSeparateWords = (string) =>
  string.replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase()

export const isAllFieldsEmpty = (obj) => {
  for (let key in obj) {
    if (obj[key]) {
      if (typeof obj[key] !== 'object') return false
      if (!isAllFieldsEmpty(obj[key])) return false
    }
  }
  return true
}

export const defaultDate = (date, platformLang) => {
  if (platformLang) return moment(date).locale(platformLang).format('L')
  return moment(date).format('L')
}

export const getWidgetDetails = (
  widgetName,
  widgetData,
  projectId,
  moduleName
) => {
  return {
    ...widgetData,
    ...widgetsConfig[widgetName],
    name: widgetName,
    widgetName: stringToPascalCase(widgetName),
    isWidget: true,
    moduleName: moduleName,
    projectId,
  }
}

export const getUniqueColors = (data, key) => {
  const prefColors = [...PREDEFINED_COLORS]
  const colors = new Map()

  data.forEach((element) => {
    if (!colors.has(element[key])) {
      colors.set(element[key], prefColors.shift())
    }
  })

  return colors
}

export const sortSentiment = (sentiments) => {
  const newSentiments = [...sentiments]

  newSentiments.sort(({sentiment: sentimentA}, {sentiment: sentimentB}) => {
    const indexA = SORTED_SENTIMENT.indexOf(sentimentA)
    const indexB = SORTED_SENTIMENT.indexOf(sentimentB)

    return indexA - indexB
  })

  return newSentiments
}
