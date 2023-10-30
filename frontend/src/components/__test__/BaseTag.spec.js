import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseTag from '@/components/BaseTag'

describe('BaseTag component', () => {
  let store, wrapper
  beforeEach(() => {
    store = createNewStore()
    wrapper = mount(BaseTag, {
      global: {
        plugins: [store],
        mixins: [mockmixin],
      },
      props: {
        modelValue: [],
      },
    })
  })

  describe('when the input data is set', () => {
    it('should be filled modelValue', async () => {
      expect(wrapper.vm.modelValue).toEqual([])

      const textInput = wrapper.find('input[type="text"]')
      await textInput.setValue('Some value')
      textInput.trigger('keydown.enter')

      expect(wrapper.vm.modelValue).toEqual(['Some value'])
    })
  })
})
