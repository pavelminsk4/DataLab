import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import ExpertModeTab from '@/components/workspace/ExpertModeTab'
import SearchScreen from '@/components/project/search/SearchScreen'

const createWrapper = (store) => {
  return mount(SearchScreen, {
    global: {
      plugins: [store],
    },
    props: {currentProject: {id: 1}},
    data() {
      return {
        isExpertMode: false,
      }
    },
  })
}

describe('SearchScreen component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the variable "isExpertMode: false"', () => {
    it('should display the simple mode', () => {
      expect(wrapper.findAllComponents(SimpleModeTab).length).toEqual(1)
    })
  })

  describe('when the variable "isExpertMode: true"', () => {
    it('should display the expert mode', async () => {
      await wrapper.setData({isExpertMode: true})

      expect(wrapper.findAllComponents(ExpertModeTab).length).toEqual(1)
    })
  })
})
