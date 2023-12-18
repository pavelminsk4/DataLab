import {mount} from '@vue/test-utils'
import {action} from '@store/constants'
import router from '@router/__mocks__/router'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {dragAndDropStatuses} from '@lib/configs/tfsStatusesConfig'

import TFSDragAndDrop from '@components/twenty-four-seven/drag-n-drop/TFSDragAndDrop'
import TFSDashboardScreen from '@components/twenty-four-seven/screens/TFSDashboardScreen'

const createWrapper = (store) =>
  mount(TFSDashboardScreen, {
    global: {
      plugins: [store, router],
      mocks: {
        $route: {
          params: {
            workspaceId: 2,
            projectId: 7,
          },
        },
        $router: {
          push: jest.fn(),
        },
      },
      props: {currentProject: {id: 7}},
      mixins: [mockmixin],
      data() {
        return {
          currentStatuses: dragAndDropStatuses,
        }
      },
      stubs: {
        TFSDragAndDrop,
      },
    },
  })

describe('TFSDashboardScreen component', () => {
  it('should display the text only from statuses', () => {
    const modules = {
      twentyFourSeven: {
        namespaced: true,
        actions: {[action.GET_TFS_ITEMS]: jest.fn()},
        state: {
          sortType: {label: 'Latest'},
        },
      },
    }
    const store = createNewStore({}, {modules})
    const wrapper = createWrapper(store)

    expect(wrapper.text()).toMatch('Picking')
    expect(wrapper.text()).toMatch('Summary')
  })

  describe('when the items be reveived', () => {
    it('should display the cards with content', () => {
      const modules = {
        twentyFourSeven: {
          namespaced: true,
          actions: {[action.GET_TFS_ITEMS]: jest.fn()},
          state: {
            items: {
              Summary: {
                count: 1,
                next: null,
                previous: null,
                results: [
                  {
                    header: 'Test post',
                    id: 1,
                    original_content: 'qwerty',
                    post: {
                      feedlink__alexaglobalrank: '12345',
                      entry_summary: 'Summary',
                      entry_title: 'Test post',
                      id: 1,
                      sentiment: 'neutral',
                    },
                    project: 7,
                    status: 'Summary',
                    text: 'test123',
                  },
                ],
              },
            },
            sortType: {label: 'Latest'},
          },
        },
      }
      const store = createNewStore({}, {modules})
      const wrapper = createWrapper(store)

      expect(wrapper.text()).toMatch('Neutral')
      expect(wrapper.text()).toMatch('Summary')
      expect(wrapper.text()).toMatch('Test post')
    })
  })
})
