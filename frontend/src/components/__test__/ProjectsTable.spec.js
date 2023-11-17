import {mount} from '@vue/test-utils'
import {createNewStore, mockmixin} from '@lib/test-helpers'

import BaseTable from '@components/common/BaseTable'
import ProjectsTable from '@/components/ProjectsTable'
import BaseTableRow from '@components/common/BaseTableRow'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import ProjectsTableActions from '@/components/ProjectsTableActions'

const createWrapper = (store) =>
  mount(ProjectsTable, {
    global: {
      plugins: [store],
      mixins: [mockmixin],
    },
    props: {
      tableHeader: [
        {name: 'name', width: ''},
        {name: 'phone', width: '15%'},
        {name: 'email', width: '40%'},
      ],
      values: ['Jenny', '37529', 'jenny@gmail.com'],
    },
    data() {
      return {
        isOpenDeleteModal: false,
      }
    },
  })

describe('ProjectsTable component', () => {
  const store = createNewStore()
  const wrapper = createWrapper(store)

  it('should be show components', () => {
    expect(wrapper.findAllComponents(BaseTable).length).toEqual(1)
    expect(wrapper.findAllComponents(BaseTableRow).length).toEqual(3)
    expect(wrapper.findAllComponents(ProjectsTableActions).length).toEqual(3)
  })

  describe('when the variable "isOpenDeleteModal" is true', () => {
    it('should be show component', async () => {
      expect(wrapper.findAllComponents(AreYouSureModal).length).toEqual(0)

      await wrapper.setData({isOpenDeleteModal: true})

      expect(wrapper.findAllComponents(AreYouSureModal).length).toEqual(1)
    })
  })
})
