import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import WorkspaceCard from '@/components/dashboard/WorkspaceCard'
import AreYouSureModal from '@/components/modals/AreYouSureModal'

const createWrapper = (store) =>
  mount(WorkspaceCard, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    props: {
      members: [{user_profile: {photo: 'photo'}}],
    },
    data() {
      return {
        isOpenDeleteModal: false,
      }
    },
  })

describe('WorkspaceCard component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the variable "isOpenDeleteModal" is true', () => {
    it('should be displayed component', async () => {
      expect(wrapper.findAllComponents(AreYouSureModal).length).toEqual(0)

      await wrapper.setData({isOpenDeleteModal: true})

      expect(wrapper.findAllComponents(AreYouSureModal).length).toEqual(1)
    })
  })
})
