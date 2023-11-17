import {mount} from '@vue/test-utils'
import {createNewStore} from '@lib/test-helpers'
import {router} from '@router/__mocks__/router'

import NotFoundPage from '@/components/NotFoundPage'
import BaseButton from '@/components/common/BaseButton'

const mockRouter = {
  push: jest.fn(),
}

const createWrapper = (store) =>
  mount(NotFoundPage, {
    global: {
      plugins: [store, router],
      mocks: {
        $router: mockRouter,
      },
    },
    stubs: [BaseButton],
  })

describe('NotFoundPage component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show text', () => {
    expect(wrapper.text()).toMatch('Looks Like You Are Lost...')
  })

  describe('when the button is pressed', () => {
    it('should be redirected to the main page', async () => {
      const button = wrapper.find('.base-button')
      await button.trigger('click')

      expect(mockRouter.push).toHaveBeenCalledTimes(1)
    })
  })
})
