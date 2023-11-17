import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import SaveAsModal from '@/components/expert-filter/SaveAsModal'
import PresetCreatedModal from '@/components/expert-filter/PresetCreatedModal'
import CreateNewGroupModal from '@/components/expert-filter/CreateNewGroupModal'

const createWrapper = (store) =>
  mount(SaveAsModal, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    props: {
      expertQuery: '',
    },
    data() {
      return {
        newName: null,
        newSelectedGroup: null,
        isOpenCreateGroupModal: false,
        isOpenAlertModal: false,
      }
    },
  })

describe('SaveAsModal component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show text', async () => {
    expect(wrapper.text()).toMatch('Save as')
  })

  describe('when the variable "newSelectedGroup" is set', () => {
    it('should be show text', async () => {
      await wrapper.setData({newSelectedGroup: 'Animals'})

      expect(wrapper.text()).toMatch('Animals')
      expect(wrapper.vm.newSelectedGroup).toEqual('Animals')
    })
  })

  describe('when the variable "newName" is set', () => {
    it('should be show text', async () => {
      await wrapper.setData({newName: 'Tiger'})

      expect(wrapper.vm.newName).toEqual('Tiger')
    })
  })

  describe('when the variable "isOpenCreateGroupModal" is set', () => {
    it('should be show component', async () => {
      expect(wrapper.findAllComponents(CreateNewGroupModal).length).toEqual(0)

      await wrapper.setData({isOpenCreateGroupModal: true})

      expect(wrapper.findAllComponents(CreateNewGroupModal).length).toEqual(1)
    })
  })

  describe('when the variable "isOpenAlertModal" is set', () => {
    it('should be show component', async () => {
      expect(wrapper.findAllComponents(PresetCreatedModal).length).toEqual(0)

      await wrapper.setData({isOpenAlertModal: true})

      expect(wrapper.findAllComponents(PresetCreatedModal).length).toEqual(1)
    })
  })
})
