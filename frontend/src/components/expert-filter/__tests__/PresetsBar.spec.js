import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import PresetsBar from '@components/expert-filter/PresetsBar'
import DropdownOptionsContainer from '@components/DropdownOptionsContainer'
import CreateNewGroupModal from '@/components/expert-filter/CreateNewGroupModal'

const createWrapper = (store) =>
  mount(PresetsBar, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    data() {
      return {
        isOpenPresetsOptions: false,
        isOpenCreateGroupModal: false,
      }
    },
  })

describe('PresetsBar component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the variable "isOpenCreateGroupModal" is set', () => {
    it('should be displayed component', async () => {
      expect(wrapper.findAllComponents(CreateNewGroupModal).length).toEqual(0)

      await wrapper.setData({isOpenCreateGroupModal: true})

      expect(wrapper.findAllComponents(CreateNewGroupModal).length).toEqual(1)
    })
  })

  describe('when the variable "isOpenPresetsOptions" is set', () => {
    it('should be displayed component', async () => {
      expect(
        wrapper.findAllComponents(DropdownOptionsContainer).length
      ).toEqual(0)

      await wrapper.setData({isOpenPresetsOptions: true})

      expect(
        wrapper.findAllComponents(DropdownOptionsContainer).length
      ).toEqual(1)
    })
  })
})
