import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import Datepicker from '@vuepic/vue-datepicker'
import ProjectCalendar from '@components/datepicker/ProjectCalendar'

const createWrapper = (store) =>
  mount(ProjectCalendar, {
    global: {
      plugins: [store],
    },
  })

describe('ProjectCalendar component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display the Datepicker', () => {
    expect(wrapper.findAllComponents(Datepicker).length).toEqual(1)
  })
})
