<template>
  <TFSDragAndDrop
    :itemsTest="items"
    @update-status="updateStatus"
    @change-status-via-dropdown="updateStatus"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllEmptyFields} from '@/lib/utilities'
import {defaultStatuses} from '@/lib/configs/tfsStatusesConfig'

import TFSDragAndDrop from '@/components/twenty-four-seven/TFSDragAndDrop'

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
    if (isAllEmptyFields(this.items)) {
      defaultStatuses.forEach((element) => {
        this[action.GET_TFS_ITEMS]({projectId: this.projectId, status: element})
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TFS_ITEMS, action.UPDATE_ITEM_STATUS]),
    async updateStatus(itemId, newStatus, oldStatus) {
      await this[action.UPDATE_ITEM_STATUS]({
        projectId: this.projectId,
        itemId: itemId,
        value: {status: newStatus},
        oldStatus,
      })
    },
  },
}
</script>
