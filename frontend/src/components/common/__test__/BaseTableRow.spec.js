import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import BaseTableRow from '@components/common/BaseTableRow'
import BaseCheckbox from '@components/BaseCheckbox'

const createWrapper = (store) =>
  mount(BaseTableRow, {
    global: {
      plugins: [store],
    },
    props: {
      modelValue: [1, 2, 3],
      id: 1,
    },
  })

describe('BaseTableRow component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show component', () => {
    expect(wrapper.findAllComponents(BaseCheckbox).length).toEqual(1)
  })
})
