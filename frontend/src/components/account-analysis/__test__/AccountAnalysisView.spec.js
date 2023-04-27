import {mount} from '@vue/test-utils'

import AccountAnalysisView from '@components/account-analysis/AccountAnalysisView.vue'

const wrapper = mount(AccountAnalysisView)

describe('AccountAnalysisView component', () => {
  it('should displayed the html tag which was passed in slot', () => {
    expect(wrapper.text()).toMatch('test')
  })
})
