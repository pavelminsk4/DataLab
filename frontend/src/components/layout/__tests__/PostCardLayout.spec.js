import {h} from 'vue'
import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'

import BaseTooltip from '@components/BaseTooltip'
import SentimentChips from '@components/SentimentChips'
import ClippingIcon from '@components/icons/ClippingIcon'
import PostCardLayout from '@components/layout/PostCardLayout'

const createWrapper = (store) =>
  mount(PostCardLayout, {
    global: {
      plugins: [store],
    },
    props: {
      isClippingWidget: false,
    },
    slots: {
      title: h('span', {}, 'Title'),
      description: h('div', {}, 'Description'),
      'post-type': h('div', {}, 'Online'),
      information: h('div', {}, 'Info'),
    },
  })

describe('PostCardLayout component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should display slots', () => {
    expect(wrapper.html()).toContain('<span>Title</span>')
    expect(wrapper.html()).toContain('<div>Description</div>')
    expect(wrapper.html()).toContain('<div>Online</div>')
    expect(wrapper.html()).toContain('<div>Info</div>')
  })

  it('should display component', () => {
    expect(wrapper.findAllComponents(SentimentChips).length).toEqual(1)
  })

  describe('when the "isClippingWidget: true"', () => {
    it('should not display components', async () => {
      expect(wrapper.findAllComponents(ClippingIcon).length).toEqual(1)
      expect(wrapper.findAllComponents(BaseTooltip).length).toEqual(1)

      await wrapper.setProps({isClippingWidget: true})

      expect(wrapper.findAllComponents(ClippingIcon).length).toEqual(0)
      expect(wrapper.findAllComponents(BaseTooltip).length).toEqual(0)
    })
  })
})
