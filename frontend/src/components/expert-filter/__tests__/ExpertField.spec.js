import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import ExpertField from '@components/expert-filter/ExpertField'

const createWrapper = (store) =>
  mount(ExpertField, {
    global: {
      plugins: [store],
      //   mixins: [mockmixin],
    },
    props: {
      modelValue: [''],
      'update:modelValue': (e) => wrapper.setProps({modelValue: e}),
      label: '',
      hasLineNumbering: false,
    },
  })

describe('ExpertField component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the label is set', () => {
    it('should be displayed text', async () => {
      await wrapper.setProps({label: 'Expert Filter'})

      expect(wrapper.text()).toMatch('Expert Filter')
    })
  })

  describe('when the modelValue is set', () => {
    it('should be displayed text', async () => {
      await wrapper.find('.expert-input').trigger('focus')
      expect(wrapper.emitted('focus')).toBeTruthy()
      await wrapper.find('.expert-input').setValue('focus')

      console.log(wrapper.html())

      expect(wrapper.text()).toMatch('cat OR dog')
    })
  })
})
