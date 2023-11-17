import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseInput from '@components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import CreateNewGroupModal from '@/components/expert-filter/CreateNewGroupModal'

const createWrapper = (store) =>
  mount(CreateNewGroupModal, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    data() {
      return {
        newName: '',
        newDescription: '',
      }
    },
  })

describe('CreateNewGroupModal component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show text', () => {
    expect(wrapper.text()).toMatch('Create new group')
  })

  it('should be show components', () => {
    expect(wrapper.findAllComponents(BaseInput).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseTextarea).length).toEqual(1)
  })

  describe('when the newName ana the newDescription are set', () => {
    it('should be show name and description', async () => {
      expect(wrapper.vm.name).toBe('')
      expect(wrapper.vm.description).toBe('')

      await wrapper.setData({newName: 'John', newDescription: 'Doe'})

      expect(wrapper.vm.name).toBe('John')
      expect(wrapper.vm.description).toBe('Doe')
    })
  })
})
