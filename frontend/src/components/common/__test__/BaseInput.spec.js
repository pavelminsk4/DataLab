import {h} from 'vue'
import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import BaseInput from '@/components/common/BaseInput'
import SearchIcon from '@/components/icons/SearchIcon'
import ErrorIcon from '@/components/icons/ErrorIcon'
import CustomText from '@/components/CustomText'

const createWrapper = (store) =>
  mount(BaseInput, {
    global: {
      plugins: [store],
    },
    props: {label: 'Test', modelValue: 'Test', isSearch: true, hasError: false},
    slots: {
      default: h('span', {}, 'Named Slot'),
    },
  })

describe('BaseInput component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  describe('when the label is provided', () => {
    it('should be created component and displayed input', () => {
      expect(wrapper.find('label').exists()).toBe(true)
      expect(wrapper.find('input').exists()).toBe(true)
      expect(wrapper.findAllComponents(CustomText).length).toEqual(1)
    })

    it('should displayed the html tag which was passed in slot', () => {
      expect(wrapper.html()).toMatch('<span>Named Slot</span>')
    })

    describe('when the "modelValue" is changed', () => {
      it('should be changed input value ', async () => {
        expect(wrapper.find('input').element.value).toBe('Test')

        await wrapper.setProps({modelValue: 'New Value'})
        expect(wrapper.find('input').element.value).toBe('New Value')
      })
    })

    describe('and "isSearch" is true', () => {
      it('should displayed the search icon', () => {
        expect(wrapper.findAllComponents(SearchIcon).length).toEqual(1)
      })
    })

    describe('and "hasError" is true', () => {
      it('should displayed the error icon', async () => {
        await wrapper.setProps({hasError: true})

        expect(wrapper.findAllComponents(ErrorIcon).length).toEqual(1)
        expect(wrapper.findAllComponents(CustomText).length).toEqual(2)
      })
    })
  })

  describe('when the label is not provided', () => {
    it('should not be created component', async () => {
      await wrapper.setProps({label: ''})

      expect(wrapper.find('label').exists()).toBe(false)
    })
  })
})
