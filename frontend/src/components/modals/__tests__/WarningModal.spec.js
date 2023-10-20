import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/common/BaseButton'
import WarningModal from '@/components/modals/WarningModal'

const createWrapper = (store) =>
  mount(WarningModal, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
  })

describe('WarningModal component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display the text and components', () => {
    expect(wrapper.findAllComponents(BaseModal).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseButton).length).toEqual(2)
    expect(wrapper.text()).toMatch('Are you sure about the words you entered?')
  })
})
