<template>
  <TFSWorkingModal
    v-if="modalName === 'Working' && postInfo"
    :post="postInfo"
    :current-project="currentProject"
    @open-modal="openModal"
    @close="close"
  />

  <TFSLinkedPostsModal
    v-if="modalName === 'LinkedPosts'"
    :selected-linked-post="selectedLinkedPost"
    @update-page="updatePage"
    @close="close"
  />

  <TFSDashboardFilters
    :selected-sort-value="sortType.label"
    :selected-interval-value="intervalValue.label"
    @sort-selection="setSortValue"
    @show-status-cards="showStatusCards"
    @refresh-results="setRefreshInterval"
  />

  <TFSDragAndDrop
    :card-results="items"
    :current-statuses="currentStatuses"
    @update-status="updateStatus"
    @change-status-via-dropdown="updateStatus"
    @update-page="updatePage"
    @open-modal="openModal"
    @open-linked-modal="openLinkedModal"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@/lib/utilities'
import {
  defaultStatuses,
  dragAndDropStatuses,
} from '@/lib/configs/tfsStatusesConfig'

import TFSDragAndDrop from '@/components/twenty-four-seven/drag-n-drop/TFSDragAndDrop'
import TFSWorkingModal from '@/components/twenty-four-seven/modals/TFSWorkingModal'
import TFSDashboardFilters from '@/components/twenty-four-seven/TFSDashboardFilters'
import TFSLinkedPostsModal from '@/components/twenty-four-seven/modals/TFSLinkedPostsModal'

const {mapActions, mapState} = createNamespacedHelpers('twentyFourSeven')

const IRRELEVANT_STATUS = 'Irrelevant'

export default {
  name: 'TFSDashboardScreen',
  components: {
    TFSDragAndDrop,
    TFSWorkingModal,
    TFSDashboardFilters,
    TFSLinkedPostsModal,
  },
  props: {
    currentProject: {type: Object, default: () => {}},
  },
  data() {
    return {
      postInfo: null,
      timer: null,
      intervalValue: {label: 'No automatic refresh', value: 0},
      selectedLinkedPost: [],
      currentStatuses: dragAndDropStatuses,
    }
  },
  computed: {
    ...mapState(['items', 'sortType']),
    projectId() {
      return this.$route.params.projectId
    },
    modalName() {
      return this.$route.query?.modal
    },
  },
  created() {
    if (isAllFieldsEmpty(this.items)) {
      this.getAllStatuses()
    }
    if (isAllFieldsEmpty(this.items)) {
      this.$router.push({
        name: 'TFSDashboard',
      })
    }

    this.showStatusCards(null)
  },
  methods: {
    ...mapActions([
      action.GET_TFS_ITEMS,
      action.UPDATE_TFS_ITEM_STATUS,
      action.CLEAR_TFS_WHATSAPP_MESSAGE,
      action.CLEAR_TFS_RELATED_CONTENT,
      action.CLEAR_TFS_AI_SUMMARY,
      action.CLEAR_TFS_TRANSLATED_TEXT,
      action.UPDATE_TFS_SORT_TYPE,
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
    showStatusCards(status) {
      defaultStatuses.forEach((key) => {
        this.currentStatuses[key].isShow = status
          ? key === status
          : key !== IRRELEVANT_STATUS
      })
    },
    setSortValue(sortValue) {
      this[action.UPDATE_TFS_SORT_TYPE](sortValue)
      this.getAllStatuses()
    },
    getAllStatuses() {
      defaultStatuses.forEach((status) => {
        this[action.GET_TFS_ITEMS]({
          projectId: this.projectId,
          status: status,
          page: 1,
        })
      })
    },
    setRefreshInterval(newInterval) {
      clearInterval(this.timer)

      this.intervalValue = newInterval
      if (!newInterval.value) return

      this.timer = setInterval(() => {
        this.getAllStatuses()
      }, newInterval.value)
    },
    openModal(postInfo) {
      this[action.CLEAR_TFS_RELATED_CONTENT]()

      this.$router.push({
        name: 'TFSDashboard',
        query: {modal: 'Working', tab: 'Original content'},
      })
      this.postInfo = postInfo
    },
    openLinkedModal(post) {
      this.selectedLinkedPost = post

      this.$router.push({
        name: 'TFSDashboard',
        query: {modal: 'LinkedPosts'},
      })
    },
    close() {
      this[action.CLEAR_TFS_WHATSAPP_MESSAGE]()
      this[action.CLEAR_TFS_AI_SUMMARY]()
      this[action.CLEAR_TFS_TRANSLATED_TEXT]()

      this.$router.push({
        name: 'TFSDashboard',
      })
    },
  },
}
</script>
