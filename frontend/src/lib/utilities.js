import {widgetsConfig} from '@/lib/configs/widgetsConfigs'
import moment from 'moment'

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

export const isAllFieldsEmpty = (obj) => {
  for (let key in obj) {
    if (obj[key]) {
      if (typeof obj[key] !== 'object') return false
      if (!isAllFieldsEmpty(obj[key])) return false
    }
  }
  return true
}

export const defaultDate = (date) => {
  return moment(date).format('ll')
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
