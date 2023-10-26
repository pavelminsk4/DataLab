import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseSwitcher from '@/components/BaseSwitcher'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import ExpertModeTab from '@/components/workspace/ExpertModeTab'
import ProgressBar from '@/components/workspace/WorkspaceProgressBar'
import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'

const createWrapper = (store) =>
  mount(CreateSearchScreen, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    data() {
      return {
        isExpertMode: false,
      }
    },
    stubs: [BaseSwitcher],
  })

describe('CreateSearchScreen component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display components', () => {
    expect(wrapper.findAllComponents(ProgressBar).length).toEqual(1)
    expect(wrapper.findAllComponents(SimpleModeTab).length).toEqual(1)
  })

  describe('when the isExpertMode variable is true', () => {
    it('should display component', async () => {
      expect(wrapper.findAllComponents(ExpertModeTab).length).toEqual(0)

      await wrapper.setData({isExpertMode: true})

      expect(wrapper.findAllComponents(ExpertModeTab).length).toEqual(1)
      expect(wrapper.findAllComponents(SimpleModeTab).length).toEqual(0)
    })
  })
})
