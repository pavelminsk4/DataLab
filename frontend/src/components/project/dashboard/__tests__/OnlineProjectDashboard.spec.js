import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {router} from '@router/__mocks__/router'

import SearchResults from '@/components/SearchResults'
import OnlineProjectDashboard from '@/components/project/dashboard/OnlineProjectDashboard'
import OnlineProjectDashboardWidgets from '@/components/project/dashboard/OnlineProjectDashboardWidgets'

const createWrapper = (store) =>
  mount(OnlineProjectDashboard, {
    global: {
      plugins: [store, router],
      mixins: [mockmixin],
    },
    props: {
      currentProject: {
        id: 1,
        source: 'Online',
        start_search_date: new Date(),
        end_search_date: new Date(),
      },
    },
  })

describe('OnlineProjectDashboard component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be displayed components', () => {
    expect(wrapper.findAllComponents(SearchResults).length).toEqual(1)
    expect(
      wrapper.findAllComponents(OnlineProjectDashboardWidgets).length
    ).toEqual(1)
  })
})
