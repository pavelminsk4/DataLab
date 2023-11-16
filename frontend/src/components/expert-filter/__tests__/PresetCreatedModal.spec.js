import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/common/BaseButton'
import PresetCreatedModal from '@/components/expert-filter/PresetCreatedModal'

const createWrapper = (store) =>
  mount(PresetCreatedModal, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    props: {
      presetName: 'Tigers',
      groupName: 'Animals',
    },
  })

describe('PresetCreatedModal component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be displayed components', () => {
    expect(wrapper.findAllComponents(BaseModal).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseButton).length).toEqual(1)
  })

  describe('when the variable "isOpenPresetOptions" is set', () => {
    it('should be displayed component', async () => {
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
