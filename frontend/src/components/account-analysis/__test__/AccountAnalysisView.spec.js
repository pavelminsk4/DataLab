import {mount} from '@vue/test-utils'

import AccountAnalysisModuleView from '@components/account-analysis/AccountAnalysisModuleView'

const wrapper = mount(AccountAnalysisModuleView)

describe('AccountAnalysisModuleView component', () => {
  it('should displayed the html tag which was passed in slot', () => {
    expect(wrapper.text()).toMatch('test')
  })
})
