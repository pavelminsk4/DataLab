import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import SaveAsModal from '@/components/expert-filter/SaveAsModal'
import ExpertField from '@components/expert-filter/ExpertField'
import ExpertFilterModal from '@/components/expert-filter/ExpertFilterModal'

const createWrapper = (store) =>
  mount(ExpertFilterModal, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    data() {
      return {
        expertQuery: [''],
        isOpenSaveAsModal: false,
        isShowExpertInput: true,
      }
    },
  })

describe('ExpertFilterModal component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show text', () => {
    expect(wrapper.text()).toMatch('Expert filter')
  })

  describe('when the variable "isOpenSaveAsModal" is true', () => {
    it('should be show component', async () => {
      await wrapper.setData({isOpenSaveAsModal: true})

      expect(wrapper.findAllComponents(SaveAsModal).length).toEqual(1)
    })
  })

  describe('when variable "expertQuery" is set', () => {
    it('should be show text', async () => {
      await wrapper.setData({expertQuery: ['cat OR dog']})

      expect(wrapper.vm.expertQuery).toEqual(['cat OR dog'])
      expect(wrapper.findAllComponents(ExpertField).length).toEqual(1)
    })
  })
})
