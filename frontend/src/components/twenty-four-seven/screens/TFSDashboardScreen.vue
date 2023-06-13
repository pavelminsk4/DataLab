<template>
  <TFSWorkingModal
    v-if="modalName === 'Working' && postInfo"
    :post="postInfo"
    @open-modal="openModal"
    @close="close"
  />
  <TFSDragAndDrop
    :card-results="items"
    @update-status="updateStatus"
    @change-status-via-dropdown="updateStatus"
    @update-page="updatePage"
    @open-modal="openModal"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@/lib/utilities'
import {defaultStatuses} from '@/lib/configs/tfsStatusesConfig'

import TFSDragAndDrop from '@/components/twenty-four-seven/drag-n-drop/TFSDragAndDrop'
import TFSWorkingModal from '@/components/twenty-four-seven/modals/TFSWorkingModal'

const {mapActions, mapState} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSDashboardScreen',
  components: {TFSDragAndDrop, TFSWorkingModal},
  props: {
    currentProject: {type: Object, default: () => {}},
  },
  data() {
    return {
      postInfo: null,
    }
  },
  computed: {
    ...mapState(['items']),
    projectId() {
      return this.$route.params.projectId
    },
    modalName() {
      return this.$route.query?.modal
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
    if (isAllFieldsEmpty(this.items)) {
      this.$router.push({
        name: 'TFSDashboard',
      })
    }
  },
  methods: {
    ...mapActions([
      action.GET_TFS_ITEMS,
      action.UPDATE_TFS_ITEM_STATUS,
      action.GET_TFS_RELATED_CONTENT,
      action.CLEAR_TFS_WHATSAPP_MESSAGE,
      action.CLEAR_TFS_RELATED_CONTENT,
      action.CLEAR_TFS_AI_SUMMARY,
    ]),
    async updateStatus(postId, newStatus, oldStatus, page, isBack) {
      await this[action.UPDATE_TFS_ITEM_STATUS]({
        projectId: this.projectId,
        postId: postId,
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
    openModal(postInfo) {
      this[action.CLEAR_TFS_RELATED_CONTENT]()

      this.$router.push({
        name: 'TFSDashboard',
        query: {modal: 'Working', tab: 'Original content'},
      })
      this.postInfo = postInfo

      this[action.GET_TFS_RELATED_CONTENT](postInfo.id)
    },
    close() {
      this[action.CLEAR_TFS_WHATSAPP_MESSAGE]()
      this[action.CLEAR_TFS_AI_SUMMARY]()

      this.$router.push({
        name: 'TFSDashboard',
      })
    },
  },
}
</script>
