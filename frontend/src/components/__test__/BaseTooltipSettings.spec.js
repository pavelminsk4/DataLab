import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import PointsIcon from '@/components/icons/PointsIcon'
import BaseTooltipSettings from '@/components/BaseTooltipSettings'

const createWrapper = (store) =>
  mount(BaseTooltipSettings, {
    global: {
      plugins: [store],
    },
    data() {
      return {isOpenSettings: false}
    },
    slots: {
      default: ['<div id="test">Test</div>'],
    },
  })

describe('BaseTooltipSettings component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display the component', () => {
    expect(wrapper.findAllComponents(PointsIcon).length).toEqual(1)
  })

  describe('when the variable "isOpenSettings" is true', () => {
    it('should display the html tag which was passed in slot', async () => {
      expect(wrapper.find('#test').exists()).toBe(false)

      await wrapper.setData({isOpenSettings: true})

      expect(wrapper.find('#test').exists()).toBe(true)
    })
  })
})
