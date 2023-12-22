import {mount} from '@vue/test-utils'
import {action, get} from '@store/constants'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import CreateSearchScreen from '@components/workspace/screens/CreateSearchScreen'
import OnlineCreateSearchScreen from '@components/workspace/screens/OnlineCreateSearchScreen'

const createWrapper = (store) =>
  mount(OnlineCreateSearchScreen, {
    props: {
      workspaceId: '1',
      moduleName: 'Online',
    },
    global: {
      plugins: [store],
      mixins: [mockmixin],
      mocks: {
        $route: {
          name: 'OnlineWorkspaceStep3',
          params: {
            workspaceId: 1,
          },
        },
      },
    },
  })

describe('OnlineCreateSearchScreen component', () => {
  const modules = {
    online: {
      namespaced: true,
      actions: {
        [action.POSTS_PREVIEW]: jest.fn(),
        [action.GET_COUNTRIES]: jest.fn(),
        [action.GET_SOURCES]: jest.fn(),
        [action.GET_LANGUAGES]: jest.fn(),
        [action.GET_AUTHORS]: jest.fn(),
      },
      getters: {
        [get.SEARCH_LISTS]: () => {
          return {countries: []}
        },
      },
    },
  }
  const store = createNewStore({}, {modules})
  const wrapper = createWrapper(store)

  it('should display component', () => {
    expect(wrapper.findAllComponents(CreateSearchScreen).length).toEqual(1)
  })

  describe('should be a method ', () => {
    it('that converts an array to a url', () => {
      const filters = {
        keywords: ['python', 'vue'],
        addition: ['sql', 'psql'],
        countries: [],
      }

      expect(wrapper.vm.strFilters(filters)).toBe(
        'keywords[]=python&keywords[]=vue&addition[]=sql&addition[]=psql'
      )
    })
  })
})
