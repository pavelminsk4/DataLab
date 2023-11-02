<template>
  <FeaturesScreen
    :number-of-posts="numberOfPosts"
    :current-project="currentProject"
    :is-open-download-report-modal="isOpenDownloadReportModal"
    @download-report="downloadReport"
    @close-modal="toggleWidgetsModal('isOpenDownloadReportModal')"
  />
</template>

<script>
import {mapGetters, mapState, createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import FeaturesScreen from '@/components/project/screens/FeaturesScreen'

const {mapActions} = createNamespacedHelpers('online')

export default {
  name: 'OnlineFeaturesView',
  components: {FeaturesScreen},
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      isOpenDownloadReportModal: false,
    }
  },
  computed: {
    ...mapGetters({
      numberOfPosts: get.POSTS_NUMBER,
    }),
    ...mapState({
      downloadingInstantReport: (state) => state.downloadingInstantReport,
    }),
  },
  methods: {
    ...mapActions([action.GET_INSTANT_REPORT]),
    toggleWidgetsModal(val) {
      this.togglePageScroll(false)
      this[val] = !this[val]
    },
    async downloadReport() {
      if (!this.downloadingInstantReport) {
        try {
          this.toggleWidgetsModal('isOpenDownloadReportModal')
          const res = await this[action.GET_INSTANT_REPORT]({
            projectId: this.currentProject.id,
          })

          const anchor = document.createElement('a')
          anchor.href = res
          anchor.download = 'instant_report.pdf'

          document.body.appendChild(anchor)
          anchor.click()
          document.body.removeChild(anchor)
        } catch (error) {
          console.error(error)
        } finally {
          this.toggleWidgetsModal('isOpenDownloadReportModal')
        }
      }
    },
  },
}
</script>
