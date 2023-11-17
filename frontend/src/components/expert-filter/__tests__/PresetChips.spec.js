import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import BaseChips from '@/components/BaseChips'
import ArrowheadIcon from '@components/icons/ArrowheadIcon'
import PresetChips from '@components/expert-filter/PresetChips'
import DropdownOptionsContainer from '@components/DropdownOptionsContainer'

const createWrapper = (store) =>
  mount(PresetChips, {
    global: {
      plugins: [store],
    },
    props: {
      presetId: 1,
      presetName: 'preset',
    },
    data() {
      return {
        isOpenPresetOptions: false,
      }
    },
  })

describe('PresetChips component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show components', () => {
    expect(wrapper.findAllComponents(BaseChips).length).toEqual(1)
    expect(wrapper.findAllComponents(ArrowheadIcon).length).toEqual(1)
  })

  describe('when the variable "isOpenPresetOptions" is set', () => {
    it('should be show component', async () => {
      expect(
        wrapper.findAllComponents(DropdownOptionsContainer).length
      ).toEqual(0)

      await wrapper.setData({isOpenPresetOptions: true})

      expect(
        wrapper.findAllComponents(DropdownOptionsContainer).length
      ).toEqual(1)
    })
  })
})
