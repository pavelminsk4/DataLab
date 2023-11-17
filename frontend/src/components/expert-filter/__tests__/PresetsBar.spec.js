import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import PresetsBar from '@components/expert-filter/PresetsBar'
import CreateNewGroupModal from '@/components/expert-filter/CreateNewGroupModal'

const createWrapper = (store) =>
  mount(PresetsBar, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    data() {
      return {
        isOpenCreateGroupModal: false,
      }
    },
  })

describe('PresetsBar component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the variable "isOpenCreateGroupModal" is set', () => {
    it('should be show component', async () => {
      expect(wrapper.findAllComponents(CreateNewGroupModal).length).toEqual(0)

      await wrapper.setData({isOpenCreateGroupModal: true})

      expect(wrapper.findAllComponents(CreateNewGroupModal).length).toEqual(1)
    })
  })
})
