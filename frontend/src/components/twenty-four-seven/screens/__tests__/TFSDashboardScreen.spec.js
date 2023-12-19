import {mount} from '@vue/test-utils'
import {action} from '@store/constants'
import router from '@router/__mocks__/router'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {dragAndDropStatuses} from '@lib/configs/tfsStatusesConfig'

import TFSPostCard from '@components/TFSPostCard'
import TFSWorkingModal from '@components/twenty-four-seven/modals/TFSWorkingModal'
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
          query: {
            modal: 'Working',
            tab: 'Original content',
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
          postInfo: null,
          currentStatuses: dragAndDropStatuses,
        }
      },
      stubs: {
        TFSDragAndDrop,
      },
    },
  })

describe('TFSDashboardScreen component', () => {
  it('should display the text only from statuses and does not display posts', () => {
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
    expect(wrapper.findAllComponents(TFSPostCard).length).toEqual(0)
  })

  describe('when the items be reveived', () => {
    const item = {
      header: 'Test post',
      id: 1,
      original_content: 'qwerty',
      linked_items: [1, 2],
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
    }

    const modules = {
      twentyFourSeven: {
        namespaced: true,
        actions: {
          [action.GET_TFS_ITEMS]: jest.fn(),
          [action.CLEAR_TFS_RELATED_CONTENT]: jest.fn(),
          [action.GET_TFS_RELATED_CONTENT]: jest.fn(),
        },
        state: {
          relatedContent: [item],
          items: {
            Summary: {
              count: 1,
              next: null,
              previous: null,
              results: [item],
            },
          },
          sortType: {label: 'Latest'},
        },
      },
    }
    const store = createNewStore({}, {modules})
    const wrapper = createWrapper(store)

    it('should display the posts with content', () => {
      expect(wrapper.text()).toMatch('Neutral')
      expect(wrapper.text()).toMatch('Summary')
      expect(wrapper.text()).toMatch('Test post')
      expect(wrapper.findAllComponents(TFSPostCard).length).toEqual(1)
    })

    describe('and when the user cliks on the "take to work" button', () => {
      it('should display the modal window', async () => {
        expect(wrapper.findAllComponents(TFSWorkingModal).length).toEqual(0)

        await wrapper.setData({
          postInfo: item,
        })

        const button = wrapper.find('.work-button')
        await button.trigger('click')

        expect(wrapper.text()).toMatch('Original content')
        expect(wrapper.findAllComponents(TFSWorkingModal).length).toEqual(1)
      })
    })
  })
})
