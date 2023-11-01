import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseSearchField from '@/components/BaseSearchField'
import ProjectCalendar from '@/components/datepicker/ProjectCalendar'
import CreateAccountAnalysisProject from '@/components/account-analysis/CreateAccountAnalysisProject'
import AccountAnalysisSourcesTabs from '@/components/account-analysis/AccountAnalysisSourcesTabs'

const createWrapper = (store) =>
  mount(CreateAccountAnalysisProject, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    data() {
      return {
        projectName: '',
      }
    },
  })

describe('CreateAccountAnalysisProject component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be included compoenents', () => {
    expect(wrapper.findAllComponents(BaseSearchField).length).toEqual(1)
    expect(wrapper.findAllComponents(ProjectCalendar).length).toEqual(1)
    expect(
      wrapper.findAllComponents(AccountAnalysisSourcesTabs).length
    ).toEqual(1)
  })

  describe('when the project name are filled and profile are selected', () => {
    it('should be displayed button', async () => {
      const button = wrapper.find('.button')
      expect(button.element.disabled).toBe(true)

      await wrapper.setData({projectName: 'Project name'})

      expect(button.element.disabled).toBe(false)
    })
  })
})
