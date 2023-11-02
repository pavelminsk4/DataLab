import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {router} from '@router/__mocks__/router'

import OnlineFeaturesView from '@/views/online/OnlineFeaturesView'
import FeaturesScreen from '@/components/project/screens/FeaturesScreen'

const createWrapper = (store) =>
  mount(OnlineFeaturesView, {
    global: {
      plugins: [store, router],
      mixins: [mockmixin],
    },
    props: {
      currentProject: {
        title: 'project',
      },
      numberOfPosts: 100,
    },
    stubs: ['router-view'],
  })

describe('OnlineFeaturesView component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be displayed component', () => {
    expect(wrapper.findAllComponents(FeaturesScreen).length).toEqual(1)
  })
})
