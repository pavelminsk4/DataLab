import {h} from 'vue'
import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import CustomText from '@components/CustomText'
import BaseModal from '@components/modals/BaseModal'
import BaseButton from '@components/common/BaseButton'
import WarningModal from '@components/modals/WarningModal'

const createWrapper = (store) =>
  mount(WarningModal, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    slots: {
      default: h(CustomText, {
        tag: 'p',
        text: 'Test text',
        'data-test': 'slot-text',
      }),
    },
  })

describe('WarningModal component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display the text and components', () => {
    const text = wrapper.get('[data-test="slot-text"]')
    expect(text.html()).toContain('Test text')
    expect(wrapper.findAllComponents(CustomText).length).toEqual(4)
    expect(wrapper.findAllComponents(BaseModal).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseButton).length).toEqual(2)
  })
})
