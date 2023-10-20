import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import Datepicker from '@vuepic/vue-datepicker'
import CommonCalendar2 from '@/components/datepicker/CommonCalendar2'

const createWrapper = (store) =>
  mount(CommonCalendar2, {
    global: {
      plugins: [store],
    },
  })

describe('CommonCalendar2 component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display the Datepicker', () => {
    expect(wrapper.findAllComponents(Datepicker).length).toEqual(1)
  })
})
