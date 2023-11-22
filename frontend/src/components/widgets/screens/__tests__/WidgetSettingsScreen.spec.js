import {mount, RouterLinkStub} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseButton from '@/components/common/BaseButton'
import BaseTabs from '@/components/project/widgets/modals/BaseTabs'
import FiltersScreen from '@/components/project/screens/FiltersScreen'
import WidgetSettingsScreen from '@/components/widgets/screens/WidgetSettingsScreen'
import ChartTypesRadio from '@/components/project/widgets/modals/screens/ChartTypesRadio'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'

const widgetDetails = {
  id: 1,
  title: 'Summary',
  name: 'summary',
  projectId: 1,
  hasPreview: false,
  moduleName: 'Online',
  settingsTabs: ['General'],
  aggregation_period: 'day',
  hasDownloadCSVButton: false,
}

const createWrapper = (store) =>
  mount(WidgetSettingsScreen, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    props: {
      hasAggregationPeriod: false,
      widgetDetails,
    },
    data() {
      return {
        panelName: 'General',
      }
    },
    stubs: {
      RouterLink: RouterLinkStub,
    },
  })

describe('WidgetSettingsScreen component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should show the components', () => {
    expect(wrapper.findAllComponents(BaseTabs).length).toEqual(1)
    expect(wrapper.findAllComponents(BasicSettingsScreen).length).toEqual(1)
  })

  describe('when the variable panelName will be changed to "filters"', () => {
    it('should show the component', async () => {
      expect(wrapper.findAllComponents(FiltersScreen).length).toEqual(0)

      await wrapper.setData({panelName: 'Filters'})
      expect(wrapper.findAllComponents(FiltersScreen).length).toEqual(1)
    })
  })

  describe('when the variable panelName will be changed to "Chart Layout"', () => {
    it('should show the component', async () => {
      expect(wrapper.findAllComponents(ChartTypesRadio).length).toEqual(0)

      await wrapper.setData({panelName: 'Chart Layout'})
      expect(wrapper.findAllComponents(ChartTypesRadio).length).toEqual(1)
    })
  })

  describe('when the variable hasDownloadCSVButton will be true', () => {
    it('should show the "Download CSV" button', async () => {
      await wrapper.setProps({
        widgetDetails: {
          ...widgetDetails,
          hasDownloadCSVButton: true,
        },
      })

      expect(wrapper.find('a').attributes('href')).toBe(
        `/api/${widgetDetails.moduleName.toLowerCase()}/${
          widgetDetails.projectId
        }/${widgetDetails.id}/download`
      )
    })

    describe('when projectId and widgetId will be changed', () => {
      it('should change href for download link', async () => {
        await wrapper.setProps({
          widgetDetails: {
            ...widgetDetails,
            id: 2,
            projectId: 2,
            hasDownloadCSVButton: true,
          },
        })

        expect(wrapper.find('a').attributes('href')).toBe(
          `/api/online/2/2/download`
        )
      })
    })
  })
})
