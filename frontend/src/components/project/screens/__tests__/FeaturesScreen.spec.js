import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'
import {router} from '@router/__mocks__/router'

import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import FeaturesScreen from '@/components/project/screens/FeaturesScreen'
import TotalResults from '@/components/TotalResults'
import DownloadInformationModal from '@/components/project/modals/DownloadInformationModal'

const createWrapper = (store) =>
  mount(FeaturesScreen, {
    global: {
      plugins: [store, router],
      mixins: [mockmixin],
    },
    props: {
      numberOfPosts: 100,
      currentProject: {title: 'project'},
      isOpenDownloadReportModal: false,
    },
    stubs: ['router-view'],
  })

describe('FeaturesScreen component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show components', () => {
    expect(wrapper.findAllComponents(TotalResults).length).toEqual(1)
    expect(wrapper.findAllComponents(MainLayoutTitleBlock).length).toEqual(2)
  })

  describe('when a isOpenDownloadReportModal variable change value', () => {
    it('should be show modal window', async () => {
      expect(
        wrapper.findAllComponents(DownloadInformationModal).length
      ).toEqual(0)

      await wrapper.setProps({isOpenDownloadReportModal: true})
      expect(
        wrapper.findAllComponents(DownloadInformationModal).length
      ).toEqual(1)
    })
  })
})
