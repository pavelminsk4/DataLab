import {action} from '@store/constants'

export default {
  [action.GET_TRANSLATED_TEXT]: jest.fn(),
  [action.UPDATE_ADDITIONAL_FILTERS]: jest.fn(),
  [action.OPEN_FLASH_MESSAGE]: jest.fn(),
  [action.POST_PLATFORM_LANGUAGE]: jest.fn(),
  [action.GET_LIST_OF_PROFILE_HANDLE]: jest.fn(),
  [action.POST_SEARCH]: jest.fn(),
  [action.GET_PRESETS_GROUPS]: jest.fn(),
  [action.GET_FILTERS_OPTIONS]: jest.fn(),
  [action.UPDATE_KEYWORDS_LIST]: jest.fn(),
  [action.GET_AUTHORS]: jest.fn(),
  [action.GET_COUNTRIES]: jest.fn(),
  [action.GET_SOURCES]: jest.fn(),
  [action.GET_LANGUAGES]: jest.fn(),
}
