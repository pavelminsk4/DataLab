<template>
  <TFSDragAndDrop
    :card-results="items"
    @update-status="updateStatus"
    @change-status-via-dropdown="updateStatus"
    @update-page="updatePage"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@/lib/utilities'
import {defaultStatuses} from '@/lib/configs/tfsStatusesConfig'

import TFSDragAndDrop from '@/components/twenty-four-seven/drag-n-drop/TFSDragAndDrop'

const {mapActions, mapState} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSDashboardScreen',
  components: {TFSDragAndDrop},
  computed: {
    ...mapState(['items']),
    projectId() {
      return this.$route.params.projectId
    },
  },
  created() {
    if (isAllFieldsEmpty(this.items)) {
      defaultStatuses.forEach((status) => {
        this[action.GET_TFS_ITEMS]({
          projectId: this.projectId,
          status: status,
          page: 1,
        })
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TFS_ITEMS, action.UPDATE_ITEM_STATUS]),
    async updateStatus(itemId, newStatus, oldStatus, page, isBack) {
      await this[action.UPDATE_ITEM_STATUS]({
        projectId: this.projectId,
        itemId: itemId,
        value: {status: newStatus, is_back: isBack},
        oldStatus,
        page: page,
      })
    },
    updatePage(page, status) {
      this[action.GET_TFS_ITEMS]({
        projectId: this.projectId,
        status: status,
        page: page,
      })
    },
  },
}
</script>
