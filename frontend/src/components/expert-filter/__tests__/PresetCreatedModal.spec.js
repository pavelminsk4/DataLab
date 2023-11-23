import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseModal from '@components/modals/BaseModal'
import BaseButton from '@components/common/BaseButton'
import PresetCreatedModal from '@components/expert-filter/PresetCreatedModal'

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

  it('should be show components', () => {
    expect(wrapper.findAllComponents(BaseModal).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseButton).length).toEqual(1)
  })

  it('should be show text', () => {
    expect(wrapper.text()).toMatch(
      'You saved the Tigers preset to the Animals group'
    )
  })
})
