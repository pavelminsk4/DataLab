import {widgetsConfig} from '@/lib/configs/widgetsConfigs'

export const capitalizeFirstLetter = (string) =>
  string?.charAt(0)?.toUpperCase() + string?.slice(1)

export const lowerFirstLetter = (string) =>
  string?.charAt(0)?.toLowerCase() + string?.slice(1)

export const stringToPascalCase = (str) =>
  (' ' + str).toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => {
    return chr.toUpperCase()
  })

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

export const getWidgetDetails = (widgetName, widgetData, projectId) => {
  return {
    ...widgetData,
    ...widgetsConfig[widgetName],
    name: widgetName,
    widgetName: stringToPascalCase(widgetName),
    isWidget: true,
    projectId,
  }
}
