import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import ExpertField from '@components/expert-filter/ExpertField'

const createWrapper = (store) =>
  mount(ExpertField, {
    global: {
      plugins: [store],
    },
    props: {
      modelValue: ['cat OR dog'],
      label: '',
      hasLineNumbering: false,
    },
    data() {
      return {
        isFocus: true,
      }
    },
  })

describe('ExpertField component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the label is set', () => {
    it('should be show text', async () => {
      await wrapper.setProps({label: 'Expert Filter'})

      expect(wrapper.text()).toMatch('Expert Filter')
    })
  })

  describe('when the modelValue is set', () => {
    it('should be show text', () => {
      expect(wrapper.text()).toMatch('cat OR dog')
    })
  })
})
