import {mount} from '@vue/test-utils'
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
      expect(wrapper.findAllComponents(BaseButton).length).toEqual(1)

      await wrapper.setProps({
        widgetDetails: {
          ...widgetDetails,
          hasDownloadCSVButton: true,
        },
      })
      expect(wrapper.findAllComponents(BaseButton).length).toEqual(2)
    })
  })
})
