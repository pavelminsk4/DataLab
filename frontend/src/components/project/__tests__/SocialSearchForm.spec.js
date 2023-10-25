import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseSearchField from '@/components/BaseSearchField'
import ProjectCalendar from '@/components/datepicker/ProjectCalendar'
import SocialSearchForm from '@/components/project/SocialSearchForm'

const createWrapper = (store) => {
  return mount(SocialSearchForm, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    props: {currentProject: {}},
  })
}

describe('SocialSearchForm component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display components', () => {
    expect(wrapper.findAllComponents(ProjectCalendar).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseSearchField).length).toEqual(3)
  })
})
