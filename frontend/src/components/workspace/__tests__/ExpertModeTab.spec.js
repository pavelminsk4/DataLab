import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import CustomText from '@/components/CustomText'
import BaseButton from '@/components/common/BaseButton'
import ExpertModeTab from '@/components/workspace/ExpertModeTab'
import ProjectCalendar from '@/components/datepicker/ProjectCalendar'

const createWrapper = (store) =>
  mount(ExpertModeTab, {
    global: {
      plugins: [store],
    },
    props: {
      moduleName: '',
      filters: [],
      isKeywordsFieldsDisable: false,
    },
    stubs: [CustomText, BaseButton],
  })

describe('ExpertModeTab component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display component with datepicker', () => {
    expect(wrapper.findAllComponents(ProjectCalendar).length).toEqual(1)
  })

  it('should display textarea', () => {
    expect(wrapper.html()).toContain('textarea')
  })

  describe('when the "isKeywordsFieldsDisable" is true', () => {
    it('should add a new class', async () => {
      await wrapper.setProps({isKeywordsFieldsDisable: true})

      expect(wrapper.html()).toContain('disable')
    })
  })
})
