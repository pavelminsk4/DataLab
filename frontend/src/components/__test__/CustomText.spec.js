import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {userInfo} from '@store/__mocks__/state'

import CustomText from '@components/CustomText'

const createWrapper = (store, props) =>
  mount(CustomText, {
    props,
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
  })

describe('CustomText component', () => {
  it('should display the text in English', () => {
    const text = 'This text is for testing'
    const store = createNewStore()
    const wrapper = createWrapper(store, {text})

    expect(wrapper.find('div').exists()).toBe(true)
    expect(wrapper.html()).toContain(text)
  })

  it('should display the text in Arabic on p tag', () => {
    const text = 'This text is for testing'
    const translationText = 'Translation text'
    userInfo.user_profile.platform_language = 'ar'
    const store = createNewStore({
      userInfo,
      translation: {
        [text]: translationText,
      },
    })
    const wrapper = createWrapper(store, {text, tag: 'h3'})

    expect(wrapper.find('h3').exists()).toBe(true)
    expect(wrapper.html()).toContain(translationText)
  })
})
