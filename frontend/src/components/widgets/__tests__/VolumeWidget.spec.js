import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import ChartsView from '@/components/charts/ChartsView'
import VolumeWidget from '@/components/widgets/VolumeWidget'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

const createWrapper = (store) =>
  mount(VolumeWidget, {
    global: {
      plugins: [store],
    },
    props: {
      widgetDetails: {id: 1, title: 'widget'},
      isSettings: false,
    },
  })

describe('VolumeWidget component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should show the components', () => {
    expect(wrapper.findAllComponents(ChartsView).length).toEqual(1)
    expect(wrapper.findAllComponents(WidgetsLayout).length).toEqual(1)
  })

  describe('when the variable isSettings is true', () => {
    it('should not show the component', async () => {
      expect(wrapper.findAllComponents(WidgetsLayout).length).toEqual(1)
      
      await wrapper.setProps({isSettings: true})
      expect(wrapper.findAllComponents(WidgetsLayout).length).toEqual(0)
    })
  })
})
