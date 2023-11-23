import {h} from 'vue'
import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import BaseButton from '@components/common/BaseButton'
import BaseButtonSpinner from '@components/BaseButtonSpinner'

const createWrapper = (store) =>
  mount(BaseButton, {
    global: {
      plugins: [store],
    },
    props: {isDisabled: false, buttonLoading: false},
    slots: {
      default: h('h1', {}, 'Named Slot'),
    },
  })

describe('BaseButton component', () => {
  describe('when there is loading', () => {
    const store = createNewStore({loading: true})
    const wrapper = createWrapper(store)

    it('should display the spinner', () => {
      expect(wrapper.findAllComponents(BaseButtonSpinner).length).toEqual(1)
    })

    it('should be hide', () => {
      expect(wrapper.html()).toContain('hide-content')
    })
  })

  describe('when there is no loading', () => {
    const store = createNewStore({loading: false})
    const wrapper = createWrapper(store)

    it('should not display the spinner', () => {
      expect(wrapper.findAllComponents(BaseButtonSpinner).length).toEqual(0)
    })

    it('should display the html tag which was passed in slot and "hide-content" class does not apear', () => {
      expect(wrapper.html()).toMatch('<h1>Named Slot</h1>')
      expect(wrapper.html()).not.toContain('hide-content')
    })
  })
})
