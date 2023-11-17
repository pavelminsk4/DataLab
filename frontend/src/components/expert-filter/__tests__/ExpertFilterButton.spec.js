import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import BaseButton from '@components/common/BaseButton'
import ExpertFilterIcon from '@components/icons/ExpertFilterIcon'
import ExpertFilterButton from '@components/expert-filter/ExpertFilterButton'

const createWrapper = (store) =>
  mount(ExpertFilterButton, {
    global: {
      plugins: [store],
    },
  })

describe('ExpertFilterButton component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should show the components', () => {
    expect(wrapper.findAllComponents(BaseButton).length).toEqual(1)
    expect(wrapper.findAllComponents(ExpertFilterIcon).length).toEqual(1)
  })

  it('should show the text', () => {
    expect(wrapper.text()).toMatch('Expert Filter')
  })
})
