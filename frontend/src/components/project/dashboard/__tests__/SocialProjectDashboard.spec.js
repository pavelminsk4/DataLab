import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {router} from '@router/__mocks__/router'

import SearchResults from '@/components/SearchResults'
import SocialProjectDashboard from '@/components/project/dashboard/SocialProjectDashboard'
import SocialProjectDashboardWidgets from '@/components/project/dashboard/SocialProjectDashboardWidgets'

const createWrapper = (store) =>
  mount(SocialProjectDashboard, {
    global: {
      plugins: [store, router],
      mixins: [mockmixin],
    },
    props: {
      currentProject: {
        id: 1,
        source: 'Social',
        start_search_date: new Date(),
        end_search_date: new Date(),
      },
    },
  })

describe('SocialProjectDashboard component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show components', () => {
    expect(wrapper.findAllComponents(SearchResults).length).toEqual(1)
    expect(
      wrapper.findAllComponents(SocialProjectDashboardWidgets).length
    ).toEqual(1)
  })
})
