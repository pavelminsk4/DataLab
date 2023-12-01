import {h} from 'vue'
import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import CustomText from '@components/CustomText'
import BaseCheckbox from '@components/BaseCheckbox'
import BaseTable from '@components/common/BaseTable'

const createWrapper = (store) =>
  mount(BaseTable, {
    global: {
      plugins: [store],
    },
    props: {
      tableHeader: [
        {name: 'name', width: ''},
        {name: 'phone', width: '15%'},
        {name: 'email', width: '40%'},
      ],
    },
    slots: {
      default: h('span', {}, 'Named Slot'),
    },
  })

describe('BaseTable component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should show the html tag which was passed in slot', () => {
    expect(wrapper.html()).toMatch('<span>Named Slot</span>')
  })

  it('should show the CustomText and BaseCheckbox components', () => {
    expect(wrapper.findAllComponents(CustomText).length).toEqual(4)
    expect(wrapper.findAllComponents(BaseCheckbox).length).toEqual(1)
  })

  describe('when "hasCheckbox" is false', () => {
    it('should not show BaseCheckbox component', async () => {
      await wrapper.setProps({hasCheckbox: false})

      expect(wrapper.findAllComponents(BaseCheckbox).length).toEqual(0)
    })
  })
})
