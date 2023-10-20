import {action} from '@store/constants'

export default {
  [action.GET_TRANSLATED_TEXT]: jest.fn(),
  [action.UPDATE_ADDITIONAL_FILTERS]: jest.fn(),
  [action.OPEN_FLASH_MESSAGE]: jest.fn(),
}
